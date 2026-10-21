# Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals
_id: `on_policy_distillation_objectives` · sub-patterns: K605, K606, K607, K608, K609, K610 · 3 candidate_pattern · 3 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Change the loss rather than the data: reward sampled student tokens by the reverse-KL log-ratio to a white-box teacher (K605); score the student's tokens with a privileged-context copy of itself and add the divergence to GRPO (K606); train one model jointly under privileged and deployment views and deploy the plain view (K607); sample target actions from a privileged copy and verify or match them (K608); reward student candidates by semantic agreement with black-box teacher actions (K609); or prefer the teacher's harness-conditioned action over its harness-stripped action (K610).

**Operational signature.** student samples at its own states → teacher signal: white-box logits / same weights with privileged context / joint privileged view / privileged-self sampled actions / black-box teacher actions matched by a judge / with-vs-without-harness teacher pair → per-token divergence, agreement reward or preference loss (often with a gate or validity filter) → policy-gradient or preference update → deploy without privilege

**When to apply.** When the needed teacher access exists — logits and shared tokenization, an interpretable privileged channel the student-sized model can use, or cheap black-box teacher queries with judgeable discrete actions — and teacher-student divergence is moderate.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K605](../sub/K605.md) | case | On-policy distillation from a white-box teacher's token logits at student-visited states | roll out the student, reward each sampled action token by the negative student-teacher log-ratio, and update by policy gradient, using… |
| [K606](../sub/K606.md) | candidate_pattern | Score the student's own tokens with a privileged-context copy of itself and add the divergence to RL | let the student sample without privileged info, score its tokens with the same weights conditioned on privileged context, and add a… |
| [K607](../sub/K607.md) | candidate_pattern | Train one model jointly under privileged and deployment-context views, deploying only the plain view | train one model at once on privileged-context and deployment-context prompts and deploy only the plain view |
| [K608](../sub/K608.md) | candidate_pattern | Sample target actions from a model copy given privileged context, then verify or match | sample target actions from a copy of the model given privileged context and use them as student targets after verification or as an… |
| [K609](../sub/K609.md) | case | Reward student candidates by semantic agreement with black-box teacher actions at the same state | at each learner state, sample several teacher actions and student candidates, reward candidates by semantic match, optimize PPO-clipped… |
| [K610](../sub/K610.md) | case | Prefer the teacher's harness-conditioned action over its harness-stripped action at student states | at student-visited states, sample teacher actions with and without harness text, apply a pairwise preference for the harness-conditioned… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **White-box logits with reverse KL.** LIBERO average 48.9% -> 87.4% (distill) and 93.4% (distill + GRPO) vs teacher 93.9% (2603.26666#s1); reverse KL improves steadily where forward KL drops >50% early and hard-CE plateaus lowest (2603.26666#s2).
- **Information-rich privilege at moderate divergence.** Privileged self-distillation reaches 37.5% vs RL 27.5% on TravelPlanner (2602.04942#s2); next-screenshot privilege adds +3.17 over an unprivileged teacher, with AndroidWorld 52.73 vs GRPO 47.13 over 3 seeds (2608.06065#s1).
- **Joint, interleaved privileged and plain views.** Joint T+I+R training gives 22.98% vs 20.58% task success, while a staged schedule collapses to 7.03% (2610.20261#s2); joint training reaches 44.1% vs 32.3% for SFT+RL (2602.04942#s1).
- **Privileged-self targets verified by the harness.** Verified privileged-self targets give 20.58% vs 15.61% (OPD), 7.72% (GSPO) and 2.06% (SFT on ground truth) (2610.20261#s1).
- **Agreement reward with commit-best continuation.** OOD average +5.1/+6.9 pp for a 4B student with two teachers (2610.19820#s1); replacing commit-best with random commit lowers pass^1 40.0 -> 37.5 (2610.19820#s2).
- **Harness-contrast preference with a validity filter.** ALFWorld unseen 63.4% vs 47.0% best OPD baseline, above the 8B teacher (2610.02858#s1); removing the validity filter lowers average SR 57.4 -> 50.8 (2610.02858#s2).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Teacher ceiling and teacher access.** The distilled student stays below its teacher and the method needs logits, so black-box API teachers are excluded; agreement-trained students remain far below teachers (37.7 vs 71.2) (2603.26666#s1, 2610.19820#s1).
- **Weak, uninterpretable or over-strong privilege.** Reference action alone as privilege gives 58.62 vs SFT 59.05; negative privilege utility makes student-only training fail; excessive KL overrides utility and degrades OOD on a smaller model (2608.06065#s1, 2602.04942#s1, 2602.04942#s2).
- **Schedules collapse.** Teacher-only training collapses when KL nears zero and no single mixing weight is best; staged schedules degrade closed-loop success (2602.04942#s1, 2610.20261#s2).
- **Agreement or validity is not correctness.** Matcher false positives/negatives misassign reward and teacher errors become targets; valid-but-incorrect positives cannot be filtered (2610.19820#s1, 2610.02858#s2).
- **Holding state makes visitation off-policy.** Rolling several candidates from one held state introduces off-policy state visitation (2610.19820#s2).
- **Small gains outside one text environment.** WebShop SR 19.6 vs 19.0; untested on multimodal, embodied, long-horizon or partially observed physical tasks (2610.02858#s1, 2608.06065#s1).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E11 (baseline, common_practice).** Compare an on-policy correction or OPD method with three baselines at a matched data or teacher-query budget: (a) offline BC/SFT on teacher successes, (b) student RL (GRPO) from the same initialization, (c) token-level OPD where a white-box teacher exists. Report teacher cost per intervention. — _applies when_ a claim that teacher corrections at learner-induced states (first-error repair, review, action-agreement, preference) beat offline distillation.
- **E12 (ablation, common_practice).** When teacher supervision uses information the student cannot observe (harness state, memory, simulator ground truth, next frame), ablate the content of that privileged channel and check what the student can recover from its own observations. In the readings, some privileged channels give no gain over SFT or have negative utility. — _applies when_ a student trained from a privileged or harness-richer teacher and deployed with less information.
- **E21 (ablation, common_practice).** To claim that a student has internalized part of the harness, evaluate the student with those harness components removed or hidden at deployment. Compare it with the teacher and the base model under the same reduced interface. — _applies when_ a claim that a distilled student internalizes harness information or works under a minimal interface.

## Cognitive barriers
- "An action-level teacher signal is as good as a distribution." The hard-CE (black-box-style argmax relabel) objective plateaus lowest with entropy collapse (2603.26666#s2).

## Related anti-patterns
[AP6](../anti-patterns.md#ap6), [AP13](../anti-patterns.md#ap13), [AP14](../anti-patterns.md#ap14), [AP16](../anti-patterns.md#ap16), [AP17](../anti-patterns.md#ap17), [AP18](../anti-patterns.md#ap18), [AP21](../anti-patterns.md#ap21)
