# Pipeline — how a paper gets from "someone mentioned it" to the board

Distilled from the CUA Radar build and adapted to this repo ([`research/PIPELINE.md`](../research/PIPELINE.md) is the
log of this build). Every step names its input, output, who does it, and the check that must pass. Deterministic
steps are scripts. Judgment steps are LLM work, and a script validates their output before anything is published.

```
Grok bot ──▶ inbox/YYYY-MM-DD.jsonl
                 │
                 ▼  (D) research/ingest.py         dedup, arXiv metadata → corpus.jsonl, full text, HF code links
            research/queue/YYYY-MM-DD-HHMM.txt  ──▶ 本地打分 session（双盲席位 + 仲裁）
                 │
                 ▼  (L) 1 screen        research/SCREEN_RUBRIC.md            → research/screen.jsonl         tier A/B/C
                 ▼  (D) 2 full text     research/fetch_fulltext.py           → research/fulltext/<id>.txt    (A/B, local only)
                 ▼  (L) 3 assign+judge  docs/agents/JUDGE_BATCH.md           → research/patterns/assign_<B>.jsonl,
                 │                                                             research/judgments/<B>.jsonl
                 ▼  (D) 4 merge         research/merge_assign.py             → research/patterns/assignments.jsonl
                 ▼  (D) 5 score         research/score.py check / build      → research/scores.jsonl
                 ▼  (D) 6 board         research/build_board.py              → papers/README.md, README top block
                 ▼  (D) 7 checks        see "Check suite"                    → commit
```
(D) = deterministic script · (L) = LLM judgment, validated by a script

## Steps

| # | Step | Who | Input → output | Validation (must pass) |
|---|---|---|---|---|
| 0 | Collect candidates | Grok bot | arXiv / HF Papers / GitHub / X / lab blogs / source-list updates → `inbox/YYYY-MM-DD.jsonl` | `inbox/README.md` format |
| 1 | Ingest + queue | Grok bot (script) | inbox → `corpus.jsonl`, `fulltext/<id>.txt`, `hf_meta.jsonl`, `queue/<stamp>.txt` | prints the remaining LLM steps |
| 2 | Screen | 打分 session | title + abstract → `screen.jsonl` row (tier, kind, platforms, components, confidence) | `python3 research/check_screen.py <file> <ids>` |
| 3 | Assign | 打分 session | full text + `research/patterns/taxonomy_view.json` + 1–3 closest `patterns/sub/*.md` → `assign_<B>.jsonl` (`sub_pattern`, `fit: good\|weak`) | sub id exists; `merge_assign.py` |
| 4 | Judge ×2（盲） | 两席位（`judge.py --seat`：gpt-6.1-sol、claude-sonnet-5-5） | full text + spec + conditions + anti-patterns → `passes/<B>.{sol,son55}.jsonl` | each record passes `score.py check` before being kept |
| 4b | Merge + arbitrate | script + 仲裁席（claude-opus-5-5） | `merge_judgments.py`：一致保留、分歧 unclear+FLAG → `judge.py --arb` → `<B>.jsonl` 最终单条记录 | `--apply-arb` re-checks the batch; `score.py check <B>.jsonl <ids>` = 0 problems |
| 5 | Score | script | final judgments → `scores.jsonl` | `score.py build` reports 0 skipped |
| 6 | Board | 打分 session (script) | scores → `papers/README.md`, README block | — |
| 7 | Diagnosis card (optional, top new A papers) | Dots | `cards/_TEMPLATE.md` | `python3 check_cards.py` |

Tier C stops after step 2. A paper whose full text has no HTML rendering gets `FULLTEXT: none`: every evidence
value, S and F is `unclear` and every anti-pattern `no` (see `JUDGE_BATCH.md`).

## Check suite (run before every commit)

```bash
python3 test_check_cards.py && python3 check_cards.py
python3 -m py_compile research/*.py
python3 research/merge_assign.py
PYTHONPATH=research python3 research/score.py check research/judgments/<B>.jsonl research/judgments/ids_<B>.txt
PYTHONPATH=research python3 research/score.py build && python3 research/build_board.py
```

After editing a main card (a human change), rerun `python3 research/build_conditions.py` so
`research/patterns/conditions.json` matches the card's S/F ids.

## Periodic work

| Cadence | Task | How |
|---|---|---|
| per queue file | steps 1–7 | commits `triage: …` / `score: …` |
| weekly | diagnosis cards for the week's top 1–3 new A papers; `python3 research/fetch_hf_meta.py` for missing code links; check the source lists in `refs/lists/SOURCES.md` for new ids | commit `cards: …` / `maintenance: …` |
| when weak fits pile up | share of new papers with `fit: weak`; if > 30%, propose (do not apply) new sub-patterns induced from the `fit_note`s of weak rows | issue for a human |

## Data rules that cost rework (keep them)

- **Judge only from the full-text file.** Never use venue, acceptance, citations, stars, demo videos or author
  reputation.
- **Closed-loop, execution-checked success is "online"; real-robot claims need trial counts.** Open-loop action
  accuracy, plan-text scores, replays and videos are at most `partial` / `offline`.
- **Development tasks are not held-out.** Gains on tasks, scenes or objects used to design the harness, synthesise
  skills, build memory, collect teacher data or run harness search are `held_out_env: partial/no` and at most `online`.
- **A learned success detector, stop checker, judge, reward model, acceptance gate or proxy simulator between the agent
  and the ground truth is audited separately** (`validator_check`).
- **Code availability comes from data, not from a truncated text** (quote → verified anchors in `keywords.json` →
  arXiv comment → Hugging Face Papers).
- **Off-field arXiv categories are auto-C** (primary category outside cs / stat.ML / eess): several source lists mix
  in unrelated papers, and "harness" also names wire and test harnesses.
- **Local only, never committed:** `research/fulltext/`, `.forge/`, credentials.
- Pattern cards cite papers as `arXiv#signature`; diagnosis cards (`cards/`) must cite versions and SHAs.
