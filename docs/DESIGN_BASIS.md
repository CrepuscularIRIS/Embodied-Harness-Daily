# 设计依据：ResearchStudio Idea → Harness 逆向研究 → 评分 → Reel

2026-10-21 修订。保留已完成的卡片和原始资料，替代当日初版过于简化的七维评分草案。
本次核查的是本地 ResearchStudio 源码、Open Scientist 0.3.0 规范及本仓库历史设计；尚未定位网页端所指的 Astra 对话，不把本稿冒充那段原设计。

## 采用哪些设计

| 来源 | 采用的内容 | 在本项目的位置 |
|---|---|---|
| IdeaSpark `bottleneck_identify.txt` | 方法谱系、最近邻、frontier residual、具体瓶颈及其代价 | 逐篇 gap identify；先确定问题，再评方法，不用“没人把 X 用到 Y”代替 gap |
| IdeaSpark `pattern-summary-rubric.md` | 按实际执行操作匹配模式；允许 outside_taxonomy；区别执行模式与解决问题 | 既有 Harness 卡的条件检查，不强套原 15+31 分类 |
| IdeaQuality | 问题位置、方法质量、problem-fit | 完成论文的 G/M/X 分析；其 idea 阶段原总分不直接移植 |
| Open Scientist `domain/read` | 固定版本全文、operation signature、信息可见性、条件与反证；提取阶段不评分 | 每篇的证据事实层 |
| Open Scientist `domain/cards` | 按操作＋信息＋条件聚合，保留 counterexamples 与 unassigned | Harness 版模式卡逆向归纳；已有卡继续使用，缺口才增修 |
| Open Scientist `domain/profile` | 从真实 review 或论文实践/局限形成适用的 reviewer expectations | 领域评价判据；无审稿照样可用 |
| ResearchStudio Reel `paper2assets` / `paper2poster` | 证据资产包、按内容选图、可编辑源、渲染与视觉核验 | 只处理高分且入选的少量论文 |

IdeaSpark 的新想法生成、强制候选组合等步骤不逐篇执行；本任务是在已完成论文中逆向识别问题与研究操作。
Open Scientist 用来按缺口选择下一步：材料不全回阅读，谱系不明回检索，条件冲突回审阅；不是每篇都重建整个领域。

## 领域资产先行，逐篇评审随后

语料 → 范围筛选 → 完整阅读/操作签名 → 机制归类 → 条件/失败/反例 → 领域审稿期望 → rubric 锚点 → 校准冻结。
目前已有 `patterns/` 与 taxonomy/conditions：先核版本、来源与缺口，不重复造一套替代卡。

每张更新候选应含：稳定 ID/版本、object、information（含不可见信息）、operation、output、选择与留存规则（如适用）、
条件、失败/反例、成员签名引用、证据定位、适用期望、与朴素替代的区别。
只用摘要的成员不能证成机制；单篇为 `case`，至少两篇全文支持才可提 `candidate_pattern`，独立审阅后才可 `checked_for_scope`。
共享关键词不能证明共享机制；同操作但信息权限/条件不同须分开或明确子条件。历史卡若缺新字段，列增补任务而非伪称已满足。
日常新论文只提交 card_revision proposal；证据不足可保持 unassigned，不能为适配评分现场改卡。

## 无审稿时，明确使用审稿期望

- `observed_in_reviews`：存在可解析的真实 review、原句及来源。
- `common_practice`：至少三个独立、实际读过的论文提供 paper_practice / paper_limitation 依据。
- `single_source`：仅一至两个来源，保留适用条件与较弱来源强度。
- 尚无来源的领域判断只能列为待查假设，不能装作已经形成的期望。

这些都能提出“一个严格审稿人会追问什么”，但只有第一类可说“真实审稿人指出”。
不能用“不具备 reviews”取消期望分析，也不能用“accepted / rejected gap”预测某篇质量。
现有 RSI 卡保留了含 outcome 的历史段落；评审材料只提取机制、条件与期望，隐藏录用统计，避免权威偏差。
GUI/EH 卡与本地 profile 中的期望来源需逐条回到 signatures/原文；profile 存在不代表这次已经复核每条。

## 本领域首要检查

- 定位具身感知、技能调用、闭环控制、停止/完成判断、教师数据或学生学习的瓶颈；明确本体与部署信息条件。
- 说明改动发生在 planner、tool、VLA executor、verifier、memory、训练数据或优化环；区分 teacher 特权与 student 可用信息。
- 检查外部动作门控、监控与 hand-back、技能复用、训练/部署接口；已有 K201–K204 等卡提供机制与失败条件。
- 闭环执行/真机分母与 verifier 误判；同模型/任务/预算对照；留出场景；教师-基座学生-训练学生与特权信息消融。


## 从现有卡到审稿问题的示例

[外部验证与控制卡](../patterns/main/external_verification_control.md)与本地 domain profile 的期望可映射为：

- E02：声称 gate/verifier 造成提升时，隔离组件并固定基座 → E 因果项。
- E19 / E20：真机试验分母，以及 depth/STOP 的标定与信息条件 → E 测量项；必要条件的实现另记 X。
- profile E17 / E18：声称 skill/memory/harness 留存提升时，检查独立留出、接受规则、接受/拒绝数量与 ungated 对照 → E 留出/因果项。
- profile E09 / E21：蒸馏主张检查同 harness 下教师/基座学生/训练学生，以及移除教师侧组件后的部署 → E 因果/范围项。

本地 profile 的 paper_practice / paper_limitation 来源仍需逐篇回读；这些例子不是本次重新验证的论文结果。

## Claude Code 中使用 Open Scientist

建议安装并使用：这次不仅需要计算权重，还需要 gap、谱系、模式条件、期望和独立审阅的方法。
安装后以一个有范围的 study 检查现有领域资产与评分依据；按 `forge next` 返回步骤推进，已有完整的 domain 不重建。
日常评价消费冻结的卡片/期望/rubric；出现会改变判据的新证据时，回 study 修订并版本化。
安装插件本身不会提高评分可靠性；实际全文、引用语义与留出校准才是验收依据。未安装时仍可读这些资产按同一方法工作。
本次只读规范和修改工作流程，没有创建 study、安装插件、调用评审 API 或执行实验。

## 可复核来源快照

ResearchStudio 本地 git commit：`063f10088af49909e1a4a7ea8d29efe19633f34e`，
[上游源码](https://github.com/microsoft/ResearchStudio/tree/063f10088af49909e1a4a7ea8d29efe19633f34e)。下表 hash 固定本次实际读取的本地文件。
Open Scientist 版本 0.3.0；源码随本地插件安装。原始全文、profile 与私有会话不提交到公共仓库。

| 文件 | SHA-256 |
|---|---|
| ResearchStudio Idea: bottleneck_identify | `58b822ea26d9de94d10a9ad7dcf9a94879489361b435cbd610c5fb310adcf68c` |
| ResearchStudio Idea: pattern-summary-rubric | `743bcb71345a96edb6d796b00b078a25a2d859981404fd07f4d5d1b7140ff755` |
| ResearchStudio IdeaQuality | `2defd8d45c65c72ea1fb42115c09f8642912d427c6fbda96462ba6ea975f3f23` |
| ResearchStudio Reel: paper2poster | `40776d3bae1000f8df15243c0f2aa9cb220e7d417d6745ba5c8686731107f55c` |
| Open Scientist 0.3.0: domain/read | `6d0739a6d96ce9b2907f505a7c3c1d1b21f5989ff17b0f858c3035c20a121a28` |
| Open Scientist 0.3.0: domain/cards | `2aa39adc49b4ee546809de7ed7587896fc320718013f32b4ddd569b49c9c8081` |
| Open Scientist 0.3.0: domain/profile | `c43f1e5ee3af8368d73be3064996671b41122ebb34012a28a42deaf0326aef38` |

仓库内历史依据：`archive/2026-10-21-reset/research/PIPELINE.md` 与原有 `patterns/`。
归档里的旧运行统计属于历史记录，不被此设计重新认证为有效评分或科学结论。
