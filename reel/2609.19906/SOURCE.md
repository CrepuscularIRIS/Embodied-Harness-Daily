# SOURCE · 2609.19906

- 论文：Learning and Transferring Closed-Loop Robot Software，arXiv **2609.19906v1**（2026-09-17），https://arxiv.org/abs/2609.19906
- 阅读材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2609.19906.txt`（html-full，sha256 前 16 位 e80a444bec6a1e65；私有缓存不提交）
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl` paper_id=2609.19906（batch b024，screen_score 88.75，GMXE 4/4/4/3，evidence_level=online，supported_in_material）；入选见 `reel/selection-opus.md`（C6）
- 核对：`reel/2609.19906/verify.md`（pass）
- 图形：全部为本刊据原文数字自绘的示意，非原论文插图（原文 Fig. 1–3 未使用）。

## 数字 / 断言 → 原文定位

| 画报内容 | 原文 | 定位 |
|---|---|---|
| 源任务 4 个、目标任务 9 个；RoboCasa / PandaOmron；gpt-6-astra high | 同 | §IV-A、§IV-D、Fig. 3 图注 |
| 源侧：10 示范→首代码→Train 反馈改写至第 5 代→Validation 选→整份入档；运行时不调模型 | 同 | §III-B、式(2)、§IV-A |
| 目标侧：只读档案、无源-目标配对、不自动复制；5 示范、5 Train、改 1 轮（报错可多 1 轮）、10 Test、30 分钟/80 调用 | 同 | §III-C、§IV-D |
| 无参考 45.2%（122/270）、Initial4 41.5%（112/270）、Best4 57.0%（154/270） | 同 | Table III 均值行、Abstract |
| Best4 三次运行均高于 Initial4，平均 +15.6pp | 同（表内均值相减为 15.5，四舍五入差） | §IV-D、Abstract |
| 逐任务 6 胜 1 平（OpenCabinet）2 负（TurnOffMicrowave、CoffeeSetupMug） | 同 | §I、§IV-D |
| 右注任务键 27/23/27 … 0/3/0（成功/30） | 同 | Table III 各行 |
| 中图纵坐标 = (Initial4 或 Best4 计数 − 无参考计数)/30，如 ④ +73.3→+56.7，② −60.0→+10.0；均值 −3.7 / +11.8 | 本刊由 Table III 计算 | Table III |
| 中图横坐标 28.3% / 64.2%（34/120、77/120） | 同 | Table I A 栏 |
| 象限竖向分界（46.25%）及象限命名 | 本刊示意 | — |
| “过度特化”担忧 | 作者假设 | §I、§II-B、§IV-D |
| 分支数 622→741（作者称不足以证明特化） | 同 | §IV-D |
| 在线控制 51.7%（62/120），52.6 次调用/回合；BC-Transformer 9.2%（11/120）；GR00T N1.5 62.5%、π0.5 58.3% | 同（计数由各格相加） | Table I、§IV-B |
| 消融 Full 65.0% → 去 GT-Geom 35.0%，单次运行 | 同 | Table II、§IV-C |
| 限制：源档案固定、改进轮数单一、计算量不等、仅仿真 | 同 | §IV-D、§V |
| 限制：参考价值仅条件平均、未报告实际参考了哪份代码 | 本刊阅读判断（由 §III-C “No source–target mapping” 与表中无归因得出） | §III-C、§IV-D |
