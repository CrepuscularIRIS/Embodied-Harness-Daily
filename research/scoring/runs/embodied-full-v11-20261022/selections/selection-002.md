# selection-002 · embodied-full-v11-20261022

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 精选席（内部 Subagent）；日期 2026-10-22
- 候选池：`candidates-s002-pool.json`，327 篇。327篇全为P3/confirmed（L2第二波后to_l3共336，扣s001已选9）；其中L1=P2、L2上移P3者56篇（progress记第二波上移67篇，其余未进to_l3或非confirmed）。
- 结果：入选 9 篇（其中第二波上移篇 8 篇）；同题去重 33 篇（对本期入选 7、对 s001 入选 26）；多样性截断 285 篇。
- s001 已选 9 篇不在本池，未重复入选。档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。

## 入选

| # | paper_id | 标题 | 族 | q3 | 上移 | 类型 | 入选理由 |
|---|---|---|---|---|---|---|---|
| 1 | 2306.15724 | REFLECT: Summarizing Robot Experiences for Failure Explanation and Cor | F0/F2 | capability | P2→P3 | 失败解释→纠正 | 固定GPT-4在100个注入失败上，完整层次经验摘要纠正率79.1/80.7%，去掉解释仅41.9/56.1%，直接说明“先定位致因再纠正”是可测的独立瓶颈，而非只判成败。 |
| 2 | 2309.09919 | Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Ag | F2 | capability | P2→P3 | 形式约束门控 | 同一GPT-4规划器下，提示里写禁令安全率仅56%，可执行LTL自动机门控升至100%且成功率98%，把“语言服从”换成“动作级剪枝”的对照清楚。 |
| 3 | 2409.01652 | ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints fo | F0/F4 | capability | P2→P3 | 约束生成+优化求解 | 同7个真机任务上VoxPoser/自动ReKep/人工标注约束为10.0/44.3/68.6%，既测到自动生成关键点约束的真实能力，也给出人工上界，问题与差距同时清楚。 |
| 4 | 2603.26666 | VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action | F2/F4 | capability | P2→P3 | 在线蒸馏目标 | on-policy蒸馏目标卡唯一候选：同batch对照中forward-KL成功率早期跌逾50%、硬CE熵坍缩而reverse-KL稳定，直接回答“在学生自身状态上用什么目标蒸馏VLA”。 |
| 5 | 2501.11858 | EmbodiedEval: Evaluate Multimodal LLMs as Embodied Agents | F0/F5 | judgment | P2→P3 | 单体MLLM闭环评测 | 同一观测/动作空间下人类97.26%对GPT-4o 25.00%、交互动作有效率96.81%对9.56%，并有固定模型加历史图像反而退化的干预，直接挑战“静态图文能力≈具身能力”。 |
| 6 | 2307.01928 | Robots That Ask For Help: Uncertainty Alignment for Large Language Mod | F2 | capability | — | 不确定性校准求助 | s001已列为求助槽下期首选；以共形预测校准“何时求助”，在相近规划成功率下比Simple Set基线少求助（规划0.87时帮助率0.67 vs 0.81），问题与保证边界都清楚。 |
| 7 | 2506.06677 | RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipula | F1/F0 | judgment | P2→P3 | 分层归因诊断 | 固定微调OpenVLA并对齐子目标切换，GPT-4o规划16.04%、盲视觉15.10%、GT-plan 25.16%，直接显示高层观察/规划指标与闭环成功脱节、低层仍是硬约束。 |
| 8 | 2512.02002 | LLM-Driven Corrective Robot Operation Code Generation with Static Text | F2/F3 | judgment | P2→P3 | 反馈来源替代 | 同20个规则化任务三次重复，静态LLM文本模拟反馈与动态模拟语义反馈均93.3%成功，直接检验“修码环必须运行专用动态模拟器”这一配置依赖。 |
| 9 | 2609.35318 | DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulat | F0/F4 | capability | P2→P3 | 人视频→示范数据生成 | 单次人类视频经可检验的重建、接触/轨迹优化与扩增生成示范，11类真机任务每任务10次平均63.6%对最强数据基线18.2%，把绳、抽屉、多物体任务带进视觉闭环策略范围。 |

### 画报侧重（供制作环节分配版式）

- **2306.15724**（失败解释→纠正）：问题：只看终态或平铺叙述会漏掉早期致因，LLM能否从多模态执行历史定位失败并给出可执行纠正；结果：执行/规划失败纠正79.1%/80.7%，无解释41.9%/56.1%，去渐进摘要60.5%/64.9%。版式宜做“事件→子目标层次摘要→定位致因→纠正计划”的时间轴；须注明模拟用真值对象状态、真实30段只报解释/定位无闭环纠正分母。
- **2309.09919**（形式约束门控）：问题：自然语言时序禁令如何变成执行前可检查、又不阻断可完成任务的约束；结果：FourRoom/MobileManip安全率基础38/30、NL约束56/56、未验证chip84/94、专家验证chip100/100（SR98/98），Spot两任务chip安全100%。版式宜做“语言禁令 vs 自动机剪枝”四档阶梯条；必须标注依赖专家验证翻译、完美命题标签与转移模型，不能写成真实系统无条件安全。
- **2409.01652**（约束生成+优化求解）：问题：能否从RGB-D与语言自动产生可由优化器执行的时空关键点约束，而不逐任务手写；结果：7任务×10次平均10.0/44.3/68.6%，3种扰动各10次6.7/26.7/46.7%。版式宜做“关键点+约束代码→优化器”管线与三档成功率条；须突出44.3%绝对值与人工版差距，主要失败为跟踪、缺关键点和VLM引用错误，服装实验73.8%是条件成功率。
- **2603.26666**（在线蒸馏目标）：问题：在学生访问状态上蒸馏VLA时如何避免熵膨胀/坍缩并保留预训练能力；结果：LIBERO一轨迹学生48.9→87.4（+GRPO 93.4），RoboTwin四任务45.2→71.1（教师74.0），并比较OPD与离线SFT遗忘。版式宜做三种目标的训练曲线/熵对比；须注明精细消融集中于一任务，需白盒教师logits与相容tokenizer，不推广到黑盒API。
- **2501.11858**（单体MLLM闭环评测）：问题：静态感知能力能否代表闭环交互能力；结果：GPT-4o总成功25.00% vs 人类97.26%，交互动作有效率9.56% vs 96.81%，固定Gemini-Flash增加历史图像除spatial QA外下降。版式宜做“人 vs 模型”同接口对照与“历史越多越差”折线；须注明327/328测试数差异、无重复置信区间，失败分类为描述性。
- **2307.01928**（不确定性校准求助）：问题：歧义指令下如何校准LLM规划器何时求助，在保证成功覆盖率的同时减少人类帮助；结果：移动操作目标覆盖0.85、规划0.87、任务0.76，帮助率0.67；Simple Set同规划0.87需帮助0.81。版式宜做“预测集大小→是否求助”示意与帮助率对比；须注明保证只在校准/测试同分布与人类忠实回答假设下成立，不是任务必然成功或物理安全保证。
- **2506.06677**（分层归因诊断）：问题：长程任务里观察、记忆、规划失败与低层执行失误如何区分；结果：600 rollouts中GPT-4o 16.04%、blind 15.10%、GT-plan 25.16%，SFT Qwen观察判断66.83%但成功仅9.33%。版式宜做“看见/不看见/给真计划”三柱对比与“观察分高≠成功”散点；须注明GT-plan仍低说明固定执行器不等于完全隔离推理，anchor切换不测自主停止。
- **2512.02002**（反馈来源替代）：问题：有明确运动API与执行规则时，静态文本模拟能否替代动态模拟反馈保留纠码效果；结果：PX4/o4-mini两者均93.3%，代码评估91.7% vs 92.1%，去规则/示例退化；真机UAV/地面车各8任务约87.5–91.7%。版式宜做“动态仿真环 vs 文本模拟环”并列流程与持平条；须注明限规则化轨迹任务与受控API，配置/时延节省未充分量化，不等价物理世界模型或安全认证。
- **2609.35318**（人视频→示范数据生成）：问题：人手轨迹直接重定向难覆盖接触拓扑，如何把单次人类视频转成可学的灵巧操作示范；结果：11任务×10次真实闭环平均63.6% vs 18.2%，抽屉80%、绳50%。版式宜做“人视频→重建→接触优化→扩增→学生策略”四阶段流水；须区分Table III单次重放覆盖与Table IV重复成功率，增强与轨迹生成贡献尚未隔离。

## 原文核对状态

全部 9 篇：**未核对**。制作前由 Opus 5.5 读完整原文及必要附录；发现 L2 判断错误则暂停该篇、写 correction 退回 Sol 单篇修订。Reel 成品路径：暂无。

## 同题去重

| paper_id | 标题 | 类别 | 保留篇 | 理由 |
|---|---|---|---|---|
| 2407.20242 | BadRobot: Jailbreaking Embodied LLM Agents in the Physical W | 同题去重（s001已选） | 2610.27350 | s001已判同题：同问“文本对齐能否延伸到动作安全”；本篇跨平台权限/终点不一，2610.27350以同模型同首帧对照更直接隔离问题。 |
| 2410.13691 | Jailbreaking LLM-Controlled Robots | 同题去重（s001已选） | 2610.27350 | s001已判同题：同问“文本对齐能否延伸到动作安全”；本篇跨平台权限/终点不一，2610.27350以同模型同首帧对照更直接隔离问题。 |
| 2402.04210 | Task Success is not Enough: Investigating the Use of Video-L | 同题去重（s001已选） | 2411.04549 | s001已判同题：同问“VLM批评/进度信号能否当验证器”；本篇主证据依赖人工完美grounding上界，GVL有同模型去捷径对照更直接。 |
| 2610.22496 | Scaling Online Exploration for Robot Agents | 同题去重（s001已选） | 2610.25114 | s001已判同题：同卡同题（在线试错编译为可复用程序）；本篇缺同信息同预算的继承/反馈消融且含人工介入，归因不如2610.25114直接。 |
| 2305.16291 | Voyager: An Open-Ended Embodied Agent with Large Language Mo | 同题去重（s001已选） | 2610.25114 | s001已判同题：技能库自主累积/复用同题组；2610.25114明确拆分收益来源并测冻结复用，问题更清楚。 |
| 2405.15019 | Agentic Skill Discovery | 同题去重（s001已选） | 2610.25114 | s001已判同题：技能库自主累积/复用同题组；2610.25114明确拆分收益来源并测冻结复用，问题更清楚。 |
| 2509.24160 | Memory Transfer Planning: LLM-driven Context-Aware Code Adap | 同题去重（s001已选） | 2610.25114 | s001已判同题：技能库自主累积/复用同题组；2610.25114明确拆分收益来源并测冻结复用，问题更清楚。 |
| 2506.15635 | FindingDory: A Benchmark to Evaluate Memory in Embodied Agen | 同题去重（s001已选） | 2510.20328 | s001已判同题：同卡“行动所需历史记忆”同题组；FindingDory缺无/乱序历史对照，其余为特定表示方法，MemER固定低层真机对照最直接。 |
| 2409.13682 | ReMEmbR: Building and Reasoning Over Long-Horizon Spatio-Tem | 同题去重（s001已选） | 2510.20328 | s001已判同题：同卡“行动所需历史记忆”同题组；FindingDory缺无/乱序历史对照，其余为特定表示方法，MemER固定低层真机对照最直接。 |
| 2411.17735 | 3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoni | 同题去重（s001已选） | 2510.20328 | s001已判同题：同卡“行动所需历史记忆”同题组；FindingDory缺无/乱序历史对照，其余为特定表示方法，MemER固定低层真机对照最直接。 |
| 2306.17840 | Statler: State-Maintaining Language Models for Embodied Reas | 同题去重（s001已选） | 2510.20328 | s001已判同题：同卡“行动所需历史记忆”同题组；FindingDory缺无/乱序历史对照，其余为特定表示方法，MemER固定低层真机对照最直接。 |
| 2504.13059 | RoboTwin: Dual-Arm Robot Benchmark with Generative Digital T | 同题去重（s001已选） | 2610.15572 | s001已判同题：privileged_teacher_supervision同卡；均为教师数据生成规模/鲁棒性，未像2610.15572那样等量数据只换教师策略。2504.13059另有later_work 2506.18088（同系列扩展），二者均未入选。 |
| 2506.18088 | RoboTwin 2.0: A Scalable Data Generator and Benchmark with S | 同题去重（s001已选） | 2610.15572 | s001已判同题：privileged_teacher_supervision同卡；均为教师数据生成规模/鲁棒性，未像2610.15572那样等量数据只换教师策略。2504.13059另有later_work 2506.18088（同系列扩展），二者均未入选。 |
| 2406.18915 | Manipulate-Anything: Automating Real-World Robots using Visi | 同题去重（s001已选） | 2610.15572 | s001已判同题：privileged_teacher_supervision同卡；均为教师数据生成规模/鲁棒性，未像2610.15572那样等量数据只换教师策略。2504.13059另有later_work 2506.18088（同系列扩展），二者均未入选。 |
| 2403.12482 | Embodied LLM Agents Learn to Cooperate in Organized Teams | 同题去重（s001已选） | 2411.00081 | s001已判同题：同问“多智能体协作/通信是否真带来效率”；2403.12482 GPT-4结构收益p=.20，Robotouille/ELHPlan为单一设置，PARTNR受控维度最全、证据最直接。 |
| 2502.05227 | Robotouille: An Asynchronous Planning Benchmark for LLM Agen | 同题去重（s001已选） | 2411.00081 | s001已判同题：同问“多智能体协作/通信是否真带来效率”；2403.12482 GPT-4结构收益p=.20，Robotouille/ELHPlan为单一设置，PARTNR受控维度最全、证据最直接。 |
| 2509.24230 | ELHPlan: Efficient Long-Horizon Task Planning for Multi-Agen | 同题去重（s001已选） | 2411.00081 | s001已判同题：同问“多智能体协作/通信是否真带来效率”；2403.12482 GPT-4结构收益p=.20，Robotouille/ELHPlan为单一设置，PARTNR受控维度最全、证据最直接。 |
| 2509.22653 | See, Point, Fly: A Learning-Free VLM Framework for Universal | 同题去重（s001已选） | 2602.15875 | s001已判同题：UAV零样本导航/航空VLN同题组；Fly0固定其余栈只换目标接口，隔离最直接。2509.22653与其问题最近（文本3D动作→视觉grounding）。 |
| 2505.05622 | CityNavAgent: Aerial Vision-and-Language Navigation with Hie | 同题去重（s001已选） | 2602.15875 | s001已判同题：UAV零样本导航/航空VLN同题组；Fly0固定其余栈只换目标接口，隔离最直接。2509.22653与其问题最近（文本3D动作→视觉grounding）。 |
| 2505.08765 | Towards Autonomous UAV Visual Object Search in City Space: B | 同题去重（s001已选） | 2602.15875 | s001已判同题：UAV零样本导航/航空VLN同题组；Fly0固定其余栈只换目标接口，隔离最直接。2509.22653与其问题最近（文本3D动作→视觉grounding）。 |
| 2508.00288 | UAV-ON: A Benchmark for Open-World Object Goal Navigation wi | 同题去重（s001已选） | 2602.15875 | s001已判同题：UAV零样本导航/航空VLN同题组；Fly0固定其余栈只换目标接口，隔离最直接。2509.22653与其问题最近（文本3D动作→视觉grounding）。 |
| 2410.07087 | Towards Realistic UAV Vision-Language Navigation: Platform,  | 同题去重（s001已选） | 2602.15875 | s001已判同题：UAV零样本导航/航空VLN同题组；Fly0固定其余栈只换目标接口，隔离最直接。2509.22653与其问题最近（文本3D动作→视觉grounding）。 |
| 2602.12281 | Scaling Verification Can Be More Effective than Scaling Poli | 同题去重（s001已选） | 2506.17811 | 同问“可部署验证器能否从多个候选中选出更好动作”；与s001 RoboMonkey同卡同题，且PolaRiS绝对成功率仍低（3.8→13.1%）。 |
| 2603.17312 | Recurrent Reasoning with Vision-Language Models for Estimati | 同题去重（s001已选） | 2411.04549 | 同问“VLM进度估计能否作可用信号”；本篇为流式效率版本，进度真值为等权插值，GVL的去捷径对照更直接。 |
| 2610.26848 | Where is Physical RSI capability from? An Observational Scal | 同题去重（s001已选） | 2610.25114 | 同问“反复尝试增益是否来自保留经验/冻结产物能否迁移”；与s001自我改进归因篇问题重合。 |
| 2607.29600 | HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Sho | 同题去重（s001已选） | 2510.20328 | 同问“要记什么而非记更多历史”（导航版）；s001 MemER已占该问题，本篇每基准100集子集。 |
| 2410.00371 | AHA: A Vision-Language-Model for Detecting and Reasoning Ove | 同题去重 | 2306.15724 | 同问“失败判断如何从二元标签变成可用于纠正的原因反馈”；REFLECT以去解释消融直接量到纠正率差，AHA主要是检测/推理准确率。 |
| 2409.19471 | SELP: Generating Safe and Efficient Task Plans for Robot Age | 同题去重 | 2309.09919 | 同问“自然语言时序要求→LTL约束计划”；Safety Chip给出未验证/专家验证门控分档与真机对照，SELP限有限任务约束满足率。 |
| 2305.15695 | Asking Before Acting: Gather Information in Embodied Decisio | 同题去重 | 2307.01928 | 同属“何时/如何向人求助或询问”题组；KnowNo有覆盖率保证与帮助率对照，证据最完整（s001已记为该槽首选）。 |
| 2310.07968 | Think, Act, and Ask: Open-World Interactive Personalized Rob | 同题去重 | 2307.01928 | 同属“何时/如何向人求助或询问”题组；KnowNo有覆盖率保证与帮助率对照，证据最完整（s001已记为该槽首选）。 |
| 2412.01250 | Collaborative Instance Object Navigation: Leveraging Uncerta | 同题去重 | 2307.01928 | 同属“何时/如何向人求助或询问”题组；KnowNo有覆盖率保证与帮助率对照，证据最完整（s001已记为该槽首选）。 |
| 2307.05973 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation  | 同题去重 | 2409.01652 | 同问“语言→空间约束/价值图→优化器合成运动”；ReKep在同任务直接对照VoxPoser（10.0 vs 44.3）并给出人工约束上界，差距更清楚。 |
| 2610.00854 | Are Frontier VLM Agents Ready to Be Robot Generalists? An Em | 同题去重 | 2501.11858 | 同问“局部/静态能力能否转成完整具身目标达成”；EmbodiedEval有同接口人类上限与固定模型历史干预，对照更直接。 |

## 多样性截断

### 下期备选（next_candidate）

- **2402.14623** RoboScript: Code Generation for Free-Form Manipulation Tasks across Re （P2→P3）：代码正确≠执行成功的分层计分；与RoboCerebra同为“高层指标≠闭环成功”诊断，本期截断。
- **2506.23127** Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Le （P2→P3）：仅完成奖励的多轮RL无需SFT；RL类型s001已有教师引导RL，下期原生RL槽备选。
- **2606.10267** What Matters in Orchestrating Robot Policies: A Systematic Study of Hi：分层vs平面策略的受控设计研究（Best 83.8% vs Flat 43.3%）；与RoboCerebra同属分层归因，本期截断。
- **2607.06256** Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Lang：技能交接诊断（同checkpoint干净快照vs组合终态，串联进度19.5%）问题极清楚；本期分层槽给了RoboCerebra，下期交接槽首选，与2607.18060同题需二选一。
- **2607.18060** RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Polici （P2→P3）：异构策略交接（MemoryBridge）与2607.06256同题；下期交接槽与其二选一。
- **2607.19190** Agentic Real2Sim: Physics-based World Modeling with Vision-Language Ag （P2→P3）：Agentic Real2Sim（录像→MuJoCo孪生，sim-real r=.92）；与2609.13082同属评测基础设施，下期备选。
- **2607.22999** WCM: World-Cognition Model for Generalizable Human-Robot Interaction （P2→P3）：在线人机交互/语言教学（去interaction-sensing 69→0%）；本期人机交互位给KnowNo，下期备选。
- **2608.05715** Hijacking Robots with a Piece of Paper: A Systematic Study of Physical：纸面文字物理提示注入（ASR至29.4%、中性纸条0%）；与s001安全诊断类型同质，下期安全槽备选。
- **2609.10522** Show-Harness: Just a VLM Agent Can Play Robots （P2→P3）：固定其余部件只换动作名/约定（任意符号1/20），对照很干净；但与s001 Fly0同属动作接口类型，避免同质，下期接口槽备选（与2609.34412比较）。
- **2609.13082** Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Bench （P2→P3）：评测产物有效性（仅末端检查有效率10.4% vs 过程QC 93.7%）是新类型；本期评测槽给EmbodiedEval，下期评测基础设施槽首选。
- **2610.10498** EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided （P2→P3）：假设驱动的交互预算分配（同50 episode 27.1% vs 72.9%）；与s001自我改进归因同族，下期备选。

### 其余按主卡汇总

| 主卡 | 篇数 | 其中上移 | 理由 | paper_id |
|---|---|---|---|---|
| observe_act_interface | 56 | 6 | 观察—动作接口族；s001已有Fly0接口篇，本期仅以ReKep（约束生成）间接覆盖，其余截断。 | 2201.07207 2207.04429 2209.07753 2209.11302* 2212.04088 2303.03480 2306.08647 2309.04077 2309.09969* 2309.10103 2309.16650* 2404.06645 2409.10906 2503.10069 2506.04217* 2506.17462* 2602.04157 2602.04315 2603.18520 2603.26997 2605.01371 2605.18746 2605.26637 2606.10577 2607.11119 2607.13653 2607.22014 2607.26148 2608.03924 2608.11246 2608.30396 2609.01404 2609.12285 2609.12541 2609.19138 2609.19554 2609.20116 2609.22966 2609.23133* 2609.23841 2609.24170 2609.28530 2609.29389 2609.29861 2609.29964 2609.31112 2609.33007 2609.34412 2609.38078 2610.10388 2610.10409 2610.10787 2610.12126 2610.23479 2610.27613 2610.28259 |
| external_verification_control | 43 | 1 | 验证/门控/恢复族；本期已入选失败解释（REFLECT）、形式约束门控与校准求助三种不同问题，其余按类型多样性截断。 | 2207.05608 2307.00329 2412.04455 2412.13178 2503.07885 2503.08663 2503.18666 2505.23450* 2506.09937 2506.16402 2509.16072 2510.21302 2601.15486 2602.12405 2602.19983 2603.10682 2603.13528 2604.07395 2604.22591 2607.00218 2607.13049 2607.23532 2608.14822 2608.17386 2608.22657 2609.03611 2609.05178 2609.06508 2609.15195 2609.20791 2609.20822 2609.26313 2609.32801 2609.34356 2609.34484 2609.40306 2610.13862 2610.19677 2610.21453 2610.27003 2610.27917 2610.28381 2610.28476 |
| harness_memory_skill_reuse | 38 | 9 | 记忆/技能复用族；s001已选MemER与冻结技能篇，本期不再开记忆槽。 | 2310.10021 2311.10678 2404.19065 2406.14596 2406.18746* 2504.09587* 2505.13948* 2508.01415* 2509.18597* 2511.19033 2602.20323 2603.02623* 2603.19137* 2604.02318 2605.07594 2605.10332 2605.10921 2606.18847 2606.19419 2606.25206 2607.14047 2608.04933 2608.09410 2608.17209 2608.29537 2609.08292 2609.08444 2609.15976 2609.24124 2609.27526* 2609.28236 2609.28798 2609.34261 2609.36595 2610.01569 2610.12424* 2610.18867 2610.29329 |
| planner_composes_code_and_policies | 29 | 4 | 规划器组合技能/VLA族；本期分层问题由RoboCerebra代表。 | 2204.01691 2302.01560 2410.06237 2410.06473 2504.09532* 2507.01485* 2510.03342* 2605.13119 2605.18727 2605.30326 2606.07723 2607.08448 2607.17213 2608.09516 2608.16889 2609.02653* 2609.11308 2609.18869 2609.23578 2609.35432 2609.35690 2609.39018 2610.01939 2610.09228 2610.18352 2610.18874 2610.20474 2610.27618 2610.30136 |
| multi_robot_llm_coordination | 18 | 3 | 多机器人协调族；s001已有PARTNR，本期未留多智能体槽。 | 2307.02485 2307.04738 2309.10062* 2401.12963 2404.06413 2407.10031 2409.15146 2410.22662 2503.16408* 2503.22122 2605.12920 2607.06990 2608.28266 2609.08402 2609.18520 2609.23997 2609.27720* 2609.28247 |
| harness_effect_evaluation | 18 | 1 | 评测/诊断族；本期已入选EmbodiedEval与RoboCerebra两篇诊断，按诊断集中规则截断。 | 2311.11183 2401.12202 2402.08178* 2410.07166 2412.18194 2502.09560 2603.22435 2604.05226 2606.14674 2607.27180 2609.33807 2609.39507 2610.07594 2610.19600 2610.22471 2610.30043 2610.30051 2610.30108 |
| code_policy_trial_revision | 17 | 3 | 代码策略试错修订族；本期以2512.02002（反馈来源替代）代表，s001另有自我改进归因篇。 | 2501.04268* 2601.20334 2606.16458 2607.00272 2607.05369 2607.23784 2608.16978 2609.19906 2609.27308 2609.29166 2609.29394 2609.30233 2609.30249* 2609.37359 2610.10479* 2610.12369 2610.12549 |
| harness_self_optimization | 12 | 2 | harness自优化/自改进族；与s001自我改进归因同族，本期截断。 | 2605.09423 2606.08610* 2608.07555 2608.11350* 2608.16590 2609.29204 2609.31760 2609.33378 2609.39304 2610.02204 2610.08995 2610.14977 |
| llm_symbolic_solver_planning | 11 | 3 | LLM+符号/优化求解族；本期由ReKep代表。 | 2304.11477 2502.19135 2503.01700 2507.00833* 2510.25548* 2601.11063 2602.01662* 2604.26988 2608.28300 2609.19315 2610.25930 |
| learner_state_teacher_correction | 7 | 0 | 学习者状态纠正/自适应族；本期未留该槽。 | 2310.17555 2609.32416 2609.35575 2609.38178 2609.38905 2610.01178 2610.21450 |
| trained_vlm_vla_hierarchy | 7 | 1 | 训练式分层VLA族；本期分层问题由RoboCerebra代表。 | 2412.04453 2502.19417 2503.12533 2504.14588* 2602.13193 2606.12299 2607.05377 |
| offline_harness_distillation | 5 | 3 | 离线harness蒸馏族；本期蒸馏位由VLA-OPD（在线目标）占用。 | 2404.04619* 2510.12693* 2606.18363 2606.27871 2607.26809* |
| teacher_seeded_sparse_rl | 5 | 0 | 教师引导稀疏RL族；s001已有LLM教师RL篇。 | 2404.14285 2606.09630 2609.21650 2609.32069 2609.32698 |
| sample_verify_select | 4 | 1 | 采样—验证—选择族；s001已有RoboMonkey。 | 2502.16707* 2602.21198 2607.27599 2609.05927 |
| harness_native_rl | 2 | 0 | harness原生RL族；s001 RL槽已占，本期截断。 | 2505.22050 2610.28589 |
| privileged_teacher_supervision | 2 | 0 | 特权教师/数据生成族；本期由DexAgent代表，s001另有教师标注策略篇。 | 2609.24563 2610.17593 |

`*` = L2 第二波 P2→P3 上移篇。

## 多样性说明

9篇对应9种机制类型，均不与s001九类重复：失败解释→纠正、形式约束门控、约束生成+优化求解、在线蒸馏目标、单体MLLM闭环评测、不确定性校准求助、分层归因诊断、反馈来源替代、人视频→示范数据生成。问题族F0–F5全覆盖（F0×5、F2×5、F4×3、F1/F3/F5各1）；q3为capability 6、judgment 3（s001为judgment 5，合计两期12:6→各9）。诊断/评测类2篇（2501.11858、2506.06677）。external_verification_control主卡3篇，但分属失败解释、时序约束门控、求助校准三个不同问题；其余主卡各≤1。8/9篇为L2第二波P2→P3上移篇。

## 编辑理由

- 候选池327篇全为P3 confirmed；不按数值排序，先按主卡+problem_statement聚同题组，组内保留问题最清楚、对照最直接的一篇。
- 与s001的去重：s001已记“同题去重”的22篇仍归入其入选篇；新增4篇（2602.12281、2603.17312、2610.26848、2607.29600）与s001入选篇同问，记为同题去重（s001已选）。
- 按用户要求优先取L2第二波P2→P3上移篇（池内56篇）：入选8篇来自上移篇；唯一非上移入选2307.01928，是s001明确留给下期的求助槽首选，按承诺补位。
- 类型避让：s001已覆盖安全诊断/验证信号/自我改进归因/记忆/特权监督/采样验证/教师RL/多智能体评测/动作接口；本期在这些类型上的强候选（2608.05715、2602.12281、2610.10498、2607.29600、2609.10522等）记多样性截断或同题去重，并在next_candidate标注下期备选。
- Safety Chip虽同属安全议题，但机制为形式化动作剪枝而非诊断，与s001 2610.27350不同类型；EmbodiedEval为单体闭环评测，与s001 PARTNR多智能体评测问题不同，且s001已列其为评测槽备选。
- ReKep与VoxPoser同题二选一：ReKep同任务直接对照VoxPoser并给人工约束上界，差距可量化；VoxPoser记同题去重。
- 分层诊断槽选RoboCerebra（含blind与GT-plan对照，F1归因）而非2607.06256技能交接诊断：后者问题同样清楚，但本期诊断类已2篇，留作下期交接槽首选。
- later_work：9篇入选均无later_work记录。
- 入选篇原文核对尚未进行；按SELECTION.md最终制作条件，制作前须读完整原文及必要附录，若发现L2错误则暂停并写correction退回Sol单篇修订。

## 待补与退回项

- 待补清单沿用 selection-001 及 progress.md（pending_experiment / needs_material），本期未新增；补齐后由 Sol 单篇 L2，不在此直接入选。
- 退回项：无（原文核对尚未开始）。
