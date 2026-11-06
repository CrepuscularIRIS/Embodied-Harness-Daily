# SOURCE · 2611.06453

- 论文：Beyond Infraction Scores: Failure-Boundary Profiles for Closed-Loop Evaluation of Driving and Robot Navigation Agents，arXiv **2611.06453v1**（2026-11-04；Milan Bulat、Gino Ardelean、Ellington Kirby）
- 阅读原文：钉定缓存 `research/fulltext/2611.06453.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §2、§3.3 尾、§3.4 大部、§4.4 尾与 Limitations 尾）。缺失部分补读自同版本 arXiv HTML `https://arxiv.org/html/2611.06453v1`（2026-11-05 取得，转换稿仅在 /tmp，不提交）。该版本无附录。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-09.jsonl`（L2，P3 / confirmed / to_l3；F2,F3；judgment）；入选：`selections/selection-009.md` #3。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-11-05）

通过，无 correction。L2 facts（Charger 堵死宽度 SimLingo 12/12 接触、DS 52.2，TF++/TFv6/Expert 均 12/12 停、DS 40.6/39.1/37.8；DA Expert 0.74 [0.67, 0.81] vs TFv6 0.60 [0.53, 0.68]；仓储两个微调版在留出族通过更多但堵死处均不停）与原文一致。L2 记缺 §3.4：补读后 §3.4 给出几何认证（±5 mm、仿真内落点复核 ≤ 10 mm）和对向车流四层证书，与 L2 判断一致。

收录范围：被测对象（端到端驾驶模型、特权规划器、X-Mobility 导航策略）均无 LLM/VLM harness；场景族由一个 LLM“agent planner”把自然语言意图转成声明式计划（§3.4），但它不在被测回路里。按 EVIDENCE B 类“评测方法学”收录（先例：selection-007 的 2610.41857），不作 correction；画报顶部与限制栏第 1 条明示“被测对象均非 LLM harness”，“可用于 harness 停止/交还门控”标为我们的阅读判断。

展示缩窄：名次只作点估计（头部区间重叠、中段对常数敏感）；边界尺只画 Charger 一族；HiP-AD 无能力边界数值，只画承诺边界并注明。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 驾驶分 = 路线完成度 × 违规惩罚 | 摘要；§1 |
| 承诺 / 能力定义、边界 = ½ 交叉、拟合或分隔区间、DA 定义（永远停 = 0.50） | §3.2 |
| 策略下限 = 车宽＋后视镜余量＋两侧间隙；2.30 m；2.07 m 窄于下限宽于车身 | §3.2；§4.3 “Robustness”；表 1 注 |
| Charger 12 宽度 × 3 种子，最窄 4 个（0–2.07 m）堵死，3.64 m 起 | §3.3；§4.3 Charger |
| 边界值 Expert 3.14 [3.02, 3.26]；TFv6 2.82 [2.59, 3.06] / 2.84 [2.59, 3.14]；TF++ 2.67 / 2.79；HiP-AD 2.19 [1.95, 2.35]、最窄干净通过 2.51；BridgeDrive / SimLingo 全宽都冲、干净通过自 2.90 / 3.38；推车 55 m | §4.3 Charger gauntlet |
| 堵死宽度平均 DS 与停 / 接触计数（PlanT ① 另 3 次无接触穿过 2.07 m） | 表 1 及注 |
| 平均 DS 与 DA 名次 | 表 2 |
| 常数敏感性：两端不变、中段换序 | §4.3 “Robustness to the certification constants” |
| 对向车流 29 个须等窗口：Expert 13、TFv6 6、BridgeDrive 3、其余 0；滚动窗口 PlanT/HiP-AD 全抢、Expert 不抢 | §4.3 Overview 与 Oncoming flow |
| 仓储：X-Mobility、5 个策略样本、两微调只训 2 族、码放纸箱留出；15/15 → 0/15；11/35 → 35/35；头部微调边界 1.50 → 1.05；DA 0.34 → 0.50 / 0.22；留出族 0.66 → 0.50；从不走相邻通道 | §4.3 Warehouse；§4.4 |
| CARLA 同命令两次 53.7 vs 32.2 | §4.2 |
| 缺陷变体（0.99 m 售货机倾倒、最短间距对向车互撞）剔除 | §4.3 Cluttered intrusion、Oncoming flow |
| 220 GPU 小时、3 族、Expert 只作参考、仓储仅 1 留出族 | Limitations |

## 自绘与示意

- 边界尺按原文边界数值重绘（条从边界画到 3.7 m，表示“该宽度以上会走 / 能干净通过”的读法，不是原文的拟合曲线）；名次连线按表 2 绘制；结局方格按表 1 计数分组（不是逐宽度顺序）。未使用原文图片。
- 未运行论文代码，未复现实验。
