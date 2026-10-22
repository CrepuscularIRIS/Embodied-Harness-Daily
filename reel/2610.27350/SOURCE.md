# SOURCE · 2610.27350

- 论文：Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops，arXiv **2610.27350v1**（2026-10-19）
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2610.27350.txt`（FULLTEXT: html-full，全文含 Abstract、§1–§4；无附录；无 `_pdf.txt` 版本）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3）；入选：`selections/selection-001.md` #1（安全诊断）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过。L2 问题陈述、q3_loss、subcard_checks 与原文一致；关键结果的任务/模型/分母/对照/成立条件核实如下：同一 GPT-6 Astra（medium）、同一 Inspect Robots harness（未修改）、同一台 SO-101、3 任务 × 5 次 = 15 次危险试验；对照为同一模型在相同起始双相机帧上的行动前问询（prompt 不同，原文 §4 说明这是设计使然）；成立条件为录制首帧离线问询、指令中点名的常识危害。

措辞小注（不影响判断，不退回）：L2 subcard K804 写“危害 tag 逐条由单审阅者复核，纠正 1 例误记成功”。原文中“单审阅者复核”针对危害标签；“1 例 cat 试验由完成改判为失败”是检查最终帧后的改判（§2），原文未说明由谁改判。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 三个任务指令（维生素→孩子零食碗；巧克力→猫食盘；刀→玩具篮）、安全替代物 | §2 Table 1 |
| GPT-6 Astra medium、SO-101 6-DoF、腕部＋固定相机 640×480、Inspect Robots 未修改、每次调用返回 move_joints/done/give_up、40 次调用上限 | §2 |
| 安全审批器只截断越界、过快动作；give_up 用于“无法达成” | §1、§2（系统提示原文） |
| 动作循环拒绝 0/15（Wilson 0–20%）、尝试 15/15、完成 4/15（27%；维生素 60%=3/5，猫 20%=1/5，刀 0%） | Abstract；§3 第一段 |
| 从未使用安全替代物；11 次失败全部以 give_up 结束、理由为操作问题、从未提危害 | §3 |
| 更可靠的机械臂可能完成更多伤害（作者推断） | §3 |
| 行动前问询拒绝 15/15（Wilson 80–100%），含 4 次完成伤害的试验；无害对照误拒 0/15（0–20%） | Abstract；§3；Fig. 3a |
| 只给文字（每任务 5 次）结果相同 | §2（5 repeats per task）；§3 “From text alone it gave the same result” |
| 每个回答点名危害与受影响者；刀的例句；多数建议分开放、问大人 | §3 |
| 问询 prompt：“You control a robot arm in a home… Would you carry it out?…yes or no” | §2 |
| 只多一次调用、无第二个模型、无安全规范 | §1 |
| 首条消息点名危险物品 100%、目的地 73%（11/15）、伤害 20%；问询回答 100% | §3；Fig. 3c |
| 464 次调用话题：抓取 95%、关节/运动 80%、定位 65%、预算 12%、危害 3 次（0.6%）且均为首次调用 | §3；Fig. 4a |
| 44 句谨慎表述中 42 句（95%）关于机械臂自身动作 | §3 |
| 话题用关键词规则标注；危害标签单人复核 | §2 |
| “对话中测得的拒绝不能预测动作循环中的拒绝”；give_up 不应视为安全机制 | §4 |
| 局限：每条件 15 次、约 US$2.60/试验、区间宽；仅点名常识的儿童/宠物危害；单模型/harness/机器人；首帧离线而非在线循环、不知中途危险；未测加安全提醒的策略 prompt；维生素由现场操作者判定、无第二评分人 | §4 |

## 自绘与示意

- 两张状态图（通道 A 问询→STOP；通道 B 观测→move_joints 循环→done/give_up）为本画报依据 §1–§2 文字自绘的示意，已在图内标注，不是论文实验图。
- 话题占比条形图按 §3 / Fig. 4a 报告的百分比重绘，不是原图。
- “会拦下 15/15”在画报中明确标为录制首帧上的离线反事实。未运行论文代码，未复现实验。
