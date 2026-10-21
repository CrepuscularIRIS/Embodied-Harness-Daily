# Separate the Harness Effect from the Model Effect
_id: `harness_effect_evaluation` · sub-patterns: K801, K802, K803, K804, K805 · 4 candidate_pattern · 1 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Evaluation designs that attribute outcomes to harness or model and report more than end-to-end pass rate: a model-by-harness factorial with paired statistics and tokens per solved task (K801); one-at-a-time component toggles with the backbone fixed (K802); embodied model swaps under a fixed harness and harness swaps under a fixed model on the same episodes (K803); failure-endpoint and per-task repeat decomposition (K804); and cost re-priced from raw per-turn usage and reconciled with billed spend (K805).

**Operational signature.** fix tasks, sandbox, verifier and budgets → cross models x harnesses (or toggle one component, or swap one factor on fixed episodes) → repeat runs → paired task-level statistics (bootstrap CI, permutation, sign tests) → classify failures by endpoint and per-task repeat pattern → re-price from raw usage and reconcile cost

**When to apply.** Whenever a paper claims that a harness, component, interface or training recipe — rather than the model — moves success or cost.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K801](../sub/K801.md) | candidate_pattern | Cross frozen models with harnesses on fixed tasks and report harness variance with paired statistics | run a model-by-harness grid with everything else fixed and report harness variance, model variance, ranking reversals, paired bootstrap CIs… |
| [K802](../sub/K802.md) | candidate_pattern | Hold the model fixed and toggle one harness component or layer at a time | hold the backbone (or distilled student) fixed and add, remove or swap one harness component or layer at a time |
| [K803](../sub/K803.md) | candidate_pattern | Swap the model under a fixed embodied harness and the harness under a fixed model on the same episodes | hold the harness fixed and swap the model, and hold the model fixed and swap the harness or loop director, on fixed embodied episodes |
| [K804](../sub/K804.md) | candidate_pattern | Decompose outcomes into failure categories, endpoints and per-task repeat patterns | classify failed runs by cause or terminal state and tasks by repeated-run outcome pattern, and report these with pass rate |
| [K805](../sub/K805.md) | case | Re-price runs from raw per-turn usage and reconcile against billed spend | re-price every run from raw per-turn usage with explicit cache terms, reconcile against the ledger and billed spend |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Model-by-harness grid with paired statistics.** Harness variance 18.48 pp^2 vs model variance 2.37 pp^2 (7.80x), with 6 of 9 ranking comparisons reversing (2605.23950#s1); tokens per solved task vary ~40x across harnesses vs 1.0-1.3x across models (2607.22585#s1); a post-hoc interaction with label-permutation p=0.003 (BH q=0.013) (2609.11987#s1).
- **One component toggled with typed interfaces fixed.** Variants differ only in the chosen module: memory gains are mediated by the reasoner (8.54 -> 30.67 with ReAct) (2606.14674#s1); scenes, seeds and backbone are fixed across safety-harness layers (2609.20822#s3).
- **Same-backbone reruns on fixed episodes.** Baselines rerun with the same model on the same 100 episodes: harness gaps of +11/+6/+22 SR across three backbones (2606.10577#s4) and +14.0/+18.0 SR (2609.15195#s4).
- **Repeated runs with endpoints and per-task patterns.** Six runs per task: 62 tasks always succeed, 8 always fail, 30 are mixed (2609.29861#s2); no-action turns 2.0-2.16 vs 0.2-0.3 per task replicate across models (2607.22585#s2).
- **Cost reconciled against billing.** Re-pricing raw usage corrects cache share to 87-98% (vs 48% under a double-count defect) and matches billed spend within 2-4% for one provider (2609.11987#s3).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Differences within noise.** 50 tasks (1 task = 2 pp) leave most pass-rate differences within noise; intervals 11-17 pp wide leave moderate effects undetectable (2607.22585#s1, 2609.11987#s1).
- **Cumulative harness layers.** Compared harnesses are cumulative, so per-layer contributions are not isolated, and the 7.80x ratio is stated as not universal (2605.23950#s1).
- **Single embodied runs without cost.** Embodied swaps are single runs without variance; harness gain varies 6-22 SR with the backbone and no cost is reported (2609.15195#s4, 2606.10577#s4).
- **Complete systems compared.** Serving and context handling differ across harnesses, and workflow vs agent is confounded with the action interface (strong models drop 82.3 -> 65 in a fixed workflow) (2607.26148#s3); hierarchy components swing success ~95% -> ~0% even with a near-perfect VLA proxy (2606.10267#s4).
- **Decomposition descriptive, not causal.** Attribution is co-movement; the category-assignment procedure is unspecified; persistent failures are not tied to causes or interventions (2605.23950#s2, 2606.14674#s3, 2609.29861#s2).
- **Ablations on the wrong model.** Harness ablations are run on base models only, not on the distilled student (a 2B model reaches 2.2% in the same harness) (2606.18363#s1).
- **Budget endings and missing usage.** 22 of 81 ceiling-cancelled runs had a passing patch (2609.11987#s2); 58 runs lack usage records and cache-write pricing is uncertain by ~2x (2609.11987#s3).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E01 (ablation, common_practice).** Hold the frontier backbone fixed and compare the proposed harness with at least one alternative harness or loop organization on the same episodes. For zero-shot VLN-CE the alternative is a rerun of a published zero-shot harness or workflow (2606.10577#s4, 2609.15195#s4) with the same model; for coding agents, a second deployable harness. — _applies when_ a claim that a harness (rather than the model) raises embodied or agentic success.
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E08 (reproducibility, common_practice).** State contamination and development-overlap caveats. Frontier 'zero-shot' describes how the model was used, not what it was trained on. Disclose whether the evaluation tasks were used during harness development, and whether ablations ran under a privileged action space that is not comparable to the benchmark protocol. — _applies when_ a benchmark claim by a frontier-model harness, or ablations run under non-standard execution.
- **E16 (metric, common_practice).** Break failures down by endpoint as well as SR: never reached vs reached but wrong stop (the OSR-SR gap), false completion declarations, stuck or no-progress runs, and per-task repeat patterns. Stopping is the dominant residual failure in the read navigation papers. — _applies when_ an embodied navigation or manipulation agent's success claim, especially one that adds a stop or completion check.
- **E22 (reproducibility, common_practice).** Compare interfaces and harnesses at a matched interaction budget: the same caps on LLM calls, turns, wall-clock time and GPU. Disclose any asymmetry, such as uncapped turns or extra compute for tool runs, because budget endings drive many success differences. — _applies when_ a comparison between harnesses, interfaces or tool bundles with the model fixed.

## Cognitive barriers
- "The model is the main variable." With the model fixed, harness changes move a coding model by 8.5-13.0 points vs 2.5-5.0 for model changes at a fixed harness (2605.23950#s1), and strong embodied models lose 82.3 -> 65 when moved into a fixed workflow (2607.26148#s3).

## Related anti-patterns
[AP1](../anti-patterns.md#ap1), [AP2](../anti-patterns.md#ap2), [AP3](../anti-patterns.md#ap3), [AP5](../anti-patterns.md#ap5), [AP7](../anti-patterns.md#ap7), [AP8](../anti-patterns.md#ap8), [AP9](../anti-patterns.md#ap9), [AP15](../anti-patterns.md#ap15)
