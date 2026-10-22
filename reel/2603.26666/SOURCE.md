# SOURCE · 2603.26666

- 论文：VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation，arXiv **2603.26666v1**（2026-03-27）
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2603.26666.txt`（FULLTEXT: html-full，Abstract、§1–§6 全文；无附录，无 `_pdf.txt` 版本）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3）；入选：`selections/selection-002.md` #4（在线蒸馏目标）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过，无 correction。L2 problem_statement、q3_loss、facts 与 subcard_checks（K605 三条）与原文一致：

- 目标对照：§4.4 “All ablation experiments are conducted with a fixed batch size of 32”；Fig. 4 为 RoboTwin2.0 Beat Block Hammer 单任务；Forward KL “success rate drops by more than 50% during early stages”，Hard CE 熵坍缩并停在最低平台，Reverse KL 熵有界、成功率最高最稳。
- LIBERO 48.9→87.4（+GRPO 93.4，教师 93.9）；RoboTwin 45.2→71.1（教师 74.0）；遗忘为 4 个留出任务（2 Object＋2 Spatial）的散点图。

展示缩窄（不退回）：

1. 原文“drops by more than 50%”未说明是相对还是绝对百分点，且 Fig. 4 无数值；画报写“下降超过 50%（原文措辞）”，不写成“掉一半”。
2. L2 写“师生共享动作表示”：原文 Algorithm 1 在同一 token a_t 上同时查询学生与教师 logits，隐含同一动作词表，但没有单独一句陈述；画报写作访问条件，不写成作者明示。
3. “1 条示范”只指学生初始化；教师 SimpleVLA-RL 已经过 RL 训练，其成本不在学生数据量里。画报在边界中注明。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 学生 1-traj SFT 初始化、on-policy 采样 G 条轨迹、教师冻结只给 logits 不执行、逐 token 反向 KL 奖励 r_t、组内平均策略梯度、不用结果奖励 | §3.1 Algorithm 1；§3.2–3.4 式 (5)(6)(7) |
| 前向 KL mode-covering → 熵爆炸；硬 CE（标准 DAgger）丢弃软概率 → 熵过早坍缩；反向 KL zero-forcing → 有界 mode-seeking | §3.4 “Theoretical Analysis”；§5.1 |
| Beat Block Hammer、批 32、FKL 早期成功率下降逾 50%、Hard CE 最低平台、RKL 最高最稳；熵：FKL 爆炸、Hard CE 坍缩、RKL 有界 | §4.4 第 1 项；Fig. 4(a)(b) |
| LIBERO 四套件逐项：学生 63.6/54.9/59.6/17.3（均 48.9）、只蒸馏 84.3/93.8/92.5/78.9（87.4）、＋GRPO 93.4/95.3/94.5/90.2（93.4）、教师 94.2/96.1/94.6/90.7（93.9） | Table 2 |
| 50-traj 全量基线 Octo 75.1、OpenVLA 76.5、π0+FAST 85.5、Nora 87.9 | Table 2 |
| 批 64、G=8（主实验，沿用 SimpleVLA-RL） | §4.2 首段 |
| LIBERO-Long 约 50 步近 80%，GRPO 需 150 步以上（3×） | §4.2；Fig. 2(b) 图注 |
| RoboTwin 四任务：学生 29.7/77.3/33.1/40.6（45.2）、只蒸馏 66.4/90.6/52.3/75.0（71.1）、教师 68.3/94.2/57.8/75.8（74.0）；π0 50.5、RDT 32.0；1000 demos/task 初始化 | Table 3；§4.2 |
| 遗忘：4 个留出任务；离线 SFT 留出任务坍塌（Object 接近 0），RL 与 OPD 大体保持；仅散点图 | §4.3；Fig. 3 |
| 教师 SimpleVLA-RL、学生 OpenVLA-OFT、离线 SFT 基线用全量数据 | §4.1 |
| 依赖特定教师模型（作者 future work） | §6 |

## 自绘与示意

- 中部 (a) 成功率 / (b) 熵两幅曲线为本画报依据 §3.4 与 §4.4 文字绘制的**示意**，图内已标注；纵轴无刻度，曲线形状不是 Fig. 4 原始数据。
- 下部哑铃图按 Table 2/3 数值以 0–100 线性刻度重绘，不是原图。
- 未运行论文代码，未复现实验。
