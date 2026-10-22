# SOURCE · 2609.35318

- 论文：DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library，arXiv **2609.35318v2**（2026-09-28）
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2609.35318.txt`（FULLTEXT: html-full，Abstract、§I–§VI、附录 VI-A–VI-D 全部读过；图仅有图注）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3，F0/F4）；入选：`selections/selection-002.md` #9（人视频→示范数据生成）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过，不退回。Table IV 平均 63.6% vs 最强数据基线 SPIDER 18.2%、抽屉 80%、绳打结 50%（基线全 0）均与原文一致，且按单元格复算平均值无误（8 行全部吻合）；Table III 为“10 次重放中 ≥1 次成功”的覆盖指标，L2 已正确区分。问题判断（q1–q4、P3）成立。

措辞小注（不影响判断，但修正了展示的边界表述）：
1. selection-002 写“增强与轨迹生成贡献尚未隔离”。§V-A 明确：所有方法使用**同一数据增强与视觉处理协议、同一 π0.5**，缺失环节由统一实现补齐，因此跨方法对照已控制增强环节；真正未隔离的是 DexAgent **内部**各阶段（重建、轨迹、校验器、工具库）的贡献，以及扩增时基线轨迹是否也经过 DexAgent 校验器（原文未说明）。画报按此表述。L2 subcard K503 第 4 条“模块、数据量、额外工具及技能库更新效果尚未完全独立控制”表述正确。
2. §V-B 正文写 “Table IV reports successful replay on all eleven tasks”，实指 Table III（引用笔误）。
3. 工具库规模在图注（100 段后 85 技能/168 校验器）、正文（第 78 段达 85/168）、附录 VI-D（当前 103/188）之间口径不同；处理耗时在 Fig. 4 图注（新运行 2.1 h）与正文（首段 4.3 h、复用技能 2.2 h、复用资产 13.1 min）不一致。画报只用 85/168，未展示耗时。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 输入：一段第一视角 RGB 人类视频＋任务提示 | Abstract；§III-B |
| 四阶段：语义理解 / 按属性重建 / 轨迹优化 / 数据生成 | §III、Fig. 2 图注 |
| 每阶段 ≤100 轮或预算，耗尽记为失败；通过校验器才进入下一阶段 | §III 第一段 |
| 技能、校验器为带类型 Python 函数，改进时分叉不覆盖，入库复用 | §III-A |
| 阶段 1 输出 JSON：物体类型/属性、子任务、执行手 | §III-B |
| 阶段 2：参数化重建技能、编辑 URDF、刚体/铰接/可变形校验器、3 个变体复检、IoU 摆放、相机估计 | §III-C |
| 阶段 3：子目标成功条件、重定向/接触优化/生成抓取、举起摇晃/滑动旋转测试、IK＋代码连接、回改前段、整轨迹校验 | §III-D |
| 阶段 4：随机初始状态、同样校验、VOID 去除演示者、Blender 重贴图、腕部视角 | §III-E |
| 1500 种子可行性检查后取 500 条，三视角 | 附录 VI-A |
| HOI4D F-5：刚体 0.83 vs 0.72；铰接 0.47 vs 0.40 | Table I |
| OakInk 通过率 85.7 vs Do-as-I-Do 81.0；旋转误差 0.12 vs 0.15 | Table II |
| 重放覆盖：DexAgent 11/11、SPIDER 6/11、V2D 5/11、GPT-6 Astra 5/11（≥1/10 即算；GPT-6 Astra 第一轮后加入） | Table III 及图注 |
| 策略成功率 11 任务 × 8 方法单元格与平均 | Table IV |
| 对照控制：同一视频、保留各自环节、统一补齐、同一增强/视觉处理、同一 π0.5、500 条、10 次随机初始状态；GPT-6 Astra 零样本 | §V-A |
| 双 Sharpa 手、YamBox、D435 第一视角、Zed Mini 腕部相机；MuJoCo 或 Isaac Sim | §V-A；§V |
| 85 技能、168 校验器（100 段 EgoDex） | Fig. 4 图注；§V-B |
| 作者自述局限：语义/几何错误、校验不完备、错误随工具库传播、力敏感交互仿真通过而真机失败 | §VI |

任务中文名：Cup＝放杯、Giftbox＝礼盒打包、Drawer＝抽屉放置、Rope Knot＝绳打结、Scissors＝剪刀、Drawing＝绘画擦拭、Computer＝电脑安装、Bottle＝开瓶、Battery＝电池插入，依 §V-A 任务描述对应；Biology→移液（pipetting）、Multi-object→多杯抓取（multi-cup grasping）为本画报推断，已在画报页脚注明。

## 本画报计算 / 自绘

- 转换管线图为依据 §III 与附录文字自绘的示意，不是论文 Fig. 2 原图。
- 热力图为 Table IV 数值重绘，颜色深浅线性映射 0–100%；生成时用脚本断言每行平均与原文一致。
- 未运行论文代码，未复现实验。
