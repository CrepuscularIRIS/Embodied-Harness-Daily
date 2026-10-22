# SOURCE · 2306.15724

- 论文：REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction，arXiv **2306.15724v4**（缓存头标 2023-06-27）
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2306.15724.txt`（FULLTEXT: html-full，Abstract、§1–§6、附录 A–B 全文）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3）；入选：`selections/selection-002.md` #1（失败解释→纠正）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过。L2 的问题陈述、q3_loss、facts 与 subcard_checks 与原文一致：固定 GPT-4；RoboFail 模拟 100 个人工注入失败；完整方法纠正 79.1 / 80.7%，无解释 41.9 / 56.1%，去渐进 60.5 / 64.9%；模拟对象检测与状态用真值；真实 30 段（11 任务）只报 Exp/Loc，无纠正分母。

措辞与原文小注（不影响判断，不退回）：
- L2 facts 把 Table 1 定位为“§3–4”，本缓存版本中 Table 1/2 在 §5 Evaluation，RoboFail 数据集在 §4。
- 原文未列执行/规划两类失败各自数量。按百分比反推，执行 43 / 规划 57 与 Exp、Co-plan 各值一致（如 79.1% = 34/43，80.7% = 46/57），但执行 Loc 96.0 不能被 43 整除得到（41/43 = 95.3），属原文数值本身；画报照录，不写分母。
- 附录 Table 5（GPT-3.5 对比）表头为 Loc/Co-plan，但 GPT-4 行数值与 Table 2 真实场景的 Exp/Loc 相同，原文表述可能有误；画报只引用“GPT-3.5 明显下降”的定性结论。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 问题：从多感官历史生成摘要、让 LLM 定位/解释失败并指导纠正 | Abstract；§1 |
| 三层摘要（感官输入：场景图、CLIP 状态、8 种空间关系、AudioCLIP；事件：场景图变化/声音起止/子目标结束取关键帧；子目标：每个子目标结束帧） | §3.1.1–3.1.3；附录 A.1 |
| 渐进式提问：逐个子目标问 Yes/No；No → 取事件摘要问致因；全 Yes 仍失败 → 原计划+终态问计划错误与最相关时刻 | §3.2；Fig. 3 |
| 纠正规划器输入（任务、原计划、失败解释、终态、目标）与动作映射 | §3.3 |
| 时间轴例：烧水，00:36 掉锅（声音 something drops、夹爪空），00:44 子目标未满足，解释回溯到 00:36 | 附录 A.3.1–A.3.2 |
| RoboFail：模拟 100 个失败（10 任务 × 10，人工注入，AI2THOR）；真实 30 段、11 任务，人遥操作 UR5e 模仿策略 | §4；§5 |
| 模拟用真值检测/状态；真实用 MDETR / CLIP / AudioCLIP；GPT-4 | §5 |
| 指标定义 Exp（人工判正确且有信息量）、Loc（落入标注区间）、Co-plan（执行纠正计划后终态满足目标） | §5 |
| Table 1 全部数值（五种方法 × Exp/Loc/Co-plan × 执行/规划） | §5 Table 1 |
| Table 2 数值（BLIP2、w/o sound、w/o progressive、REFLECT） | §5 Table 2（画报省略 Subgoal only、LLM summary 两行） |
| 去掉声音执行失败 Exp/Loc 约降 20% | §5 “Audio data is useful” |
| Fig. 8 例：咖啡机里有杯子；带解释先移开杯子；无解释只重复原计划 | §5 “Failure explanation helps correction” |
| 人工评审 2 组 × 3 人、多数票 | 附录 B.4 |
| GPT-3.5 定位与纠正下降 | 附录 B.2 |
| 局限：启发式场景图、预设状态列表、静态环境、低层控制失败 | §5 Limitations |

## 我们的计算与读法

- 差距 37.2 / 24.6 个百分点 = Table 1 Co-plan 相减。
- “解释越接近真实致因，纠正越有效”“纠正效果受是否定位到致因约束”是阅读判断，已在画报中标为我们的读法。

## 自绘与示意

- 时间轴（按附录 A.3.2 提示词例重绘）、三层摘要+渐进提问流程图（据 §3）为本画报自绘示意，不是论文原图。
- 双柱图为 Table 1 Co-plan 数值重绘。未运行论文代码，未复现实验。
