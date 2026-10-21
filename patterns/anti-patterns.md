# Anti-patterns — failure-prone moves in embodied agent-harness research

Source: `antipatterns.json` of the frozen domain `embodied-agent-harness/v1` (130 qualitative candidates, status `no_outcome_labels`). The candidates — the When-it-fails lines of the domain cards — are grouped below into recurring moves AP1–AP21. These are reading-derived candidates, **not statistics**: no acceptance or outcome contrast backs them. Every candidate appears under exactly one anti-pattern, quoted verbatim with its card and citations. Expectation ids `E..` are from the domain's `profile/expectations.json`.

**Scoring note.** AP1, AP2, AP3, AP4 and AP5 are recorded but not penalised by `score.py` (`AP_INFO_ONLY`): each is a pure duplicate of evidence items in `research/EVIDENCE_SCHEMA.md` that already price it (AP1 `strong_baselines`; AP2 `component_ablation`; AP3 `variance`; AP4 `held_out_env`; AP5 `cost_reported`, `budget_matched`). The other anti-patterns name domain-specific moves that no evidence item checks.

## AP1 — Harness credited without holding the model fixed

**Failure mode.** Crediting a harness, interface or planner hierarchy for a gain when the baselines run a different backbone, the compared systems also differ in serving, context handling or action interface, or the planner backbone alone swings the result.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs](main/planner_composes_code_and_policies.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E01, E08

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`strong_baselines`).

**Evidence (4 candidates).**
- [K104](sub/K104.md): Errors concentrate on fine-grained grasping and placement; agentic baselines may not be model-fixed (2609.10522#s1)
- [K107](sub/K107.md): Planner backbone swings results with the harness fixed; Composite-Unseen stays at 13.8-15%; no ablation of analytic primitives vs vla_act; open loop between planner and VLA (2607.08448#s1)
- [K108](sub/K108.md): Two checkpoints differ in more than reasoning; association not mechanism; one backbone family (2608.03327#s1)
- [K803](sub/K803.md): Serving and context handling differ across harnesses, so complete systems are compared; workflow vs agent confounded with action interface (2607.26148#s3)

## AP2 — Component gains credited from bundle-level, cumulative or missing ablations

**Failure mode.** Attributing an improvement to one harness component (depth tool, memory, skill library, gate, rewriting step) when the evidence is a bundle comparison, a cumulative A -> +B -> +C stack, or no ablation of that component at all.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs](main/planner_composes_code_and_policies.md), [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Build Context, Notes and Skills with the Weights Frozen](main/harness_memory_skill_reuse.md), [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Train the Policy Through, or Aligned with, the Deployment Harness](main/harness_native_rl.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E02

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`component_ablation`).

**Evidence (12 candidates).**
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

## AP3 — Thin evaluation: single runs, 100-episode subsets, a handful of trials

**Failure mode.** Resting comparisons on one run per setting, a 100-episode or 18-trial subset, one task or two, or one seed, so that differences of a few points sit within noise.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Build Context, Notes and Skills with the Weights Frozen](main/harness_memory_skill_reuse.md), [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E04, E06

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`variance`).

**Evidence (10 candidates).**
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

## AP4 — Evaluation overlapping harness development, search, mining or training

**Failure mode.** Reporting gains on the tasks used to develop the harness, search harness candidates, mine skills or replay cards, or train the student (new seeds or initial states only), or without addressing benchmark contamination.

**Main patterns affected.** [Build Context, Notes and Skills with the Weights Frozen](main/harness_memory_skill_reuse.md), [Revise the Harness Itself from Execution Traces](main/harness_self_optimization.md), [Make Sparse-Success Embodied RL Learnable](main/teacher_seeded_sparse_rl.md)

**Reviewer expectations that catch it.** E17, E08

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`held_out_env`).

**Evidence (6 candidates).**
- [K302](sub/K302.md): Not shown for partially observable or novel tasks (2606.10267#s3)
- [K303](sub/K303.md): Single synthesis pass mined from the evaluation tasks; transfer to unseen tasks not ablated (2603.22435#s2)
- [K304](sub/K304.md): Best card selected on the reporting seeds (optimistic); new subgoals or recovery need online planning; tasks without a successful source trace score 0 (2607.08448#s3)
- [K401](sub/K401.md): Only one proposer studied; TerminalBench-2 search equals test; component contributions not ablated (2603.28052#s1)
- [K401](sub/K401.md): Navigation gains measured on the same recurring tasks with ground-truth feedback; EQA non-monotonic across passes (2609.39207#s3)
- [K704](sub/K704.md): No held-out evaluation (2609.27308#s4)

## AP5 — Cost, latency and interaction budget left unpriced or unmatched

**Failure mode.** Comparing harnesses, teachers or students without per-episode calls, tokens, latency and dollars (including failed trials), or at unequal compute, call or turn budgets.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Generate Supervision with a Privileged Teacher the Student Cannot See](main/privileged_teacher_supervision.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E05, E22

**Scoring.** Recorded but not penalised by `score.py` (`AP_INFO_ONLY`): already priced by evidence items in `research/EVIDENCE_SCHEMA.md` (`cost_reported`, `budget_matched`).

**Evidence (5 candidates).**
- [K101](sub/K101.md): High inference cost and 3-19 s latency per call; benchmark contamination of proprietary models not verifiable (2607.26148#s1, 2609.29861#s1)
- [K204](sub/K204.md): Bundle-level ablation only; compute not matched (extra GPU); single run per task (2609.27308#s2)
- [K506](sub/K506.md): Real failures from contact mismatch; with 3x budget a full-state flow clone closes much of the gap; most pixel-BC cells single-seed (2609.34018#s1)
- [K601](sub/K601.md): Verification cost grows linearly with audited events (>=4,192 suffix rollouts for 19 admissions) (2609.32416#s1)
- [K805](sub/K805.md): 58 runs without usage records; cache-write pricing uncertain ~2x; truncation probe inconclusive (2609.11987#s3)

## AP6 — Proxy checks treated as success

**Failure mode.** Relying on a gate, completion detector, entropy or discriminator gate, agreement matcher or validity filter as if passing it meant task success, without measuring its false positives and false negatives.

**Main patterns affected.** [Gate, Monitor and Diagnose Actions Outside the Model](main/external_verification_control.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md)

**Reviewer expectations that catch it.** E16, E20, E11

**Evidence (9 candidates).**
- [K201](sub/K201.md): Catches only syntax-level errors: 52% of unresolved instances are wrong implementations the linter misses (2405.15793#s2)
- [K201](sub/K201.md): Stop gate passes outside the success region (fresh depth 1.20 m vs goal distance 2.15 m) and near wrong endpoints; OSR-SR gap 19.0 on HM3D-OVON (2609.15195#s3)
- [K201](sub/K201.md): Box-only verifier on an approximately measured scene misses unmodeled constraints; small gain for GPT-5.5 on Level II (2609.20822#s1)
- [K202](sub/K202.md): High false-positive rates collapse performance; correlated false negatives can stall a command; long fixed horizons cause timeouts (2606.10267#s1)
- [K603](sub/K603.md): Early discriminator errors misclassify; too strong a discriminator increases aliasing; only small 3-4 goal tasks (2505.09546#s1)
- [K603](sub/K603.md): Entropy conflates uncertainty with multimodality; continuous VLM actions poor; a random teacher degrades (2609.01567#s1)
- [K608](sub/K608.md): Only successful reference prefixes supervised; exact-match verifier needs a reference action, unavailable in open-ended embodied control (2610.20261#s1)
- [K609](sub/K609.md): Agreement is not correctness; matcher errors; few matches when decisions are dispersed; students far below teachers (37.7 vs 71.2) (2610.19820#s1)
- [K610](sub/K610.md): Cannot remove valid-but-incorrect positives (2610.02858#s2)

## AP7 — Stopping and endpoint failures left undiagnosed or decomposed only descriptively

**Failure mode.** Reporting success rate without separating never-reached from reached-but-wrong-stop, false completion and stuck runs, or presenting a failure taxonomy as causal when it is co-movement with no intervention.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Make Sparse-Success Embodied RL Learnable](main/teacher_seeded_sparse_rl.md), [Separate the Harness Effect from the Model Effect](main/harness_effect_evaluation.md)

**Reviewer expectations that catch it.** E16

**Evidence (9 candidates).**
- [K101](sub/K101.md): Residual failures are wrong target/route and wrong stop; target-visible ObjectNav failures (2607.26148#s1)
- [K101](sub/K101.md): Stuck forward batches with pixel-identical views and inconsistent recovery; episodes entering the goal radius but stopping elsewhere; 8/100 tasks fail in all six runs (2609.29861#s1)
- [K604](sub/K604.md): Early termination remains dominant (21-37%); reconnect-chunk collisions unanalysed; single seed (2610.21450#s1)
- [K708](sub/K708.md): Late termination increases; stop timing remains the main residual failure; no real aircraft (2610.21450#s2)
- [K804](sub/K804.md): Metrics not estimated on any grid; attribution is co-movement (2605.23950#s2)
- [K804](sub/K804.md): No-action turns are a proxy; 20% manually reviewed (2607.22585#s2)
- [K804](sub/K804.md): Category assignment procedure unspecified (2606.14674#s3)
- [K804](sub/K804.md): Does not identify causes or test interventions (2609.29861#s2)
- [K804](sub/K804.md): Cannot tell when a correct patch first existed (2609.11987#s2)

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

**Evidence (2 candidates).**
- [K102](sub/K102.md): Map missed a fallen object's new location; stale labels confused assessment; map ablation removes it from execution and diagnosis together (2610.12549#s3)
- [K301](sub/K301.md): A task-progress record can propagate a wrong judgement (authors' interpretation, untested) (2606.10577#s3)

## AP11 — Geometry, contact and embodiment assumptions that hold only in simulation

**Failure mode.** Assuming calibrated metric depth, visible valid-depth targets, contact feedback and realized motion — or reporting real-robot transfer qualitatively — when these are untested outside the simulator.

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs](main/planner_composes_code_and_policies.md)

**Reviewer expectations that catch it.** E20, E19

**Evidence (6 candidates).**
- [K101](sub/K101.md): On a physical Go2: no body awareness, under-rotation without realized-motion feedback, weak persistent spatial state (2607.26148#s1)
- [K102](sub/K102.md): Behaviour with non-metric or scene-dependent depth scaling is untested (2606.10577#s2)
- [K102](sub/K102.md): Articulated/multi-stage contact lower (63.3%), two-arm handover 5% (2609.29389#s1)
- [K103](sub/K103.md): Targets restricted to visible pixels with valid depth; single run, 100 episodes, no variance (2606.10577#s1)
- [K105](sub/K105.md): Contact without feedback (button presses) and tight fits remain unsolved where pretrained policies reach 83-96% (2610.01939#s2)
- [K105](sub/K105.md): Real humanoid tasks take 10-20 min and are qualitative (2609.39207#s1)

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

**Main patterns affected.** [Design the Frozen Model's Observation and Action Interface](main/observe_act_interface.md), [Distil Success-Filtered Teacher Harness Trajectories into a Compact Student](main/offline_harness_distillation.md), [Generate Supervision with a Privileged Teacher the Student Cannot See](main/privileged_teacher_supervision.md), [Correct, Review or Relabel at Learner-Induced States](main/learner_state_teacher_correction.md), [Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals](main/on_policy_distillation_objectives.md)

**Reviewer expectations that catch it.** E12

**Evidence (6 candidates).**
- [K109](sub/K109.md): Best variant relies on privileged contact info (2606.10267#s2)
- [K501](sub/K501.md): Mixing teachers hurt; privileged execution during collection leaves real-executor states uncovered; no on-policy correction (2606.27871#s2)
- [K503](sub/K503.md): Multi-step tasks unsupported; top-down grasp fits boxes; privileged inputs replaced by learned perception untested (2609.21650#s1)
- [K505](sub/K505.md): No check whether templated privileged descriptions (e.g. out-of-view direction) are identifiable from student observations (2610.15572#s2)
- [K604](sub/K604.md): Theory tabular with synthetic noise; active information gathering unexplored; belief contraction does not predict RL suboptimality (dog-walk) (2510.03207#s1)
- [K608](sub/K608.md): Gains smaller than with external teachers; identifiability of privileged-guided actions not analysed (2610.19820#s3)

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
