# Generate Supervision with a Privileged Teacher the Student Cannot See
_id: `privileged_teacher_supervision` · sub-patterns: K503, K505, K506 · 1 candidate_pattern · 2 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Use simulator privilege to produce supervision for a student that sees only its own observations: a frontier LLM or coding agent with full state iterates a solver program from failure logs until it succeeds (K503); a privileged rule teacher acts step by step in the student's own skill vocabulary and annotates templated state reasoning (K505); or a perception module learns to estimate the missing state inputs of a frozen differentiable privileged expert (K506).

**Operational signature.** privileged simulator state (poses, masks, metric depth, paths, bearings) → teacher (LLM-iterated program, rule teacher in the student's vocabulary, frozen differentiable expert) → success-checked demonstrations or state targets → student trained on cameras, proprioception and instruction only

**When to apply.** When the simulator exposes the state a teacher needs, a success checker can filter teacher output, and the student's observations plausibly contain the information the teacher's labels encode.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K503](../sub/K503.md) | candidate_pattern | Use a frontier LLM with privileged simulator state to iterate a program teacher until it succeeds | have a frontier LLM or coding agent with full simulator state write or revise a solver program from failure logs until it succeeds, and… |
| [K505](../sub/K505.md) | case | A privileged rule teacher acts step by step in the student's skill vocabulary, with templated state reasoning | let a privileged rule teacher choose each next skill from the student's vocabulary after observing the result, annotate each step with… |
| [K506](../sub/K506.md) | case | Instead of cloning a privileged expert, estimate its missing state inputs and run it frozen | train a perception module to predict the privileged expert's missing state inputs from cameras, feed them with proprioception to the frozen… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Privilege raises teacher coverage.** LLM revision of the program teacher gives at least one success on all 57 LIBERO-PRO tasks, vs 12 of 57 with no success without revision (2609.21650#s1); full-state coding agents reach up to 82% success (2609.27308#s1).
- **Supervision emitted in the student's action vocabulary.** A rule teacher acting in the student's skills with templated reasoning: 69.6% at 28,480 examples vs 38.8% for 152,478 trajectory-relabeled examples, 71.76% full-task vs 21.90% (2610.15572#s1); spatial-reasoning labels add 65.88% -> 71.76% on the same data (2610.15572#s2).
- **Estimate the expert's inputs instead of cloning its actions.** At a matched 40k-step budget, estimators feeding a frozen expert beat pixel BC (PandaCube 99.0% vs 6.1%, AllegroCube 79.2% vs 0.7%) and transfer to a real arm at 76% (19/25) (2609.34018#s1); a linear state-to-action loss ramp raises TrayPlate 28.9% -> 64.1% (2609.34018#s2).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Teacher hacks the scorer.** Full-state coding agents hack the scorer (43% and 39% for two models), over-commit to failing decompositions and leave the hardest tasks unsolved (2609.27308#s1).
- **Identifiability unchecked.** No check whether templated privileged descriptions (e.g. out-of-view direction) are identifiable from student observations; replacing privileged inputs with learned perception is untested (2610.15572#s2, 2609.21650#s1).
- **Teacher diversity bounds the student.** Generalization is bounded by teacher data diversity; real robot 38% end to end; only short single-room navigation; no on-policy correction (2610.15572#s1).
- **Loss schedule fragile.** An abrupt switch or flat action weight collapses (<4% on tray tasks); action-only training converges in 1 of 3 seeds (2609.34018#s2).
- **Advantage shrinks with more budget.** With 3x budget a full-state flow clone closes much of the gap on reaching and tray tasks; most pixel-BC cells are single-seed (2609.34018#s1).
- **Single-primitive scope.** Multi-step tasks are unsupported and the enforced top-down grasp fits box-shaped objects (2609.21650#s1).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E09 (baseline, common_practice).** For harness distillation, report three rows in the identical harness on identical episodes: the frontier teacher, the untrained compact student, and the distilled student. Add an end-to-end VLA or student trained on the same source episodes. — _applies when_ a claim that a compact VLM/VLA student distilled from frontier-harness trajectories approaches or exceeds the teacher.
- **E10 (reproducibility, common_practice).** Disclose how teacher data were filtered for success: teacher success or acceptance rate, how many trajectories were kept, and how the kept data skew by task difficulty. Collection success does not predict distillation value, and tasks where the teacher rarely succeeds provide little SFT data. — _applies when_ any student trained on success-filtered teacher trajectories.
- **E12 (ablation, common_practice).** When teacher supervision uses information the student cannot observe (harness state, memory, simulator ground truth, next frame), ablate the content of that privileged channel and check what the student can recover from its own observations. In the readings, some privileged channels give no gain over SFT or have negative utility. — _applies when_ a student trained from a privileged or harness-richer teacher and deployed with less information.
- **E13 (ablation, common_practice).** Before sparse-success RL, report how many target tasks start at zero success. Compare teacher-initialized RL against direct RL from the same policy at matched RL compute. In the readings, zero-success groups give no gradient and BC-initialized RL can stall. — _applies when_ a claim that SFT/teacher initialization plus RL beats RL alone, or that RL lifts a student beyond its SFT data.
- **E15 (reproducibility, common_practice).** Report reward-integrity defenses and measured hack rates. This covers hiding verifier-only or full simulator state from the policy, blocking leakage routes, and auditing rollouts. In the readings, policies with privileged state access hack the scorer. — _applies when_ a policy or coding agent trained or evaluated against an automatic success checker it could access or tamper with.

## Cognitive barriers
- "Copying a privileged expert transfers its competence." Estimating the expert's inputs beats pixel BC at matched budget (2609.34018#s1), but only where the privilege is a fixed state vector; a tool-using frontier teacher has no such input vector.

## Related anti-patterns
[AP5](../anti-patterns.md#ap5), [AP13](../anti-patterns.md#ap13), [AP14](../anti-patterns.md#ap14), [AP16](../anti-patterns.md#ap16), [AP20](../anti-patterns.md#ap20)
