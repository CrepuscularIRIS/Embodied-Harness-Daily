# SOURCE · 2610.31841

- 论文：FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation，arXiv **2610.31841v1**（2026-10-22）
- 阅读原文：钉定缓存 `research/fulltext/2610.31841.txt`（头标 `FULLTEXT: html`、v1；core 版，缺 §II 相关工作与图注）。§II 与 Fig. 1–9 图注补读自同版本 arXiv HTML `https://arxiv.org/html/2610.31841v1`；论文无附录。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-03.jsonl`（L2，P3 / confirmed / to_l3；F0,F4；capability）；入选：`selections/selection-003.md` #2。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-26）

通过，无 correction。L2 facts（100 Hz、运行时无模型调用、≤20 rollout / 4 小时、30 N 算失败、人负责授权与场景；抽屉 10/10 vs 4/10、门 10/10 vs 1/10；擦拭 99%/93% vs 73%/21%；手持测试沿用静止版程序）与原文一致；subcard 限定（单条开发链、力反馈与日志诊断同时变化、缺一次生成与手写控制器基线）均有原文依据。

补读要点：Fig. 9 图注“Executions 18–20 repeat Forca’s final program”，与 Table IV 门把手 17 轮一致；画报据此把 17 标为首次成功、18–20 标为重复执行。敲方块任务只报告迭代数（从零 13 轮、新条件平均 2 轮），无仅视觉对照与冻结后重复计数，画报单列并注明。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 不用示范、任务训练或仿真；对照为同一智能体的仅视觉版本 | Abstract；§I；§IV-A Baseline |
| Claude Fable 5；技能库（感知、抓取、PyRoKi 运动规划）；100 Hz RTDE 回路；执行中不调用模型 | §III-A、III-B；§IV-A |
| 读力迹与图像、写分析代码、修订；修订前检查；≤20 rollout / 4 小时；30 N 硬限算失败；人负责授权、场景操作与验收 | §III-C；§IV-A |
| 仅视觉：同模型、指令、技能；生成/修订/执行均无力数据；安全保护不暴露 | §IV-A Baseline |
| 门把手两条开发记录（阶段、装置故障、第 10/16 轮修订；仅视觉第 7、13–20 轮） | §IV-D Table V；Fig. 9 图注 |
| 抽屉/门：成功、平移/旋转抓取误差 | §IV-B1 Table I |
| 擦花瓶：静止/手持 去除率、失接触；手持沿用静止版程序 | §IV-B3 Table II |
| 削黄瓜：失接触、过压、削皮比例 | §IV-B3 Table III |
| 失接触/过压定义（1.5 N、0.8 N、≥0.2 s、10 N）；力迹仅离线评分 | §IV-B3 Contact metrics |
| 敲方块：61.9 g / 663.6 g，白板/木板；从零 13 轮、新条件平均 2 轮 | §IV-B2；Fig. 5–6；Table IV |
| 每轮推理 4–10 分钟、运动 1–3 分钟；门 17、抽屉 8、擦拭/削皮 20 轮 | §IV-C Table IV |
| 限制：迭代成本、腕部力矩信息有限、复杂任务可能失败 | §V |

## 自绘与示意

- 顶部四格流程与开发时间线由原文 §III–IV 与 Table V、Fig. 9 图注重绘，非原文图。第 9–10 轮原文写作 “Approach, press down” 的装置故障，画报以虚线框“装”跨两阶段表示，不区分具体卡在哪一步。
- 未运行论文代码，未复现实验。
