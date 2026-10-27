# SOURCE · 2610.34370

- 论文：ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation，arXiv **2610.34370v1**（2026-10-25）
- 阅读原文：钉定缓存 `research/fulltext/2610.34370.txt`（头标 `FULLTEXT: html`、v1；core 版，§III-C 在关键帧细节处截断）。全文补读自同版本 arXiv HTML `https://arxiv.org/html/2610.34370v1`（2026-10-27 取得，转换稿仅在 /tmp），含 §III-D 与 §IV 全部表格；本文无附录。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-04.jsonl`（L2，P3 / confirmed / to_l3；F0,F3；capability）；入选：`selections/selection-004.md` #2。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-27）

通过，无 correction。L2 facts（11 工具；五任务 20/20/10/10/10 次、成功 17/18/8/6/5，合计 54/70；plan-then-act 26/70；三任务消融去关键帧 64%、完整 82%；干扰下 11/15、固定计划 0/15）与原文一致。

补读要点（缩窄展示，不改判断）：
- 表列 Avg 77.0% 实为合计 54/70 = 77.14% 的写法（同表其余行 37.1/18.6/24.3 均为合计口径、四舍五入正确）；按任务平均为 73.0%。画报写 54/70 并注明三种口径。
- §III-D 关键帧 = 机器人与物体接触的时刻，只记 RGB、机器人状态、子任务与工具名；无检测误报/漏报数据，L2 缺口成立。
- Table III “Ours”行与 Table II 同为 17/18/6，即沿用主实验试验，非另跑。
- plan-then-act 基线“the LLM constructs a high-level plan … and execute each tool”，未说明是否含 5 个技能与姿态计算；其在干扰实验的 0/15 作者归因于计划固定（由设定决定）。
- ACT/π0.5 每子任务 50 条示范；作者把其失败归因于导航后站位偏差。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 平台 Lenovo BOT MX 轮足四足＋Agilex PiPER；GPT-5.6 Sol | §IV-A |
| 4 域 11 工具（拍图、SAM3 检测、地图/目标导航、抓/抬/放/推/拉、速度、姿态） | §III-B Table I |
| 速度控制 HIM RL 策略；姿态控制脚位固定 IK | §III-B 式 (2)(3) |
| 5 技能；子任务后检查重排；找物每次 45°；θ = atan2(z, √(x²+y²)) | §III-C 式 (4) |
| 关键帧定义与记录内容 | §III-D |
| 五任务逐次结果、合计、Avg 77.0 | §IV-B Table II |
| ACT/π0.5 用 50 条示范/子任务；站位偏差解释 | §IV-B |
| 消融 12/0/2、14/15/3、17/18/6 | §IV-C Table III |
| 户外四地面 × 1/2/3 件 × 5 次 | §IV-D Table IV |
| 干扰实验 1/2/1、2/2/1、0/0/0、4/5/2；人工复原方式 | §IV-E Table V |

## 自绘与示意

- “两种循环”为自绘示意（依 Fig. 2 与 §III-C–D），非原文图。
- 所有方块图按原表逐次重绘（每格一次试验），未使用原文图片。
- 未运行论文代码，未复现实验。
