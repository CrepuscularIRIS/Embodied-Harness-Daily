# Distil Success-Filtered Teacher Harness Trajectories into a Compact Student
_id: `offline_harness_distillation` · sub-patterns: K501, K502, K504 · 3 candidate_pattern · 0 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Teacher traces collected without the student in the loop become SFT data for a compact VLM: the student pilots the identical harness from the identical context (K501), the student trains on teacher data while part of the teacher's harness is removed from its context (K502), or successful teacher runs are branched from saved simulator checkpoints with injected failures or variation and only verified branches are kept (K504).

**Operational signature.** frontier teacher runs the harness → log per-turn reasoning + tool call → keep successful episodes (plus verified branches from checkpoints with injected failures) → drop or rewrite turns that depend on removed components → SFT a compact VLM (LoRA, vision encoder frozen) → optional GRPO in the same harness → deploy with the full or a reduced harness

**When to apply.** When teacher success is high enough that success filtering keeps data, the student can afford the harness context at deployment (or the removed components' dependence can be detected), and the simulator supports checkpoints and success predicates.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K501](../sub/K501.md) | candidate_pattern | SFT a compact VLM on success-filtered frontier-teacher turns so it pilots the identical harness | log the frontier teacher's per-turn reasoning and tool call while it runs the harness, keep successful episodes, and SFT a compact VLM on… |
| [K502](../sub/K502.md) | candidate_pattern | Train the student on teacher data while the student's interface lacks part of the teacher's harness | train the student on teacher data while dropping harness components from the student's context, either by giving it a minimal context or by… |
| [K504](../sub/K504.md) | candidate_pattern | Branch successful teacher runs from saved simulator checkpoints to add recovery and diversity, keeping only verified branches | save simulator checkpoints along a successful teacher run, branch from them with injected failures or varied scene/strategy/phase/noise… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Student keeps the full harness, with the three-row comparison.** Teacher, untrained student and distilled student are reported in the identical harness: a 4B student reaches 87.1% sim success (base 22.2%, teacher 90.4%) and 90.0% real (teacher 93.3%), with call latency 4.168 s -> 0.587 s (2606.18363#s3).
- **Hundreds of success-filtered decisions.** About 500 decision samples or about 110 episodes are used; the student rises 21% -> 43-47% SR and queries per episode fall 30.61 -> 9.41 (2606.27871#s2, 2609.29389#s2, 2609.29964#s3).
- **Verified checkpoint branches compared at equal dataset size.** With teacher success about 90%, perturbation branches at equal dataset size (2,268) raise overall success 79.3% -> 87.1% and unseen tasks 77.1% -> 90.8% (2606.18363#s2); verified branches lift a VLA 18% -> 69% mean success from 10 to 400 demos (2609.27308#s3).
- **Removed components handled explicitly.** Teacher turns that depend on a removed component are rewritten and filtered: 64.6% vs 55.2% for mask-only, SFT 18.1% -> 65.1% (2610.28589#s1); demonstrations share the student's semantic unit space (2609.10522#s3).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Student does not run standalone.** Sub-agents remain frontier calls at evaluation; without the frontier planner the student gets 10% on reasoning-intensive tasks (2609.29964#s3, 2609.10522#s3).
- **Only teacher-visited states supervised.** Held-out-task accuracy stays at 13.9% with success-filtered teacher data; recovery supervision comes from teacher-visited perturbed states, not student-induced ones; privileged execution during collection leaves real-executor states uncovered, with no on-policy correction (2609.29389#s2, 2606.18363#s2, 2606.27871#s2).
- **Teacher quality does not predict student quality.** Mixing teachers hurt (41%), and the stronger teacher (56%) yields the weaker student (41% vs 43%) (2606.27871#s2).
- **Evaluated on the training tasks.** Evaluation uses the same tasks with new initial states or new seeds (2610.28589#s1, 2609.29964#s3).
- **Branch data can hurt seen tasks.** Some seen tasks drop with perturbation data (push basket 86.7 -> 66.7, shell game 70.0 -> 63.3) (2606.18363#s2).
- **Small end-to-end coverage.** Only six tasks reach VLA training, the pipeline is never run end to end, and real full-task success is 20% (2609.27308#s3).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E07 (baseline, common_practice).** For a tabletop manipulation harness or student, evaluate on LIBERO-PRO position/task perturbations, possibly with RoboTwin 2.0 or RoboCasa365. Compare against frozen VLAs (pi0.5, OpenVLA or OpenVLA-OFT) and agentic coding or VLA-steering baselines (2603.22435#s3, 2607.08448#s1). — _applies when_ an empirical claim that an agentic manipulation harness or harness-distilled student beats end-to-end VLAs.
- **E09 (baseline, common_practice).** For harness distillation, report three rows in the identical harness on identical episodes: the frontier teacher, the untrained compact student, and the distilled student. Add an end-to-end VLA or student trained on the same source episodes. — _applies when_ a claim that a compact VLM/VLA student distilled from frontier-harness trajectories approaches or exceeds the teacher.
- **E10 (reproducibility, common_practice).** Disclose how teacher data were filtered for success: teacher success or acceptance rate, how many trajectories were kept, and how the kept data skew by task difficulty. Collection success does not predict distillation value, and tasks where the teacher rarely succeeds provide little SFT data. — _applies when_ any student trained on success-filtered teacher trajectories.
- **E19 (other, common_practice).** Real-robot claims need trial counts and success rates per task. Qualitative demonstrations, or success judged by a human operator without counts, do not support transfer claims. — _applies when_ a claim that a harness or harness-distilled student transfers to a physical robot or aerial vehicle.
- **E21 (ablation, common_practice).** To claim that a student has internalized part of the harness, evaluate the student with those harness components removed or hidden at deployment. Compare it with the teacher and the base model under the same reduced interface. — _applies when_ a claim that a distilled student internalizes harness information or works under a minimal interface.

## Cognitive barriers
- "The student must internalize the harness to be small." A student that keeps the harness comes within 3.3 points of the teacher (87.1 vs 90.4) (2606.18363#s3), while a student with the planner removed fails reasoning tasks (10%) (2609.10522#s3).

## Related anti-patterns
[AP2](../anti-patterns.md#ap2), [AP3](../anti-patterns.md#ap3), [AP13](../anti-patterns.md#ap13), [AP14](../anti-patterns.md#ap14), [AP15](../anti-patterns.md#ap15)
