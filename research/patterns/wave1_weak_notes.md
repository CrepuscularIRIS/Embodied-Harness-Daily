# Wave-1 weak fits — induction notes (partial, 2026-10-21)

Status: **induction complete (2026-10-21)**. All 60 weak papers were read in full text (group 5 below; groups 1–5 in
`wave1_notes/g1.md`–`g5.md`) and re-clustered into the board-induced sub-patterns
[R01](../../patterns/sub/R01.md)–[R07](../../patterns/sub/R07.md); per-paper outcomes are in `reassign_wave1.jsonl` and the
build-log entry in `research/PIPELINE.md`. The cluster table below is the pre-reading draft and is kept for reference:
clusters a, b, c, d, e, f and h became R01, R02, R03, R04, R05, R06 and R07 (with members moved after reading); g split
into two singletons.

## Candidate clusters (from the 60 fit notes; verify against full text before writing R cards)

| key | mechanism | example ids (from fit notes) |
|---|---|---|
| a | LLM translates the task into a symbolic planner / solver representation (PDDL, Prolog, SMT, scheduling graph, behaviour tree); solver gates or produces the plan; optional failure-feedback repair | 2502.19135, 2510.25548, 2601.11063, 2602.21670, 2603.02669, 2603.01113, 2503.01700 |
| b | trained high-level VLM planner driving a trained low-level VLA / skill policy (both trained; language or waypoint interface) | 2502.19417, 2505.03673, 2509.01106, 2510.03342, 2503.12533, 2504.14588, 2601.14681 |
| c | multi-agent / multi-robot LLM coordination (role split, grouping, negotiation, allocation) | 2602.06967, 2509.24230, 2511.22354, 2507.01485, 2511.01594, 2503.23875 |
| d | robot-agent middleware: ROS / MCP tool exposure, backend switching (system papers, often no evaluation) | 2505.07532, 2512.10394, 2603.18520, 2602.13591, 2603.11558 |
| e | LLM writes reward or controller code and revises it from trial traces / simulation | 2503.04280, 2603.04466, 2508.02629 |
| f | verifier- or self-critic-guided best-of-N over sampled policy actions (incl. test-time training from hindsight) | 2506.17811, 2602.21198 |
| g | memory write-gating / experience-based policy routing | 2601.20831, 2603.07892 |
| h | spatial maps rendered into the prompt as advice | 2505.08765, 2603.18210 |
| — | UAV LLM control systems mostly fit existing K104 weakly because evidence is qualitative | 2503.08302, 2504.21432, 2505.07236, 2506.07509 |

## Group-5 readings (10 papers, full text)

- **2601.20831 v1 MemCtrl** → (g). Trainable MLP gate keeps/discards each (obs, action) before it enters a frozen MLLM's memory; trained offline on GPT-4o success labels or online with REINFORCE. EB-ALFRED Qwen 4.7→14.2 (RL); Habitat 14.3→22.8. Fails: prompted untrained gate recovers much of the gain (Gemma ALFRED 28 vs 32.2); no keep-all baseline; no variance; gating hurts some subsets (Complex 38→32).
- **2602.04157 v1 situated HRC recipe** → K108 (good). Real-time LM calls 5 attention/perception tools; tool-decision Acc 0.72±0.10 (OpenAI) / 0.77±0.07 (Gemini); ablating object tools Acc 0.28. Fails: 24 videos, kappa 0.41, author-selected scenarios, no task-success metric; tool removal interacts with selection of others.
- **2602.04315 v1 GeneralVLA** → other (trained pointer → depth back-projection → frozen LLM waypoint path → classical executor; + lesson bank; + sim-filtered BC distillation). 14/14 RLBench tasks produce demos vs 10/9/7 for baselines; ASM ablation Open_box 35.33→8.67. Fails: lesson bank never ablated; baselines' missing data patched with system demos; real world 4 tasks.
- **2602.06967 v1 CLiMRS** → (c). Dynamic grouping + subgroup negotiation + executor-LLM feasibility check; CLiMBench SR 1.000 / 8.8 steps vs 0.700 / 15.8; w/o feedback SR 0.200. Fails: 4 scenarios × 5 runs, one LLM, baseline numbers copied; no SR gain on COHERENT (0.975 both).
- **2602.13591 v1 AgentRob** → (d). Forum agent + MCP tools + VLM controller over Go2/G1 primitives. No quantitative evaluation; safety only proposed.
- **2602.21198 v3 reflective test-time planning** → (f). Best-of-N with an internal reflector, hindsight external reflection, test-time training of policy and critic; 33.65% vs 11.20% (Self-Refine); w/o both reflections 10.40%. Fails: own benchmarks, GPT-5-generated specs and privileged SFT data, low absolute success; each half alone can be worse than neither.
- **2602.21670 v2 hierarchical LLM + PDDL + prompt optimization** → (a). Leaf agents write PDDL solved/validated by Fast Downward; failures drive TextGrad-style prompt edits; MAT-THOR SR 0.95/0.84/0.60 vs 0.93/0.77/0.45; single agent 0.25. Fails: full observability, ground-truth PDDL domains, prompts optimized on evaluation tasks (inferred), 173 s vs 32 s.
- **2602.23592 v2 KEEP** → other (KV-cache serving for embodied memory prompts; latency only, never beats full recompute 44.30 vs 44.63). Probably tier B/C, not a harness mechanism.
- **2603.01113 v3 MoA-assisted BT planning** → (a) + K202. LLM writes behaviour tree; expert-agent abstention cascade answers clarifications (ρ≈0.27); per-node trained policies with VLM condition nodes and bounded retry. Fails: no measured end-to-end success (analytic ≈0.34); VLM condition node not evaluated; one domain.
- **2603.02669 v1 IMR-LLM** → (a) without repair. LLM outputs operations/allocation/precedence compiled to a disjunctive graph solved by a heuristic scheduler; complex SR 0.68 vs 0.24; LLM-ordered w/o solver SR 0.00. Fails: own benchmark, one run, open loop, single-robot no gain.
