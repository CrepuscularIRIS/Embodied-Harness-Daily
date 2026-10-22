# 选读与制作名单 · run `embodied-v3-20261021-01`

`profile: embodied-v3` · `scoring: sol-batch-v3` · `quality_floor: null` · `selection_cutoff: 88.75` · `reel: 2026-10-22 第 1 期`

> 本文件记录本期的选择过程：从 500 篇评分记录到 9 张海报。分数是选读初筛优先级，不是审稿分。编辑挑选只决定读哪几篇、做哪几篇，不修改任何分数或记录。

## 1. 运行概览

本期采用单模型打分，再由编辑挑选。规则参数如下。

| 项 | 值 |
|---|---|
| run | `embodied-v3-20261021-01`（[run.md](../run.md) · [progress.md](../progress.md)） |
| 规则版本 / profile | `sol-batch-v3` / `embodied-v3` |
| 权重 | G=15 M=20 X=20 E=45，`screen_score=(15G+20M+20X+45E)/4`，满分 100 |
| quality_floor | `null`（用户未指定） |
| 候选规则 | `screen_score` 降序，同分按 E、M 排；`claim_support=contradicted/unresolved` 不入候选；取前 15 进入 Opus 原文核对 |
| 打分 | 6.1 Sol 单席，Subagent 滚动补位；b006 之后并发数从 4 升到 6 |
| 挑选、核对、海报 | Opus 5.5：编辑挑选、逐篇原文核对、制作 Reel（不超过 9 篇） |
| 评分记录 | [index.jsonl](index.jsonl)，500 篇逐篇 JSONL |

## 2. 漏斗：500 → 9

下表每一行都写明数量和去向，没有哪一篇是无声消失的。

| 步 | 输入 | 输出 | 去向 |
|---|---|---|---|
| ① 全量评分 | 500 | 487 篇 `scored` | 11 篇 `needs_material`（总分 null）→ §7；2 篇 `out_of_scope` |
| ② 候选资格 | 487 | 剔除 4 篇 `unresolved` | → §6 问题清单，先纠正或补证 |
| ③ 最高分组 | 候选 | 88.75 并列 53 篇，全部 G4/M4/X4/E3 | 规则排序在这一组失效 → §3 |
| ④ 规则前 15 | 53 | 15 篇，全部是 2204–2607 的较早编号 | 只留档；其中 6 篇进入核对名单 → §3 表 |
| ⑤ 编辑挑选 | 53 | 13 个聚类，核对名单 15 篇 | supported_in_material 9 篇，scoped 6 篇 → §4 |
| ⑥ 制作名单 | 15 | 9 篇 supported_in_material | scoped 6 篇只留档；替补 4 篇 → §8 |
| ⑦ 核对与制作 | 9 | 9/9 核对通过，9/9 画报 ready | 成品见 §5；替补未动用 |

## 3. 88.75 并列 53 篇的处理

在这个并列组里，规则排序选不出有意义的顺序，所以改用规则文件自带的编辑挑选条款。

- **规则为何失效**：53 篇的 E 和 M 完全相同，"同分按 E、M"区分不了，只能按 paper_id 升序打破并列。结果前 15 篇都是 2204–2607 的较早编号，其中 5 篇是 2022–2024 年的旧作；2608–2610 的 38 篇一篇都没进。这个顺序只反映编号，不反映质量或题材。
- **依据条款**（`radar-scoring-v3-draft/SELECTION.md` §候选池）：
  > "主题过度重复时，可优先保留证据更充分或贡献不同的论文，记录编辑选择理由，不修改论文分数"；"benchmark、负结果和审计不因类型被排除"
- **性质**：这是编辑选择，不是重评。输入是 [reel/tie8875.md](../../../../../reel/tie8875.md)，只用其中 Sol 记录的摘要（move / gap / patterns / caveat / claim_support / evidence_level）。没有读全文，没有派 Subagent，Sol 的分数和记录都没改。

规则前 15 篇如下（全部 88.75，G/M/X/E 均为 4/4/4/3）。"去向"一列给出每篇在编辑挑选后的结果。

| # | paper_id | 聚类 | claim_type | claim_support | 一句话 move | 去向 |
|---|---|---|---|---|---|---|
| 1 | 2204.01691 | C1 | system_method | supported_in_material | 逐步将固定技能文本的语言模型似然与当前状态的技能可行性分数相乘，执行最高分技能后继续选择。 | **制作** |
| 2 | 2207.04429 | C4 | system_method | scoped | GPT-3抽取地标、CLIP在预采集拓扑图中接地，联合可达性搜索后由冻结ViNG控制器执行。 | 落选 |
| 3 | 2305.16291 | C6 | system_method | scoped | 用自动课程提出目标，以执行反馈迭代代码，并将成功技能存库供后续检索组合。 | 落选 |
| 4 | 2307.01928 | C1 | system_method | scoped | 将下一步规划转为多选题，用序列级共形阈值构造动作集合，非单例时请求人类澄清。 | 落选 |
| 5 | 2401.12963 | C10 | system_method | scoped | 用场景描述、宪法约束任务生成和可供性过滤，按人力预算分配遥操作与自主采集策略。 | 替补 3 |
| 6 | 2410.07166 | C11 | evaluation_resource | supported_in_material | 以对象中心状态和有限轨迹LTL统一四类决策模块接口，用符号执行、规划器与细粒度错误分类分离评测。 | **制作** |
| 7 | 2411.00081 | C11 | evaluation_resource | scoped | 以仿真过滤和人工校验生成带时空及能力约束的协作任务与轨迹级评价，并分离规划、感知和技能条件。 | 落选 |
| 8 | 2411.04549 | C8 | component_training | scoped | 将视频帧打乱并锚定首帧，让冻结VLM自回归估计进度，用于成功过滤和优势加权训练。 | 核对名单（留档） |
| 9 | 2506.09937 | C8 | component_training | scoped | 以成功和失败轨迹监督浅层探针，将冻结VLA隐特征转成累积失败分数，并用共形带选报警阈值。 | 落选 |
| 10 | 2510.20328 | C3 | component_training | supported_in_material | 训练高层VLM同时输出子任务和候选关键帧，时间聚类保留记忆，再异步指挥低层VLA。 | **制作** |
| 11 | 2602.15875 | C5 | system_method | scoped | 将VLM区域与关系输出转成经不确定性门控的持久三维锚点，由机载几何规划器持续跟踪。 | 核对名单（留档） |
| 12 | 2603.22435 | C12 | evaluation_resource | scoped | 建立分层API与反馈的代码机器人评测，再以视觉差分、复用库和候选集成改进agent，并用仿真奖励训练小模型。 | 落选 |
| 13 | 2604.25788 | C11 | evaluation_resource | supported_in_material | 构建分离感知语言因素的程序化物理推理环境、技能接口和跨规划学习范式评测。 | 替补 1 |
| 14 | 2606.10577 | C4 | system_method | supported_in_material | 将像素目标移动、按需深度查询和历史图像召回暴露为工具，配合六步文本历史、BEV和几何拒绝反馈。 | **制作** |
| 15 | 2607.00272 | C6 | system_method | scoped | 编码代理读取逐原语多模态轨迹修复程序，将验证过的修复压成技能，再用演化搜索选择候选程序。 | 落选 |

## 4. 13 个主题聚类

53 篇按 move 和 gap 分成 13 组。记录里的 title 字段只有 arXiv 链接，所以只能按这两项归类。每组至少有 1 篇进入核对名单；C3、C6 各 2 篇，且每组的第二篇与第一篇贡献类型或机制不同。完整 ID、5 篇边界不确定的归类以及每篇落选理由，见 [reel/selection-opus.md](../../../../../reel/selection-opus.md)。

| # | 聚类（代表方向） | 篇数 | 核对名单 | 本期制作 |
|---|---|---:|---|---|
| C1 | LLM 规划、技能打分与不确定性 | 2 | 2204.01691 | 2204.01691 |
| C2 | 执行约束与运行时验证（契约/编译/安全过滤） | 5 | 2609.34412 | 2609.34412 |
| C3 | 分层 VLM–VLA 与冻结策略/原语组合接口 | 5 | 2610.19600、2510.20328 | 两篇都制作 |
| C4 | 语言导航与工具化空间接口 | 4 | 2606.10577 | 2606.10577 |
| C5 | 3D 锚点与持久对象/场景记忆 | 3 | 2602.15875 | — |
| C6 | 代码策略试错修复与技能/经验库 | 5 | 2609.19906、2610.12549 | 2609.19906 |
| C7 | Harness 自优化（技能/API/上下文共演化） | 3 | 2608.11350 | 2608.11350 |
| C8 | 进度/奖励/失败信号 | 3 | 2411.04549 | — |
| C9 | 教师监督、纠正数据与蒸馏/RL 训练 | 6 | 2609.38178 | — |
| C10 | 人在回路的数据采集与调试 | 3 | 2607.13049 | — |
| C11 | 规划层/符号与特权状态诊断基准 | 3 | 2410.07166 | 2410.07166 |
| C12 | 通用模型闭环具身 agent 基准 | 7 | 2609.33807 | 2609.33807 |
| C13 | 专题失效模式基准（交接/安全/记忆/探索） | 4 | 2607.06256 | — |

## 5. 最终入选 9 篇

核对名单 15 篇中，supported_in_material 恰好是 9 篇，于是直接作为制作名单（不超过 9 篇的上限）。理由是 supported 记录的初筛证据范围最宽，符合 SELECTION 中"证据更充分者优先"的原则。

- 9 篇覆盖 8/13 个聚类（C3 占两席）。
- 贡献类型：system_method 6、component_training 1、evaluation_resource 2 [^1]。

| # | paper_id | 标题 | 聚类 | 分数 | claim_type | claim_support | 机制一句话 | 成品 |
|---|---|---|---|---:|---|---|---|---|
| 1 | [2204.01691](https://arxiv.org/abs/2204.01691) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | C1 | 88.75 | system_method | supported_in_material | 语言似然×技能可行性打分选择 | [poster](../../../../../reel/2204.01691/poster.png) · [verify](../../../../../reel/2204.01691/verify.md) |
| 2 | [2609.34412](https://arxiv.org/abs/2609.34412) | From Language to Task Maps: Compiling Semantic Relations While Preserving Task-Relevant Freedom | C2 | 88.75 | system_method | supported_in_material | LLM 写实体/关系，编译器生成任务映射 | [poster](../../../../../reel/2609.34412/poster.png) · [verify](../../../../../reel/2609.34412/verify.md) |
| 3 | [2610.19600](https://arxiv.org/abs/2610.19600) | Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System | C3 | 88.75 | system_method | supported_in_material | 最早未恢复错误诊断 → 针对性干预 | [poster](../../../../../reel/2610.19600/poster.png) · [verify](../../../../../reel/2610.19600/verify.md) |
| 4 | [2510.20328](https://arxiv.org/abs/2510.20328) | MemER: Scaling Up Memory for Robot Control via Experience Retrieval | C3 | 88.75 | component_training | supported_in_material | 高层 VLM 子任务＋关键帧记忆 | [poster](../../../../../reel/2510.20328/poster.png) · [verify](../../../../../reel/2510.20328/verify.md) |
| 5 | [2606.10577](https://arxiv.org/abs/2606.10577) | AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness | C4 | 88.75 | system_method | supported_in_material | 像素目标/深度/历史召回工具化导航 | [poster](../../../../../reel/2606.10577/poster.png) · [verify](../../../../../reel/2606.10577/verify.md) |
| 6 | [2609.19906](https://arxiv.org/abs/2609.19906) | Learning and Transferring Closed-Loop Robot Software | C6 | 88.75 | system_method | supported_in_material | 源任务性能 vs 新任务参考价值 | [poster](../../../../../reel/2609.19906/poster.png) · [verify](../../../../../reel/2609.19906/verify.md) |
| 7 | [2608.11350](https://arxiv.org/abs/2608.11350) | Self-Evolving Embodied Agents via Skill-Harness Evolution | C7 | 88.75 | system_method | supported_in_material | 冻结策略，只演化技能与上下文代码 | [poster](../../../../../reel/2608.11350/poster.png) · [verify](../../../../../reel/2608.11350/verify.md) |
| 8 | [2410.07166](https://arxiv.org/abs/2410.07166) | Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making | C11 | 88.75 | evaluation_resource | supported_in_material | 对象状态＋LTL 统一接口基准 | [poster](../../../../../reel/2410.07166/poster.png) · [verify](../../../../../reel/2410.07166/verify.md) |
| 9 | [2609.33807](https://arxiv.org/abs/2609.33807) | CodeActionBench: Evaluating Agentic Code-as-Policy for Embodied Manipulation | C12 | 88.75 | evaluation_resource | supported_in_material | 隐藏物理验证 vs agent 完成声明 | [poster](../../../../../reel/2609.33807/poster.png) · [verify](../../../../../reel/2609.33807/verify.md) |

> 结果：9/9 核对通过，9/9 画报 ready。`selection_cutoff=88.75` 是本期入选的最低分，不是永久标准。核对名单中 scoped 的 6 篇（2602.15875、2610.12549、2411.04549、2609.38178、2607.13049、2607.06256）及它们所在的 5 个未覆盖聚类 [^2]，本期不制作，只在核对名单中留档。海报总索引见 [reel/README.md](../../../../../reel/README.md)。

## 6. 问题清单：claim_support 异常，先纠正或补证

这 4 篇是 `unresolved`，按规则不进候选，也不参与排序。

| paper_id | screen_score [^3] | claim_support |
|---|---:|---|
| 2608.05738 | 58.75 | unresolved |
| 2403.10850 | 37.5 | unresolved |
| 2607.19850 | 37.5 | unresolved |
| 2606.14674 | 51.25 | unresolved |

## 7. 待补材料：needs_material 11 篇

这 11 篇总分为 null，不冒充低分，也不与有分论文混排。补齐材料后重新评分。

| paper_id | 缺什么 |
|---|---|
| 2505.23266 | 完整攻击方法与主实验表，含受害导航系统、攻击权限及闭环任务分母 |
| 2407.00632 | 导航成功率、试验分母及通信/领导组织对照实验与条件 |
| 2505.18229 | 正文方法、六类技能的评分协议及主实验表与虚实试验次数 |
| 2610.26663 | 四维评测与标注协议、主结果表及任务/轨迹分母和闭环使用条件 |
| 2610.19913 | 补齐 Tables 2–6 及实际闭环试验分母、独立校准/测试划分、模型与任务预算；澄清五实机任务与四 composition 差异。 |
| 2509.01106 · 2511.00917 · 2609.36171 · 2610.22736 · 2307.06135 · 2409.14908 | 完整全文或至少摘要与方法/主实验说明（6 篇无任何材料，记于 `batches/b999-nomaterial.jsonl`） |

## 8. 替补名单

如果核对中有一篇被暂停或退回，就按以下顺序补入（与 selection-opus.md 一致）。本期 9/9 通过，**替补未动用**。

| 顺序 | paper_id | 聚类 | 说明（摘自 selection-opus.md） |
|---|---|---|---|
| 1 | 2604.25788 | C11 | supported，但与 2410.07166 同为特权状态诊断基准，本组只留一篇；若要提高 evaluation_resource 比例，优先换入 |
| 2 | 2610.10388 | C13 | 探索专题；主瓶颈归因限于所给接口与规则 |
| 3 | 2401.12963 | C10 | AutoRT；77k 是尝试次数而非成功演示，题材新意低于 2607.13049 |
| 4 | 2609.21650 | C9 | 特权教师训练学生一类；仍依赖人工数据或逐任务设定 |

## 9. 核对收窄性结论

原文核对发现 3 处主张需要收窄。处理原则是收窄主张，不改分 [^4]：海报只呈现经过核对的范围，Sol 的分数和记录保持原样。

| paper_id | 收窄结论 | 详情 |
|---|---|---|
| 2204.01691（SayCan） | 两处作者表述无依据，未上画报 | [verify.md](../../../../../reel/2204.01691/verify.md) |
| 2410.07166 | LTL 统一接口仅对 G/Φ/Q 模块成立 | [verify.md](../../../../../reel/2410.07166/verify.md) |
| 2610.19600 | transfer 收窄为干预设计迁移 | [verify.md](../../../../../reel/2610.19600/verify.md) |

[^1]: 原文写作"system_method 7 / component_training 1 / evaluation_resource 1"，合计 9 但与逐篇记录不符。按 index.jsonl，2410.07166 与 2609.33807 都是 evaluation_resource，因此更正为 6/1/2。
[^2]: 原文写作"4 个聚类"。按 §4 表格，9 篇覆盖 8/13，未覆盖的是 C5、C8、C9、C10、C13，共 5 个，故更正为 5。
[^3]: 原文分数按一位小数显示（88.8 / 58.8 / 51.2）。本文统一改用 index.jsonl 中的 `screen_score` 原值（88.75 / 58.75 / 51.25），与 `selection_cutoff=88.75` 保持一致。
[^4]: 原文写作"不改正分"。按仓库 README 的说法"收窄不改分"统一为"不改分"。
