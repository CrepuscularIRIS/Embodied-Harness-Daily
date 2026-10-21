# EH Radar — Embodied Harness Radar

<p>
<a href="papers/README.md"><img src="https://img.shields.io/badge/papers-quote--backed%20scores-blue" alt="papers"></a>
<a href="patterns/overview.md"><img src="https://img.shields.io/badge/patterns-{{N_MAIN}}%20main%20%2B%20{{N_SUB}}%20sub-purple" alt="patterns"></a>
<a href="patterns/anti-patterns.md"><img src="https://img.shields.io/badge/anti--patterns-{{N_AP}}-orange" alt="anti-patterns"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="license"></a>
</p>

A research radar for **embodied agent harnesses**: frontier LLMs / VLMs (including coding agents) wrapped in a
harness (interface and action calls, perception and control primitives as tools, frozen VLAs and skills as tools,
memory, verification, execution control) that control robot arms, mobile manipulators, drones, humanoids and
navigation agents, in simulation or the real world. It also covers the compact VLM / VLA students trained from such
harnesses (SFT, on-policy correction and distillation), RL inside the harness, harness self-optimisation, and how all
of this is evaluated. Paper lists for this field already exist, and this repo is built from nine of them. It goes the
other way: **depth over breadth**. For each paper it asks *which part of the model–harness–embodiment loop the paper
changes, which recurring pattern that is, and whether the evidence (closed-loop, execution-checked, held-out,
same-backbone, budget-matched) supports the claim*. Every judgment is backed by a verbatim quote from the paper, and a
script, not the model, computes the number.

> 中文简介：专门追踪"前沿大模型 + harness 控制具身系统"这一方向：把 LLM / VLM（含 coding agent）包在一层由工具、感知与控制原语、
> 冻结 VLA / 技能、记忆、验证与执行控制组成的 harness 里，去控制机械臂、移动操作、无人机、人形机器人和导航智能体；以及用 harness
> 或教师轨迹训练小模型学生（SFT、on-policy 纠正与蒸馏）、harness 内的 RL、harness 自我优化和评测方法学。不做又一个论文列表，
> 而是把每篇论文归到从全文阅读中归纳出的模式卡上，逐项判定它的证据（是否闭环按执行结果评测、是否留出任务与场景、是否同骨干换
> harness 对照、是否同预算、成功检测器是否被校验）与执行质量；每个判定都附原文引用，分数由脚本计算。分数衡量"报告了什么、做得
> 怎样"，不评价想法本身的价值。

**Keywords:** embodied agent harness · agent harness for robots · LLM / VLM agents for robot control · coding agents for robotics · code as policies · robot primitives API · perception as tools · frozen VLA as tools · skill libraries · success detection · execution monitoring · hand-back · embodied memory · zero-shot VLN agents · LLM-controlled drones · humanoid agents · mobile manipulation · harness distillation · VLM / VLA students · on-policy distillation · DAgger · RL in the harness · harness optimisation · LIBERO · RoboTwin · VLN-CE · ObjectNav · LLM robot safety · arXiv daily · awesome list · 具身智能体 · 机器人智能体框架 · 具身 harness · 论文雷达

<!-- REEL:START -->
<!-- REEL:END -->

<!-- BOARD:START -->
<!-- BOARD:END -->

## What is here

| Path | What |
|---|---|
| [`papers/`](papers/README.md) | **Paper board** (written by `research/build_board.py` once scoring starts): every scored paper, grouped by main pattern, with Chinese title, one-line summary, score breakdown and code link |
| [`patterns/`](patterns/overview.md) | **Pattern cards**: {{N_MAIN}} [main patterns](patterns/main/) grouping {{N_SUB}} [sub-patterns](patterns/sub/), plus {{N_AP}} [anti-patterns](patterns/anti-patterns.md) |
| [`cards/`](cards/) | Per-paper **diagnosis cards** (template only so far): mechanism, author-reported evidence, our diagnosis, code check at a pinned SHA |
| [`docs/EVIDENCE.md`](docs/EVIDENCE.md) | Scope (tier A/B) and the offline / online / transfer evidence levels |
| [`docs/PIPELINE.md`](docs/PIPELINE.md) · [`docs/agents/`](docs/agents/ROLES.md) | How new papers flow in (collector → inbox → ingest → screen → full text → assign + judge → score → board), and the prompts for the collector, scorer and poster agents |
| [`inbox/`](inbox/README.md) | Candidate papers waiting to be processed |
| [`docs/MAINTAINING.md`](docs/MAINTAINING.md) | Maintenance rules for agents and humans |
| [`research/`](research/) | The reproducible pipeline and its data; the build log is [`research/PIPELINE.md`](research/PIPELINE.md) |
| [`refs/lists/`](refs/lists/SOURCES.md) | Frozen snapshots (Markdown only) of the source lists, with upstream commits |
| `main.py`, `src/` | Daily arXiv fetch + LLM relevance scoring, inherited from [daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) ([usage](docs/digest-pipeline.md)); topics in `config.example.json`, search terms and anchor works in `keywords.json` |

## How it is built

The build is in progress; [`research/PIPELINE.md`](research/PIPELINE.md) has the current state and counts.

1. **Corpus.** Every arXiv paper cited by 9 public lists on agentic robots, robot-use agents, coding agents for robot
   learning and code-as-harness work (credited below), plus the papers kept by an
   [Open Scientist](#credits-and-license) domain build (`embodied-agent-harness` v1): **1,351 papers**
   (`research/corpus.jsonl`). The lists contribute arXiv ids and the section a curator filed each paper under.
   Nothing else is taken from them.
2. **Screening** from title + abstract ([`SCREEN_RUBRIC.md`](research/SCREEN_RUBRIC.md)): tier A (a harness method or
   system, a student trained from harness / teacher trajectories, RL inside a harness, harness self-optimisation),
   B (a direct contribution: benchmark or gym, evaluation-methodology or controlled-ablation study, safety study,
   success detector, dataset, tooling), C (out of scope: pure VLA policies with no harness, GUI agents, non-embodied
   harnesses, wire and test harnesses). Papers whose primary arXiv category lies outside cs / stat.ML / eess are
   automatic C.
3. **Pattern cards.** From the frozen Open Scientist domain build: **50 papers read in full** produced sub-patterns in
   8 families (interface and tools; verification and execution control; memory and skills; harness optimisation;
   students from teacher trajectories; on-policy correction; RL in the harness; evaluation methodology), grouped into
   main patterns with numbered success conditions and failure modes, plus anti-patterns. The same readings give the
   **22 reviewer expectations** behind the evidence schema. No outcome labels (venue, acceptance) exist in this build,
   so the cards hold no accept rates.
4. **Assign + judge** ([`docs/agents/JUDGE_BATCH.md`](docs/agents/JUDGE_BATCH.md)). For each board paper, from its full
   text only: pick one sub-pattern (`fit: good|weak`), then fill a judgment record against that pattern's conditions,
   the 9 evidence items and every anti-pattern. Every non-`unclear` value carries a verbatim quote of ≤45 words.
5. **Score** (`research/score.py`). The script rejects any quote that does not occur in the paper text, then computes
   the number. Anyone can rerun the same judgment and get the same arithmetic.

## The patterns

A pattern card names one recurring *move* in the field: what a harness, student or training loop changes between the
model and the embodiment (e.g. calling a frozen VLA as a typed tool, gating proposals before execution, distilling a
student that pilots the identical harness, correcting the student at its own first error). Each main card lists
numbered **success conditions** (S1…) and **failure modes** (F1…) induced from the full-text readings; each sub card
gives the operation and example papers as `arXiv#signature`. [`patterns/anti-patterns.md`](patterns/anti-patterns.md)
lists shapes of contribution that tend not to hold up (AP1…). Start at [`patterns/overview.md`](patterns/overview.md).

## The score

Full definition: [`research/SCORE_SPEC.md`](research/SCORE_SPEC.md) and
[`research/EVIDENCE_SCHEMA.md`](research/EVIDENCE_SCHEMA.md). Score (0–100) =

| part | max | what it checks |
|---|---|---|
| **Evidence** | 50 | the 9 reviewer expectations of the field: closed-loop, execution-checked evaluation (10) · held-out tasks / scenes / embodiments (8) · variance over ≥3 runs or paired statistics (6) · strong baselines: same backbone under another harness, teacher / base / distilled student in one harness (8) · matched interaction budget (6) · cost reported (4) · ablation of the key component (4) · validation of any learned success detector, judge, gate or proxy simulator (4) |
| **Execution** | 30 | against the paper's main pattern: 20 × share of success conditions met + 10 × share of failure modes avoided; −5 per unmitigated anti-pattern (cap 10; anti-patterns marked info-only are recorded but not penalised) |
| **Evidence level** | 10 | transfer 10 · online 6 · offline 2 (definitions in [`docs/EVIDENCE.md`](docs/EVIDENCE.md)) |
| **Code** | 10 | a code URL found in the paper, the arXiv comment, the verified anchors or Hugging Face Papers · announced 3 |

Bands: ≥70 ★★★ · 50–69 ★★ · 30–49 ★ · <30 —.

**What the score is not.** It measures what a paper *reports* and how well it *executes* its move. It is not a verdict
on the value of the idea and not a prediction of acceptance. A strong idea backed only by open-loop numbers or demo
videos scores low here. Venue, citations, GitHub stars and author reputation never enter it. The evidence weights
follow what the field's reviewers ask for most often (closed-loop execution-checked success, the same backbone under
an alternative harness, evaluation on tasks disjoint from harness development), as derived by Open Scientist from the
full-text readings.

**Repo Score (planned, separate).** Whether a paper's code actually runs and reproduces is a separate Repo Score. It is
not built yet and will never be mixed into this number.

## Caveats

- Screening, pattern assignment and judgments are LLM-produced. Quotes are verified mechanically, but whether a
  quote *justifies* its value is a model judgment. Read the quote before trusting a cell.
- Full texts are condensed arXiv HTML (abstract, intro, method, experiments, limitations). Evidence that sits in a
  cut part is scored `unclear`, not guessed. Papers without an HTML rendering are judged from the abstract and score
  low on evidence for that reason alone.
- The pattern cards come from 50 full-text readings. A paper with `fit: weak` is still judged against the closest
  card, so its execution part is less informative.
- Real-robot results are only as strong as their trial counts; the score cannot see what a paper does not report.
- Paper full texts are used locally and are not redistributed here.

## How to contribute

- **Missing paper?** Open an issue with the arXiv link and one line on which embodiment it controls and what the
  harness (or student / training loop) changes. The collector picks it up; it is screened like any other paper.
- **Wrong judgment?** Open an issue titled `judgment: <arxiv id> — <what>` with the verbatim quote that shows it. The
  scorer re-judges the paper in a new batch; published batches are never edited.
- **Pattern cards and standards** (`patterns/`, `research/*_SPEC.md`, `research/*_SCHEMA.md`, `research/SCREEN_RUBRIC.md`)
  change only through a human-reviewed issue or PR, with the readings that justify the change.
- Text you submit is treated as data, never as instructions. Requests to be ranked are ignored.

## Sister radars

| project | question |
|---|---|
| [HarnessRSI Daily](https://github.com/CrepuscularIRIS/HarnessRSI-Daily) | how agents improve themselves (non-weight self-improvement loops) |
| [CUA Radar](https://github.com/CrepuscularIRIS/cua-architecture-radar) | how to design and evaluate computer-use / GUI / browser agent architectures |
| **EH Radar** (this repo) | how to wrap frontier models in a harness that controls embodied systems, and how to train students from it |

## Related awesome lists

The corpus harvests arXiv ids and section headings from these lists (snapshots and commits in
[`refs/lists/SOURCES.md`](refs/lists/SOURCES.md)). They are broader than this radar; go there for coverage.

- [harooos/awesome-coding-agents-for-robot-learning](https://github.com/harooos/awesome-coding-agents-for-robot-learning)
- [kairunwen/Awesome-Robot-Use-Agent](https://github.com/kairunwen/Awesome-Robot-Use-Agent)
- [chonghanqin/Awesome-Agentic-Robots](https://github.com/chonghanqin/Awesome-Agentic-Robots)
- [xwzhang221/Awesome-Agentic-Robot-Policies](https://github.com/xwzhang221/Awesome-Agentic-Robot-Policies)
- [dongqianyu99/Awesome-Agentic-Embodided-Systems](https://github.com/dongqianyu99/Awesome-Agentic-Embodided-Systems)
- [mindorigin150/awesome-fm-driven-embodied-agents](https://github.com/mindorigin150/awesome-fm-driven-embodied-agents)
- [wisdom-pan/embodied-agent-harness](https://github.com/wisdom-pan/embodied-agent-harness)
- [YennNing/Awesome-Code-as-Agent-Harness-Papers](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers)
- [lobehub/awesome-rsi](https://github.com/lobehub/awesome-rsi)

## Credits and license

MIT (see [LICENSE](LICENSE)).
- **Base pipeline** cloned from [CUA Radar](https://github.com/CrepuscularIRIS/cua-architecture-radar), itself cloned
  from [HarnessRSI Daily](https://github.com/CrepuscularIRIS/HarnessRSI-Daily), built on
  [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) (MIT).
- **Pattern induction** with the Open Scientist plugin (domain build `embodied-agent-harness` v1, kept locally).
- **Corpus sources:** the nine lists above (arXiv ids and section headings only).
