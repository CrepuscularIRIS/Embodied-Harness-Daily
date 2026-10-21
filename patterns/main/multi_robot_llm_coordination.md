# Allocate and Repair Multi-Robot Plans with LLM Agents
_id: `multi_robot_llm_coordination` · sub-patterns: R03 · 1 candidate_pattern · 0 case · domain: `board-induced` (2026-10-21, from wave-1 weak fits) · outcome labels: none in this build_

**Definition.** Coordinate a team of heterogeneous robots through LLM agents that decompose the task and allocate subtasks — centrally, by dynamic grouping with subgroup negotiation, or per robot with a consensus round — and repair the allocation from capability feasibility feedback, precondition and same-object conflict checks, learned role selection or perception events, replanning only the affected part (R03).

**Operational signature.** task + robot capabilities + shared state → allocator LLM(s) (central manager / grouped negotiators / per-robot agents) → per-robot subtasks or multi-step action chains → feasibility / conflict check (executor-LLM feedback, rule validator, role selector, event filter) → reallocate or renegotiate affected subtasks → per-robot execution (skills or composed code)

**When to apply.** When several heterogeneous robots must share objects and time, capabilities can be stated in text, the shared state is observable (or reported by onboard perception), and the number of robots is small enough for LLM calls per coordination round.

## Sub-patterns
| id | status | name | operation (abridged) |
|---|---|---|---|
| [R03](../sub/R03.md) | candidate_pattern | Let LLM agents allocate subtasks across robots and repair the allocation from feasibility, conflict or event feedback | LLM agents decompose and allocate subtasks to heterogeneous robots (centrally, by negotiating groups or per robot with consensus), check… |

## Success conditions
_Derived from the member cards' When-it-works lines and the readings' reported effects; each is phrased as a property checkable in a paper's text._
- **Feasibility or conflict feedback ablated.** Removing executor feedback drops SR 1.000 -> 0.200 on the authors' assembly benchmark, where the full system needs 8.8 steps vs 15.8 for the best baseline (2602.06967#board).
- **Coordination cost reported next to success.** Tokens and wall-clock per task are compared at similar success: 29.64K vs 70.18K tokens at transport rate 78.54 vs 77.50, and 22.22K tokens / 78.62 s vs 72.51K / 411.25 s on a second benchmark (2509.24230#board).
- **Replanning triggered by filtered events and checked on hardware with counts.** 9/10 recovery runs, 8/8 coordinated transport and 5/5 human-assisted runs, with irrelevant events filtered (2511.22354#board).
- **Role structure varied.** One, two, three and four roles are compared and the method is run at several swarm sizes (9-11) (2507.01378#board).

## Failure modes
_Derived from the member cards' When-it-fails lines; each names a design or evidence property whose presence signals the failure._
- **Plans judged as text without baselines.** Correctness is judged by an expert on text plans, replanning is scored only when the initial plan was correct, and no baseline numbers are given (2511.22354#board).
- **Validator and allocator not separated.** The precondition/conflict validator is never ablated alone, constraint violations and hallucinated actions persist, and success stays below a reflection baseline (79.17 vs 87.00) (2509.24230#board).
- **Thin, own-benchmark evidence.** Mean rewards over 30 episodes appear only in figures on the authors' own task; 4 scenarios x 5 runs with one LLM (2507.01378#board, 2602.06967#board).
- **Coordination latency.** About 15 s per LLM call for the tuned 7B model; the frontier-API baseline is confounded by API latency (2507.01378#board).
- **Ground-truth shared state.** The central planner reads simulator ground-truth object and agent states (2509.24230#board).

## Accepted vs rejected gap
pending — no outcome labels in this build

## Reviewer expectations
_From `profile/expectations.json` of the frozen domain; ids are stable across the domain. The domain was built before this board-induced pattern, so these are the nearest applicable expectations, not ones written for it._
- **E01 (ablation, common_practice).** Hold the frontier backbone fixed and compare the proposed harness with at least one alternative harness or loop organization on the same episodes. For zero-shot VLN-CE the alternative is a rerun of a published zero-shot harness or workflow (2606.10577#s4, 2609.15195#s4) with the same model; for coding agents, a second deployable harness. — _applies when_ a claim that a harness (rather than the model) raises embodied or agentic success.
- **E02 (ablation, common_practice).** Attribute a gain to a harness component only through one-at-a-time toggles (leave-one-out or single add) with the backbone fixed. A cumulative stack (A, then +B, then +C) or a bundle-level comparison does not separate components or their interactions. — _applies when_ a claim that a specific harness component (depth tool, memory, verifier, skill library, plugin, feedback channel) causes the improvement.
- **E04 (reproducibility, common_practice).** Report run-to-run variance and use paired task-level statistics: repeated runs per setting, bootstrap or permutation CIs over tasks, and sign tests on discordant episodes. A single run on a 100-episode subset is treated as descriptive. In the read single-run papers, differences of a few points sit within noise. — _applies when_ any success-rate comparison between harnesses, models or training recipes on a fixed task subset.
- **E05 (metric, common_practice).** Report cost alongside success: model calls, input and output tokens, wall-clock or per-call latency, and USD per episode or per solved task, including failed trials. Harnesses with similar pass rates can differ about 40x in tokens per solved task. — _applies when_ a claim that a harness, interface or distilled student is better or more practical than an alternative.
- **E19 (other, common_practice).** Real-robot claims need trial counts and success rates per task. Qualitative demonstrations, or success judged by a human operator without counts, do not support transfer claims. — _applies when_ a claim that a harness or harness-distilled student transfers to a physical robot or aerial vehicle.

## Cognitive barriers
- "Negotiation raises success." On an external benchmark it ties a prior LLM coordinator on success (0.975 vs 0.975) and only shortens plans (2602.06967#board).
- "More roles, better coordination." A fourth role lowers the reward (2507.01378#board).

## Related anti-patterns
[AP2](../anti-patterns.md#ap2), [AP3](../anti-patterns.md#ap3), [AP5](../anti-patterns.md#ap5), [AP22](../anti-patterns.md#ap22), [AP23](../anti-patterns.md#ap23)
