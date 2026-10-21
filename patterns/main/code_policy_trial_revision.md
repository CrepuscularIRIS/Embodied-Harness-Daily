# Write the Policy as Code and Rewrite It from Trial Diagnostics
_id: `code_policy_trial_revision` · sub-patterns: R05 · 1 candidate_pattern · 0 case · domain: `board-induced` (2026-10-21, from wave-1 weak fits) · outcome labels: none in this build_

**Definition.** Let a frozen LLM or coding agent author the whole controller as a program over perception, geometry and motion primitives, run it in simulation, diagnose failures from execution logs, phase outcomes, key frames or a VLM's reading of rollout images or video, and rewrite it between trials until it succeeds; the deployed artifact is the program, with no model in the control loop at run time (R05).

**Operational signature.** task + primitive API → LLM / coding agent writes controller program → static checks → run trials in simulation → diagnose (symbolic logs, phase outcomes, key frames, VLM critique of images or video) → rewrite program → repeat to success or budget → deploy the program (no model at run time)

**When to apply.** When trials are cheap and resettable (simulation), the primitive library covers the task, failures leave readable traces, and the controller must run without model latency or cost at deployment.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [R05](../sub/R05.md) | candidate_pattern | Write the controller as code and rewrite it between trials from execution diagnostics | have a frozen LLM or coding agent write the whole controller as a program, run trials in simulation, diagnose failures from logs, key… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Rewriting compared with one-shot code on the same tasks.** One-shot code 47.4% -> execution feedback 60.4% -> plus visual diagnosis 63.9%, and 62.1 -> 66.7 -> 71.3 on a second benchmark (2508.02629#board).
- **Rewrite history reported with the fix that mattered.** A stacking controller goes 0% -> 33% after a back-projection sign fix -> 91% at version 20; two other tasks reach 100% in 3 and 2 rewrites, with 20/20 repeats (2603.04466#board).
- **Program checked before deployment and compared with code-generation baselines.** Constraint review, static checks and simulation precede automatic deployment: 81% mean over 10 tasks x 100 trials; 74% vs 37-40% for three code-generation baselines (2503.23875#board).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **No held-out instances.** The controller is rewritten on the instances it is scored on, with unstated trial counts behind the headline (2603.04466#board).
- **Classical controller or any baseline missing.** One study has no baseline at all; in another hand-tuned flocking and assignment controllers score higher on average than the generated code (2603.04466#board, 2503.23875#board).
- **Convergence compared across different setups.** The headline iteration reduction (2.42 -> 1.76) compares two benchmarks run with different planners (2508.02629#board).
- **Perception emulated and no real-world rewriting.** Positions come from an indoor positioning system; no member rewrites code on a real robot from real failures (2503.23875#board, 2508.02629#board).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json` of the frozen domain; ids are stable across the domain. The domain was built before this board-induced pattern, so these are the nearest applicable expectations, not ones written for it._
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E07 (baseline, common_practice).** For a tabletop manipulation harness or student, evaluate on LIBERO-PRO position/task perturbations, possibly with RoboTwin 2.0 or RoboCasa365. Compare against frozen VLAs (pi0.5, OpenVLA or OpenVLA-OFT) and agentic coding or VLA-steering baselines (2603.22435#s3, 2607.08448#s1). — _applies when_ an empirical claim that an agentic manipulation harness or harness-distilled student beats end-to-end VLAs.
- **E17 (dataset, common_practice).** Evaluate harness optimization, skill libraries, memory and replay cards on held-out tasks or episodes disjoint from the search, mining or validation set, and report overfitting across iterations. Gains on recurring tasks with ground-truth feedback do not show generalization. — _applies when_ a claim that a self-improving harness, skill library, playbook or experience memory improves performance.
- **E19 (other, common_practice).** Real-robot claims need trial counts and success rates per task. Qualitative demonstrations, or success judged by a human operator without counts, do not support transfer claims. — _applies when_ a claim that a harness or harness-distilled student transfers to a physical robot or aerial vehicle.

## Cognitive barriers
- "Seeing the rollout is what fixes the code." Visual critique adds 3 points (74% vs 71%; 60.4 -> 63.9) and lowers some tasks (50 -> 27), while execution feedback carries most of the gain (2503.23875#board, 2508.02629#board).
- "The loop works with any coding agent." A second agent with the same budget solved none of three tasks (2603.04466#board).

## Related anti-patterns
[AP1](../anti-patterns.md#ap1), [AP4](../anti-patterns.md#ap4), [AP11](../anti-patterns.md#ap11), [AP24](../anti-patterns.md#ap24)
