# SOURCE · 2311.13373 LLM4Teach

- 论文：Large Language Model as a Policy Teacher for Training Reinforcement Learning Agents，arXiv 2311.13373v6（首版 2023-11-22）。
- 阅读材料：本地完整 HTML 全文缓存 `research/fulltext/review-runs/embodied-v22-20261021-01/materials/2311.13373.txt`（含附录 A.1–A.8；无单独 `_pdf.txt`）。全文不提交。
- 初筛/评分记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 confirmed，to_l3）；选题理由：`selections/selection-001.md` 第 7 条。
- 规则版本：problem-core-v1.1。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 学生 0.77 vs 教师 0.52（ColoredDoorKey 平均回报） | §4.1.2 正文，对应 Fig.3 |
| 红钥匙/蓝钥匙/蓝门的 LLM 错误例子 | §4.1.2 |
| 从零 PPO 成功率 1.9–10.1%；五任务四方法的回报/成功率表 | 附录 A.6 Table 3（MiniGrid 1000 次测试，Habitat 100 次） |
| ColoredDoorKey 教师在 Table 3 为 0.40 / 46.8% | Table 3（与正文 0.52 不一致，画报两者都标出处） |
| 分层 RL 需 >10,000 次迭代 | §4.1.2 |
| 损失 L = L_RL + λ·H(π_T‖π_θ)；软指令由多次查询估计 | §3.2 Eq.(1)，§3.3 Eq.(2)–(3)，Algorithm 1 |
| λ 日程 λ₀=10、λ_c=0.1、i₁=1000、i₂=2000；仅阶梯日程成功；退出后短期策略振荡 | 附录 A.7，Fig.7（ColoredDoorKey） |
| 学生 24K vs 教师 130B；ChatGLM-turbo | §5，§4.1.1 |
| 同一学生网络/损失；分层 RL 共享 options | §4.0.2，§4.2.1 |
| 只有 4 个 MiniGrid + 1 个 Habitat Nav&Pick | §4.1.1，§4.2.1 |

## 自绘与示意

- 训练阶段曲线为**自行绘制的示意**，形状不是原文 Fig.3 数据；只有 λ 日程参数与标注框数值来自原文。画报上已标“示意”。
- 阶段命名（教师主导/弱指导/教师退出）是我们的阅读归纳，对应 Eq.(3) 三段。

## 原文核对结论

通过（需缩窄展示）。L2 的问题、q1–q4 与关键事实与原文一致。展示时补两点：
1. 同 options 的分层 RL 最终回报接近或高于学生（DivergedDoorKey 0.59 vs 0.53），反超对象是 LLM 教师而非所有基线，收益主要是样本效率。
2. 正文与附录对教师 ColoredDoorKey 回报不一致（0.52 vs 0.40）。

数字均为论文报告，本项目未复现。
