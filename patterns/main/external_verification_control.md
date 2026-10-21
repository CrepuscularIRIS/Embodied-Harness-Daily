# Gate, Monitor and Diagnose Actions Outside the Model
_id: `external_verification_control` · sub-patterns: K201, K202, K203, K204 · 2 candidate_pattern · 2 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Move checks and control flow out of the model: gate each proposed edit, navigation target, STOP or route with a cheap external checker and return structured feedback (K201); run an executor until a completion or stagnation monitor fires and hand control back to the planner (K202); after a scored attempt, let the agent write and run a diagnostic program before reset (K203); or give a teacher-side solver checkpoint/backtrack and parameter-search tools over full simulator state (K204).

**Operational signature.** model proposes → external checker (linter, argument/provenance/reachability check, fresh-depth STOP check, obstacle clearance) dispatches or rejects with feedback → executor runs → success detector or progress monitor fires → planner advances or replans → (resettable simulation) diagnose after scoring, or backtrack from checkpoints

**When to apply.** When a cheap automatic checker exists whose pass condition correlates with task success, the completion signal is one the deployed system can compute, and — for diagnostics and backtracking — the simulator can reset or restore state.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K201](../sub/K201.md) | candidate_pattern | Treat each model proposal as a request and gate it with an external checker before execution | check each proposed edit, navigation target, STOP or route outside the model with a cheap checker and either dispatch it or reject it with… |
| [K202](../sub/K202.md) | candidate_pattern | Run the executor until a completion or stagnation monitor fires, then hand control back to the planner | keep the low-level executor on the current subgoal until a success detector or progress-threshold/stagnation rule fires, then let the… |
| [K203](../sub/K203.md) | case | After a scored attempt, let the agent write and run a diagnostic program before resetting | after each attempt, have the coding agent synthesize a separate View/Probe program to gather evidence on unresolved outcomes, then decide… |
| [K204](../sub/K204.md) | case | Give the coding-agent solver checkpoint/backtrack and parameter-search tools over full simulator state | add a checkpoint tree over simulator states, CMA-ES parameter search, parallel program sweeps and an assessment log to the agent's native… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **A cheap checker of action validity.** Each edit is linted before it is applied, and removing the linter lowers SWE-bench Lite resolve rate 18.0% -> 15.0% (2405.15793#s2).
- **Route checked against a grounded obstacle.** Waypoint polylines are checked for clearance against a segmentation-grounded obstacle with phases cut at contact events; adding the route harness raises safe success 31.3 -> 60.6 and 18.8 -> 64.4 over 32 tasks for two models (2609.20822#s1).
- **STOP gated on usable depth and reliable detection.** STOP requests pass an identity, fresh-depth and completion check: +2.0 SR on R2R and HM3D-OVON subsets, and the OSR-SR gap narrows 22.0 -> 10.0 on HM3D-v2 (2609.15195#s3).
- **Accurate completion monitor.** A success detector ends executor runs: 57.39% long-horizon vs 52.36% with a fixed 8 s horizon and 43.50% with a VLM-predicted horizon, robust to 10% injected detection error (2606.10267#s1); executors that report invocation progress cut runtime VLM calls per episode from 109.5 to 1.988 (2605.13119#s2).
- **Diagnostics run after scoring in a resettable simulator.** Diagnostic programs run after scoring and before reset: final success 75% (45/60) vs 31.7%, completion-assessment precision 90.0% vs 43.2% (2610.12549#s1).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Checker is a weak proxy for success.** The linter misses 52% of unresolved instances (wrong implementations); a STOP gate passes at fresh depth 1.20 m vs goal distance 2.15 m and the OSR-SR gap stays 19.0 on HM3D-OVON; a box-only verifier on an approximately measured scene misses unmodeled constraints (2405.15793#s2, 2609.15195#s3, 2609.20822#s1).
- **Detector false positives and privileged detectors.** False-positive rates of 30-50% sharply hurt, correlated false negatives can stall a command, and the simulation detector reads privileged state (2606.10267#s1).
- **Gate contribution not isolated.** Proposal validation alone is not ablated; teacher-side search tools are ablated only as a bundle, with an extra GPU and one run per task (2609.15195#s1, 2609.27308#s2).
- **Added control tools lower success.** Checkpoint and search tools raise one model's mean score 0.66 -> 0.70 while its success falls 50% -> 43% (2609.27308#s2).
- **Planner gains depend on executor fidelity.** A planner over a plain SFT VLA hurts on LIBERO-Long (-0.2/-11.8/-12.0); the real study is one robot and one camera (2605.13119#s2).
- **Only valid with resets.** Diagnostics need resettable simulation and do not apply to single-shot real episodes; Cabinet stays at 40% with 10 trials per task (2610.12549#s1).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E16 (metric, common_practice).** Break failures down by endpoint as well as SR: never reached vs reached but wrong stop (the OSR-SR gap), false completion declarations, stuck or no-progress runs, and per-task repeat patterns. Stopping is the dominant residual failure in the read navigation papers. — _applies when_ an embodied navigation or manipulation agent's success claim, especially one that adds a stop or completion check.
- **E19 (other, common_practice).** Real-robot claims need trial counts and success rates per task. Qualitative demonstrations, or success judged by a human operator without counts, do not support transfer claims. — _applies when_ a claim that a harness or harness-distilled student transfers to a physical robot or aerial vehicle.
- **E20 (other, common_practice).** State the depth assumption behind depth-based perception tools (pixel depth queries, back-projection, stop checks): whether depth is metric and calibrated, and whether behaviour under non-metric or scene-dependent depth was tested. — _applies when_ a harness whose tools or gates convert depth readings into distances, targets or stop decisions.
- **E22 (reproducibility, common_practice).** Compare interfaces and harnesses at a matched interaction budget: the same caps on LLM calls, turns, wall-clock time and GPU. Disclose any asymmetry, such as uncapped turns or extra compute for tool runs, because budget endings drive many success differences. — _applies when_ a comparison between harnesses, interfaces or tool bundles with the model fixed.

## Cognitive barriers
- "A gate makes stopping safe." The read STOP gates pass outside the success region and near wrong endpoints, and stopping remains the dominant residual failure (2609.15195#s3).

## Related anti-patterns
[AP2](../anti-patterns.md#ap2), [AP5](../anti-patterns.md#ap5), [AP6](../anti-patterns.md#ap6), [AP9](../anti-patterns.md#ap9), [AP17](../anti-patterns.md#ap17)
