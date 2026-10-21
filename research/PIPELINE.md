# EH Radar build log (started 2026-10-21)

Goal: a quote-backed, pattern-card-based board for embodied agent harnesses (frontier LLMs / VLMs wrapped in a harness
that control embodied systems, students trained from them, RL inside them), built on the pipeline cloned from CUA
Radar (itself cloned from HarnessRSI Daily). This file is the log of **this** build: what was done, with counts, and
what remains. The general, repeatable procedure is [`docs/PIPELINE.md`](../docs/PIPELINE.md).

Each wake-up: check background tasks/agents → do the first unchecked step whose inputs exist → tick it here → commit.
Never re-launch work that is still running.

## Done (2026-10-21)
- [x] 1 **Corpus**: 1,351 arXiv papers harvested by `research/build_corpus.py` from the 9 lists in `refs/lists/`
  (harooos/awesome-coding-agents-for-robot-learning, kairunwen/Awesome-Robot-Use-Agent,
  chonghanqin/Awesome-Agentic-Robots, xwzhang221/Awesome-Agentic-Robot-Policies,
  dongqianyu99/Awesome-Agentic-Embodided-Systems, mindorigin150/awesome-fm-driven-embodied-agents,
  wisdom-pan/embodied-agent-harness, YennNing/Awesome-Code-as-Agent-Harness-Papers, lobehub/awesome-rsi) plus the
  Open Scientist domain `embodied-agent-harness` v1 corpus (`refs/lists/open-scientist-embodied-harness/papers.md`:
  the domain's papers minus those it triaged off-topic) → `research/corpus.jsonl`. Snapshot commits and generated
  files: `refs/lists/SOURCES.md`.
- [x] 2 **Standards adapted** to the field: `research/EVIDENCE_SCHEMA.md` (9 items, from the domain's 22 reviewer
  expectations in `.forge/domains/embodied-agent-harness-v1/profile/expectations.json`), `research/SCORE_SPEC.md`,
  `research/SCREEN_RUBRIC.md` (platform and component enums, also enforced by `research/check_screen.py` and
  `check_cards.py`), `keywords.json` (scope, search phrases, exclude signals, verified anchor works).

## Remaining
- [ ] 3 **Pattern cards** from the frozen domain build: 51 sub-cards in 8 families (K1xx interface and tools · K2xx
  verification and execution control · K3xx memory and skills · K4xx harness optimisation · K5xx students from
  teacher trajectories · K6xx on-policy correction · K7xx RL in the harness · K8xx evaluation methodology), from 50
  full-text readings and 22 expectations → `patterns/main/*.md`, `patterns/sub/*.md`, `patterns/overview.md`,
  `patterns/anti-patterns.md`; `research/patterns/taxonomy.json` / `taxonomy_view.json`;
  `research/patterns/conditions.json` (S/F ids, via `build_conditions.py`).
- [ ] 4 **Screening** per `research/SCREEN_RUBRIC.md` → `research/screen.jsonl` (tier A/B/C; off-field primary arXiv
  categories automatic C in `research/screen/auto_c.jsonl`); A/B ids → `research/ab_ids.txt`.
- [ ] 5 **Trial**: a handful of anchor papers assigned, judged and scored end to end (`research/trial/`); fix specs or
  cards before the board run if the trial shows a gap.
- [ ] 6 **Board scoring**: select the first board (`research/board1_ids.txt`), the other A/B papers →
  `research/queue/<date>-backlog.txt`; assign + judge in batches (`research/judgments/b*`), every batch passing
  `score.py check`; `score.py build`; `build_board.py` writes `papers/README.md` and the README top block.
- [ ] 7 **Calibration**: build `research/calibration/gold.jsonl` from reference judgments spanning several patterns and
  bands; blind re-judge of 3 gold papers by a fresh agent via `research/calibrate.py`.
- [ ] 8 **Docs and prompts** finalised against the built cards and board: README counts (`{{N_MAIN}}`, `{{N_SUB}}`,
  `{{N_AP}}` placeholders), `docs/`, `docs/agents/` (Grok collect → ingest → maintenance; Dots Step 0 calibration,
  catch-up / steady phases, triage → assign + judge → score → board; Reel posters), CI. A first draft for this field
  is written; it still names no counts.
- [ ] 9 **Publish**: public repo `CrepuscularIRIS/embodied-harness-radar`.

## Inherited, not yet adapted
These HarnessRSI Daily / CUA Radar scripts and specs stay in the tree but have no EH Radar use yet. Do not rely on them.
- `research/openreview_pull.py`: pulls ICLR submissions matching harness-RSI terms from OpenReview (incl. rejected/withdrawn).
- `research/openreview_labels.py`: attaches OpenReview accept/reject labels to corpus papers.
- `research/fetch_reviews.py`: fetches ICLR reviews for the outcome-contrast set (rate-limited, needs credentials).
- `research/fetch_openreview_pdf.py`: downloads OpenReview PDFs as full text for non-arXiv submissions.
- `research/or_to_arxiv.py`: maps OpenReview forums to arXiv ids by fuzzy title.
- `research/contrast.py`: accept-rate statistics per pattern; there are no outcome labels in this build.
- `research/build_bundles.py`: builds per-pattern reading bundles for card writing from signatures.
- `research/check_patterns.py`: checks HarnessRSI card counts against `contrast.json`; there is no contrast data here.
- `research/calibrate.py`: compares re-judgments with a gold set `research/calibration/gold.jsonl`, which does not
  exist yet (step 7).
- `research/reel_candidates.py`, `research/check_reel.py`, `research/setup_reel.sh`: Reel poster pipeline
  (ResearchStudio), adapted in CUA Radar; `reel/` holds only the README and empty candidate files until the board
  exists. The README keeps the empty `REEL` block for `build_board.py`.
- `research/check_signatures.py` + `research/SIGNATURE_SCHEMA.md`: signature extraction for HarnessRSI pattern
  induction; here Open Scientist readings replace signatures.
- `research/monitor.py`: repo health check; it expects a board, Reel files and CI runs that do not exist yet.
- `research/build_corpus.py` is adapted and used (step 1). `research/ingest.py` and `research/fetch_hf_meta.py` are
  used as is.

## Notes / decisions
- No outcome labels (venue, acceptance) are used anywhere in this build, so cards hold no accept rates.
- The score measures reported evidence and execution against the pattern card, not idea value. Repo Score is separate.
- Full texts stay local (`research/fulltext/` is gitignored).
- The Open Scientist domain build (`.forge/`) stays local and is gitignored; committed files cite it by path only.
