# SOURCE · 2610.39775

- 论文：Teaching a Tree to Recover: Online Distillation of an LLM Supervisor with Counterfactual Replay，arXiv **2610.39775v1**（2026-10-29）
- 阅读原文：钉定缓存 `research/fulltext/2610.39775.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §2 相关工作与附录 A–B）。§2、附录 A（场景网格）、附录 B（实现细节、Table 3）补读自同版本 arXiv HTML `https://arxiv.org/html/2610.39775v1`（2026-10-31 取得，转换稿仅在 /tmp，不提交）。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-06.jsonl`（L2，P3 / confirmed / to_l3；F2,F3；capability）；入选：`selections/selection-006.md` #2。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-31）

通过，无 correction。L2 facts（留出 20 布局：无恢复 0、规则 18、LLM 16.3±1.5、树 18.3±0.6，含 2 个应叫人；100 新种子含 28 个应叫人，树 94.7±2.3、规则 95、只蒸馏 92、无重放 92.7；反事实 41% 需要、41% 弱有害、1% 强有害；退役后教师可重教）与原文一致。L2 子卡所记“静态阻塞检查用整条路线 true map”“重放＋退役为联合消融”“heldout 在训练中被多次查看”均成立。

展示缩窄（不改判断）：
- 画报主张限定为“零调用、与手写规则持平”，不写“超过手写规则”（新种子 94.7 vs 95）。
- “正确收尾”定义写明含该叫人时叫人，不写成“到达目标”。
- 反事实份额标“近似值”，并注明干净率与“需要”在连续恢复处为上界（附录 B Counterfactual replay）。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 全局规划把机器人当点、MPC 视界 4 s、遇未知大障碍停住；现有做法每次异常问 LLM | §1；§4.1 Environment and controller |
| 报告约 40 字段、最近 5 s、只给证据；每 2 s 一次；断路器 3 次恢复无 1 m 进展 | §3 Report；§4.1 Supervisor；附录 B Report and recoveries |
| 树：13 个特征签名、箱边即失败测试阈值；2 个不同回合确认后可信；约 6 μs；教师约 5.8k tokens、中位 1.5 s | §3.1；Fig. 2 说明；§4.1；附录 B Tree |
| 反事实重放标签与退役规则（10 次不必要/有害且至多 1 次需要） | §3.2；附录 B Counterfactual replay |
| 行人 wait 规则：进展裁判打高分；无重放的树等 498–517 次、规则 148；两类失败布局；方法三轮均在第 6 回合退役 | §4.3 Importance of counterfactual replay；Table 2 |
| wait 次数条：148 / 517 / 505 / 351 | Table 2 Waits 列 |
| 留出 20 布局计分板（正确收尾、调用、滞后、步数）；99% tick；早到约一成；新种子 96/92/96 vs 95 | Table 1；§4.2 |
| 反事实标签堆叠条：规则 67/26/0/6/1、只蒸馏 37/10/6/46/1、方法 41/17/1/41/0；干净率 94–99% | 附录 B Table 3；§4.5 |
| 手写规则 wait 四分之三需要、树约五分之一；重放价值在少数退役 | §4.5 |
| 教师调用 1.8→0.1 次/回合；每轮 73–81 次；200 布局不到 2 美分 | §4.3；§4.1 |
| 重复布局：23→7.5→约 1.3；滞后 7.6→1.2；结局不变；2 次重教已退役规则 | §4.4 |
| 限制：仿真方块世界、无真机、true map、墙钟漂移、联合消融、重教 | §3 Report；§4.4；§5；附录 B |

## 自行绘制

- “每 2 秒一次：谁来回答”流程图为据 Fig. 2 与 §3 重绘的示意。
- 柱条与堆叠条按 Table 2、Table 3 数值绘制。
