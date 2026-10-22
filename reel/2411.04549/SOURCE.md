# SOURCE · 2411.04549（GVL）

- 论文：Vision Language Models are In-Context Value Learners，arXiv **2411.04549v1**（2024-11-07）
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2411.04549.txt`（FULLTEXT: html-full，含正文 §1–§5 与附录 A–D；无 `_pdf.txt` 版本）。仅核对 v1；后续版本未读，画报只代表 v1。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3）；入选：`selections/selection-001.md` #2（验证信号）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过。L2 的问题陈述（顺序捷径）、facts（shuffle＋首帧锚点；同 VLM 去 shuffle 后成败 VOC 不可区分；one-shot P0.85/R0.70；open-drawer 与 remove-gears 加权下降）与原文一致。关键结果条件核实：主干 Gemini-1.5-Pro；成功检测为 6 个 ALOHA 仿真任务、每任务约 50% 成功率策略各 1000 条、VOC 阈值 0.5、对照 SuccessVQA 同样输入全视频；真机为 7 任务 × 10 次、DP 加权 vs 不加权（GVL one-shot 值）。

措辞小注（不退回）：L2 subcard 写“用过滤后训练和真实执行验证效用”。原文中“过滤后训练”（ACT）在仿真；真机验证是 AWR 加权，不是过滤。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 顺序输入时 VLM 输出单调上升值、忽视轨迹质量 | §1；§3 第 2 部分（Input observation shuffling） |
| 首帧作锚点不打乱，否则倒放视频也合理；其余帧随机打乱；自回归输出 | §3 式 (2)(3) |
| 统一抽 30 帧；输出 0–100 整数百分比；可加 in-context 示例 | §3 Practical implementation；式 (4) |
| VOC = 预测值排序与时间顺序的秩相关，−1 到 1 | §4 式 (5) |
| 去掉打乱：塌缩为少数线性上升曲线、VOC 被抬高、无法区分成败 | §4.3 Fig. 7 右；§4.4；附录 D Fig. 11 |
| 打乱：失败轨迹近均匀分布，成功与失败分布可区分 | §4.3 Fig. 7 左 文字 |
| 去掉自回归（单帧逐个问）RT-1 子集平均 VOC −0.08 vs GVL 0.74 | §4.4 |
| 成功检测 Table 2：GVL-SD one-shot 0.75/0.85/0.70；zero-shot 0.71/0.71/0.71；SuccessVQA 0.62/0.33/0.73；CoT 0.63/0.44/0.68 | §4.3 Table 2 |
| 6 个仿真任务、约 50% 策略、1000 条、阈值 0.5、SuccessVQA 同样喂全视频 | §4.3；附录 C |
| 过滤后 ACT（超参在纯成功子集上调好后固定）优于 SuccessVQA 过滤 | §4.3 Fig. 8 |
| 真机 AWR Table 3（GVL+DP / DP / VOC）：bowl-in-rack 7/6 0.57；banana 7/5 0.73；close-laptop 9/6.5 0.59；open-drawer 4/6 0.09；remove-gears 4.67/7 0.19；pen-handover 1.5/0 0.43；fold-dress 7/7 0.66 | §4.3 Table 3 |
| 7 任务 × 10 次；open-drawer、remove-gears 俯视视角分辨率不足致值噪声（作者解释） | §4.3 |
| VOC 适合非周期任务；擦拭、搅拌难判 | §5 Limitations |
| 低质量轨迹低 VOC 来自重复、重试、相机位置差 | §4 Evaluation metric |
| 附录另测 GPT-4o 主干 | 附录 B Table 5；附录 D Fig. 13 |

## 自绘与示意

- 顶部两条喂帧机制条为自绘示意（帧编号 17、4、25 为举例）。
- 两幅 VOC 直方图为**示意**：原文正文未给 Fig. 7 的各柱数值，形状仅依文字描述绘制，图下已注明不可读数。
- 真机点图数值逐项转录自 Table 3；按 VOC 降序排列是本画报的排序。4.67、1.5、6.5 等非整数原文未说明来源，画报已注明。
- 未运行论文代码，未复现实验。
