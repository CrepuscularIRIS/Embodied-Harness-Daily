# Embodied-Harness-Daily

**A daily radar for embodied agent harnesses**: the loop of interfaces, tools, verifiers, memory and training signals that wraps a frontier LLM/VLM so it can drive a robot arm, a mobile manipulator, a navigator, a drone or a humanoid.
（具身智能体 harness 雷达：追踪“模型经由什么 harness 控制什么本体”的一手研究。）

**Core question:** *through which harness does the model control which embodiment, how is closed-loop success judged, and does the gain come from the harness, the policy, or privileged information / extra compute?* Scope: [EVIDENCE](docs/EVIDENCE.md).
（核心问题：模型经由哪种 harness 控制哪种本体？闭环成功如何判定？收益来自 harness、策略，还是特权信息／额外算力？）

**This season / 本季漏斗:** `514 screened at L1 → 121 checked at L2 → 91 P3-confirmed → 9 posters` · run `embodied-full-v11-20261022` · rules `problem-core-v1.1`

- **Pattern cards, reverse-engineered.** 17 main / 58 sub cards induced from full-text readings of this corpus, each condition cited to its source paper.（逆向卡片：从本语料全文逆向归纳，条件逐条锚定来源论文。）
- **Problem-first, two-layer rating of the whole corpus.** Every paper gets the four problem questions at L1; candidates get sub-card condition checks at L2.（全语料两层“问题优先”评价 problem-core-v1.1。）
- **A Reel every issue.** Opus 5.5 checks each pick against its full text and builds one poster per mechanism.（每期 Reel：全文核对后按机制做海报。）

<sub><i>embodied AI · VLA · LLM agents · robot manipulation · vision-language navigation · drones · humanoids · test-time scaling · agent harness · arXiv daily · 具身智能 · 每日论文雷达</i></sub>

## Featured Reel — Issue s001（本期海报墙）

Nine papers, nine mechanism types, each poster checked against the paper's full text. Claim narrowings are logged in `reel/<id>/SOURCE.md`. Selection log: [selection-001](research/scoring/runs/embodied-full-v11-20261022/selections/selection-001.md) · [Reel index](reel/README.md).
（九篇九种机制；海报与全文逐项核对，收窄之处记在 SOURCE.md。）

<table>
<tr>
<td width="33%" align="center" valign="top"><a href="reel/2610.27350/poster.png"><img src="reel/2610.27350/poster.png" width="260" alt="2610.27350 poster"></a><br>
<b><a href="https://arxiv.org/abs/2610.27350">2610.27350</a> · Safety diagnosis</b><br>
Same model, same first frame: 15/15 refusals when asked vs 0/15 in the action loop.<br>同一输入、两条通道：问答会拒绝，动作循环不拒绝。</td>
<td width="33%" align="center" valign="top"><a href="reel/2411.04549/poster.png"><img src="reel/2411.04549/poster.png" width="260" alt="2411.04549 poster"></a><br>
<b><a href="https://arxiv.org/abs/2411.04549">2411.04549</a> · Verification signal</b><br>
Is a VLM progress score measuring progress, or echoing temporal order? Shuffle the frames.<br>打乱帧序，看进度分数到底在测什么。</td>
<td width="33%" align="center" valign="top"><a href="reel/2610.25114/poster.png"><img src="reel/2610.25114/poster.png" width="260" alt="2610.25114 poster"></a><br>
<b><a href="https://arxiv.org/abs/2610.25114">2610.25114</a> · Self-improvement attribution</b><br>
Gain split into feedback / inheritance / selection; frozen skills run under cheap cross-family callers.<br>自我改进收益拆解，冻结技能交给廉价异族模型。</td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><a href="reel/2510.20328/poster.png"><img src="reel/2510.20328/poster.png" width="260" alt="2510.20328 poster"></a><br>
<b><a href="https://arxiv.org/abs/2510.20328">2510.20328</a> · Memory</b><br>
MemER: what matters is <i>what</i> to remember, not how much.<br>该记什么，而非记更多。</td>
<td width="33%" align="center" valign="top"><a href="reel/2610.15572/poster.png"><img src="reel/2610.15572/poster.png" width="260" alt="2610.15572 poster"></a><br>
<b><a href="https://arxiv.org/abs/2610.15572">2610.15572</a> · Privileged supervision</b><br>
Equal data; only the teacher's labelling policy changes: 46.3 → 65.5 → 69.6%.<br>等量数据，只换教师标注策略。</td>
<td width="33%" align="center" valign="top"><a href="reel/2506.17811/poster.png"><img src="reel/2506.17811/poster.png" width="260" alt="2506.17811 poster"></a><br>
<b><a href="https://arxiv.org/abs/2506.17811">2506.17811</a> · Test-time sample–verify</b><br>
RoboMonkey: a verifier without an oracle turns samples into closed-loop gains, at what latency?<br>采样—打分—选择及其时延代价。</td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><a href="reel/2311.13373/poster.png"><img src="reel/2311.13373/poster.png" width="260" alt="2311.13373 poster"></a><br>
<b><a href="https://arxiv.org/abs/2311.13373">2311.13373</a> · RL with a teacher</b><br>
A fallible LLM teacher speeds up a small RL student, which then outgrows it (0.77 vs 0.52).<br>会犯错的教师与超越教师的学生。</td>
<td width="33%" align="center" valign="top"><a href="reel/2411.00081/poster.png"><img src="reel/2411.00081/poster.png" width="260" alt="2411.00081 poster"></a><br>
<b><a href="https://arxiv.org/abs/2411.00081">2411.00081</a> · Multi-agent evaluation</b><br>
PARTNR: an LLM partner made humans <i>slower</i> (3046 → 4267 steps).<br>人机合作的反直觉结果：伙伴反而拖慢人类。</td>
<td width="33%" align="center" valign="top"><a href="reel/2602.15875/poster.png"><img src="reel/2602.15875/poster.png" width="260" alt="2602.15875 poster"></a><br>
<b><a href="https://arxiv.org/abs/2602.15875">2602.15875</a> · Action interface</b><br>
Fly0: fix everything, swap only the goal interface. SR 62.1 → 70.4, false-lock 0.16 → 0.05.<br>其余不变，只换目标接口。</td>
</tr>
</table>

## High-Score Papers (2026)（高分论文）

17 rows: the 9 Reel papers (any year) plus 8 papers from 2026 (4 L2-confirmed, 4 L1-only chosen to widen card coverage). Source: [readme-2026-p3.json](research/scoring/runs/embodied-full-v11-20261022/readme-2026-p3.json) and [l2-merged.json](research/scoring/runs/embodied-full-v11-20261022/l2-merged.json).
**Score = a numeric view of the tier, not a separate rating.** **95** = P3 confirmed at L2, change type `capability`; **92** = P3 confirmed at L2, change type field `judgment`; **85 / 82** = P3 from the L1 screen only (abstract + introduction, capability / judgment), not yet confirmed. Rows with the same score are not ranked.
（分数只是档位的数字视图：95＝L2 确认的 P3·能力；92＝L2 确认的 P3·领域判断；85/82＝仅 L1 初筛判 P3（能力／判断），尚未核对。同分不排名。）
The Good Question gives an English rendering, then Sol's original `problem_statement` in Chinese (trimmed near 60 characters).（英文为转写，中文为 Sol 原句。）

| Paper | Score · Tier | Idea Cards（pattern 卡） | The Good Question | Links |
|---|---|---|---|---|
| [MemER](https://arxiv.org/abs/2510.20328) `2510.20328` | **95** · P3 ✓ | [`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md)<br><sub>冻结权重下的记忆技能复用</sub><br>[`trained_vlm_vla_hierarchy`](patterns/main/trained_vlm_vla_hierarchy.md)<br><sub>高层VLM-低层VLA层级</sub> | In real-robot tasks that depend on minutes of history, how can key visual events be kept for a high-level policy under limited compute and context, instead of piling up every observation?<br><sub>在依赖数分钟历史的真机操作中，如何在有限计算和上下文下保留关键视觉事件并供高层策略调用，而不是堆积全部观测。</sub> | [arXiv](https://arxiv.org/abs/2510.20328) · [project](https://jen-pan.github.io/memer/) · [poster](reel/2510.20328/poster.png) |
| [LLM as a Policy Teacher for RL Agents](https://arxiv.org/abs/2311.13373) `2311.13373` | **95** · P3 ✓ | [`teacher_seeded_sparse_rl`](patterns/main/teacher_seeded_sparse_rl.md)<br><sub>教师引导的稀疏奖励RL</sub><br>[`on_policy_distillation_objectives`](patterns/main/on_policy_distillation_objectives.md)<br><sub>在策略蒸馏信号</sub> | In embodied sequential tasks such as MiniGrid and Habitat, how can a fallible, costly LLM teacher help a small RL student explore less, while the student finally leaves and surpasses it?<br><sub>在 MiniGrid 和 Habitat 等具身序贯任务中，如何用会犯错且部署昂贵的 LLM 教师帮助小型 RL 学生减少探索…</sub> | [arXiv](https://arxiv.org/abs/2311.13373) · code — · [poster](reel/2311.13373/poster.png) |
| [EmboTeam](https://arxiv.org/abs/2601.11063) `2601.11063` | **95** · P3 ✓ | [`llm_symbolic_solver_planning`](patterns/main/llm_symbolic_solver_planning.md)<br><sub>LLM形式模型+求解器规划</sub><br>[`multi_robot_llm_coordination`](patterns/main/multi_robot_llm_coordination.md)<br><sub>多机器人LLM协调</sub> | For heterogeneous multi-robot teams with long-horizon task dependencies and changing team size, how can a language goal become a synchronizable, reactive execution structure?<br><sub>异构多机器人面对长程任务依赖和动态团队规模时，如何把自然语言目标转为可同步、可反应的执行结构。</sub> | [arXiv](https://arxiv.org/abs/2601.11063) · code — |
| [Fly0](https://arxiv.org/abs/2602.15875) `2602.15875` | **95** · P3 ✓ | [`observe_act_interface`](patterns/main/observe_act_interface.md)<br><sub>冻结模型的观测/动作接口</sub> | For zero-shot drone VLN, how can low-rate, uncertain language grounding become a metric goal still usable for high-rate safe control after the target leaves view?<br><sub>零样本无人机VLN如何把低频、带不确定性的语言定位变成目标离开视野后仍可用于高频安全控制的度量目标？</sub> | [arXiv](https://arxiv.org/abs/2602.15875) · [code](https://github.com/xuzhenxing1/Fly0) · [poster](reel/2602.15875/poster.png) |
| [From Language to Task Maps](https://arxiv.org/abs/2609.34412) `2609.34412` | **95** · P3 ✓ | [`observe_act_interface`](patterns/main/observe_act_interface.md)<br><sub>冻结模型的观测/动作接口</sub> | Expanding qualitative manipulation relations straight into full poses constrains degrees of freedom the task leaves free, creating artificial conflicts between continuous control objectives.<br><sub>把定性操作关系直接展开为完整位姿会约束任务未指定的自由度，造成连续控制目标之间的人为冲突。</sub> | [arXiv](https://arxiv.org/abs/2609.34412) · code — |
| [Look Before You Move](https://arxiv.org/abs/2610.15572) `2610.15572` | **95** · P3 ✓ | [`privileged_teacher_supervision`](patterns/main/privileged_teacher_supervision.md)<br><sub>特权教师监督</sub> | When the student picks high-level skills from deployment-visible observations only, how to avoid shortest-path hindsight labels that teach moving forward but not keeping the target visible or recovering it?<br><sub>开放世界移动操作的学生只能依据部署可见观测选择高层技能时，如何避免最短路轨迹后标注只教前进、不教保持可见性和失目标恢复的监督缺口？</sub> | [arXiv](https://arxiv.org/abs/2610.15572) · code — · [poster](reel/2610.15572/poster.png) |
| [Scaling Online Exploration for Robot Agents](https://arxiv.org/abs/2610.22496) `2610.22496` | **95** · P3 ✓ | [`code_policy_trial_revision`](patterns/main/code_policy_trial_revision.md)<br><sub>代码策略试错重写</sub><br>[`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md)<br><sub>冻结权重下的记忆技能复用</sub> | With calibrated RGB-D, low-level controllers and a limited exploration budget, can a robot compile online trial-and-error into a perception–planning–control program that runs alone in unseen layouts?<br><sub>在有标定RGB-D、底层控制器和有限探索预算时，机器人能否将在线试错编译成可在未见布局独立执行的感知—规划—控制程序？</sub> | [arXiv](https://arxiv.org/abs/2610.22496) · code — |
| [PARTNR](https://arxiv.org/abs/2411.00081) `2411.00081` | **92** · P3 ✓ | [`multi_robot_llm_coordination`](patterns/main/multi_robot_llm_coordination.md)<br><sub>多机器人LLM协调</sub><br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md)<br><sub>harness 效果隔离评测</sub> | In simulated household tasks with spatial, temporal and heterogeneous-skill constraints, can an LLM partner collaborate and recover, rather than adding to the human's workload through perception, skill or coordination errors?<br><sub>在受空间、时序及异构技能约束的模拟家庭任务中，LLM伙伴能否有效协作与恢复，而非以感知、技能或协调错误增加人类工作负担？</sub> | [arXiv](https://arxiv.org/abs/2411.00081) · code — · [poster](reel/2411.00081/poster.png) |
| [VLMs are In-Context Value Learners](https://arxiv.org/abs/2411.04549) `2411.04549` | **92** · P3 ✓ | [`external_verification_control`](patterns/main/external_verification_control.md)<br><sub>外部验证与执行门控</sub><br>[`observe_act_interface`](patterns/main/observe_act_interface.md)<br><sub>冻结模型的观测/动作接口</sub> | When a frozen VLM predicts task progress from robot video, how can the shortcut of outputting values monotone in input frame order be found and removed, keeping a signal useful for success, failure and policy learning?<br><sub>冻结VLM从机器人视频预测任务进度时，如何识别并消除按输入时间顺序输出单调值的捷径，而保留对成功、失败及策略学习有用的信号？</sub> | [arXiv](https://arxiv.org/abs/2411.04549) · [project](https://generative-value-learning.github.io/) · [poster](reel/2411.04549/poster.png) |
| [RoboMonkey](https://arxiv.org/abs/2506.17811) `2506.17811` | **92** · P3 ✓ | [`sample_verify_select`](patterns/main/sample_verify_select.md)<br><sub>采样-验证-选择</sub> | At deployment, can the potentially good actions among repeated VLA samples become real closed-loop gains without an oracle action verifier?<br><sub>部署时能否将 VLA 多次采样的潜在好动作转化为真实闭环收益，而不依赖 oracle 动作验证器？</sub> | [arXiv](https://arxiv.org/abs/2506.17811) · code — · [poster](reel/2506.17811/poster.png) |
| [MAVLink Drone Agentic Harness](https://arxiv.org/abs/2601.15486) `2601.15486` | **92** · P3 ✓ | [`external_verification_control`](patterns/main/external_verification_control.md)<br><sub>外部验证与执行门控</sub><br>[`observe_act_interface`](patterns/main/observe_act_interface.md)<br><sub>冻结模型的观测/动作接口</sub><br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md)<br><sub>harness 效果隔离评测</sub> | When an untrusted LLM flies a drone through generic tools, how can an independent safety boundary hold through sustained flight, and reported task state match its actual holder?<br><sub>让不可信LLM经通用工具控制无人机时，如何在持续飞行中保持独立安全边界，并让任务状态的报告与实际持有者一致。</sub> | [arXiv](https://arxiv.org/abs/2601.15486) · code — |
| [Compile Once, Run Cheap](https://arxiv.org/abs/2610.25114) `2610.25114` | **92** · P3 ✓ | [`code_policy_trial_revision`](patterns/main/code_policy_trial_revision.md)<br><sub>代码策略试错重写</sub><br>[`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md)<br><sub>冻结权重下的记忆技能复用</sub><br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md)<br><sub>harness 效果隔离评测</sub> | Can offline code skills, once frozen, run alone or under a cheap cross-family model, and does the iterative edge come from feedback, version inheritance or selection among attempts?<br><sub>离线代码技能能否在冻结后独立或由廉价异族模型执行，迭代优势究竟来自反馈、版本继承还是尝试选择？</sub> | [arXiv](https://arxiv.org/abs/2610.25114) · code — · [poster](reel/2610.25114/poster.png) |
| [Refuses When Asked, Complies When Acting](https://arxiv.org/abs/2610.27350) `2610.27350` | **92** · P3 ✓ | [`external_verification_control`](patterns/main/external_verification_control.md)<br><sub>外部验证与执行门控</sub><br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md)<br><sub>harness 效果隔离评测</sub> | With the same model, the same explicit harmful instruction and the same first frame, is refusal in the robot action loop decoupled from an explicit pre-action safety query?<br><sub>同一模型面对相同明确有害指令和首帧时，机器人动作循环的拒绝行为是否与显式行动前安全问询分离？</sub> | [arXiv](https://arxiv.org/abs/2610.27350) · [code](https://github.com/Arnav-Gr0ver/Refuses-When-Asked-Complies-When-Acting) · [poster](reel/2610.27350/poster.png) |
| [Steerable VLA Policies](https://arxiv.org/abs/2602.13193) `2602.13193` | **85** · P3 (L1) | [`trained_vlm_vla_hierarchy`](patterns/main/trained_vlm_vla_hierarchy.md)<br><sub>高层VLM-低层VLA层级</sub><br>[`planner_composes_code_and_policies`](patterns/main/planner_composes_code_and_policies.md)<br><sub>规划器组合代码与冻结VLA</sub> | When a high-level VLM already knows where to grasp or how to move, how can the command granularity a low-level VLA understands be widened so reasoning truly controls behavior?<br><sub>高层VLM已经知道应抓哪里或怎样移动时，如何扩展低层VLA可理解的命令粒度，使推理能真正控制行为。</sub> | [arXiv](https://arxiv.org/abs/2602.13193) · code — |
| [OnFly](https://arxiv.org/abs/2603.10682) `2603.10682` | **85** · P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md)<br><sub>外部验证与执行门控</sub><br>[`observe_act_interface`](patterns/main/observe_act_interface.md)<br><sub>冻结模型的观测/动作接口</sub> | How can fully onboard zero-shot drone VLN meet high-rate goal generation, low-rate long-horizon monitoring and safe trajectory execution at once, avoiding single-stream decisions and memory overwrites?<br><sub>完全机载零样本无人机VLN如何同时满足高频目标生成、低频长程监控与安全轨迹执行，避免单流决策和记忆覆盖导致失败？</sub> | [arXiv](https://arxiv.org/abs/2603.10682) · [code](https://github.com/Robotics-STAR-Lab/OnFly) |
| [Counterfactual Failure Synthesis](https://arxiv.org/abs/2603.13528) `2603.13528` | **85** · P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md)<br><sub>外部验证与执行门控</sub><br>[`learner_state_teacher_correction`](patterns/main/learner_state_teacher_correction.md)<br><sub>学生状态教师纠正</sub> | How can valid failure–correction pairs be synthesized from successful real-robot demos, so visual failure explanations turn into executable recovery trajectories?<br><sub>如何从成功真机演示合成有效的失败—纠正配对，使视觉失败解释能转化为可执行的操作恢复轨迹？</sub> | [arXiv](https://arxiv.org/abs/2603.13528) · code — |
| [Scaling Verification > Scaling Policy Learning](https://arxiv.org/abs/2602.12281) `2602.12281` | **82** · P3 (L1) | [`sample_verify_select`](patterns/main/sample_verify_select.md)<br><sub>采样-验证-选择</sub><br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md)<br><sub>harness 效果隔离评测</sub> | When VLA actions disagree with the language intent, with data fixed, can scaling instruction rephrasing and action sampling plus verify-and-select beat scaling policy learning?<br><sub>VLA动作与语言意图不一致时，固定数据条件下，扩大指令改写和动作采样并验证选择能否比扩大策略学习更有效。</sub> | [arXiv](https://arxiv.org/abs/2602.12281) · code — |

## Pipeline and Models（流程与模型）

```mermaid
flowchart LR
  A[Grok bot<br>inbox/] --> B[ingest<br>corpus.jsonl] --> C[full-material cache] --> D[L1 screen<br>6.1 Sol] --> E[L2 check<br>6.1 Sol] --> F[L3 selection<br>Opus 5.5] --> G[Reel<br>Opus 5.5]
```

1. **Retrieve.** A Grok bot searches arXiv, HF Papers and lab pages, writes only verified primary-source candidates to `inbox/`, and never scores. → [GROK_PROMPT](docs/agents/GROK_PROMPT.md)（只收一手证据候选，不评分）
2. **Ingest and cache.** Dedupe by version-stripped ID, DOI and title into `research/corpus.jsonl`; cache the uncropped full text once, locally. → [ingest.py](research/ingest.py) · [fetch_fulltext.py](research/fetch_fulltext.py)（去重入库，全文本地缓存一次）
3. **L1 screen (6.1 Sol).** Abstract + introduction; the four problem questions and a tier for every paper. → [SOL_BATCH_PROMPT](research/scoring/SOL_BATCH_PROMPT.md)（全量初筛：四问＋档位）
4. **L2 check (6.1 Sol).** Method and main-experiment sections with locators; confirm Q1/Q4, run sub-card condition checks, plus a random missed-paper audit. → [PROBLEM_CORE](research/scoring/PROBLEM_CORE.md)（全文核对＋子卡条件检查＋漏检抽查）
5. **L3 select + Reel (Opus 5.5).** Deduplicate same-problem papers, pick ≤9 for mechanism diversity (no numeric ranking), verify each against full text, build posters, run visual QA. → [SELECTION](research/scoring/SELECTION.md) · [OPUS_REEL_PROMPT](research/scoring/OPUS_REEL_PROMPT.md)（同题去重、按机制多样性选题、全文核对出海报）

| Stage this season（本季） | Count | Source |
|---|---|---|
| L1 screened | 514 (489 full run + 25 inbox increment) | [progress.md](research/scoring/runs/embodied-full-v11-20261022/progress.md) |
| L2 checked | 121 (114 + 7) | progress.md · l2-merged.json |
| Missed-paper audit | 12 audited, 3 revised up (P2→P3) | progress.md（全量 10 改 2 + 增量 2 改 1） |
| P3-confirmed candidates (to_l3) | 91 | [candidates-l3.json](research/scoring/runs/embodied-full-v11-20261022/candidates-l3.json) |
| Reel s001 posters | 9 | [reel/](reel/README.md) |

**problem-core-v1.1, two layers, never added together.** The problem layer asks four questions (does the problem exist · is it open · what changes if solved · does the method target it); the execution layer runs condition checks drawn from the sub-cards (`holds / partial / fails / unknown / NA`) and reports coverage only. Code links, venue, citations and card-match counts are never counted.
（两层分开记录、不相加：问题层四问（成立／开放／改变什么／对准）＋执行层子卡条件检查；不计代码、会议、引用与卡匹配数。）

## Pattern Cards — 17 main / 58 sub（抽卡式科研）

**Drawing cards for research.** We turn the field's recurring research operations into searchable **pattern cards**: an operational signature, the field beliefs it runs into (cognitive barriers), failure modes and success conditions checkable in a paper's text, and reviewer expectations. Draw a card for a new paper to see which operation it really performs and which conditions it guarantees; draw cards for a new idea to combine operations or challenge a recorded barrier. The cards come from this corpus, not a preset taxonomy, and are fixed for the run: we never edit a card to fit a paper.
（抽卡式科研：把领域里反复出现的研究操作逆向成可检索卡片（操作签名＋认知障碍＋失败模式＋审稿期望）。读论文时“抽卡”看它真正做了什么、保证了哪些条件；构思时组合不同卡的操作，或挑战卡上的障碍。卡片源自本语料，本 run 内版本固定。）

| Card | Mechanism（机制） | Problem families | Subs |
|---|---|---|---|
| [observe_act_interface](patterns/main/observe_act_interface.md) | Design what the frozen model observes and how its outputs are grounded into actions.<br><sub>冻结模型的观测/动作接口</sub> | F1, F5 | [K101](patterns/sub/K101.md) [K102](patterns/sub/K102.md) [K103](patterns/sub/K103.md) [K104](patterns/sub/K104.md) [K108](patterns/sub/K108.md) [K109](patterns/sub/K109.md) [K110](patterns/sub/K110.md) [R04](patterns/sub/R04.md) [R07](patterns/sub/R07.md) |
| [planner_composes_code_and_policies](patterns/main/planner_composes_code_and_policies.md) | A frontier planner writes code or typed calls over primitives, learned tools and frozen VLAs.<br><sub>规划器组合代码与冻结VLA</sub> | F1, F5 | [K105](patterns/sub/K105.md) [K106](patterns/sub/K106.md) [K107](patterns/sub/K107.md) |
| [external_verification_control](patterns/main/external_verification_control.md) | Gate, monitor and diagnose actions with checkers outside the model.<br><sub>外部验证与执行门控</sub> | F2 | [K201](patterns/sub/K201.md) [K202](patterns/sub/K202.md) [K203](patterns/sub/K203.md) [K204](patterns/sub/K204.md) |
| [harness_memory_skill_reuse](patterns/main/harness_memory_skill_reuse.md) | Build context, notes and skill libraries with the weights frozen.<br><sub>冻结权重下的记忆技能复用</sub> | F5 | [K301](patterns/sub/K301.md) [K302](patterns/sub/K302.md) [K303](patterns/sub/K303.md) [K304](patterns/sub/K304.md) |
| [harness_self_optimization](patterns/main/harness_self_optimization.md) | An optimizer reads execution traces and revises the harness itself.<br><sub>从执行轨迹改写 harness</sub> | F1, F3 | [K401](patterns/sub/K401.md) [K402](patterns/sub/K402.md) [K403](patterns/sub/K403.md) |
| [offline_harness_distillation](patterns/main/offline_harness_distillation.md) | SFT a compact student on success-filtered teacher harness trajectories.<br><sub>成功轨迹离线蒸馏小模型</sub> | F1 | [K501](patterns/sub/K501.md) [K502](patterns/sub/K502.md) [K504](patterns/sub/K504.md) |
| [privileged_teacher_supervision](patterns/main/privileged_teacher_supervision.md) | A teacher with privileged state the student cannot see generates supervision.<br><sub>特权教师监督</sub> | F3, F4 | [K503](patterns/sub/K503.md) [K505](patterns/sub/K505.md) [K506](patterns/sub/K506.md) |
| [learner_state_teacher_correction](patterns/main/learner_state_teacher_correction.md) | Correct, review or relabel at the states the student actually visits.<br><sub>学生状态教师纠正</sub> | F2, F5 | [K601](patterns/sub/K601.md) [K602](patterns/sub/K602.md) [K603](patterns/sub/K603.md) [K604](patterns/sub/K604.md) [K611](patterns/sub/K611.md) |
| [on_policy_distillation_objectives](patterns/main/on_policy_distillation_objectives.md) | Distil on-policy from logits, a privileged self, agreement or a harness contrast.<br><sub>在策略蒸馏信号</sub> | F4 | [K605](patterns/sub/K605.md) [K606](patterns/sub/K606.md) [K607](patterns/sub/K607.md) [K608](patterns/sub/K608.md) [K609](patterns/sub/K609.md) [K610](patterns/sub/K610.md) |
| [harness_native_rl](patterns/main/harness_native_rl.md) | Train the policy through, or aligned with, the deployment harness.<br><sub>在部署 harness 内做 RL</sub> | F1 | [K701](patterns/sub/K701.md) [K702](patterns/sub/K702.md) [K703](patterns/sub/K703.md) [K706](patterns/sub/K706.md) |
| [teacher_seeded_sparse_rl](patterns/main/teacher_seeded_sparse_rl.md) | Use teacher data, rollout-only hints or privileged reward so sparse RL can learn.<br><sub>教师引导的稀疏奖励RL</sub> | F1 | [K704](patterns/sub/K704.md) [K705](patterns/sub/K705.md) [K707](patterns/sub/K707.md) [K708](patterns/sub/K708.md) |
| [harness_effect_evaluation](patterns/main/harness_effect_evaluation.md) | Cross models × harnesses on fixed tasks to separate harness effect from model effect.<br><sub>harness 效果隔离评测</sub> | F1 | [K801](patterns/sub/K801.md) [K802](patterns/sub/K802.md) [K803](patterns/sub/K803.md) [K804](patterns/sub/K804.md) [K805](patterns/sub/K805.md) |
| [llm_symbolic_solver_planning](patterns/main/llm_symbolic_solver_planning.md) | The LLM writes a formal model; a classical solver plans, validates or prunes.<br><sub>LLM形式模型+求解器规划</sub> | F1, F5 | [R01](patterns/sub/R01.md) |
| [trained_vlm_vla_hierarchy](patterns/main/trained_vlm_vla_hierarchy.md) | Fine-tune the high-level VLM that commands a trained low-level policy.<br><sub>高层VLM-低层VLA层级</sub> | F1, F5 | [R02](patterns/sub/R02.md) |
| [multi_robot_llm_coordination](patterns/main/multi_robot_llm_coordination.md) | LLM agents allocate tasks across robots and repair plans from conflict checks.<br><sub>多机器人LLM协调</sub> | F1, F5 | [R03](patterns/sub/R03.md) |
| [code_policy_trial_revision](patterns/main/code_policy_trial_revision.md) | Write the controller as code; rewrite it from trial diagnostics; deploy model-free.<br><sub>代码策略试错重写</sub> | F1, F3 | [R05](patterns/sub/R05.md) |
| [sample_verify_select](patterns/main/sample_verify_select.md) | Sample N candidate actions; a verifier picks the one to execute.<br><sub>采样-验证-选择</sub> | F2, F5 | [R06](patterns/sub/R06.md) |

**58 sub-cards** in [patterns/sub/](patterns/sub/): K1xx interface 10 · K2xx verification 4 · K3xx memory 4 · K4xx self-optimization 3 · K5xx offline/privileged 6 · K6xx on-policy 11 · K7xx RL 8 · K8xx evaluation 5 · R0x board-induced 7. K101–K805 come from 50 full-text readings in the Open Scientist domain `embodied-agent-harness/v1`; R01–R07 from the wave-1 board's weak fits. See [overview](patterns/overview.md) · [anti-patterns](patterns/anti-patterns.md).（K 系首位数字是领域族，与问题族 F0–F5 是两套编号。）
**Problem families**（问题族, [PROBLEM_MAP](research/scoring/PROBLEM_MAP.md)): F1 attribution 归因 · F2 signal trust 信号可信 · F3 transfer boundary 迁移边界 · F4 information access 信息权限 · F5 monotonicity assumption 单调性假设 · F0 other 其他.

## Start here（从这里开始）

| What | Where |
|---|---|
| Rules 规则 | [PROBLEM_CORE](research/scoring/PROBLEM_CORE.md) · [PROBLEM_MAP](research/scoring/PROBLEM_MAP.md) · [scoring index](research/scoring/README.md) · [EVIDENCE](docs/EVIDENCE.md) |
| Cards 卡片 | [overview](patterns/overview.md) · [main/](patterns/main/) · [sub/](patterns/sub/) · [anti-patterns](patterns/anti-patterns.md) · [PATTERN_INDEX](research/scoring/PATTERN_INDEX.md) |
| This run 本次 run | [run.md](research/scoring/runs/embodied-full-v11-20261022/run.md) · [progress](research/scoring/runs/embodied-full-v11-20261022/progress.md) · [selection-001](research/scoring/runs/embodied-full-v11-20261022/selections/selection-001.md) |
| Reel 海报 | [reel/README](reel/README.md) · [SELECTION](research/scoring/SELECTION.md) · [OPUS_REEL_PROMPT](research/scoring/OPUS_REEL_PROMPT.md) |
| Agents 智能体 | [Grok prompt](docs/agents/GROK_PROMPT.md) · [Sol batch prompt](research/scoring/SOL_BATCH_PROMPT.md) · [CC start](docs/agents/START_CC.md) · [inbox](inbox/README.md) |
| Maintenance 维护 | [AGENTS](AGENTS.md) · [MAINTAINING](docs/MAINTAINING.md) · [PIPELINE](docs/PIPELINE.md) · [2026-10-22 reset](docs/RESET_2026-10-22.md) |

`make check` validates local structure only; passing structure, citation and arithmetic checks is not scientific validation or reproduction.（结构校验通过不等于科学验证或复现。）

---

Tiers are reading-priority judgments made by model readers (6.1 Sol at L1/L2, Opus 5.5 at L3/Reel). They are not peer review, venue endorsements or reproductions. Full texts, keys and private logs stay local.（档位是“值不值得读”的判断，不是审稿结论。）

**License:** MIT ([LICENSE](LICENSE)). **Lineage:** base pipeline cloned from [CUA Radar](https://github.com/CrepuscularIRIS/cua-architecture-radar) → [HarnessRSI Daily](https://github.com/CrepuscularIRIS/HarnessRSI-Daily) → [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) (MIT). Domain cards induced with Open Scientist (domain build `embodied-agent-harness` v1). ResearchStudio Idea 15+31 is kept as a method source under its original license.
