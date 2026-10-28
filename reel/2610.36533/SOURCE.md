# SOURCE · 2610.36533

- 论文：RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding，arXiv **2610.36533v1**（2026-10-27）
- 阅读原文：钉定缓存 `research/fulltext/2610.36533.txt`（头标 `FULLTEXT: html`、v1；core 版，缺附录 A–F）。正文与附录 A–F 补读自同版本 arXiv HTML `https://arxiv.org/html/2610.36533v1`（2026-10-28 取得，转换稿仅在 /tmp）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-05.jsonl`（L2，P3 / confirmed / to_l3；F2,F3；capability）；入选：`selections/selection-005.md` #1。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-28）

通过，无 correction。L2 facts（PRO Long 73.4 vs ASPIRE 30.8；累加消融 5.2→19.2→38.4→91.2；RoboTwin 24.5→91.5；真机为阶段完成分）与原文一致。L2 留给 L3 的项：
- 预算与 token：附录 A.2 Table 2 给出每套件 rollout 预算（45/55，RoboTwin 11），换视角与实验计入同一预算；附录 B.8 给出 16 个设置的 token 记录（几何均值 35.1M / 135.6M / 118.8M）。预算并非逐次匹配：CaP-Agent0 无搜索阶段，在测试场景内最多改 10 次（附录 A.4）。
- 基线来源（L2 子卡 R05 写“§4.1 复现 CaP baselines 使用相同 Opus 4.6”，需缩窄）：只有 LIBERO-PRO Long 与 LIBERO-Plus 上的 ASPIRE、CaP-Agent0 由作者用相同编码模型复现；LIBERO-PRO Object/Goal/Spatial 与 Robosuite 的基线数取自各原论文（附录 A.4）。不改变档位，画报逐行标“复现/引用”。
- 验证器/审计员准确率：原文未报告（L2 K202 unknown 成立）。
- 真机：附录 F 写明搜索 10 次、每次成败由人判定并重置，评测 20 次由人打阶段完成分；两种搜索方法用 Opus 5。

展示缩窄：不写“全面领先”；列出 LIBERO-Plus 布局扰动 π0.5 98.0 > RoboAuto 96.0、Robosuite 双臂交接 75 < ASPIRE 92、83 个设置中 18 个低于 ASPIRE（附录 B.2）。不把真机写成整任务成功率。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 三类基线失败（书的抓法、照搬抓取高度、灶未点着） | §1 Fig. 3；附录 D.2–D.4 |
| 知识条目字段（可供性/空间关系/效果与前提、适用条件、待测量） | §3.1；附录 C.1 |
| Molmo2＋SAM 3＋深度、主动换视角 | §3.2；附录 C.2 |
| 阶段验证器、审计员改判、自设实验、预算计入 | §3.3；附录 A.2、C.3、C.3.1 |
| 15 训练场景 / 50 测试场景（Robosuite 100）、不相交 | §4.1；附录 A.2 Table 2 |
| 各套件均值 RoboAuto / ASPIRE / π0.5 | 附录 B.2 Table 4；§4.2 |
| 复现 vs 引用的基线来源；Opus 4.6（1M） | 附录 A.4 |
| π0.5 布局 98.0；双臂交接 75 vs 92；18/83；螺母装配 74 | 附录 B.2 Tables 4、11；“Distribution of program success” |
| 累加消融 5 任务逐格 | §4.3.1 Fig. 5；附录 B.3 Table 12 |
| 半个知识库 65.2 | 附录 B.5 Table 15 |
| RoboTwin 逐任务、token 9.3M→23.6M | §4.3.2 Fig. 6；附录 B.4 Table 14、B.8 Table 18 |
| 真机 98.6 / 11.3 / 0（三任务均值）、协议 | §4.4 Table 1；附录 B.1.5 Table 3；附录 F |
| token 几何均值与同设置成功率 79.8 / 17.9 / 36.0 | 附录 B.8 |
| Opus 5：29.6 → 77.6；重复搜索 s.d. 3.1–4.0 | 附录 B.6 Table 16；B.7 Table 17 |
| 限制：真机人重置/安全 | Limitations |

## 自绘与示意

- 顶部“失败 → 组件”对应带依据 §1 与 §3 文字整理；搜索流程图据 §3.3、附录 C.3 文字重绘（原文 Fig. 13 未复制）。
- 哑铃图、消融热格、条形图按原表数值重绘；未使用原文图片。
- 未运行论文代码，未复现实验。
