# Anti-patterns — failure-prone moves in embodied agent-harness research

Source: `antipatterns.json` of the frozen domain `embodied-agent-harness/v1` (130 qualitative candidates, status `no_outcome_labels`). The candidates — the When-it-fails lines of the domain cards — are grouped below into recurring moves AP1–AP21. Board-induced sub-patterns R01–R07 (2026-10-21, from the wave-1 weak fits; not from the frozen domain) add their 30 When-it-fails lines: 23 under existing anti-patterns where the move is identical, and 7 forming AP22–AP24. These are reading-derived candidates, **not statistics**: no acceptance or outcome contrast backs them. Every candidate appears under exactly one anti-pattern, quoted verbatim with its card and citations. Expectation ids `E..` are from the domain's `profile/expectations.json`.

**Scoring note.** AP1, AP2, AP3, AP4, AP5 and AP23 are recorded but not penalised by `score.py` (`AP_INFO_ONLY`): each is a pure duplicate of evidence items in `research/EVIDENCE_SCHEMA.md` that already price it (AP1 `strong_baselines`; AP2 `component_ablation`; AP3 `variance`; AP4 `held_out_env`; AP5 `cost_reported`, `budget_matched`; AP23 `online_eval`). The other anti-patterns name domain-specific moves that no evidence item checks.

## AP1 — Harness credited without holding the model fixed

**Failure mode.** Crediting a harness, interface or planner hierarchy for a gain when the baselines run a different backbone, the compared systems also differ in serving, context handling or action interface, or the planner backbone alone swings the result.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs](main/planner_composes_code_and_policies.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md), [Train the High-Level VLM That Commands a Low-Level Policy](main/trained_vlm_vla_hierarchy.md), [Write the Policy as Code and Rewrite It from Trial Diagnostics](main/code_policy_trial_revision.md)

**Reviewer expectations that catch it.** E01, E08

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`strong_baselines`).

**Evidence (7 candidates; 3 board-induced).**
- [K104](sub/K104.md): Errors concentrate on fine-grained grasping and placement; agentic baselines may not be model-fixed (2609.10522#s1)
- [K107](sub/K107.md): Planner backbone swings results with the harness fixed; Composite-Unseen stays at 13.8-15%; no ablation of analytic primitives vs vla_act; open loop between planner and VLA (2607.08448#s1)
- [K108](sub/K108.md): Two checkpoints differ in more than reasoning; association not mechanism; one backbone family (2608.03327#s1)
- [K803](sub/K803.md): Serving and context handling differ across harnesses, so complete systems are compared; workflow vs agent confounded with action interface (2607.26148#s3)
- [R02](sub/R02.md): Baselines differ in more than the trained high level: the frontier high-level baseline is not fine-tuned on the robot data, and a comparison with an on-device model family is not like-for-like; over 90% of development evaluation episodes ran in simulation (2502.19417#board, 2510.03342#board)
- [R05](sub/R05.md): Convergence claims mix incomparable settings: the headline iteration reduction (2.42 -> 1.76) compares two benchmarks run with different planners; tasks whose skill is missing from the library stay at 0% (2508.02629#board)
- [R07](sub/R07.md): Multi-agent results are compared with single-agent baselines: a subtask counts as solved if either of two agents reaches the goal, ablations use 50 val_seen episodes rather than val_unseen, and the single-agent SR is reported as both 38.6 and 32.0 (2603.18210#board)

## AP2 — Component gains credited from bundle-level, cumulative or missing ablations

**Failure mode.** Attributing an improvement to one harness component (depth tool, memory, skill library, gate, rewriting step) when the evidence is a bundle comparison, a cumulative A -> +B -> +C stack, or no ablation of that component at all.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs](main/planner_composes_code_and_policies.md), [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Build Context, Notes and Skills with the Weights Frozen](main/harness_memory_skill_reuse.md), [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Train the Policy Through, or Aligned with, the Deployment Harness](main/harness_native_rl.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md), [Let a Solver Plan from an LLM-Written Formal Model](main/llm_symbolic_solver_planning.md), [Allocate and Repair Multi-Robot Plans with LLM Agents](main/multi_robot_llm_coordination.md)

**Reviewer expectations that catch it.** E02

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`component_ablation`).

**Evidence (15 candidates; 3 board-induced).**
- [K102](sub/K102.md): Paired comparison changes perception, memory, motion and completion feedback together (18 trials); benchmark conditions overlap with harness development (2609.29389#s1)
- [K103](sub/K103.md): No per-component ablation (contact views vs rehearsal vs drag correction); failures from cross-view grasp misjudgment, losing object identity, premature completion; bounded by the backbone's multi-view integration (2609.29964#s1)
- [K104](sub/K104.md): Scene graph cannot bind transient or compositional semantics; sparse VLM verification misses cues; no harness-component ablation (2606.27871#s1)
- [K105](sub/K105.md): Composition, persistent state and selective feedback are not isolated; many code-only successes are tool-calling budget exhaustion (2610.01939#s1)
- [K109](sub/K109.md): No VLM backbone ablation, so the gain is not separated from the converter's own capability; wall time roughly doubles; insertion/pouring remain brittle (2603.22435#s1)
- [K201](sub/K201.md): Contribution of proposal validation alone is not ablated (2609.15195#s1)
- [K301](sub/K301.md): Cumulative single-run ablation; graph adds only +1 SR on ObjectNav (2609.15195#s2)
- [K302](sub/K302.md): Memory ablation on one suite with one planner; task vs global memory not separated; Composite-Unseen stays low; bootstrapping needs resets per task (2607.08448#s2)
- [K303](sub/K303.md): No ablation of the Reviewer or human-teaching component; single evaluation per setting (2609.29964#s2)
- [K502](sub/K502.md): Recipes differ in content and coverage, so rewriting is not isolated; evaluation on the same tasks with new initial states (2610.28589#s1)
- [K706](sub/K706.md): Cumulative ablation, single evaluation (2610.15572#s3)
- [K801](sub/K801.md): 7.80x ratio not universal; harnesses cumulative, per-layer contributions not isolated (2605.23950#s1)
- [R01](sub/R01.md): Human repair carries the pipeline and is not separated: a human confirms validation and hand-fixes knowledge bases that do not plan, there is no end-to-end success without that repair, the repair loop is not ablated, and the real robot is a demo (2502.19135#board)
- [R03](sub/R03.md): The validator and the allocator are not separated: the precondition validator is never ablated on its own, constraint violations and hallucinated actions still occur, and success stays below a reflection baseline (transport rate 79.17 vs 87.00) (2509.24230#board)
- [R04](sub/R04.md): Retraining gains are not separated from data volume: each iteration adds 50 samples with no equal-data manual control, long-horizon results are figure-only, and the VLM success judge is not validated (2603.11558#board)

## AP3 — Thin evaluation: single runs, 100-episode subsets, a handful of trials

**Failure mode.** Resting comparisons on one run per setting, a 100-episode or 18-trial subset, one task or two, or one seed, so that differences of a few points sit within noise.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Build Context, Notes and Skills with the Weights Frozen](main/harness_memory_skill_reuse.md), [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md), [Let a Solver Plan from an LLM-Written Formal Model](main/llm_symbolic_solver_planning.md), [Train the High-Level VLM That Commands a Low-Level Policy](main/trained_vlm_vla_hierarchy.md), [Allocate and Repair Multi-Robot Plans with LLM Agents](main/multi_robot_llm_coordination.md), [Sample Candidate Actions and Let a Verifier Choose](main/sample_verify_select.md)

**Reviewer expectations that catch it.** E04, E06

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`variance`).

**Evidence (15 candidates; 5 board-induced).**
- [K101](sub/K101.md): 100-episode subsets, mostly single runs; no harness ablation in the reasoning-effort VLN-CE study (2607.26148#s1, 2609.29861#s1)
- [K110](sub/K110.md): Iterative search makes agents page exhaustively; too small or too large windows hurt; ablations single-run on one model; authors leave transfer beyond programmatic tasks open (2405.15793#s1)
- [K301](sub/K301.md): Only the automatic context window is ablated, on 18 cases single-run (2609.29389#s3)
- [K501](sub/K501.md): RL shown on two tasks only; sequential observe-reason-act loop limits responsiveness to fast scenes (2606.18363#s3)
- [K601](sub/K601.md): Selection-rule ablation on one task with small numbers (2609.32416#s3)
- [K604](sub/K604.md): Smoothing is proof-of-concept on two tasks and vanishes under deterministic dynamics (2510.03207#s2)
- [K801](sub/K801.md): 50 tasks, most differences within noise; turn-budget asymmetry (2607.22585#s1)
- [K801](sub/K801.md): Intervals 11-17 pp wide; post-hoc workload split; coding only (2609.11987#s1)
- [K802](sub/K802.md): Single benchmark, no seed variance (2609.20822#s3)
- [K803](sub/K803.md): Single runs without variance (2609.15195#s4)
- [R01](sub/R01.md): Evidence rests on small own benchmarks and single runs: 42 tasks with an ablation row equal to the baseline row on all six numbers, 49 tasks with one run, 50 tasks with one run, 30 problems per domain in simulation (2601.11063#board, 2603.08814#board, 2603.02669#board, 2510.25548#board)
- [R02](sub/R02.md): Real-world evidence is thin: the real-world check of the correction loop is one drawer task with 20 corrections, after training on 3,644 online human interventions and 7,365 offline annotations besides 6,378 expert demonstrations (2504.14588#board)
- [R03](sub/R03.md): Results are figure-only or on tiny own benchmarks: mean rewards over 30 episodes appear only in figures on the authors' own task with qualitative software-in-the-loop checks; 4 scenarios x 5 runs with one LLM (2507.01378#board, 2602.06967#board)
- [R06](sub/R06.md): Ablations and real tests are small: a 90-pair subset from 8 scans without variance; 10 real trials per task (2601.18492#board, 2506.17811#board)
- [R07](sub/R07.md): Evidence is one 100-episode run, far below supervised methods (52-60 SR), with a single-step undo and a collision figure in the text that does not match the table (2503.10069#board)

## AP4 — Evaluation overlapping harness development, search, mining or training

**Failure mode.** Reporting gains on the tasks used to develop the harness, search harness candidates, mine skills or replay cards, or train the student (new seeds or initial states only), or without addressing benchmark contamination.

**Main patterns affected.** [Build Context, Notes and Skills with the Weights Frozen](main/harness_memory_skill_reuse.md), [Revise the Harness Itself from Execution Traces](main/harness_self_optimization.md), [Make Sparse-Success Embodied RL Learnable](main/teacher_seeded_sparse_rl.md), [Let a Solver Plan from an LLM-Written Formal Model](main/llm_symbolic_solver_planning.md), [Write the Policy as Code and Rewrite It from Trial Diagnostics](main/code_policy_trial_revision.md), [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md)

**Reviewer expectations that catch it.** E17, E08

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`held_out_env`).

**Evidence (9 candidates; 3 board-induced).**
- [K302](sub/K302.md): Not shown for partially observable or novel tasks (2606.10267#s3)
- [K303](sub/K303.md): Single synthesis pass mined from the evaluation tasks; transfer to unseen tasks not ablated (2603.22435#s2)
- [K304](sub/K304.md): Best card selected on the reporting seeds (optimistic); new subgoals or recovery need online planning; tasks without a successful source trace score 0 (2607.08448#s3)
- [K401](sub/K401.md): Only one proposer studied; TerminalBench-2 search equals test; component contributions not ablated (2603.28052#s1)
- [K401](sub/K401.md): Navigation gains measured on the same recurring tasks with ground-truth feedback; EQA non-monotonic across passes (2609.39207#s3)
- [K704](sub/K704.md): No held-out evaluation (2609.27308#s4)
- [R01](sub/R01.md): Settings are tuned on the evaluation problems: the re-prompt threshold is picked per domain by fewest failures and prompts are optimised on the tasks they are scored on (2510.25548#board, 2602.21670#board)
- [R05](sub/R05.md): Rewriting and scoring use the same task instances, with no held-out split; the trial counts behind the 91% are not stated; 3 simulated tasks only (2603.04466#board)
- [R07](sub/R07.md): Settings are tuned on the evaluation tasks: the advice threshold is swept on the same tasks it is reported on, which are 605 of 2,420 tasks (25%) in a single run without variance (2505.08765#board)

## AP5 — Cost, latency and interaction budget left unpriced or unmatched

**Failure mode.** Comparing harnesses, teachers or students without per-episode calls, tokens, latency and dollars (including failed trials), or at unequal compute, call or turn budgets.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Generate Supervision with a Privileged Teacher the Student Cannot See](main/privileged_teacher_supervision.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md), [Let a Solver Plan from an LLM-Written Formal Model](main/llm_symbolic_solver_planning.md), [Allocate and Repair Multi-Robot Plans with LLM Agents](main/multi_robot_llm_coordination.md), [Sample Candidate Actions and Let a Verifier Choose](main/sample_verify_select.md)

**Reviewer expectations that catch it.** E05, E22

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`cost_reported`, `budget_matched`).

**Evidence (8 candidates; 3 board-induced).**
- [K101](sub/K101.md): High inference cost and 3-19 s latency per call; benchmark contamination of proprietary models not verifiable (2607.26148#s1, 2609.29861#s1)
- [K204](sub/K204.md): Bundle-level ablation only; compute not matched (extra GPU); single run per task (2609.27308#s2)
- [K506](sub/K506.md): Real failures from contact mismatch; with 3x budget a full-state flow clone closes much of the gap; most pixel-BC cells single-seed (2609.34018#s1)
- [K601](sub/K601.md): Verification cost grows linearly with audited events (>=4,192 suffix rollouts for 19 admissions) (2609.32416#s1)
- [K805](sub/K805.md): 58 runs without usage records; cache-write pricing uncertain ~2x; truncation probe inconclusive (2609.11987#s3)
- [R01](sub/R01.md): Planning time grows and is partly left out: 173 s vs 32 s without prompt optimisation; 62.27 s vs 12.83 s for direct LLM planning; the reported planning time excludes VLM prompting (2602.21670#board, 2603.08814#board, 2510.25548#board)
- [R03](sub/R03.md): Coordination is slow: about 15 s per LLM call on one GPU for the tuned 7B model, and the frontier-API baseline is confounded by API latency (2507.01378#board)
- [R06](sub/R06.md): Latency grows with the candidate count and is partly unreported: 16 candidates take 650 ms and the real system runs at about 1.5 Hz; the K x P verification overhead is not timed (2506.17811#board, 2601.18492#board)

## AP6 — Proxy checks treated as success

**Failure mode.** Relying on a gate, completion detector, entropy or discriminator gate, agreement matcher or validity filter as if passing it meant task success, without measuring its false positives and false negatives.

**Main patterns affected.** [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md), [Let a Solver Plan from an LLM-Written Formal Model](main/llm_symbolic_solver_planning.md), [Sample Candidate Actions and Let a Verifier Choose](main/sample_verify_select.md)

**Reviewer expectations that catch it.** E16, E20, E11

**Evidence (11 candidates; 2 board-induced).**
- [K201](sub/K201.md): Catches only syntax-level errors: 52% of unresolved instances are wrong implementations the linter misses (2405.15793#s2)
- [K201](sub/K201.md): Stop gate passes outside the success region (fresh depth 1.20 m vs goal distance 2.15 m) and near wrong endpoints; OSR-SR gap 19.0 on HM3D-OVON (2609.15195#s3)
- [K201](sub/K201.md): Box-only verifier on an approximately measured scene misses unmodeled constraints; small gain for GPT-5.5 on Level II (2609.20822#s1)
- [K202](sub/K202.md): High false-positive rates collapse performance; correlated false negatives can stall a command; long fixed horizons cause timeouts (2606.10267#s1)
- [K603](sub/K603.md): Early discriminator errors misclassify; too strong a discriminator increases aliasing; only small 3-4 goal tasks (2505.09546#s1)
- [K603](sub/K603.md): Entropy conflates uncertainty with multimodality; continuous VLM actions poor; a random teacher degrades (2609.01567#s1)
- [K608](sub/K608.md): Only successful reference prefixes supervised; exact-match verifier needs a reference action, unavailable in open-ended embodied control (2610.20261#s1)
- [K609](sub/K609.md): Agreement is not correctness; matcher errors; few matches when decisions are dispersed; students far below teachers (37.7 vs 71.2) (2610.19820#s1)
- [K610](sub/K610.md): Cannot remove valid-but-incorrect positives (2610.02858#s2)
- [R01](sub/R01.md): An LLM validation gate is sycophantic: a weaker open model accepts all three deliberately invalid specifications and yields no feasible knowledge base (2502.19135#board)
- [R06](sub/R06.md): The verifier is trained or scored on a proxy: the reward model ranks by distance to the demonstration action, a proxy for success, and the scaling argument assumes an oracle verifier against ground-truth error (2506.17811#board)

## AP7 — Stopping and endpoint failures left undiagnosed or decomposed only descriptively

**Failure mode.** Reporting success rate without separating never-reached from reached-but-wrong-stop, false completion and stuck runs, or presenting a failure taxonomy as causal when it is co-movement with no intervention.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Make Sparse-Success Embodied RL Learnable](main/teacher_seeded_sparse_rl.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E16

**Evidence (10 candidates; 1 board-induced).**
- [K101](sub/K101.md): Residual failures are wrong target/route and wrong stop; target-visible ObjectNav failures (2607.26148#s1)
- [K101](sub/K101.md): Stuck forward batches with pixel-identical views and inconsistent recovery; episodes entering the goal radius but stopping elsewhere; 8/100 tasks fail in all six runs (2609.29861#s1)
- [K604](sub/K604.md): Early termination remains dominant (21-37%); reconnect-chunk collisions unanalysed; single seed (2610.21450#s1)
- [K708](sub/K708.md): Late termination increases; stop timing remains the main residual failure; no real aircraft (2610.21450#s2)
- [K804](sub/K804.md): Metrics not estimated on any grid; attribution is co-movement (2605.23950#s2)
- [K804](sub/K804.md): No-action turns are a proxy; 20% manually reviewed (2607.22585#s2)
- [K804](sub/K804.md): Category assignment procedure unspecified (2606.14674#s3)
- [K804](sub/K804.md): Does not identify causes or test interventions (2609.29861#s2)
- [K804](sub/K804.md): Cannot tell when a correct patch first existed (2609.11987#s2)
- [R04](sub/R04.md): Open discovery produces false completions: under service discovery the agent marks the task done without the needed calls, sometimes without executing anything (2603.18520#board)

## AP8 — Tool or harness value measured at one backbone strength assumed general

**Failure mode.** Treating a tool's or harness's measured gain as general (or as transferring to a compact student) when it was measured on one backbone and the read evidence shows the same tool helping weak models and not strong ones.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E03, E09

**Evidence (5 candidates).**
- [K108](sub/K108.md): The same tool can help weak and not strong models: tool effects interact with the backbone; several settings single runs (2607.26148#s2)
- [K802](sub/K802.md): Ablations on base models only, not the student (2606.18363#s1)
- [K802](sub/K802.md): Best module environment-dependent; small suites, missing cells (2606.14674#s1)
- [K802](sub/K802.md): Magnitude varies across model-interface pairs; two tasks (2610.12549#s2)
- [K803](sub/K803.md): Harness gain varies 6-22 SR with backbone; no cost reported (2606.10577#s4)

## AP9 — Low-level executor assumed reliable below the interface

**Failure mode.** Building a planner interface on a VLA, learned tool or hierarchy and assuming the executor is competent outside its training distribution, follows edited instructions, or makes the planner's gains independent of invocation fidelity.

**Main patterns affected.** [Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs](main/planner_composes_code_and_policies.md), [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E07, E02

**Evidence (5 candidates).**
- [K106](sub/K106.md): Invocation-aligned post-training first reduced pi0.5 (93.4 -> 91.2); primitives absent from data need new demos; progress target is a temporal proxy (2605.13119#s1)
- [K106](sub/K106.md): Trained for atomic behaviours, not global exploration; object search needs a separate planner (2609.39207#s2)
- [K107](sub/K107.md): Tool access without guidance gives 0% on the real robot; instruction/attention edits unreliable on task-specific fine-tuned pi0.5 (2609.33378#s1)
- [K202](sub/K202.md): Planner never trained; one robot/camera real study; planner gains depend on executor invocation fidelity (2605.13119#s2)
- [K803](sub/K803.md): Hierarchy components swing success from ~95% to ~0% even with a near-perfect VLA proxy (2606.10267#s4)

## AP10 — Persistent state trusted without re-verification

**Failure mode.** Carrying maps, labels or task-progress records forward across steps and acting on them without re-checking against fresh observations.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Build Context, Notes and Skills with the Weights Frozen](main/harness_memory_skill_reuse.md)

**Reviewer expectations that catch it.** E02, E16

**Evidence (3 candidates; 1 board-induced).**
- [K102](sub/K102.md): Map missed a fallen object's new location; stale labels confused assessment; map ablation removes it from execution and diagnosis together (2610.12549#s3)
- [K301](sub/K301.md): A task-progress record can propagate a wrong judgement (authors' interpretation, untested) (2606.10577#s3)
- [R04](sub/R04.md): State shared between LLM agents drifts: two LLM agents occasionally disagree about the embodiment, and making LLM agents responsible for mission-state synchronisation causes inconsistencies (2505.07532#board)

## AP11 — Geometry, contact and embodiment assumptions that hold only in simulation

**Failure mode.** Assuming calibrated metric depth, visible valid-depth targets, contact feedback and realized motion — or reporting real-robot transfer qualitatively — when these are untested outside the simulator.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs](main/planner_composes_code_and_policies.md), [Write the Policy as Code and Rewrite It from Trial Diagnostics](main/code_policy_trial_revision.md)

**Reviewer expectations that catch it.** E20, E19

**Evidence (7 candidates; 1 board-induced).**
- [K101](sub/K101.md): On a physical Go2: no body awareness, under-rotation without realized-motion feedback, weak persistent spatial state (2607.26148#s1)
- [K102](sub/K102.md): Behaviour with non-metric or scene-dependent depth scaling is untested (2606.10577#s2)
- [K102](sub/K102.md): Articulated/multi-stage contact lower (63.3%), two-arm handover 5% (2609.29389#s1)
- [K103](sub/K103.md): Targets restricted to visible pixels with valid depth; single run, 100 episodes, no variance (2606.10577#s1)
- [K105](sub/K105.md): Contact without feedback (button presses) and tight fits remain unsolved where pretrained policies reach 83-96% (2610.01939#s2)
- [K105](sub/K105.md): Real humanoid tasks take 10-20 min and are qualitative (2609.39207#s1)
- [R05](sub/R05.md): Perception is emulated or simulated: swarm robots get positions from an indoor positioning system rather than onboard sensing; no member rewrites code on a real robot from real failures (2503.23875#board, 2508.02629#board)

## AP12 — Revisions or corrections accepted by point-estimate gates on small validation sets

**Failure mode.** Accepting harness edits, playbooks, co-evolution steps or teacher patches by a strict-improvement rule on a few dozen reused validation tasks, without significance, overfitting checks or the count of rejected proposals.

**Main patterns affected.** [Revise the Harness Itself from Execution Traces](main/harness_self_optimization.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md)

**Reviewer expectations that catch it.** E18, E17, E04

**Evidence (7 candidates).**
- [K401](sub/K401.md): Best search-set harness not always best held-out; held-out can plateau or decline (2610.08432#s1)
- [K401](sub/K401.md): In manipulation the shared harness stays below separately optimized ones (2610.08432#s2)
- [K402](sub/K402.md): Acceptance rule does not guarantee termination; initial unrefined playbook hurts the recipient; real-robot playbook had to be adapted by the teacher; small eval sets (2609.33378#s2)
- [K403](sub/K403.md): Progress not monotonic: weight stages can reduce validation score; one training run per condition; text/tool tasks only (2609.37105#s1)
- [K403](sub/K403.md): Validation reuse across rounds risks adaptive selection; strict-improvement gate on noisy point estimates; 53-58 validation tasks (2609.37105#s2)
- [K403](sub/K403.md): Acceptance is not a significance test; extra rollouts plus teacher calls; 184-rollout comparisons would be far costlier in embodied settings (2610.28069#s2)
- [K601](sub/K601.md): Large trainer-seed variance; a thin admission regressed 76% -> 58%; pooling tasks causes interference (2609.32416#s2)

## AP13 — Student bounded by teacher coverage and competence

**Failure mode.** Training on success-filtered teacher trajectories, teacher-visited states or a teacher that is weak where the student fails, then claiming student generalization beyond what the teacher covered.

**Main patterns affected.** [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Generate Supervision with a Privileged Teacher the Student Cannot See](main/privileged_teacher_supervision.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md), [Train the Policy Through, or Aligned with, the Deployment Harness](main/harness_native_rl.md)

**Reviewer expectations that catch it.** E10, E11, E09

**Evidence (10 candidates).**
- [K501](sub/K501.md): Held-out-task accuracy modest (13.9%); simulation only; success-filtered teacher data only (2609.29389#s2)
- [K504](sub/K504.md): Recovery supervision comes from teacher-visited perturbed states, not student-induced states (2606.18363#s2)
- [K504](sub/K504.md): Only six tasks reach VLA training; pipeline never run end to end; real full-task success 20%; no on-policy correction (2609.27308#s3)
- [K505](sub/K505.md): Generalization bounded by teacher data diversity; real robot 38%; only short single-room navigation; no on-policy correction (2610.15572#s1)
- [K601](sub/K601.md): Teacher quality limits data yield; 5K -> 10K SFT data no gain (2509.14257#s1)
- [K601](sub/K601.md): Weaker editor teachers give weaker students; student about half teacher success; live web below 8% (2610.19834#s1)
- [K602](sub/K602.md): Weaker reviewers net harmful (-12.0 pp Qwen3.6-35B-A3B replacing 66% of steps); latency roughly doubles; context management not expressible (2609.24974#s1)
- [K603](sub/K603.md): AWBC no consistent benefit; direct VLM performance does not predict teacher usefulness (2609.01567#s2)
- [K605](sub/K605.md): Student ceiling is the teacher; not applicable to black-box API teachers; cross-interface untested (2603.26666#s1)
- [K701](sub/K701.md): RL adds 5.9 pp over SFT; Goal/Spatial stay low where the teacher rarely succeeds; 2,304 episodes up to 7,200 s each (2610.28589#s2)

## AP14 — Privileged supervision without an identifiability check

**Failure mode.** Supervising a student with simulator ground truth, privileged contact or execution, or privileged-context actions without checking that the student can recover that information from its own observations.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Generate Supervision with a Privileged Teacher the Student Cannot See](main/privileged_teacher_supervision.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md), [Sample Candidate Actions and Let a Verifier Choose](main/sample_verify_select.md)

**Reviewer expectations that catch it.** E12

**Evidence (7 candidates; 1 board-induced).**
- [K109](sub/K109.md): Best variant relies on privileged contact info (2606.10267#s2)
- [K501](sub/K501.md): Mixing teachers hurt; privileged execution during collection leaves real-executor states uncovered; no on-policy correction (2606.27871#s2)
- [K503](sub/K503.md): Multi-step tasks unsupported; top-down grasp fits boxes; privileged inputs replaced by learned perception untested (2609.21650#s1)
- [K505](sub/K505.md): No check whether templated privileged descriptions (e.g. out-of-view direction) are identifiable from student observations (2610.15572#s2)
- [K604](sub/K604.md): Theory tabular with synthetic noise; active information gathering unexplored; belief contraction does not predict RL suboptimality (dog-walk) (2510.03207#s1)
- [K608](sub/K608.md): Gains smaller than with external teachers; identifiability of privileged-guided actions not analysed (2610.19820#s3)
- [R06](sub/R06.md): Supervision comes from a frontier model with privileged information: task specifications are generated by a frontier model and the SFT data are privileged, on the authors' own benchmarks with low absolute success (2602.21198#board)

## AP15 — Internalization claimed while deployment keeps teacher or harness parts

**Failure mode.** Claiming the student absorbed the harness while frontier sub-agents or planners stay in the loop at evaluation, or without evaluating the student with the components removed.

**Main patterns affected.** [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E21, E09

**Evidence (4 candidates).**
- [K501](sub/K501.md): Sub-agents remain frontier calls, so the student does not run standalone; OOD only new seeds (2609.29964#s3)
- [K502](sub/K502.md): Without the frontier planner the student fails reasoning-intensive tasks (10%); 1B students over-adjust; distillation of plugin context not studied (2609.10522#s3)
- [K602](sub/K602.md): Deep domain knowledge internalized less (30.0 vs 38.0) (2609.24974#s2)
- [K802](sub/K802.md): Internalization interpretation suggestive; ALFWorld only (2610.02858#s3)

## AP16 — Distillation objective weighting and schedule left fragile

**Failure mode.** Reporting one weighting or schedule of KL, state and action losses when the read evidence shows collapse under abrupt switches, staged schedules, near-zero or excessive KL, or hard relabels.

**Main patterns affected.** [Generate Supervision with a Privileged Teacher the Student Cannot See](main/privileged_teacher_supervision.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md)

**Reviewer expectations that catch it.** E11, E12

**Evidence (5 candidates).**
- [K506](sub/K506.md): Weighting task-dependent; abrupt switch or flat action weight collapses; action-only converges 1/3 seeds (2609.34018#s2)
- [K605](sub/K605.md): Objective ablation on one task, curves only; hard-CE (black-box-style relabel) weakest (2603.26666#s2)
- [K606](sub/K606.md): Excessive KL overrides utility; OOD degradation on Qwen3-4B (2602.04942#s2)
- [K607](sub/K607.md): Teacher-only training collapses when KL nears zero; student-only fails with negative privilege utility; no single best alpha (2602.04942#s1)
- [K607](sub/K607.md): T+I or T+R alone leave success unchanged; staged schedules degrade; per-harness rebuild needed (2610.20261#s2)

## AP17 — Reset, snapshot or fork access assumed

**Failure mode.** Building correction, verification or RL on replay, snapshot restore, held states or per-step forking, then presenting it as applicable where state cannot be restored cheaply or episodes are single-shot.

**Main patterns affected.** [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Make Sparse-Success Embodied RL Learnable](main/teacher_seeded_sparse_rl.md)

**Reviewer expectations that catch it.** E05, E11

**Evidence (5 candidates).**
- [K203](sub/K203.md): Adds inference and interaction overhead; bounded by onboard perception errors and unreachable viewpoints; probing gives no hardware safety; Cabinet still 40%; not applicable to single-shot real episodes (2610.12549#s1)
- [K609](sub/K609.md): State-group rollout makes visitation off-policy (2610.19820#s2)
- [K611](sub/K611.md): Not reported for long-horizon or non-replayable environments; reward scale tuned on a small search (2509.14257#s2)
- [K611](sub/K611.md): Longer training; struggles in large exploration spaces; not tested with visual policies (2505.09546#s2)
- [K705](sub/K705.md): Per-step bandit-like RL, not full-episode credit; requires forking; text/table SR mismatch (2606.27871#s3)

## AP18 — Sparse binary reward with zero-signal groups and coarse credit

**Failure mode.** Running group RL on binary success where many groups are all-0 or all-1, credit is assigned only at rollout level, and noisy or absent reward is not reported.

**Main patterns affected.** [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md), [Train the Policy Through, or Aligned with, the Deployment Harness](main/harness_native_rl.md), [Make Sparse-Success Embodied RL Learnable](main/teacher_seeded_sparse_rl.md)

**Reviewer expectations that catch it.** E13

**Evidence (7 candidates).**
- [K606](sub/K606.md): If all resamples fail the gate, no hindsight signal (2608.06065#s2)
- [K702](sub/K702.md): Only 3 training steps profiled; cross-chain credit out of scope (2605.24220#s2)
- [K702](sub/K702.md): Within-rollout credit left open; token-mean unstable with long negative samples; single seed (2608.17528#s2)
- [K703](sub/K703.md): Zero-variation groups grow as the policy improves; defenses cover only observed failures; binary reward cannot credit recovery (2608.17393#s2)
- [K704](sub/K704.md): Far below GPT-6 Astra; more give-ups; no claim of manipulation skill; single run (2610.01939#s3)
- [K704](sub/K704.md): Three simple tasks, per-task training; S2 rewards noisy enough for credit-assignment ambiguity (2603.22435#s4)
- [K708](sub/K708.md): Coverage correlation not isolated; SFT forgetting; below teacher on two tasks; real closed-loop failed (2609.21650#s2)

## AP19 — Training scaffold differs from the deployment harness or context rules

**Failure mode.** Training under one harness, context-compaction or prompt format and deploying (or claiming transfer) under another, or dropping the rewritten spans the deployment harness produces.

**Main patterns affected.** [Train the Policy Through, or Aligned with, the Deployment Harness](main/harness_native_rl.md)

**Reviewer expectations that catch it.** E14

**Evidence (6 candidates).**
- [K701](sub/K701.md): Small gain when the base is already harness-aligned (+0.6); SWE only (2605.24220#s1)
- [K701](sub/K701.md): Compacted or rewritten histories are dropped; each harness trained separately (2608.17393#s1)
- [K701](sub/K701.md): Cross-harness transfer not reported; single run (2608.17393#s3)
- [K702](sub/K702.md): Template non-compositionality, retokenize drift and tool-call reserialization break prefixes (2608.17528#s1)
- [K706](sub/K706.md): Drop rule discards the only visual evidence when a call fails semantically (2608.03327#s3)
- [K706](sub/K706.md): The summary-conditioned RL policy does not train with the exact deployment scaffold; differences may be within noise (2606.14674#s2)

## AP20 — Scorer or verifier state reachable by the policy

**Failure mode.** Letting the teacher or policy read or edit the grader, tests or full simulator state during training or data generation without reporting hack rates or ablating the defenses.

**Main patterns affected.** [Generate Supervision with a Privileged Teacher the Student Cannot See](main/privileged_teacher_supervision.md), [Train the Policy Through, or Aligned with, the Deployment Harness](main/harness_native_rl.md)

**Reviewer expectations that catch it.** E15

**Evidence (2 candidates).**
- [K503](sub/K503.md): Hardest tasks unsolved; poor visual grounding, over-commitment to a failing decomposition, scorer hacking (43% Sol, 39% Terra) (2609.27308#s1)
- [K703](sub/K703.md): Not ablated separately from the training objective (2608.17528#s4)

## AP21 — Text, SWE or tabular evidence taken as embodied evidence

**Failure mode.** Carrying a result from fully observable text, coding, tool-use or tabular settings to embodied control without testing partial observability, multimodal input, latency or irreversible actions.

**Main patterns affected.** [Revise the Harness Itself from Execution Traces](main/harness_self_optimization.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md), [Make Sparse-Success Embodied RL Learnable](main/teacher_seeded_sparse_rl.md)

**Reviewer expectations that catch it.** E12, E06, E07

**Evidence (5 candidates).**
- [K401](sub/K401.md): Trace-vs-score ablation only on text classification (2603.28052#s2)
- [K602](sub/K602.md): Ablation only on USPTO; single seed; text/tool domains, fully observable (2609.24974#s3)
- [K606](sub/K606.md): Gains not uniform per app; untested on long-horizon or partially observed physical tasks (2608.06065#s1)
- [K610](sub/K610.md): Gains small outside ALFWorld; untested on multimodal/embodied (2610.02858#s1)
- [K707](sub/K707.md): General skill bank does not help; single seed; software repair only (2610.28069#s1)

## AP22 — Symbolic domain, abstract state or full observability handed to the planner

**Failure mode.** Evaluating an LLM-plus-solver or multi-robot LLM planner with a hand-written planning domain, ground-truth abstracted states, full observability or the whole simulator state given as text, planning open loop without replanning after execution failures — so the perception, grounding and state-estimation errors that a deployed robot team would face never enter the result.

**Main patterns affected.** [Let a Solver Plan from an LLM-Written Formal Model](main/llm_symbolic_solver_planning.md), [Allocate and Repair Multi-Robot Plans with LLM Agents](main/multi_robot_llm_coordination.md)

**Reviewer expectations that catch it.** none in the frozen domain (closest: E08 on privileged action spaces, E20 on depth assumptions)

**Scoring.** Penalised by `score.py`: no evidence item checks whether the planner's symbolic state and domain are given rather than perceived.

**Evidence (2 candidates; 2 board-induced).**
- [R01](sub/R01.md): The symbolic domain and state are handed to the planner: ground-truth PDDL domains, abstracted states, full observability or the whole state as text, with open-loop plans and no replanning when execution fails (2601.11063#board, 2602.21670#board, 2503.01700#board, 2603.08814#board, 2603.02669#board)
- [R03](sub/R03.md): Simulator ground-truth states are given to the central planner, so perception and communication errors are not tested (2509.24230#board)

## AP23 — Plan text, offline accuracy or a judge's score reported in place of closed-loop task success

**Failure mode.** Supporting an embodied claim with offline planning or affordance accuracy, expert or LLM judgements of plan text, a VLA benchmark run underneath a middleware, or qualitative demonstrations, while the system's own closed-loop task success is never measured.

**Main patterns affected.** [Train the High-Level VLM That Commands a Low-Level Policy](main/trained_vlm_vla_hierarchy.md), [Allocate and Repair Multi-Robot Plans with LLM Agents](main/multi_robot_llm_coordination.md), [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md)

**Reviewer expectations that catch it.** E19 (closest; the evidence item `online_eval` prices it directly)

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): a pure duplicate of the evidence item `online_eval` (`partial`/`no` for open-loop, plan-text or qualitative evidence).

**Evidence (3 candidates; 3 board-induced).**
- [R02](sub/R02.md): Planning is scored offline: multi-robot planning, pointing and affordance accuracy on in-distribution synthetic data, with real-world deployment shown as demonstrations and no end-to-end success or ablation of the shared memory, scheduler or error correction (2505.03673#board)
- [R03](sub/R03.md): Success is judged on plan text or by experts, with no baseline numbers: correctness is scored by an expert on text plans, replanning is scored only when the initial plan was correct, and event filtering and status monitoring are not ablated (2511.22354#board)
- [R04](sub/R04.md): Agent-level task success is not measured: the middleware is validated by a VLA benchmark and qualitative cases, and the real robot study "emphasizes feasibility and runtime semantics rather than large-scale statistical performance"; the framework paper reports only qualitative outcomes (2512.10394#board, 2505.07532#board)

## AP24 — Classical or specialist controller left out of the comparison, or ahead of the method

**Failure mode.** Presenting an LLM-written or LLM-selected controller as effective without comparing it with the hand-tuned classical controller or trained specialist it would replace — or reporting that comparison only in a supplement where the classical or supervised system scores higher.

**Main patterns affected.** [Write the Policy as Code and Rewrite It from Trial Diagnostics](main/code_policy_trial_revision.md), [Sample Candidate Actions and Let a Verifier Choose](main/sample_verify_select.md)

**Reviewer expectations that catch it.** none in the frozen domain (closest: E07, which asks for frozen-VLA and agentic baselines)

**Scoring.** Penalised by `score.py`: not a pure duplicate of `strong_baselines`, which asks for same-kind baselines (the same backbone under another harness, end-to-end VLAs, teacher/student rows), not the non-LLM controller the method replaces.

**Evidence (2 candidates; 2 board-induced).**
- [R05](sub/R05.md): Baselines are missing or weaker than the classical controller: one study has no baseline at all, and in another hand-tuned flocking and assignment controllers score higher on average than the generated code (2603.04466#board, 2503.23875#board)
- [R06](sub/R06.md): Gains are far below trained specialists and small on another split: SR 52 vs 81 for a fully supervised navigator; +0.41 SR over a prior LLM navigator on RxR (2601.18492#board)
