# Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs
_id: `planner_composes_code_and_policies` · sub-patterns: K105, K106, K107 · 3 candidate_pattern · 0 case · domain: `embodied-agent-harness/v1` · outcome labels: none in this build_

**Definition.** Keep the frontier model as planner and give it executable leverage over lower levels: code cells that compose perception, geometry and motion primitives, branch and retry locally and return only requested observations (K105); a compact policy trained to be invoked through a typed call (K106); or a frozen VLA wrapped as a primitive that the planner stages into its competent regime, bounds with stop predicates, inspects and edits before committing (K107).

**Operational signature.** frozen planner in a coding runtime → writes code cells or typed calls → primitives / learned tool policy / frozen VLA execute (stop predicate, progress head, candidate inspection without stepping) → only requested observations return → planner branches, retries, stages or replans

**When to apply.** When lower-level skills already exist and can be checked — primitives with known calibration, a frozen VLA competent on in-distribution local contact, or demonstrations that segment into invocation windows — and the planner should own composition, staging and retries.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [K105](../sub/K105.md) | candidate_pattern | Have the frozen planner write code cells that compose perception, geometry and motion primitives | let the frozen frontier model write and run code that composes primitives, computes geometry, branches and retries locally, and returns… |
| [K106](../sub/K106.md) | candidate_pattern | Train a compact policy to be invoked by a planner through a typed call | train a compact policy whose input is a typed planner call (tool family + local instruction, or a JSON command) and expose it as a callable… |
| [K107](../sub/K107.md) | candidate_pattern | Wrap a frozen VLA as a planner-controlled primitive and inspect before committing | wrap a frozen VLA as a primitive the planner stages, bounds, inspects and retries, or whose inputs/outputs it edits before approving |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Code composition compared at a matched call budget.** Same model, primitives, tasks and LLM-call budget: code cells raise success 63.1% -> 71.7%, and on jointly solved instances cut LLM calls 17.0 -> 8.7, input tokens 788k -> 276k and cost $1.63 -> $0.74 (2610.01939#s1).
- **Minimal calibrated geometry library.** A minimal geometric library with known calibration reaches 51.6% average SR on 2,100 episodes, 2.3x direct end-effector control by the same model, and 52.9% mean over 3 seeds (s.d. 0.35) with simulator depth (2610.01939#s2).
- **Generated motion validated before execution.** Generated motion passes MuJoCo/kinematic checks and a safety validation layer before execution, with replay-based repair (2609.39207#s1).
- **Frozen VLA staged into its competent regime.** The planner stages a frozen, in-distribution-competent VLA into a pre-contact state with a stop predicate: the same frozen VLA goes LIBERO-Pro 50.0% -> 72.1-92.63% depending on the planner while standard LIBERO is preserved (96.0 vs 95.3) (2607.08448#s1); candidates are inspected without advancing the environment (2609.33378#s1).
- **Tool policy trained for the call it receives.** Demonstrations are segmented into invocation windows with a data-derived tool taxonomy; tool-aligned post-training plus the interface reaches 95.6/97.2 vs 80.2/80.4 for the interface alone on LIBERO-Long (2605.13119#s1).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Contact without feedback.** Button presses and tight fits stay unsolved where pretrained policies reach 83-96%; failures concentrate on contact relative to perception accuracy (2610.01939#s2).
- **Mechanism not isolated and budget endings counted as failures.** Composition, persistent state and selective feedback are not separated; 52 of 96 code-only successes are tool-calling budget exhaustion, and including failures the cost is about equal on one suite (2610.01939#s1).
- **Planner backbone swings results with the harness fixed.** LIBERO-Pro 72.1 vs 82.4 vs 92.63 across planners; Composite-Unseen stays at 13.8-15.0%; analytic primitives and the VLA call are not ablated separately (2607.08448#s1).
- **Learned tool helps weak backends only.** A learned navigation tool adds +11 pp SR for one backend, while the strongest backend drops on RxR (93 -> 86); it is trained for atomic behaviours, not global exploration (2609.39207#s2).
- **Unguided access to a frozen policy.** Tool access without a playbook gives 0/75 on the real robot; instruction and attention edits are unreliable on a task-specific fine-tuned VLA (2609.33378#s1).
- **Tool coverage gaps.** Invocation-aligned post-training first reduced the base VLA 93.4 -> 91.2; primitives absent from the data need new demonstrations; the progress target is a temporal proxy (2605.13119#s1).
- **Real-world evidence qualitative.** Real humanoid tasks take 10-20 minutes and are reported qualitatively (2609.39207#s1).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json`; ids are stable across the domain._
- **E01 (ablation, common_practice).** Hold the frontier backbone fixed and compare the proposed harness with at least one alternative harness or loop organization on the same episodes. For zero-shot VLN-CE the alternative is a rerun of a published zero-shot harness or workflow (2606.10577#s4, 2609.15195#s4) with the same model; for coding agents, a second deployable harness. — _applies when_ a claim that a harness (rather than the model) raises embodied or agentic success.
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E03 (ablation, common_practice).** Report the harness or tool effect under at least two backbones of different strength. Several read papers find that tools and imposed structure help weak models and are neutral or harmful for strong ones. A gain measured on the teacher therefore does not predict the gain for a compact student. — _applies when_ a claim that a harness component or tool helps in general, or that a teacher-measured tool value will carry to a student.
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E07 (baseline, common_practice).** For a tabletop manipulation harness or student, evaluate on LIBERO-PRO position/task perturbations, possibly with RoboTwin 2.0 or RoboCasa365. Compare against frozen VLAs (pi0.5, OpenVLA or OpenVLA-OFT) and agentic coding or VLA-steering baselines (2603.22435#s3, 2607.08448#s1). — _applies when_ an empirical claim that an agentic manipulation harness or harness-distilled student beats end-to-end VLAs.
- **E19 (other, common_practice).** Real-robot claims need trial counts and success rates per task. Qualitative demonstrations, or success judged by a human operator without counts, do not support transfer claims. — _applies when_ a claim that a harness or harness-distilled student transfers to a physical robot or aerial vehicle.
- **E22 (reproducibility, common_practice).** Compare interfaces and harnesses at a matched interaction budget: the same caps on LLM calls, turns, wall-clock time and GPU. Disclose any asymmetry, such as uncapped turns or extra compute for tool runs, because budget endings drive many success differences. — _applies when_ a comparison between harnesses, interfaces or tool bundles with the model fixed.

## Cognitive barriers
- "Code wins because it is code." Gains persist with the VLA or guides removed, but composition, persistent state and selective feedback are not separated, and making tool calls return images only on request alone drops LIBERO-PRO 83.0% -> 68.5% (2610.01939#s1).
- "A planner on top always helps." A planner over a plain SFT VLA hurts on LIBERO-Long (-0.2/-11.8/-12.0), so the gain depends on the executor (2605.13119#s2).

## Related anti-patterns
[AP1](../anti-patterns.md#ap1), [AP2](../anti-patterns.md#ap2), [AP9](../anti-patterns.md#ap9), [AP11](../anti-patterns.md#ap11)
