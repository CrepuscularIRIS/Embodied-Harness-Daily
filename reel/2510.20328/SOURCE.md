# SOURCE · 2510.20328 MemER

- 论文：MemER: Scaling Up Memory for Robot Control via Experience Retrieval，arXiv 2510.20328**v1**（2025-10-23）
- 阅读来源：本地缓存 `research/fulltext/review-runs/embodied-v22-20261021-01/materials/2510.20328.txt`（html-full，含附录 A–G；sha256 前 16 位 `178c2dbda06b3625`）。全文不提交。无 `_pdf.txt`；图 5/6 只有图注，图中百分比未取用。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（paper_id=2510.20328，L2，P3/confirmed/to_l3）；入选理由见 `selections/selection-001.md` 第 4 行。
- 规则：problem-core-v1.1；制作席 Opus 5.5；2026-10-22。

## 核对结论：通过（无 correction）

| L2 判断 | 原文核对 |
|---|---|
| 问题：分钟级历史、有限上下文下保留关键视觉事件 | §1、§3.1 Memory-Based Tasks 成立 |
| 固定低层、比较无历史/8 帧/32 帧/HumanHL | §4.1 "baselines change the input context of π_h while using the same π_l"，表 1 成立 |
| 32 帧约 16 秒 | §4.1 "32 frames (~16 seconds of memory) incurs an inference cost of 1 second" |
| 专有模型为离线预测 | §4.1 Q2，表 2：API 延迟 10–15 s，闭环完全失败，改离线 |
| 对象搜索同 15 类对象、非未见物体迁移 | §4 Object Search "train and test with the same set of 15 objects"；Dust 训练 17 件、测试 9 件子集 |
| 关键帧选择与高层训练适配部分耦合（R02 partial） | §3.3：高层同时学子任务与关键帧，无单独拆分实验，成立 |

补充边界（不改变 L2 档位）：模型融合 α=0.8 对所有基线一致（§3.3）；附录 C 的跨任务换物体只在两类物体集之间互换，仍不是新物体。

## 画报数字映射

| 画报内容 | 原文位置 |
|---|---|
| 高层 Qwen2.5-VL-7B 微调、低层 π0.5（DROID 版） | §3.3 |
| 最近 N=8 帧 + 关键帧 \|K_t\| ≤ 8 | §3.2 |
| 1D 单链聚类 d=5 帧，取中位帧 | §3.2、图 3、附录 D 算法 1 |
| 高层约 1 Hz、低层约 2 Hz，2 Hz 采样输入 | §3.3 Closed-Loop Deployment；§4 Evaluation Setup |
| 每方法每任务 20 次 | 图 4 注；表 1 注 "raw counts across 20 trials" |
| 表格全部数字（32/25/61/5·4·5·7；38/31/26/14·14·11·12；47/41/12/11·11·12·12；59/57/1/20·19·18·20；58/58/0/19·19·18·17） | 表 1 |
| 物体搜索满分 60 = 3 物体 × 20 次 | §4 Object Search 指标定义 + 20 次（分母为我们按定义计算） |
| 长历史平均比 MemER 低 34% | §4.1 Q1 原句 |
| 短历史+文字 40/60、舀错 10；MemER+文字舀错 13 | 表 3 |
| 文字记忆失败原因（过度依赖记忆中文字） | §4.1 Q3 |
| 关键帧只增不删、1 Hz/2 Hz、单一平台 | §5 Discussion |
| GPT-5 / Gemini Robotics-ER 1.5 离线比较 | §4.1 Q2、表 2 |

## 我们的推算与示意

- "约 4 秒"：8 帧 ÷ 2 Hz 推算，原文未直接给出，画报已注明"按 2 Hz 推算"。
- "擦拭归位并未变好"：比较表 1 短历史 14·14·11·12 与长历史 11·11·12·12 得出，属阅读判断。
- 机制图为自行重绘的示意（参照图 3 与附录 D），非论文原图；柱高与簇位置是示例，不对应真实数据。
- 未运行任何代码，未复现。
