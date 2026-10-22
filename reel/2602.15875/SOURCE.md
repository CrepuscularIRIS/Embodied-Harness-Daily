# SOURCE · 2602.15875 Fly0

- 论文：Fly0: Persistent Metric Anchoring for Zero-Shot Aerial Vision-Language Navigation，arXiv 2602.15875v2（缓存标注日期 2026-02-02；Table XIII 自述“April 2026 test environment”，日期元数据与正文不一致，未影响所用数字）。
- 阅读材料：本地完整 HTML 全文缓存 `research/fulltext/review-runs/embodied-v22-20261021-01/materials/2602.15875.txt`（含附录 A–D；无单独 `_pdf.txt`）。全文不提交。
- 初筛/评分记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，audit_sample，P2→P3 confirmed，to_l3）；选题理由：`selections/selection-001.md` 第 9 条及“漏检抽查改判”记录。
- 规则版本：problem-core-v1.1。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 同栈接口阶梯 SR 62.1/64.0/66.1/68.0/70.4，错误锁定 0.16/0.14/0.12/0.09/0.05；SPF-Qwen+Ego 57.6/0.19 | §V-B.3 Table V（AerialVLN，前五行共享栈） |
| 固定项：Qwen2.5VL-32B、RGB-D、LiDAR、VIO、Ego-Planner、定位噪声、停止规则 | Table V 表注；§V-A.4；附录 A-E |
| 20 个随机种子均值 | §V-A.1、§V-A.3 |
| 错误锁定定义（错误锚生效 >3 s） | Table IX 表注 |
| MLLM 推理均值 612 ms / P95 931 ms；LiDAR 10 Hz；Ego-Planner 50 Hz、P95 18.7 ms；PX4 100 Hz | §V-B.4 Table VII；§IV-E |
| JSON 点/框/关系/置信度 | §IV-A Eq.(5)；附录 B |
| 中位深度、前侧 2 m 偏移、自由空间投影、跳变 3 m、两次一致或第二视角、4 s 悬停 / 10 s 返航 | §IV-B～IV-D；附录 A-C；Table XVI–XVII |
| +1 s 延迟 55.2，10 s 断云 53.9，正常 62.9 | Table VIII（Fly0-Real） |
| 暂不可见目标 52.4 vs SPF-Qwen 23.7，占 10% | Table X |
| 对 SPF +23.7 SR；bootstrap/McNemar | §V-B.2（针对 Table IV 主对比） |
| 嵌套/组合关系 SR@2m 34.2 | Table XI |
| 错误重复物体被多视角一致锁定 | §V-B.7 失败案例；Limitations |
| 61% 碰撞/险情发生在锚龄 >4 s | §V-B.4 |
| 18 个场景（14 个评测）、160 条指令 × 5 = 800 次飞行；RTK 仅用于标注与评测 | Table I；附录 A-D；§V-A.2 |
| 指令示例（意译） | §V-B.7 成功案例 |

## 自绘与示意

- 分层栈图为**自行绘制的示意**；接口层内的条形按 Table V 数值等比例绘制（SR 0–80、错误锁定 0–0.20，均从 0 起）。
- “+8.3”为 Table V 第一行与第五行之差，是我们的计算。

## 原文核对结论

通过（需缩窄展示）。L2 所列 Table V/VIII/X 数字与原文一致，P2→P3 改判成立：严格同栈只换目标接口。补充说明：L2 子卡写“正文给匹配结果 bootstrap/McNemar”，原文的检验针对与 SPF 的主对比（Table IV），Table V 接口消融本身没有区间或检验。画报限制栏已写明。数字均为论文报告，本项目未复现。
