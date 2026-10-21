# Build Context, Notes and Skills with the Weights Frozen
_id: `harness_memory_skill_reuse` · sub-patterns: K301, K302, K303, K304 · 3 candidate_pattern · 1 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Reuse experience without training: rebuild each call's context from a bounded within-episode window plus a compact map or graph, with older history reachable only by retrieval (K301); summarize repeated-task experience into notes injected into later episodes (K302); mine, consolidate and review a skill library from successes or demonstrations (K303); or compile a successful trajectory into a planner-free replay card (K304).

**Operational signature.** run episodes → (within episode) keep recent records + compact map/graph, retrieve older content by model-pulled recall or harness-ranked retrieval → (across episodes) summarize into notes, mine and review skills, or compile replay cards → inject into later contexts or replay with anchors re-localized

**When to apply.** When tasks recur or share subgoal structure, success-filtered rollouts or demonstrations exist, and (for within-episode maps) localization is available.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K301](../sub/K301.md) | candidate_pattern | Rebuild each call's context from a bounded within-episode selection with retrieval for the rest | rebuild each model call from a short window of recent records/images plus a compact map or graph, and give access to older history only by… |
| [K302](../sub/K302.md) | candidate_pattern | Summarize repeated-task experience into notes injected into later episodes | run the system on a task, have a model summarize what worked and failed into notes or parameterized traces, and inject them into later… |
| [K303](../sub/K303.md) | candidate_pattern | Mine, consolidate and review a reusable skill library from successful executions or demonstrations | extract reusable skills from successes or demos, have a frontier model consolidate/edit/review them, and expose the frozen library at run… |
| [K304](../sub/K304.md) | case | Compile a successful harness trajectory into a planner-free replay card | compile each successful trajectory into a card with anchor-relative waypoints and VLA prompts, re-localize anchors at deployment, and… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Bounded window with pull-based recall.** Context is a short window plus recall tools rather than accumulated history: removing the recall tool drops SR 76 -> 64, and accumulating all historical images lowers SR to 66 (SPL -12.45) (2606.10577#s3).
- **Memory variants compared with model and episodes fixed.** Event memory adds +7.0 SR on both R2R and HM3D-OVON with the model and 100 episodes fixed (2609.15195#s2).
- **Notes used where tasks recur.** Same tasks repeated across episodes or sharing subgoals with a reference seed: a summary of previous episodes raises long-horizon success 52.36% -> 60.00% (2606.10267#s3), and target-setting memory raises LIBERO-Pro Goal-S 31.0% -> 87.0% (2607.08448#s2).
- **Skill library with the model fixed and demo scenes disjoint.** LIBERO-Pro average 28.9% (no skills) -> 43.3% (seed) -> 75.6% (evolved) with the model fixed and demonstration scenes disjoint from evaluation (2609.29964#s2); a library mined from success-filtered programs improves average success (2603.22435#s2).
- **Replay cards for fixed-structure tasks.** Fixed subgoal order and directly localizable objects: planner-free replay reaches 72.63% (581/800) vs 62.50% for a planner without reasoning, with 56.17 s tool time (2607.08448#s3).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Memory mined from or selected on the evaluation tasks.** The skill library is mined from evaluation-task rollouts in a single pass; the best replay card is selected on the reporting seeds; tasks without a successful source trace score 0 (2603.22435#s2, 2607.08448#s3).
- **Novel or partially observable tasks untested.** Experience notes are not shown for partially observable or novel tasks, and in-episode memory gives no benefit under full observability (2606.10267#s3).
- **Cumulative, single-run memory ablations.** The scene graph adds only +1 SR on ObjectNav in a cumulative single-run ablation; only the automatic context window is ablated, on 18 cases (2609.15195#s2, 2609.29389#s3).
- **Stored content can mislead.** Seed skills can hurt (Goal Pos. 30.0 -> 26.7); a task-progress record may carry a wrong judgement forward (2609.29964#s2, 2606.10577#s3).
- **Bootstrapping needs privileged resets.** Notes are bootstrapped with a RESET primitive, a generous budget and the benchmark success predicate; task vs global memory are not separated (2607.08448#s2).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E03 (ablation, common_practice).** Report the harness or tool effect under at least two backbones of different strength. Several read papers find that tools and imposed structure help weak models and are neutral or harmful for strong ones. A gain measured on the teacher therefore does not predict the gain for a compact student. — _applies when_ a claim that a harness component or tool helps in general, or that a teacher-measured tool value will carry to a student.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E17 (dataset, common_practice).** Evaluate harness optimization, skill libraries, memory and replay cards on held-out tasks or episodes disjoint from the search, mining or validation set, and report overfitting across iterations. Gains on recurring tasks with ground-truth feedback do not show generalization. — _applies when_ a claim that a self-improving harness, skill library, playbook or experience memory improves performance.

## Cognitive barriers
- "More history is better." Accumulating all images lowers SR 76 -> 66, and more than one past image can add stale context (2606.10577#s3, 2609.29389#s3).

## Related anti-patterns
[AP2](../anti-patterns.md#ap2), [AP3](../anti-patterns.md#ap3), [AP4](../anti-patterns.md#ap4), [AP10](../anti-patterns.md#ap10)
