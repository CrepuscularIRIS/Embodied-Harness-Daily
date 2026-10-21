# Train the High-Level VLM That Commands a Low-Level Policy
_id: `trained_vlm_vla_hierarchy` · sub-patterns: R02 · 1 candidate_pattern · 0 case · domain: `board-induced` (2026-10-21, from wave-1 weak fits) · outcome labels: none in this build_

**Definition.** Replace the frozen frontier planner with a fine-tuned high-level VLM: it maps images, the user's prompt or interjection and feedback to an atomic language command, a coarse motion instruction or a subtask plan, and a trained low-level VLA, motion-conditioned policy or skill library executes it; the high level is trained on robot-specific data (human skill labels with back-generated prompts, expert motion pairs and human corrections, LLM-generated planning data) and re-runs at a fixed rate, per utterance or on detected failure (R02).

**Operational signature.** robot data → segment into skills / motions and label (human annotation, larger-VLM back-generated prompts and interjections, human corrections, LLM-generated plans) → fine-tune the high-level VLM → (low level trained on the same command vocabulary) → at run time high level emits command every step-interval or on utterance / failure → low-level policy executes → (optional) trained correction module rewrites the command

**When to apply.** When the planner must run on the robot's own compute or at high rate, the command vocabulary can be covered by low-level training data, and robot-specific data (labels, corrections) are affordable; when the frontier model's zero-shot breadth is less important than grounding in the robot's skills.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [R02](../sub/R02.md) | candidate_pattern | Fine-tune the high-level VLM that issues language or motion commands to a trained low-level policy | split the policy into a fine-tuned high-level VLM that emits atomic commands, motion instructions or subtask plans and a trained low-level… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Trained high level compared with a prompted frontier high level over the same low level.** The same decomposition with a frontier VLM that is not fine-tuned, and a flat VLA, score lower than the fine-tuned high level; removing the synthetic prompt data also loses (2502.19417#board).
- **Correction trained as a separate module and ablated against co-training.** A separate motion-correction MLLM gives 57.8% mean success over 9 tasks x 50 trials vs 46.9% (prediction only) and 51.3% (one model co-trained on the same correction data) (2504.14588#board).
- **Low-level competence checked with an oracle high level.** With expert-human high-level commands the low-level policy executes nearly flawlessly, so remaining failures are located in the high level (2502.19417#board).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Plan quality scored offline.** Planning, pointing and affordance accuracy on in-distribution synthetic data stand in for end-to-end success; real deployment is shown as demonstrations (2505.03673#board).
- **Real-robot evidence thin.** The real-world check of the correction loop is one drawer task with 20 corrections, after training on thousands of human interventions and annotations (2504.14588#board).
- **Baselines differ in more than the training of the high level.** The frontier high-level baseline is not fine-tuned on the robot data; one model-family comparison is not like-for-like, and over 90% of development evaluation episodes ran in simulation (2502.19417#board, 2510.03342#board).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json` of the frozen domain; ids are stable across the domain. The domain was built before this board-induced pattern, so these are the nearest applicable expectations, not ones written for it._
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E07 (baseline, common_practice).** For a tabletop manipulation harness or student, evaluate on LIBERO-PRO position/task perturbations, possibly with RoboTwin 2.0 or RoboCasa365. Compare against frozen VLAs (pi0.5, OpenVLA or OpenVLA-OFT) and agentic coding or VLA-steering baselines (2603.22435#s3, 2607.08448#s1). — _applies when_ an empirical claim that an agentic manipulation harness or harness-distilled student beats end-to-end VLAs.
- **E19 (other, common_practice).** Real-robot claims need trial counts and success rates per task. Qualitative demonstrations, or success judged by a human operator without counts, do not support transfer claims. — _applies when_ a claim that a harness or harness-distilled student transfers to a physical robot or aerial vehicle.

## Cognitive barriers
- "A frontier planner on top is always the stronger high level." A small fine-tuned VLM beats a prompted frontier VLM over the same low-level policy when the frontier model is not adapted to the robot's skills (2502.19417#board).
- "Separate the corrector from the predictor." Co-training one model on mixed expert and correction data beats the separated module on two tasks (90 vs 86; 26 vs 20) (2504.14588#board).

## Related anti-patterns
[AP1](../anti-patterns.md#ap1), [AP3](../anti-patterns.md#ap3), [AP23](../anti-patterns.md#ap23)
