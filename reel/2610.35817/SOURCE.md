# SOURCE · 2610.35817

- 论文：Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent，arXiv **2610.35817v1**（2026-10-26）
- 阅读原文：钉定缓存 `research/fulltext/2610.35817.txt`（头标 `FULLTEXT: html`、v1；core 版，缺附录 A–E）。附录补读自同版本 arXiv HTML `https://arxiv.org/html/2610.35817v1`（2026-10-27 取得，转换稿仅在 /tmp）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-04.jsonl`（L2，P3 / confirmed / to_l3；F3,F1；capability）；入选：`selections/selection-004.md` #1。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-27）

通过，无 correction。L2 facts（同 harness base 8.3 → SFT 58.3 → RL 74.0；10 个真机任务每模型 3 次，ZAP 与同 harness Astra 均 29/30；146 vs 397 s、$0.29 vs $4.87；Franka RoboLab-120 55.9%）与原文一致。L2 留给 L3 的三项：
- 奖励专用状态隔离：附录 A 写明仿真中感知只用渲染图像与深度，“never reads any privileged information such as object poses”；K703 Operation 可视为成立（奖励仍按终局场景状态计算，策略不可见）。
- 任务泄漏：§3.2 40 个训练任务均不在 RoboLab-120；真机 10 任务从 RoboLab-120 任务表复刻，与训练任务同为抓放/叠放族。
- 成本口径：Table 3 注明 ZAP 为单卡 B300 $7.10/h 自托管折算，Astra 为 API；17× 不是同一计费口径。

展示缩窄：标题只写“打平”与“新本体仅仿真”；“预训练知道做什么”无语义预训练消融，画报不作此归因；§5 五个新任务各为单次演示，画报标“无成功率”。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| Base 看得懂但不会动（作者读思考文本） | §4.1 |
| 自采成功轨迹 SFT、短 GRPO 预热、前缀树搜索 ≤~1000 叶 | §3.3；附录 Fig. 8 |
| 分段奖励 0.2/0.2/0.55/0.9、成功 5.0、保持 0.5 s；无调用/无效调用罚，4%→0%、34%→3% | §3.2 |
| 5 个工具、绝对末端位姿、无抓取宏、越界拒绝、仿真不读真值 | §3.1；附录 A |
| 40 个训练任务不在 RoboLab-120 | §3.2 |
| 仿真 8.3/58.3/74.0、Astra 72.2、Opus 5.5 61.2 | §4.1 Table 2 |
| SFT 455 条 17.2 vs 3.9k 条 58.3 | §4.4 Table 5 左 |
| 真机 96.7/96.7/36.7/33.3/16.7；30 次/模型；Astra 推理 max | §4.2 Table 3 |
| 逐任务成功次数（两因素图计数由此加总：29/29/11/10/5） | 附录 D Table 6 |
| 魔方“进碗” 3/3 vs “碗后面” 0/3；“恰好 3 根”放多 | §4.2 |
| 时间、轮数、每轮时长、费用；B300 定价 | §4.2 Table 3 右 |
| Franka 55.9 vs Lakeside 51.0、FLUX 3 Action 42.9（排行榜）；9B 版 53.4 | §4.3 Table 4；§4.4 Table 5 右 |
| 试管、左上角孔、交接、井字棋、象棋 | §5 Figs. 3–6 |

## 自绘与示意

- 顶部训练/部署流程与“模型 × harness”两因素图为自绘重排，数字来自 Table 3 与附录 Table 6；“未测”格为原文未报告的组合。
- 其余条形图与热格由原表重绘；未使用原文图片。
- 未运行论文代码，未复现实验。
