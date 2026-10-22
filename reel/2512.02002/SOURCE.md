# SOURCE · 2512.02002

- 论文：LLM-Driven Corrective Robot Operation Code Generation with Static Text-Based Simulation，arXiv **2512.02002v3**
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2512.02002.txt`（FULLTEXT: html-full，Abstract、§I–§VI、附录 VI-A/VI-B 全部读过）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3，F2/F3）；入选：`selections/selection-002.md` #8（反馈来源替代）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过，不退回。L2 事实与原文一致：20 个 Advanced 任务、6–19 个动作、3 次重复（§IV-A）；PX4 / o4-mini 本文与 Semantic 均 93.3%（Table II）；评估准确率均值 91.7 vs 92.1（Table IV）；去规则/示例退化（Table V）；真机 UAV 87.5/91.7、地面车 87.5/87.5（Table VI）。subcard 判断（R05 challenged/NA/partial/partial）合理。

措辞小注（不影响判断）：
1. “同为 93.3%” 只是四个设置中的一格；完整为 simple_flight o3-mini 85.0=85.0、o4-mini 90.0 vs 88.3、PX4 o3-mini 86.7 vs 88.3、o4-mini 93.3=93.3。画报展示全部四格。
2. Table V 中 o4-mini 完整版 SR 91.7 / 完成度 97.7 与 Table I（90.0/98.3）、Table II（93.3/96.9）都不一致，原文未说明消融所用控制器（o3-mini 行 85.0/97.0 与 Table I 一致）。已在画报页脚注明。
3. 原文未说明 Semantic 方法 [13] 是否为本文作者前作；画报只写“文献 [13]”。
4. 最终 SR/完成度仍由仿真器（或真机 MAVSDK）状态测量（§IV-A1、§V-A1）；“不跑仿真器”仅指修码环。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 修码环需真机或定制仿真器，配置费工、执行耗时 | Abstract；§I |
| 生成—模拟—评估环；评估器沿用 [13]；代码生成用 GSCE 策略 | §III-A、§III-B、§III-D |
| 静态模拟 O=⟨S,A,T,C⟩，F: C×S×A→S；提示含 role/APIs/policies/examples | §III-C |
| 对照：Direct（[11]，不模拟）、Numerical（[12]，仿真数值）、Semantic（[13]，数值→语义，实验中改写转换算法） | §IV-A3 |
| o3-mini / o4-mini；AirSim simple_flight 与 PX4-Gazebo；3 次重复 | §IV-A1 |
| 20 任务、6–19 动作、两种仿真中人工验证 | §IV-A2 |
| SR 与完成度定义 | §IV-B1 |
| 四格 SR（Direct / Numerical / Semantic / Ours）：SF o3 43.3/73.3/85.0/85.0；SF o4 33.3/81.7/88.3/90.0；PX4 o3 55.0/83.3/88.3/86.7；PX4 o4 25.0/86.7/93.3/93.3 | Table I、Table II |
| PX4 o4-mini 完成度 96.9 vs 98.6 | Table II |
| 轨迹描述准确率 97.5（o3）/100（o4） vs 100/100 | Table III |
| 评估判对率均值 91.7 vs 92.1；措辞非确定性解释 | Table IV 及正文 |
| 消融 SR：o3 85.0/83.3/81.7/71.7；o4 91.7/83.3/83.3/68.3 | Table V |
| 5 条规则（坐标系、偏航正负、NED、初始朝北、角度映射） | 附录 VI-A Policies |
| 真机 Holybro X500 V2（PX4）8 任务、ROSMASTER X3 8 任务；SR 87.5–91.7 | §V-A、Table VI |

## 本画报计算 / 自绘

- 四格差值（0.0、+1.7、−1.6、0.0）为 Table I/II 相减。
- 双路径流程图为依据 §III、§IV-A3 文字的自绘示意，不是论文 Fig. 1/2 原图；点图按表值重绘（4.5 px / 百分点）。
- 未运行论文代码，未复现实验。
