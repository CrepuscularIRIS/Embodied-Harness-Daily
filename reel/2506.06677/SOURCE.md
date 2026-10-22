# SOURCE · 2506.06677

- 论文：RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation，arXiv **2506.06677v2**
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2506.06677.txt`（FULLTEXT: html-full，Abstract、§1–§6、附录 A.1–A.9 全部读过；图仅有图注）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3，F1/F0）；入选：`selections/selection-002.md` #7（分层归因诊断）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过，不退回。L2 问题陈述、q3_loss、subcard_checks（K802 holds/partial/holds）与原文一致：固定微调 OpenVLA（§5.1），anchor 统一子目标切换（§5.1），60 任务 × 10 次 = 600 rollouts（§5.1），GPT-4o 16.04 / Blind 15.10 / GT-plan 25.16（Table 4），SFT Qwen Acc_C 66.83 但 SR 9.33（Table 5）。

措辞小注（不影响判断）：
1. SR 按式 1 定义为每个任务关键状态转移满足比例的平均（部分得分），不是二元成功率；L2 写“闭环成功”，画报统一写“SR＝关键状态转移完成比例”。
2. Table 3 图注写“over 10 rollouts for each method”，与 §5.1 “600 rollouts (60 tasks × 10 trials)” 表述不一；画报采用 §5.1。
3. Table 5 中 SFT Qwen 的计划匹配率 Acc_P 也最低（30.00），故“观察分高、成功低”混有计划质量因素；画报标为描述性对照。
4. Table 4 的 GPT-4o 行（16.04，各子任务数值）与 Table 3 的 Planner+OpenVLA* 行完全相同，即一次性规划设置。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 固定低层：100 个训练任务实例拆成单步微调 OpenVLA（OpenVLA*） | §5.1 System 1 Models |
| anchor 点决定子目标切换，与规划模型解耦 | §5.1 Evaluation Protocol |
| 600 rollouts＝60 任务 × 10 次 | §5.1 |
| System 2 三类：预训练 VLM、Blind（关闭视觉）、SFT VLM | §5.1 System 2 Models |
| SR 定义（关键状态转移比例） | §3.4 式 1 |
| GT-plan 25.16、GPT-4o 16.04、GPT-4o-Blind 15.10、Qwen2.5-VL-Blind 11.87、Qwen2.5-VL 11.19 | Table 4 |
| “GPT-4o 与 GT-plan 差 9% 以上，归因于缺少环境交互与视觉域差” | §5.3 正文 |
| OpenVLA*（无规划器）4.57；分层框架 16.55；Planner+OpenVLA* 16.04 | Table 3 |
| Acc_P / Acc_C / SR：GPT-4o 68.33/32.66/16.04；Blind 61.37/0.00/15.10；LLaVA-Next-Video-7B 40.00/37.19/11.37；Qwen2.5-VL-7B 44.67/47.74/11.19；Qwen2.5-VL-7B-SFT 30.00/66.83/9.33 | Table 5 |
| π0-fast：GT-plan 23.04、GPT-4o 15.15、GPT-4o-Blind 13.63 | 附录 A.2 Table 6 |
| 局限：仅仿真（LIBERO）、GPT 生成任务、System1–2 交互有限 | §3.2；§6 Limitations |

## 本画报计算 / 自绘

- 漏斗各层差值（−74.84、−9.12、−0.94、−10.53）为原文均值相减；“约 3/4”由 100−25.16 得出。原文未报方差或区间。
- 漏斗外形为示意，条宽按 SR 等比例（5.6 px / 百分点）。π0-fast 条形图按 Table 4/6 数值重绘。
- “SR 排序更接近计划匹配率”为本画报对 Table 5 五个点的阅读，已在画报标注“我们的阅读”，不是原文结论。
- 未运行论文代码，未复现实验。
