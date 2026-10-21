# Let a Solver Plan from an LLM-Written Formal Model
_id: `llm_symbolic_solver_planning` · sub-patterns: R01 · 1 candidate_pattern · 0 case · domain: `board-induced` (2026-10-21, from wave-1 weak fits) · outcome labels: none in this build_

**Definition.** Use the frozen LLM/VLM as a translator rather than the planner: it writes a formal model of the task — PDDL problems, a Prolog knowledge base, SMT constraints, a precedence/scheduling graph, or executable search code — and a classical solver or search computes, checks or prunes the plan; solver failures (no plan, inconsistency, refinement failure) go back to the LLM for repair, and the plan is compiled into skills, behaviour trees or robot programs (R01).

**Operational signature.** instruction + scene (text state, or image + geometry text) → frozen LLM/VLM writes the formal model (PDDL / Prolog KB / SMT constraints / scheduling graph / search code) → solver or search plans, validates or prunes → on failure, structured feedback to the LLM → repair (bounded rounds) → compile to behaviour trees, skill calls or robot programs → execute (mostly open loop)

**When to apply.** When the task is combinatorial (multi-robot allocation, precedence and timing, long rearrangements, geometric feasibility) and a symbolic domain with a reliable state abstraction already exists, so that the LLM only has to fill in the problem and the solver can be trusted with the search.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [R01](../sub/R01.md) | candidate_pattern | Have the LLM write a formal planning model and let a classical solver compute, check or prune the plan | have a frozen LLM/VLM translate the instruction and scene into PDDL, a Prolog KB, SMT constraints, a scheduling graph or search code; a classical… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Solver step ablated against LLM-only planning.** The combinatorial step is removed or replaced by direct LLM output with the model fixed: LLM-ordered operations instead of the scheduling graph drop complex multi-robot SR 0.68 -> 0.00; a single LLM writing one large PDDL problem instead of a hierarchy of small ones drops SR 0.84 -> 0.25 (2603.02669#board, 2602.21670#board).
- **Solver failures fed back for repair, and the repair toggled.** Planner failures, inconsistencies or refinement failures return to the LLM and the repair channel is ablated: SR 0.84 vs 0.47 without failure-driven prompt optimisation; failure-revised SMT constraints are the only method at 100% success on a cooking TAMP domain (2602.21670#board, 2510.25548#board).
- **Checkers separate and backbones varied.** LLM-written and rule-based checkers are removed one at a time and the method is run on more than one backbone: GPT-4o 52.3 vs 42.7 / 41.3 without either checker; 63.9 vs 28.8 (Claude) and 46.0 vs 26.9 (Mistral) (2503.01700#board).
- **Compared with LLM-planning and LLM+PDDL baselines on the same tasks.** Aggregate SR 12% -> 55% over the strongest LLM+PDDL baseline; TCR 78% vs 53% and 39% for two PDDL baselines, with planning time reported (62.27 s vs 12.83 s) (2601.11063#board, 2603.08814#board).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Hand-written domain and abstracted or fully observed state.** The planner receives ground-truth PDDL domains, abstracted symbolic states, full observability or the whole state as text, and plans open loop without replanning on execution failure (2601.11063#board, 2602.21670#board, 2503.01700#board, 2603.08814#board).
- **Human or LLM validation carries the pipeline unmeasured.** A human confirms validation and hand-fixes knowledge bases that do not plan, with no end-to-end success without that repair; an LLM validation gate accepts all three deliberately invalid specifications with a weaker model (2502.19135#board).
- **Planning cost unpriced or partly excluded.** 173 s vs 32 s per task with the repair loop; reported planning time excludes VLM prompting (2602.21670#board, 2510.25548#board).
- **Settings tuned on the evaluation problems.** Re-prompt thresholds are picked per domain by fewest failures and prompts are optimised on the tasks they are scored on (2510.25548#board, 2602.21670#board).
- **Small own benchmarks and single runs.** 42-50 tasks or 30 problems per domain, one run, and in one case an ablation row identical to the baseline row on all six numbers (2601.11063#board, 2603.08814#board, 2603.02669#board).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json` of the frozen domain; ids are stable across the domain. The domain was built before this board-induced pattern, so these are the nearest applicable expectations, not ones written for it._
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E08 (reproducibility, common_practice).** State contamination and development-overlap caveats. Frontier 'zero-shot' describes how the model was used, not what it was trained on. Disclose whether the evaluation tasks were used during harness development, and whether ablations ran under a privileged action space that is not comparable to the benchmark protocol. — _applies when_ a benchmark claim by a frontier-model harness, or ablations run under non-standard execution.
- **E17 (dataset, common_practice).** Evaluate harness optimization, skill libraries, memory and replay cards on held-out tasks or episodes disjoint from the search, mining or validation set, and report overfitting across iterations. Gains on recurring tasks with ground-truth feedback do not show generalization. — _applies when_ a claim that a self-improving harness, skill library, playbook or experience memory improves performance.
- **E19 (other, common_practice).** Real-robot claims need trial counts and success rates per task. Qualitative demonstrations, or success judged by a human operator without counts, do not support transfer claims. — _applies when_ a claim that a harness or harness-distilled student transfers to a physical robot or aerial vehicle.

## Cognitive barriers
- "The LLM plans; the solver only checks." In the strongest results the solver does the search and the LLM writes the problem: LLM-ordered operations reach SR 0.00 on complex tasks where the solver reaches 0.68 (2603.02669#board).
- "A formal layer always helps." On vague or single-robot tasks the symbolic stage adds nothing (TCR 71 vs 71; comparable to a prompt-based baseline), and direct answering beats the method on one backbone's box task (67.1% vs 52.2%) (2603.08814#board, 2603.02669#board, 2503.01700#board).

## Related anti-patterns
[AP2](../anti-patterns.md#ap2), [AP3](../anti-patterns.md#ap3), [AP4](../anti-patterns.md#ap4), [AP5](../anti-patterns.md#ap5), [AP6](../anti-patterns.md#ap6), [AP22](../anti-patterns.md#ap22)
