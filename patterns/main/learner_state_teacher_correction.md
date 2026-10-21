# Correct, Review or Relabel at Learner-Induced States
_id: `learner_state_teacher_correction` · sub-patterns: K601, K602, K603, K604, K611 · 4 candidate_pattern · 1 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Bring the teacher to the states the student actually visits: repair a failed student episode from its earliest harmful step and admit only validated corrections (K601); review every student proposal before execution and replace unsound ones with corrections valid in the minimal harness (K602); query the teacher only at gate-flagged learner states (K603); relabel learner-visited states with a privileged expert when dynamics allow (K604); or start sparse-reward RL from states produced by teacher-student interaction (K611).

**Operational signature.** student rolls out in its harness → locate first error / intercept proposal / gate flags state → teacher (black-box frontier, privileged expert or label generator) repairs, replaces or relabels → admission check (final answer, grounding filter, paired-advantage bound from snapshot restore) → SFT/BC on admitted data, or reset RL to correction-derived states → deploy without teacher

**When to apply.** When the teacher is competent at the states where the student fails, teacher queries at arbitrary student states are affordable, and the environment can replay or restore intermediate states.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K601](../sub/K601.md) | candidate_pattern | Repair the student's failed episode from its earliest harmful step and admit only validated corrections | on a failed student rollout, have a black-box teacher locate the earliest harmful step, keep the prefix, replace from there, and admit the… |
| [K602](../sub/K602.md) | case | A frontier harnessing agent reviews every student proposal and replaces unsound ones with corrections valid in the minimal harness | intercept each student proposal before execution, pass or replace it with the smallest correction valid under the minimal target harness… |
| [K603](../sub/K603.md) | candidate_pattern | Query the teacher only at learner states flagged by a gate | during learner rollouts, query the teacher only at states flagged by a gate and train on those teacher actions |
| [K604](../sub/K604.md) | candidate_pattern | Relabel learner-visited states with a privileged expert, when dynamics allow | relabel learner-visited states with a privileged expert or geometric label generator and aggregate DAgger-style, choosing this over RL only… |
| [K611](../sub/K611.md) | candidate_pattern | Start student RL from states produced by teacher-student interaction | start the student's sparse-reward RL rollouts from intermediate states derived from teacher-student interaction instead of the task start |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Corrections validated before training.** At the same data budget, first-error repair beats BC (46.1 vs 43.0) (2509.14257#s1); three verified patches give 46/50 vs 3/50 for success-filtered teacher demonstrations (2609.32416#s3); teacher edits rewritten in the student's style give 41.1% vs 17.5% for off-policy teacher takeover (2610.19834#s1).
- **Capable reviewer at every step.** Per-step review and replacement under the minimal harness averages 81.1% vs 78.1% (code-as-harness) and 68.6% (minimal harness) (2609.24974#s1); the distilled student's macro average rises 23.3 -> 44.3, above the base model under the evolved harness (41.7) (2609.24974#s3).
- **Gate cuts teacher queries.** The teacher is queried on 1.2-13.3% of training steps, 7.5x-86x fewer calls than full-query baselines, and not at deployment (2609.01567#s1).
- **Relabel where dynamics are near-deterministic.** Online distillation reaches the best return under deterministic dynamics while RL wins under higher motor noise (2510.03207#s1); relabeling with recovery raises full-chunk SR 16.45% -> 63.46% (seen) (2610.21450#s1).
- **RL restarted from correction states.** Compute-matched, RL from verified prefixes reaches 52.3 avg vs 48.4 without short-horizon starts (2509.14257#s2); resets to teacher-reached states give near-perfect success on three simulated tasks and 100% on 12 real drawer-search episodes (2505.09546#s2).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Teacher weak where the student fails.** Weaker editor teachers give weaker students (33.3% and 26.9% vs 41.1%); weaker reviewers are net harmful (-12.0 pp while replacing 66% of steps); a random teacher degrades training (2610.19834#s1, 2609.24974#s1, 2609.01567#s1).
- **Verification, review and reset cost.** >=4,192 suffix rollouts for 19 admissions with snapshot restore; per-step review roughly doubles latency (237.2 s vs 100.1 s per trial) (2609.32416#s1, 2609.24974#s1).
- **Seed variance and thin admissions.** Trainer-seed variance is large (spill 50/33/33); a refinement with one thin admission regressed 76% -> 58%; pooling tasks causes interference (2609.32416#s2).
- **Information-gathering regime excluded.** The distill-vs-RL theory excludes active information gathering; early termination remains dominant after relabeling (21-37%) (2510.03207#s1, 2610.21450#s1).
- **Gate signal confounded.** Entropy conflates uncertainty with multimodality; early discriminator errors misclassify states and a too-strong discriminator increases aliasing (2609.01567#s1, 2505.09546#s1).
- **Fully observable text domains only.** The review ablation runs on one domain with a single seed; live-web success stays below 8%; text/tool sandboxes are fully observable (2609.24974#s3, 2610.19834#s1).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E10 (reproducibility, common_practice).** Disclose how teacher data were filtered for success: teacher success or acceptance rate, how many trajectories were kept, and how the kept data skew by task difficulty. Collection success does not predict distillation value, and tasks where the teacher rarely succeeds provide little SFT data. — _applies when_ any student trained on success-filtered teacher trajectories.
- **E11 (baseline, common_practice).** Compare an on-policy correction or OPD method with three baselines at a matched data or teacher-query budget: (a) offline BC/SFT on teacher successes, (b) student RL (GRPO) from the same initialization, (c) token-level OPD where a white-box teacher exists. Report teacher cost per intervention. — _applies when_ a claim that teacher corrections at learner-induced states (first-error repair, review, action-agreement, preference) beat offline distillation.
- **E18 (ablation, common_practice).** When harness revisions or teacher corrections are accepted by a gate, state the acceptance rule and the number of rejected and accepted proposals, and compare against ungated acceptance. A point-estimate improvement on small validation sets is not a significance test. — _applies when_ a method that iteratively accepts harness, playbook or teacher-patch revisions from noisy rollouts.

## Cognitive barriers
- "More teacher data closes the gap." Doubling SFT data 5K -> 10K gives no clear gain (2509.14257#s1), and success-filtered teacher demonstrations give 3/50 where verified corrections give 46/50 (2609.32416#s3).

## Related anti-patterns
[AP3](../anti-patterns.md#ap3), [AP5](../anti-patterns.md#ap5), [AP6](../anti-patterns.md#ap6), [AP7](../anti-patterns.md#ap7), [AP12](../anti-patterns.md#ap12), [AP13](../anti-patterns.md#ap13), [AP14](../anti-patterns.md#ap14), [AP15](../anti-patterns.md#ap15), [AP17](../anti-patterns.md#ap17), [AP21](../anti-patterns.md#ap21)
