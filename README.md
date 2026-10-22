# Embodied-Harness-Daily

**A daily radar for embodied agent harnesses**: the loop of interfaces, tools, verifiers, memory and training signals that wraps a frontier LLM/VLM so it can drive a robot arm, a mobile manipulator, a navigator, a drone or a humanoid.
（具身智能体 harness 雷达：追踪“模型经由什么 harness 控制什么本体”的一手研究。）

Core question: *through which harness does the model control which embodiment, how is closed-loop success judged, and does the gain come from the harness, the policy, or privileged information / extra compute?* Scope and evidence levels: [EVIDENCE](docs/EVIDENCE.md).

> Current run: `embodied-full-v11-20261022` · rules `problem-core-v1.1` · 514 papers screened at L1, 121 checked at L2, 91 P3-confirmed candidates, 9 posters in Reel s001. The ratings rank reading priority. They are not peer review and do not endorse any venue.
> （档位是“值不值得读”的判断，不是审稿结论。）

## Featured Reel — Issue s001

Nine papers, nine mechanism types, **9 distinct layouts**. Each poster was checked against the paper's full text by Opus 5.5 and passed visual QA. Where a poster narrows a claim, the change is logged with numbers mapped to sections and tables in `reel/<id>/SOURCE.md` (3 places this issue). Selection log: [selection-001](research/scoring/runs/embodied-full-v11-20261022/selections/selection-001.md) · [Reel index](reel/README.md).

| | | |
|:-:|:-:|:-:|
| <a href="reel/2610.27350/poster.png"><img src="reel/2610.27350/poster.png" width="240"></a><br>**[2610.27350](https://arxiv.org/abs/2610.27350) · Safety diagnosis**<br>Same model, same first frame: 15/15 refusals when asked versus 0/15 refusals inside the action loop.<br>同一输入、两条通道：问答会拒绝，动作循环不拒绝。<br>*Layout: side-by-side contrast* | <a href="reel/2411.04549/poster.png"><img src="reel/2411.04549/poster.png" width="240"></a><br>**[2411.04549](https://arxiv.org/abs/2411.04549) · Verification signal**<br>Is a VLM progress score measuring progress, or just echoing temporal order? Shuffle the frames and find out.<br>进度分数到底在测什么。<br>*Layout: ablation contrast* | <a href="reel/2610.25114/poster.png"><img src="reel/2610.25114/poster.png" width="240"></a><br>**[2610.25114](https://arxiv.org/abs/2610.25114) · Self-improvement attribution**<br>Splits the gain into feedback, version inheritance and attempt selection; frozen skills then run under cheap callers from other model families.<br>自我改进收益拆解。<br>*Layout: gain decomposition* |
| <a href="reel/2510.20328/poster.png"><img src="reel/2510.20328/poster.png" width="240"></a><br>**[2510.20328](https://arxiv.org/abs/2510.20328) · Memory**<br>MemER: for minute-long, partially observable manipulation, what matters is *what* to remember, not how much.<br>该记什么，而非记更多。<br>*Layout: condition matrix* | <a href="reel/2610.15572/poster.png"><img src="reel/2610.15572/poster.png" width="240"></a><br>**[2610.15572](https://arxiv.org/abs/2610.15572) · Privileged supervision**<br>Equal data; only the teacher's labelling policy changes (shortest path → visibility → recovery): 46.3 → 65.5 → 69.6%.<br>等量数据只换教师标注策略。<br>*Layout: progressive ladder* | <a href="reel/2506.17811/poster.png"><img src="reel/2506.17811/poster.png" width="240"></a><br>**[2506.17811](https://arxiv.org/abs/2506.17811) · Test-time sample–verify**<br>RoboMonkey: can a verifier without an oracle turn many VLA samples into closed-loop gains, and at what latency?<br>采样—打分—选择及其时延。<br>*Layout: pipeline* |
| <a href="reel/2311.13373/poster.png"><img src="reel/2311.13373/poster.png" width="240"></a><br>**[2311.13373](https://arxiv.org/abs/2311.13373) · RL with a teacher**<br>A fallible LLM teacher speeds up a small RL student, which then outgrows it (0.77 vs 0.52).<br>会犯错的 LLM 教师与超越教师的学生。<br>*Layout: stage curve* | <a href="reel/2411.00081/poster.png"><img src="reel/2411.00081/poster.png" width="240"></a><br>**[2411.00081](https://arxiv.org/abs/2411.00081) · Multi-agent evaluation**<br>PARTNR: an LLM partner made humans *slower* (3046 → 4267 steps).<br>人机合作的反直觉结果。<br>*Layout: grid + bars* | <a href="reel/2602.15875/poster.png"><img src="reel/2602.15875/poster.png" width="240"></a><br>**[2602.15875](https://arxiv.org/abs/2602.15875) · Action interface**<br>Fly0: fix the MLLM, sensing and planner, swap only the goal interface. SR 62.1 → 70.4, false-lock 0.16 → 0.05.<br>只换目标接口。<br>*Layout: layered stack* |

## High-Score Papers (2026)

The table lists the 30 papers from 2026 that this run rated P3. **8 of them (✓)** are 2026 papers from the 91 P3-confirmed L3 candidates; L2 confirmed both the problem and the method fit. **The other 22 are P3 (L1)**: P3 from the abstract-and-introduction screen only. They have not reached L2 and remain unconfirmed. The 91 candidates are those confirmed through L2; most of the 514 screened papers never reached L2. Rows are not ranked. The question column keeps Sol's original `problem_statement`, in Chinese.
（✓ = L2 已核对确认；P3 (L1) = 仅初筛档位，未经 L2。表内不排名。）

| Paper | Tier | Idea Cards | The Good Question | Links |
|---|---|---|---|---|
| [EmboTeam: Grounding LLM Reasoning into Reactive Behavior Trees via PDDL for Embodied Multi…](https://arxiv.org/abs/2601.11063) `2601.11063` | P3 ✓ | [`llm_symbolic_solver_planning`](patterns/main/llm_symbolic_solver_planning.md)<br>[`multi_robot_llm_coordination`](patterns/main/multi_robot_llm_coordination.md) | 异构多机器人面对长程任务依赖和动态团队规模时，如何把自然语言目标转为可同步、可反应的执行结构。 | [arXiv](https://arxiv.org/abs/2601.11063) · code — |
| [An LLM-Agnostic, MAVLink-Based Drone Command and Control Interface and Agentic Harness Usi…](https://arxiv.org/abs/2601.15486) `2601.15486` | P3 ✓ | [`external_verification_control`](patterns/main/external_verification_control.md)<br>[`observe_act_interface`](patterns/main/observe_act_interface.md)<br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md) | 让不可信LLM经通用工具控制无人机时，如何在持续飞行中保持独立安全边界，并让任务状态的报告与实际持有者一致。 | [arXiv](https://arxiv.org/abs/2601.15486) · code — |
| [Fly0: Persistent Metric Anchoring for Zero-Shot Aerial Vision-Language Navigation](https://arxiv.org/abs/2602.15875) `2602.15875` | P3 ✓ | [`observe_act_interface`](patterns/main/observe_act_interface.md) | 零样本无人机VLN如何把低频、带不确定性的语言定位变成目标离开视野后仍可用于高频安全控制的度量目标？ | [arXiv](https://arxiv.org/abs/2602.15875) · [code](https://github.com/xuzhenxing1/Fly0) · [poster](reel/2602.15875/poster.png) |
| [From Language to Task Maps: Compiling Semantic Relations While Preserving Task-Relevant Fr…](https://arxiv.org/abs/2609.34412) `2609.34412` | P3 ✓ | [`observe_act_interface`](patterns/main/observe_act_interface.md) | 把定性操作关系直接展开为完整位姿会约束任务未指定的自由度，造成连续控制目标之间的人为冲突。 | [arXiv](https://arxiv.org/abs/2609.34412) · code — |
| [Look Before You Move: Agent-Interface-Aligned Supervision for Open-World Mobile Manipulati…](https://arxiv.org/abs/2610.15572) `2610.15572` | P3 ✓ | [`privileged_teacher_supervision`](patterns/main/privileged_teacher_supervision.md) | 开放世界移动操作的学生只能依据部署可见观测选择高层技能时，如何避免最短路轨迹后标注只教前进、不教保持可见性和失目标恢复的监督缺口？ | [arXiv](https://arxiv.org/abs/2610.15572) · code — · [poster](reel/2610.15572/poster.png) |
| [Scaling Online Exploration for Robot Agents](https://arxiv.org/abs/2610.22496) `2610.22496` | P3 ✓ | [`code_policy_trial_revision`](patterns/main/code_policy_trial_revision.md)<br>[`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md) | 在有标定RGB-D、底层控制器和有限探索预算时，机器人能否将在线试错编译成可在未见布局独立执行的感知—规划—控制程序？ | [arXiv](https://arxiv.org/abs/2610.22496) · code — |
| [Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive S…](https://arxiv.org/abs/2610.25114) `2610.25114` | P3 ✓ | [`code_policy_trial_revision`](patterns/main/code_policy_trial_revision.md)<br>[`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md)<br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md) | 离线代码技能能否在冻结后独立或由廉价异族模型执行，迭代优势究竟来自反馈、版本继承还是尝试选择？ | [arXiv](https://arxiv.org/abs/2610.25114) · code — · [poster](reel/2610.25114/poster.png) |
| [Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops](https://arxiv.org/abs/2610.27350) `2610.27350` | P3 ✓ | [`external_verification_control`](patterns/main/external_verification_control.md)<br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md) | 同一模型面对相同明确有害指令和首帧时，机器人动作循环的拒绝行为是否与显式行动前安全问询分离？ | [arXiv](https://arxiv.org/abs/2610.27350) · [code](https://github.com/Arnav-Gr0ver/Refuses-When-Asked-Complies-When-Acting) · [poster](reel/2610.27350/poster.png) |
| [Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334) `2601.20334` | P3 (L1) | [`observe_act_interface`](patterns/main/observe_act_interface.md)<br>[`code_policy_trial_revision`](patterns/main/code_policy_trial_revision.md) | 在可读取特权环境状态的操作仿真中，未经机器人专用修改的通用软件agent能否无需演示和微调完成以任务级推理为主的控制。 | [arXiv](https://arxiv.org/abs/2601.20334) · [code](https://github.com/robiemusketeer/faea-sim) |
| [MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/abs/2601.20831) `2601.20831` | P3 (L1) | [`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md) | 小型具身MLLM在在线存储和计算受限时，如何主动保留、更新或丢弃经历而非依赖全量历史检索。 | [arXiv](https://arxiv.org/abs/2601.20831) · code — |
| [A Modern System Recipe for Situated Embodied Human-Robot Conversation with Real-Time Multi…](https://arxiv.org/abs/2602.04157) `2602.04157` | P3 (L1) | [`observe_act_interface`](patterns/main/observe_act_interface.md) | 机器人实时对话时，如何把连续语音生成与主动转头、寻找物体和请求新视觉信息交错，以维持共享注意。 | [arXiv](https://arxiv.org/abs/2602.04157) · code — |
| [GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory P…](https://arxiv.org/abs/2602.04315) `2602.04315` | P3 (L1) | [`planner_composes_code_and_policies`](patterns/main/planner_composes_code_and_policies.md)<br>[`observe_act_interface`](patterns/main/observe_act_interface.md)<br>[`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md) | 无需真机演示时，如何把基础模型语义知识转成满足几何约束的3D操作轨迹，并生成可训练学生的数据。 | [arXiv](https://arxiv.org/abs/2602.04315) · [code](https://github.com/AIGeeksGroup/GeneralVLA) |
| [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Languag…](https://arxiv.org/abs/2602.12281) `2602.12281` | P3 (L1) | [`sample_verify_select`](patterns/main/sample_verify_select.md)<br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md) | VLA动作与语言意图不一致时，固定数据条件下，扩大指令改写和动作采样并验证选择能否比扩大策略学习更有效。 | [arXiv](https://arxiv.org/abs/2602.12281) · code — |
| [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) `2602.12405` | P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md) | 在大量二元失败标签而少量语言解释标签的机器人视频条件下，如何检测并解释未预定义的失败？ | [arXiv](https://arxiv.org/abs/2602.12405) · code — |
| [Agentic AI for Robot Control: Flexible but still Fragile](https://arxiv.org/abs/2602.13081) `2602.13081` | P3 (L1) | [`observe_act_interface`](patterns/main/observe_act_interface.md)<br>[`external_verification_control`](patterns/main/external_verification_control.md) | 已提供技能工具、语义状态和恢复循环的LLM机器人控制，为何在真实部分可观测执行中仍会出现提示敏感、随机次优和指令错误。 | [arXiv](https://arxiv.org/abs/2602.13081) · code — |
| [Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control](https://arxiv.org/abs/2602.13193) `2602.13193` | P3 (L1) | [`trained_vlm_vla_hierarchy`](patterns/main/trained_vlm_vla_hierarchy.md)<br>[`planner_composes_code_and_policies`](patterns/main/planner_composes_code_and_policies.md) | 高层VLM已经知道应抓哪里或怎样移动时，如何扩展低层VLA可理解的命令粒度，使推理能真正控制行为。 | [arXiv](https://arxiv.org/abs/2602.13193) · code — |
| [Contextual Safety Reasoning and Grounding for Open-World Robots](https://arxiv.org/abs/2602.19983) `2602.19983` | P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md) | 无预给地图和安全规格时，机器人如何从视觉在线推断情境安全规则、空间grounding并在感知不确定性下执行约束？ | [arXiv](https://arxiv.org/abs/2602.19983) · code — |
| [PhysMem: Scaling Test-Time Memory for Embodied Physical Reasoning](https://arxiv.org/abs/2602.20323) `2602.20323` | P3 (L1) | [`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md) | 冻结 VLM 的部署期物理经验如何经过可检验抽象再复用，避免条件改变后直接检索经验造成反复错误？ | [arXiv](https://arxiv.org/abs/2602.20323) · code — |
| [Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/abs/2602.21198) `2602.21198` | P3 (L1) | [`sample_verify_select`](patterns/main/sample_verify_select.md) | 具身代理如何在单次长程部署中利用执行后与事后反思同时纠正动作策略和内部评估器，减少重复失败及局部反馈的错配归因？ | [arXiv](https://arxiv.org/abs/2602.21198) · code — |
| [From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?](https://arxiv.org/abs/2603.03148) `2603.03148` | P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md)<br>[`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md) | 工具、工作记忆和情节记忆包裹的 LLM，能否在模拟家庭移动操作任务中可靠规划、恢复并判断完成？ | [arXiv](https://arxiv.org/abs/2603.03148) · code — |
| [Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Mani…](https://arxiv.org/abs/2603.04466) `2603.04466` | P3 (L1) | [`code_policy_trial_revision`](patterns/main/code_policy_trial_revision.md) | 无示范、无梯度和人工奖励的连续机械臂操作中，多模态编码代理能否根据失败诊断直接重写完整低层控制器而非仅选技能？ | [arXiv](https://arxiv.org/abs/2603.04466) · code — |
| [OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency](https://arxiv.org/abs/2603.10682) `2603.10682` | P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md)<br>[`observe_act_interface`](patterns/main/observe_act_interface.md) | 完全机载零样本无人机VLN如何同时满足高频目标生成、低频长程监控与安全轨迹执行，避免单流决策和记忆覆盖导致失败？ | [arXiv](https://arxiv.org/abs/2603.10682) · [code](https://github.com/Robotics-STAR-Lab/OnFly) |
| [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558) `2603.11558` | P3 (L1) | [`planner_composes_code_and_policies`](patterns/main/planner_composes_code_and_policies.md)<br>[`external_verification_control`](patterns/main/external_verification_control.md) | 真实长程操作中，如何让同一VLM控制器贯穿自复位采集、策略学习与技能执行，减少人工重置和采集部署语义错配？ | [arXiv](https://arxiv.org/abs/2603.11558) · code — |
| [HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied…](https://arxiv.org/abs/2603.11975) `2603.11975` | P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md) | 如何独立评估并低延迟地检测家庭具身 agent 视频中的动态危险动作，而不把检测能力混进规划成功率？ | [arXiv](https://arxiv.org/abs/2603.11975) · code — |
| [Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis](https://arxiv.org/abs/2603.13528) `2603.13528` | P3 (L1) | [`external_verification_control`](patterns/main/external_verification_control.md)<br>[`learner_state_teacher_correction`](patterns/main/learner_state_teacher_correction.md) | 如何从成功真机演示合成有效的失败—纠正配对，使视觉失败解释能转化为可执行的操作恢复轨迹？ | [arXiv](https://arxiv.org/abs/2603.13528) · code — |
| [Robotic Agentic Platform for Intelligent Electric Vehicle Disassembly](https://arxiv.org/abs/2603.18520) `2603.18520` | P3 (L1) | [`observe_act_interface`](patterns/main/observe_act_interface.md) | 边缘硬件上LLM控制真实拆卸平台时，开放ROS服务自动发现为何不能像结构化工具接口一样可靠完成所需机器人动作？ | [arXiv](https://arxiv.org/abs/2603.18520) · code — |
| [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) `2603.22435` | P3 (L1) | [`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md)<br>[`observe_act_interface`](patterns/main/observe_act_interface.md) | 代码控制机械臂的成功究竟来自编码模型能力还是人工高层原语，减少设计者脚手架后增加交互计算能补回多少能力？ | [arXiv](https://arxiv.org/abs/2603.22435) · code — |
| [ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction](https://arxiv.org/abs/2603.26997) `2603.26997` | P3 (L1) | [`observe_act_interface`](patterns/main/observe_act_interface.md)<br>[`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md) | 在不同模型和 ROS 机器人之间保持执行、安全与日志接口不变，才能辨别物理行为差异来自模型还是 executive 层。 | [arXiv](https://arxiv.org/abs/2603.26997) · code — |
| [Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning](https://arxiv.org/abs/2604.02318) `2604.02318` | P3 (L1) | [`harness_memory_skill_reuse`](patterns/main/harness_memory_skill_reuse.md)<br>[`external_verification_control`](patterns/main/external_verification_control.md) | 训练自由 VLN 在空间歧义下局部振荡和反复访问，如何以进展监测与反思打破死循环而减少模型查询。 | [arXiv](https://arxiv.org/abs/2604.02318) · code — |
| [RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains](https://arxiv.org/abs/2604.05226) `2604.05226` | P3 (L1) | [`harness_effect_evaluation`](patterns/main/harness_effect_evaluation.md)<br>[`llm_symbolic_solver_planning`](patterns/main/llm_symbolic_solver_planning.md) | 如何让非专家通过语言可复现地改变操作任务约束和成功定义，以发现固定测试集隐藏的策略失败？ | [arXiv](https://arxiv.org/abs/2604.05226) · code — |

## Card-Based Research（抽卡式科研）

**Drawing cards for research.** We take the field's recurring research operations and turn them into **pattern cards** that can be searched. Each card records:

- an **operational signature**: what the method actually does, step by step;
- **cognitive barriers**: the beliefs the field holds that the operation runs into;
- **failure modes and success conditions**: properties you can check in a paper's text, each with citations;
- **reviewer expectations**: what the papers that were read do or concede (E01–E22).

There are three uses. Draw a card for a new paper: which operation does it really perform, and which conditions does it guarantee? Draw cards for a new idea: combine operations from different cards, or take a barrier on a card and challenge it. The cards also serve as the yardstick when papers are rated: questions are organised into the problem families **F1 attribution · F2 signal trust · F3 transfer boundary · F4 information access · F5 monotonicity assumption** (+ F0 other).

> 抽卡式科研：把领域里反复出现的研究操作逆向成可检索的卡片（操作签名＋认知障碍＋失败模式＋审稿期望）。读新论文时“抽卡”识别它真正做了什么、保证了哪些条件；构思新 idea 时组合不同卡的操作，或挑战卡上记录的共识与障碍（F1–F5 问题族）。

**The cards come from this corpus, not from a preset taxonomy.** We read papers in full and worked backwards from them. 51 sub-cards (K101–K805) come from 50 full-text readings in the frozen Open Scientist domain `embodied-agent-harness/v1`. 7 sub-cards (R01–R07) were induced from the wave-1 board's weak fits: 60 of the first 105 assigned papers, each read in full. Every condition carries an `arXiv#signature` citation to its source paper. The card version is **fixed for this run**: we never edit a card to fit a paper. Details: [patterns/overview](patterns/overview.md) · [anti-patterns](patterns/anti-patterns.md).
（17 张主卡、58 张子卡全部由本语料论文逆向归纳，每张卡锚定来源论文；本 run 内卡片版本固定。）

## Pattern Cards — 17 main / 58 sub

| Main card | Name | Operational signature (short) | Problem families | Subs |
|---|---|---|---|---|
| [observe_act_interface](patterns/main/observe_act_interface.md) | Design the Frozen Model's Observation and Action Interface | model observes on request and emits a primitive, semantic, pixel or pose target; the harness grounds it and returns receipts | F1, F5 | 9 |
| [planner_composes_code_and_policies](patterns/main/planner_composes_code_and_policies.md) | Let a Frontier Planner Compose Code, Learned Tools and Frozen VLAs | planner writes code cells or typed calls to primitives, learned tools and frozen VLAs; branches and replans | F1, F5 | 3 |
| [external_verification_control](patterns/main/external_verification_control.md) | Gate, Monitor and Diagnose Actions Outside the Model | external checker gates each proposal; success or stagnation monitors hand control back; diagnose or backtrack | F2 | 4 |
| [harness_memory_skill_reuse](patterns/main/harness_memory_skill_reuse.md) | Build Context, Notes and Skills with the Weights Frozen | bounded context plus retrieval; notes, skill libraries and replay cards carried across episodes | F5 | 4 |
| [harness_self_optimization](patterns/main/harness_self_optimization.md) | Revise the Harness Itself from Execution Traces | optimizer reads traces and edits the harness; same-model evaluation and an acceptance gate | F1, F3 | 3 |
| [offline_harness_distillation](patterns/main/offline_harness_distillation.md) | Distil Success-Filtered Teacher Harness Trajectories into a Compact Student | SFT a compact VLM on success-filtered teacher turns so it pilots the same or a reduced harness | F1 | 3 |
| [privileged_teacher_supervision](patterns/main/privileged_teacher_supervision.md) | Generate Supervision with a Privileged Teacher the Student Cannot See | a teacher with privileged simulator state produces success-checked targets; the student sees only cameras | F3, F4 | 3 |
| [learner_state_teacher_correction](patterns/main/learner_state_teacher_correction.md) | Correct, Review or Relabel at Learner-Induced States | teacher repairs, replaces or relabels at the states the student visits; admission check before training | F2, F5 | 5 |
| [on_policy_distillation_objectives](patterns/main/on_policy_distillation_objectives.md) | Distil On-Policy with Logit, Privileged-Self, Agreement or Harness-Contrast Signals | at student states, the signal is teacher logits, a privileged self, agreement, or a with- vs without-harness contrast | F4 | 6 |
| [harness_native_rl](patterns/main/harness_native_rl.md) | Train the Policy Through, or Aligned with, the Deployment Harness | capture calls from the unmodified harness at a proxy; outcome reward; group-relative update | F1 | 4 |
| [teacher_seeded_sparse_rl](patterns/main/teacher_seeded_sparse_rl.md) | Make Sparse-Success Embodied RL Learnable | teacher-data init, rollout-only hints or a privileged dense reward, so that sparse RL can learn | F1 | 4 |
| [harness_effect_evaluation](patterns/main/harness_effect_evaluation.md) | Separate the Harness Effect from the Model Effect | cross models × harnesses on fixed tasks; paired statistics; failure endpoints; reconcile cost | F1 | 5 |
| [llm_symbolic_solver_planning](patterns/main/llm_symbolic_solver_planning.md) | Let a Solver Plan from an LLM-Written Formal Model | LLM writes PDDL, a KB or constraints; a classical solver plans, validates or prunes | F1, F5 | 1 |
| [trained_vlm_vla_hierarchy](patterns/main/trained_vlm_vla_hierarchy.md) | Train the High-Level VLM That Commands a Low-Level Policy | fine-tune the high-level VLM that issues commands to a trained low-level VLA | F1, F5 | 1 |
| [multi_robot_llm_coordination](patterns/main/multi_robot_llm_coordination.md) | Allocate and Repair Multi-Robot Plans with LLM Agents | LLM allocators split the task across robots and repair allocations from feasibility and conflict checks | F1, F5 | 1 |
| [code_policy_trial_revision](patterns/main/code_policy_trial_revision.md) | Write the Policy as Code and Rewrite It from Trial Diagnostics | LLM writes the controller program, rewrites it from trial diagnostics, and deploys it without a model in the loop | F1, F3 | 1 |
| [sample_verify_select](patterns/main/sample_verify_select.md) | Sample Candidate Actions and Let a Verifier Choose | sample N candidate actions; a verifier or reflector picks the one to execute | F2, F5 | 1 |

Problem families follow [PROBLEM_MAP](research/scoring/PROBLEM_MAP.md). The K-series digit is the card's *domain* family (1 = interface … 8 = evaluation), which is a different scheme from the problem families F0–F5.

<details>
<summary><b>All 58 sub-cards</b> (click to expand)</summary>

**K1xx · Interface and composition (10)**

- [K101](patterns/sub/K101.md) Let a frozen frontier MLLM steer primitive actions through a minimal observe/step tool pair
- [K102](patterns/sub/K102.md) Keep dense geometry inside harness tools and return numeric receipts to the model on request
- [K103](patterns/sub/K103.md) Model proposes a visual target; harness back-projects, checks feasibility and executes or asks to reselect
- [K104](patterns/sub/K104.md) Restrict the model to a discrete semantic action vocabulary executed by a deterministic or frozen low-level executor
- [K105](patterns/sub/K105.md) Have the frozen planner write code cells that compose perception, geometry and motion primitives
- [K106](patterns/sub/K106.md) Train a compact policy to be invoked by a planner through a typed call
- [K107](patterns/sub/K107.md) Wrap a frozen VLA as a planner-controlled primitive and inspect before committing
- [K108](patterns/sub/K108.md) Offer extra tools as optional calls beside primitive actions and let the model choose
- [K109](patterns/sub/K109.md) Insert a separate VLM that turns images into text for the planner
- [K110](patterns/sub/K110.md) Replace raw shell interaction with compact LM-oriented commands (agent-computer interface)

**K2xx · Verification and control (4)**

- [K201](patterns/sub/K201.md) Treat each model proposal as a request and gate it with an external checker before execution
- [K202](patterns/sub/K202.md) Run the executor until a completion or stagnation monitor fires, then hand control back to the planner
- [K203](patterns/sub/K203.md) After a scored attempt, let the agent write and run a diagnostic program before resetting
- [K204](patterns/sub/K204.md) Give the coding-agent solver checkpoint/backtrack and parameter-search tools over full simulator state

**K3xx · Memory and skills (4)**

- [K301](patterns/sub/K301.md) Rebuild each call's context from a bounded within-episode selection with retrieval for the rest
- [K302](patterns/sub/K302.md) Summarize repeated-task experience into notes injected into later episodes
- [K303](patterns/sub/K303.md) Mine, consolidate and review a reusable skill library from successful executions or demonstrations
- [K304](patterns/sub/K304.md) Compile a successful harness trajectory into a planner-free replay card

**K4xx · Harness self-optimization (3)**

- [K401](patterns/sub/K401.md) With the model frozen, let an optimizer agent revise the harness from raw traces and keep improvements
- [K402](patterns/sub/K402.md) Teacher revises a text playbook from comparing its own and a light agent's runs; accept when the light agent matches the teacher
- [K403](patterns/sub/K403.md) Alternate RL on the student with harness revisions accepted only when they help the current checkpoint

**K5xx · Offline distillation and privileged supervision (6)**

- [K501](patterns/sub/K501.md) SFT a compact VLM on success-filtered frontier-teacher turns so it pilots the identical harness
- [K502](patterns/sub/K502.md) Train the student on teacher data while the student's interface lacks part of the teacher's harness
- [K503](patterns/sub/K503.md) Use a frontier LLM with privileged simulator state to iterate a program teacher until it succeeds
- [K504](patterns/sub/K504.md) Branch successful teacher runs from saved simulator checkpoints to add recovery and diversity, keeping only verified branches
- [K505](patterns/sub/K505.md) A privileged rule teacher acts step by step in the student's skill vocabulary, with templated state reasoning
- [K506](patterns/sub/K506.md) Instead of cloning a privileged expert, estimate its missing state inputs and run it frozen

**K6xx · On-policy correction and distillation (11)**

- [K601](patterns/sub/K601.md) Repair the student's failed episode from its earliest harmful step and admit only validated corrections
- [K602](patterns/sub/K602.md) A frontier harnessing agent reviews every student proposal and replaces unsound ones with corrections valid in the minimal harness
- [K603](patterns/sub/K603.md) Query the teacher only at learner states flagged by a gate
- [K604](patterns/sub/K604.md) Relabel learner-visited states with a privileged expert, when dynamics allow
- [K605](patterns/sub/K605.md) On-policy distillation from a white-box teacher's token logits at student-visited states
- [K606](patterns/sub/K606.md) Score the student's own tokens with a privileged-context copy of itself and add the divergence to RL
- [K607](patterns/sub/K607.md) Train one model jointly under privileged and deployment-context views, deploying only the plain view
- [K608](patterns/sub/K608.md) Sample target actions from a model copy given privileged context, then verify or match
- [K609](patterns/sub/K609.md) Reward student candidates by semantic agreement with black-box teacher actions at the same state
- [K610](patterns/sub/K610.md) Prefer the teacher's harness-conditioned action over its harness-stripped action at student states
- [K611](patterns/sub/K611.md) Start student RL from states produced by teacher-student interaction

**K7xx · RL in the harness (8)**

- [K701](patterns/sub/K701.md) Train the policy through an unmodified harness by capturing its model calls at an API proxy
- [K702](patterns/sub/K702.md) Assemble captured harness calls into training rows by prefix rules and keep credit at rollout level
- [K703](patterns/sub/K703.md) Curate a trainable task band and harden the sandbox against reward leakage
- [K704](patterns/sub/K704.md) RL a small coder/planner model directly inside an embodied code harness on sparse success
- [K705](patterns/sub/K705.md) Fork the simulator at each decision step, score completions with a privileged dense reward, continue from the best
- [K706](patterns/sub/K706.md) Train the policy under the same context-construction rules it will be deployed with
- [K707](patterns/sub/K707.md) Inject teacher-written skill hints into RL rollouts only, removed at evaluation
- [K708](patterns/sub/K708.md) Initialize from teacher-derived data so every task has nonzero success before sparse-reward RL

**K8xx · Evaluation methodology (5)**

- [K801](patterns/sub/K801.md) Cross frozen models with harnesses on fixed tasks and report harness variance with paired statistics
- [K802](patterns/sub/K802.md) Hold the model fixed and toggle one harness component or layer at a time
- [K803](patterns/sub/K803.md) Swap the model under a fixed embodied harness and the harness under a fixed model on the same episodes
- [K804](patterns/sub/K804.md) Decompose outcomes into failure categories, endpoints and per-task repeat patterns
- [K805](patterns/sub/K805.md) Re-price runs from raw per-turn usage and reconcile against billed spend

**R0x · Board-induced, 2026-10-21 (7; R04 and R07 sit under the interface main)**

- [R01](patterns/sub/R01.md) Have the LLM write a formal planning model and let a classical solver compute, check or prune the plan
- [R02](patterns/sub/R02.md) Fine-tune the high-level VLM that issues language or motion commands to a trained low-level policy
- [R03](patterns/sub/R03.md) Let LLM agents allocate subtasks across robots and repair the allocation from feasibility, conflict or event feedback
- [R04](patterns/sub/R04.md) Expose the robot software stack to the model as protocol-level tools (ROS connectors, MCP servers, policy start/switch calls)
- [R05](patterns/sub/R05.md) Write the controller as code and rewrite it between trials from execution diagnostics
- [R06](patterns/sub/R06.md) Sample several candidate actions and execute the one a verifier scores highest
- [R07](patterns/sub/R07.md) Harness turns geometry into a short candidate list or written advice; the model only chooses

</details>

## Pipeline（流程）

```mermaid
flowchart LR
  A[Grok bot<br>inbox/] --> B[ingest<br>corpus.jsonl] --> C[full-material cache] --> D[L1 screen<br>6.1 Sol] --> E[L2 check<br>6.1 Sol] --> F[L3 selection<br>Opus 5.5] --> G[Reel<br>Opus 5.5]
```

1. **Retrieve.** A Grok bot searches arXiv, HF Papers and official lab pages. It writes only to `inbox/` and keeps only candidates it has verified against a primary source. It does not score, and caps each run at 12 `ready` candidates. → [GROK_PROMPT](docs/agents/GROK_PROMPT.md) · [inbox](inbox/README.md)（只收一手证据候选）
2. **Ingest.** Candidates are deduplicated by version-stripped ID, DOI and title, then written to `research/corpus.jsonl`. → [ingest.py](research/ingest.py)
3. **Cache full material.** The uncropped arXiv HTML/PDF is cached once and kept local; we never re-download for a full rerun. → [fetch_fulltext.py](research/fetch_fulltext.py)
4. **L1 screen.** 6.1 Sol subagents get the abstract and introduction, sliced by script. They answer the four questions and assign a tier. → [SOL_BATCH_PROMPT](research/scoring/SOL_BATCH_PROMPT.md)（初筛：四问＋档位）
5. **L2 check.** Sol reads the method and main-experiment sections with locators, confirms Q1 and Q4, and runs the sub-card condition checks. A further random 10% goes to a missed-paper audit. → [PROBLEM_CORE §5–6](research/scoring/PROBLEM_CORE.md)（核对＋子卡条件检查＋漏检抽查）
6. **L3 select.** Opus 5.5 deduplicates papers that pose the same problem, then selects for diversity of mechanism type. At most 9 are chosen; there is no numeric ranking. → [SELECTION](research/scoring/SELECTION.md)
7. **Reel.** Opus 5.5 checks each selected paper against its full text, builds a poster around that paper's mechanism, and runs visual QA on the rendered result. Only papers that pass are marked ready. → [OPUS_REEL_PROMPT](research/scoring/OPUS_REEL_PROMPT.md) · [reel](reel/README.md)

Run record: [run.md](research/scoring/runs/embodied-full-v11-20261022/run.md) · [progress.md](research/scoring/runs/embodied-full-v11-20261022/progress.md). Maintenance notes: [PIPELINE](docs/PIPELINE.md) · [MAINTAINING](docs/MAINTAINING.md).

## Scoring: problem-core-v1.1（问题优先）

**We judge whether the question is good before we judge whether the execution is good.** （先判问题好不好，再判执行好不好。）

- **Layer 1 (problem), four questions:**
  - **Q1 Does the problem exist?** The basis must be measured, proven, a counterexample or a constraint conflict; an assertion is not enough.
  - **Q2 Is it open?** Compared only against work released *before* this paper, on the same problem under the same conditions.
  - **Q3 What changes if it is solved?** A `capability` or a field `judgment`.
  - **Q4 Does the method target the problem?**
- **Layer 2 (execution):** checks drawn from the sub-cards (*Operation / When it works / When it fails / Counterexamples*). Each check is marked `holds / partial / fails / unknown / NA / challenged_with_evidence`, and we report coverage only. No score is computed. Not following a card's steps does **not** count as `fails`.
- **Separate fields:** `problem_tier` (P0–P3) is kept apart from `evidence_status` (`confirmed / pending_*`), `priority` and `next_action`. **P3** means: real basis + open (barrier / failure / new bottleneck) + capability or judgment. An L1 P3 is provisional until L2 confirms Q4 = `fits`. Missing material yields `null`, never P0.
- **Funnel and budget:** L1 covers every paper. L2 takes at most 20% of the L1 count (high, then medium priority), plus a fixed 10% random audit drawn from P0/P1, F0, `needs_material` and `park`. In this run the audit moved 3 papers up from P2 to P3 (2 of them confirmed).
- **Never counted:** code links, venue, acceptance, citations, authors, writing style, and how many cards a paper matches.

> 两层分开记录、不相加：问题层四问（成立／开放／改变什么／对准）＋执行层子卡条件检查。档位 P0–P3 与证据状态分离；L1 全量、L2 ≤20% 外加 10% 漏检抽查。

## Start here（从这里开始）

| What | Where |
|---|---|
| Rules | [PROBLEM_CORE](research/scoring/PROBLEM_CORE.md) · [PROBLEM_MAP](research/scoring/PROBLEM_MAP.md) · [scoring index](research/scoring/README.md) · [EVIDENCE](docs/EVIDENCE.md) |
| Pattern cards | [overview](patterns/overview.md) · [main/](patterns/main/) · [sub/](patterns/sub/) · [anti-patterns](patterns/anti-patterns.md) · [PATTERN_INDEX](research/scoring/PATTERN_INDEX.md) |
| This run | [run.md](research/scoring/runs/embodied-full-v11-20261022/run.md) · [progress](research/scoring/runs/embodied-full-v11-20261022/progress.md) · [selection-001](research/scoring/runs/embodied-full-v11-20261022/selections/selection-001.md) |
| Reel | [reel/README](reel/README.md) · [SELECTION](research/scoring/SELECTION.md) · [OPUS_REEL_PROMPT](research/scoring/OPUS_REEL_PROMPT.md) |
| Agents | [Grok prompt](docs/agents/GROK_PROMPT.md) · [Sol batch prompt](research/scoring/SOL_BATCH_PROMPT.md) · [CC start](docs/agents/START_CC.md) |
| Candidates | [inbox](inbox/README.md) |
| Maintenance | [AGENTS](AGENTS.md) · [MAINTAINING](docs/MAINTAINING.md) · [PIPELINE](docs/PIPELINE.md) · [2026-10-22 reset](docs/RESET_2026-10-22.md) |

`make check` validates local structure only. Passing structural checks, existing citations and correct arithmetic does not mean any result has been scientifically validated or reproduced.

---

**Run** `embodied-full-v11-20261022` · **rules** `problem-core-v1.1` · cards fixed for this run. Tiers are judgments about reading priority, made by model readers (6.1 Sol at L1/L2, Opus 5.5 at L3/Reel). They are not peer review, venue endorsements or reproductions. Full texts, keys and private logs stay local.

**License:** MIT ([LICENSE](LICENSE)). Base pipeline cloned from [CUA Radar](https://github.com/CrepuscularIRIS/cua-architecture-radar), itself cloned from [HarnessRSI Daily](https://github.com/CrepuscularIRIS/HarnessRSI-Daily), built on [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) (MIT). Domain cards were induced with Open Scientist (domain build `embodied-agent-harness` v1). ResearchStudio Idea 15+31 is kept as a method source under its original license.
