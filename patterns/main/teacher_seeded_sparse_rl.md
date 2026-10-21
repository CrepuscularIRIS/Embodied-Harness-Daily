# Make Sparse-Success Embodied RL Learnable
_id: `teacher_seeded_sparse_rl` · sub-patterns: K704, K705, K707, K708 · 2 candidate_pattern · 2 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Get gradient out of sparse binary success in embodied harnesses: run GRPO/PPO on a small coder/planner inside an embodied code harness without teacher data (K704); fork the simulator at each decision step and score branches with a dense privileged reward (K705); inject teacher-written skill hints into rollouts only and remove them at evaluation (K707); or initialize from teacher-derived data so every target task has nonzero success before sparse RL (K708).

**Operational signature.** (optional) SFT on teacher-derived data until every task has nonzero success → roll out the student in the harness (forked per step, or with rollout-only hints) → binary success, rubric or privileged dense reward → GRPO/PPO/Flow-GRPO → evaluate without hints or privilege

**When to apply.** When the simulator gives a verifiable success checker, base or teacher-initialized success is nonzero on the target tasks, and (for forking) simulator state can be cloned per step.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K704](../sub/K704.md) | candidate_pattern | RL a small coder/planner model directly inside an embodied code harness on sparse success | train a small model with GRPO/PPO on verifiable simulator success inside the code-as-action harness, without teacher trajectories |
| [K705](../sub/K705.md) | case | Fork the simulator at each decision step, score completions with a privileged dense reward, continue from the best | sample a group of completions per decision step, roll each in a forked simulator branch, score with a dense privileged reward plus brevity… |
| [K707](../sub/K707.md) | case | Inject teacher-written skill hints into RL rollouts only, removed at evaluation | have a frozen teacher contrast a success and a failure rollout to write a short screened skill, inject it during GRPO rollouts for assisted… |
| [K708](../sub/K708.md) | candidate_pattern | Initialize from teacher-derived data so every task has nonzero success before sparse-reward RL | initialize the student from teacher-derived data so target tasks have nonzero success, then run sparse or outcome-based RL |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Every task starts with nonzero success.** Teacher-derived SFT covers 57/57 tasks; after PPO 97.8%/97.1% vs 41.9%/68.4% for matched direct PPO, and zero-success initializations end at 26.0% vs 91.7% (2609.21650#s2); a recovery-DAgger initialization adds +10.72 SR with RL (2610.21450#s2).
- **Teacher-free RL with frozen components and one model size.** RL inside the code harness raises unseen instances 18.8% -> 44.1% and cuts context overflows 19.2% -> 3.4% (2610.01939#s3); privileged perception during training avoids noisy rewards (Cube Lift 80%) (2603.22435#s4).
- **Dense forked-branch reward after an SFT warm start.** Forked stepwise GRPO keeps SR (49% vs 47%) while cutting tokens per query 72.1% and on-device latency 71.8% (2606.27871#s3).
- **Rollout hints that do not reveal the answer.** Mechanism skills injected only in rollouts give 38.3% vs GRPO 35.3% without hints at evaluation, and 46.5% vs 39.0% mixed-outcome groups (2610.28069#s1).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **BC initialization or zero-success start stalls.** BC-initialized Flow-GRPO stays at 19-26% SR (2610.21450#s2); direct PPO leaves 17 of 27 zero-success tasks at 0% and drives 3 solved tasks to 0% (2609.21650#s2).
- **Far below the teacher.** The RL-trained small model stays at 45.9% vs 71.7% for the frontier model, with more give-ups (25.2%) (2610.01939#s3).
- **No held-out evaluation.** Training-set numbers only (success 2.7% -> 7.5%) (2609.27308#s4); three simple tasks trained per task, with S2 rewards noisy enough for credit-assignment ambiguity (2603.22435#s4).
- **Near-answer hints hurt.** Hints that approach the answer raise training success but lower no-hint evaluation (-2.6 pp vs GRPO) (2610.28069#s1).
- **Per-step bandit credit and forking.** Greedy best-branch continuation is per-step, not full-episode credit; it needs simulator forking and privileged distance-to-goal; text (41%) and table (36%) disagree (2606.27871#s3).
- **Coverage effect not isolated; stop timing remains.** Coverage and difficulty co-vary, real closed-loop transfer failed (2609.21650#s2); late termination increases and stop timing remains the main residual failure (2610.21450#s2).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E09 (baseline, common_practice).** For harness distillation, report three rows in the identical harness on identical episodes: the frontier teacher, the untrained compact student, and the distilled student. Add an end-to-end VLA or student trained on the same source episodes. — _applies when_ a claim that a compact VLM/VLA student distilled from frontier-harness trajectories approaches or exceeds the teacher.
- **E13 (ablation, common_practice).** Before sparse-success RL, report how many target tasks start at zero success. Compare teacher-initialized RL against direct RL from the same policy at matched RL compute. In the readings, zero-success groups give no gradient and BC-initialized RL can stall. — _applies when_ a claim that SFT/teacher initialization plus RL beats RL alone, or that RL lifts a student beyond its SFT data.
- **E15 (reproducibility, common_practice).** Report reward-integrity defenses and measured hack rates. This covers hiding verifier-only or full simulator state from the policy, blocking leakage routes, and auditing rollouts. In the readings, policies with privileged state access hack the scorer. — _applies when_ a policy or coding agent trained or evaluated against an automatic success checker it could access or tamper with.

## Cognitive barriers
- "RL alone will find success." Direct PPO from zero-success tasks leaves 17 of 27 at 0% (2609.21650#s2), and BC-initialized RL stalls at 19-26% (2610.21450#s2).

## Related anti-patterns
[AP4](../anti-patterns.md#ap4), [AP7](../anti-patterns.md#ap7), [AP17](../anti-patterns.md#ap17), [AP18](../anti-patterns.md#ap18), [AP21](../anti-patterns.md#ap21)
