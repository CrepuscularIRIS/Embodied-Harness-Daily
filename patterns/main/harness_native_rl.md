# Train the Policy Through, or Aligned with, the Deployment Harness
_id: `harness_native_rl` · sub-patterns: K701, K702, K703, K706 · 4 candidate_pattern · 0 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Run RL on the student inside the harness it will deploy with, or match the training scaffold to it: capture the harness's model calls at an API proxy and train on exact contexts and logprobs (K701); assemble captured calls into training rows by prefix rules with rollout-level credit (K702); curate a band of trainable tasks and harden the sandbox against reward leakage (K703); and train under the same context-construction rules used at deployment (K706).

**Operational signature.** point the unmodified harness at a recording proxy → capture contexts, tokens, logprobs → assemble prefix chains, mask harness-inserted tokens → screen tasks to intermediate base success, hide verifier-only state, block egress → outcome reward from a post-run evaluator → group-relative update with rollout-level baselines → deploy in the same harness and context rules

**When to apply.** When the reward is verifiable, the harness exposes a configurable model endpoint, histories stay largely append-only, and rollouts are cheap enough for group RL.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K701](../sub/K701.md) | candidate_pattern | Train the policy through an unmodified harness by capturing its model calls at an API proxy | redirect the harness's model endpoint to a recording proxy that captures exact contexts, tokens and logprobs, attach outcome reward, and… |
| [K702](../sub/K702.md) | candidate_pattern | Assemble captured harness calls into training rows by prefix rules and keep credit at rollout level | partition captured calls into append-only prefix chains or exact-prefix merges, mask harness-inserted tokens, and compute group baselines… |
| [K703](../sub/K703.md) | candidate_pattern | Curate a trainable task band and harden the sandbox against reward leakage | withhold verifier-only state until grading, block egress and git history, mask infrastructure failures, and keep tasks of intermediate… |
| [K706](../sub/K706.md) | candidate_pattern | Train the policy under the same context-construction rules it will be deployed with | train the policy under the context-construction rules (compression, summaries, prompt format) used at deployment rather than applying them… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Harness unchanged from training to deployment.** Harness-native RL lifts one 4B model on SWE-bench Verified from 3.8 -> 26.4 under an unfamiliar harness and 34.2 -> 40.4 under another (2605.24220#s1); per-harness gains +6.4/+5.8/+9.4 (2608.17393#s3); with SFT initialization a robot planner goes 65.1% -> 71.0% (sign test p=0.001 on 121 vs 74 discordant episodes) (2610.28589#s2).
- **Token-exact capture.** Median Pearson between rollout and trainer logprobs is at least 0.998 per scaffold (2608.17393#s1); rollout-level advantage with exact-prefix merges reaches 38.2% vs 35.0% and 33.1% validation reward (2608.17528#s2).
- **Rollout-level assembly.** Prefix-chain assembly cuts trainer updates 1,185 -> 218 and wall-clock 189.5 -> 35.2 min (5.39x) over the same 3 steps (2605.24220#s2).
- **Intermediate-difficulty pool and leakage defenses.** Before defenses, git-history reads (4.6-20.5%) and test edits (2.4-19.4%) hack the reward; screened difficulty bands reach 0.670-0.671 validation while the unscreened pool (72.7% never solved) does not improve (2608.17393#s2).
- **Training uses the deployment context rules.** Training under the deployment compression rule reaches 37.8% vs 33.0% at 53% input cost (2608.03327#s3); the same prompt/history/schema at train and test adds 55.88% -> 71.76% cumulatively (2610.15572#s3); scaffolds stack on a summary-trained policy (8.27 vs 5.02 hourly profit) but not on plain GRPO (2606.14674#s2).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Little to gain when already aligned.** Gain is +0.6 when the base model is already harness-aligned; evidence is SWE only (2605.24220#s1).
- **Compaction and reserialization break prefix chains.** Compacted or rewritten histories are dropped; template non-compositionality, retokenize drift and tool-call reserialization break prefixes, and only 36% of coding rollouts stay a single row (2608.17393#s1, 2608.17528#s1).
- **Gains do not carry across harnesses.** A model gains +3.4 under one harness and -0.4 under another; cross-harness transfer of a trained checkpoint is not reported (2608.17393#s3).
- **Zero-variation groups grow.** All-0/all-1 groups rise from 44.7% to 51.4% as the policy improves; binary reward cannot credit recovery; defenses cover only observed failures (2608.17393#s2).
- **Embodied rollouts inherit teacher gaps at high cost.** 2,304 episodes of up to 7,200 s each; suites where the teacher rarely succeeds stay low after RL (2610.28589#s2).
- **Alignment gains in-distribution only.** Held-out accuracy under compression is unchanged and a pre-registered +15 pp bar was not met; scaffold-alignment differences may be within noise (2608.03327#s3, 2606.14674#s2).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E14 (ablation, common_practice).** For RL inside an agent harness, report the base model's score under each harness, and train and evaluate under the same harness and context rules. Results from training in one harness and deploying in another, or under different context rules, are reported separately. A gain under one control flow need not survive another. — _applies when_ a claim that RL in a training scaffold or harness improves the deployed agent.
- **E15 (reproducibility, common_practice).** Report reward-integrity defenses and measured hack rates. This covers hiding verifier-only or full simulator state from the policy, blocking leakage routes, and auditing rollouts. In the readings, policies with privileged state access hack the scorer. — _applies when_ a policy or coding agent trained or evaluated against an automatic success checker it could access or tamper with.

## Cognitive barriers
- "An RL gain belongs to the model." The same training recipe gains +3.4 under one control flow and -0.4 under another (2608.17393#s3).

## Related anti-patterns
[AP2](../anti-patterns.md#ap2), [AP13](../anti-patterns.md#ap13), [AP18](../anti-patterns.md#ap18), [AP19](../anti-patterns.md#ap19), [AP20](../anti-patterns.md#ap20)
