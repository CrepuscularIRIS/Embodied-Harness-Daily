# Revise the Harness Itself from Execution Traces
_id: `harness_self_optimization` · sub-patterns: K401, K402, K403 · 2 candidate_pattern · 1 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** An optimizer agent edits the harness — code, prompts, playbooks, skills, tools — from execution traces: with the agent model frozen (K401), for a weaker frozen recipient whose success must reach the teacher's before a revision is accepted (K402), or alternating with outcome-reward RL on the student, accepting a revision only if it helps the current checkpoint (K403).

**Operational signature.** run the harness on a search/dev set → optimizer reads prior harness code and raw traces (and the recipient's runs) → proposes edits → evaluates candidates with the same model or checkpoint → accepts by gate → optionally an RL block on the weights → repeat → report held-out

**When to apply.** When candidates are cheap enough to evaluate in tens, the search set is separate from the test set, raw traces are kept, and subtasks share environment and action space.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K401](../sub/K401.md) | candidate_pattern | With the model frozen, let an optimizer agent revise the harness from raw traces and keep improvements | let a coding-agent optimizer read prior harness code and raw execution traces, propose harness edits, evaluate them on a search set, and… |
| [K402](../sub/K402.md) | case | Teacher revises a text playbook from comparing its own and a light agent's runs; accept when the light agent matches the teacher | initialize a playbook from teacher rollouts, have the teacher compare teacher vs light-recipient executions and propose revisions, and… |
| [K403](../sub/K403.md) | candidate_pattern | Alternate RL on the student with harness revisions accepted only when they help the current checkpoint | alternate blocks of RL on the student (harness frozen) with harness revisions proposed from those trajectories, accepting a revision only… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Raw traces given to the optimizer.** The optimizer sees code, scores and raw traces: median/best accuracy 50.0/56.7 vs 34.6/41.3 with scores only (2603.28052#s2); full 76.7 vs 70.0 without traces and 63.3 with score only (2610.08432#s1).
- **Search set separate from a reported held-out set.** 27B held-out navigation 66.0 -> 75.3 and manipulation 26.4 -> 39.4, above one-shot harness rewrites (75.3 vs 67.7/65.7) (2610.08432#s1); 48.6% vs 40.9 on online text classification with 11.4K vs 50.8K context tokens (2603.28052#s1).
- **Revision accepted on the recipient's success.** Playbook length and dev-rollout limits are held equal and evaluation uses held-out initial configurations: a teacher-refined playbook lifts the light agent 31.3% -> 66.7%, at $0.63 vs $3.43 per episode for the teacher (2609.33378#s2).
- **Gated alternation compared with ungated and single-component baselines.** A validation gate beats ungated alternation 45.26 vs 40.67 and 75.19 vs 68.25, rejecting 17 regressions among 44 proposals (2609.37105#s2); joint adaptation 45.26% vs RL-only 38.83% (2609.37105#s1); candidates compared under the same checkpoint give 44.9% vs 41.7% for a harness searched with the base policy fixed (2610.28069#s2).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Harness overfits the search split.** The best search-set harness is not always best on held-out data, and held-out scores plateau or decline; on one benchmark the search set equals the test set (2610.08432#s1, 2603.28052#s1).
- **Gains on recurring tasks with ground-truth feedback.** Success 72% -> 98% (R2R) over ten passes on the same recurring 100-task subsets; EQA varies non-monotonically across passes (2609.39207#s3).
- **Point-estimate gate on small validation sets.** 53-58 validation tasks reused across rounds; the acceptance rule is not a significance test; weight stages can reduce the validation score; one training run per condition (2609.37105#s2, 2609.37105#s1, 2610.28069#s2).
- **Rollout bill.** 18,056 rollouts vs 16,928 for GRPO plus teacher calls; 184-rollout-per-side comparisons would be far costlier with embodied rollouts (2610.28069#s2).
- **Unrefined or self-refined playbooks hurt.** The initial playbook gives 31.3%, below no playbook (43.8%); self-refinement by the light agent gives 22.9%; the acceptance rule does not guarantee termination (2609.33378#s2).
- **One harness for heterogeneous subtasks.** A shared manipulation harness stays below separately optimized ones (held-out 33.8 vs 40.7) (2610.08432#s2).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E01 (ablation, common_practice).** Hold the frontier backbone fixed and compare the proposed harness with at least one alternative harness or loop organization on the same episodes. For zero-shot VLN-CE the alternative is a rerun of a published zero-shot harness or workflow (2606.10577#s4, 2609.15195#s4) with the same model; for coding agents, a second deployable harness. — _applies when_ a claim that a harness (rather than the model) raises embodied or agentic success.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E17 (dataset, common_practice).** Evaluate harness optimization, skill libraries, memory and replay cards on held-out tasks or episodes disjoint from the search, mining or validation set, and report overfitting across iterations. Gains on recurring tasks with ground-truth feedback do not show generalization. — _applies when_ a claim that a self-improving harness, skill library, playbook or experience memory improves performance.
- **E18 (ablation, common_practice).** When harness revisions or teacher corrections are accepted by a gate, state the acceptance rule and the number of rejected and accepted proposals, and compare against ungated acceptance. A point-estimate improvement on small validation sets is not a significance test. — _applies when_ a method that iteratively accepts harness, playbook or teacher-patch revisions from noisy rollouts.

## Cognitive barriers
- "Any capable agent can refine its own harness." Self-refinement by the weak recipient fails (22.9% vs 66.7% with the strong teacher refining) (2609.33378#s2), and only one proposer agent has been studied (2603.28052#s1).

## Related anti-patterns
[AP4](../anti-patterns.md#ap4), [AP12](../anti-patterns.md#ap12), [AP21](../anti-patterns.md#ap21)
