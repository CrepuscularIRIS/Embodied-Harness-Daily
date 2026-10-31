# SOURCE · 2610.37378

- 论文：VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning，arXiv **2610.37378v1**（2026-10-27）
- 阅读原文：钉定缓存 `research/fulltext/2610.37378.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §II 与附录 -A–-D）。全文含 §II 与附录 -A–-D 补读自同版本 arXiv HTML `https://arxiv.org/html/2610.37378v1`（2026-10-31 取得，转换稿仅在 /tmp，不提交）。selection-005 已读正文全文，本期补齐附录。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-05.jsonl`（L2，P3 / confirmed / to_l3；F0,F4；capability）；selection-005 多样性截断、列第一备选；入选：`selections/selection-006.md` #3。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-31）

通过，无 correction。L2 facts（六设置平均 52.8% vs VLSA 最强 23.7%；去蒸馏 14% vs 63%；逐步对齐 30% vs 63%；真机每任务/场景 15 次、碰撞 20–40%、成功 47–60%；每 seed 约 82.3M 转移）与原文一致，六设置平均由 Table I 复算一致。附录补读要点：Stem 输出全部可执行动作（-A1）、约 4.56M 参数（-A2）；VLSA 实现不估计障碍速度、仅瞬时几何（-D3 Dynamic Obstacle Handling），Stem 障碍输入同样无速度（-A1 11 维/槽）。

收录范围：冻结 VLA 作为被调用的策略、外加执行控制层，与 s003 入选的 Backtrack（2610.32941，冻结 VLA＋轻量回走模块）同口径；与 C005-1（36852，冻结 RL 步行策略、无 VLA/VLM）及 37547（冻结 ACT）不同。

展示缩窄（不改判断）：
- 不写“零训练成本”“即插即用”：画报标注每 seed 约 82.3M 仿真转移、逐任务训练、消融各需重训。
- 真机只写作者文字给出的区间，不读图估逐格数。
- “去参考”消融注明同时去输入与奖励、分不开二者。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| π0.5 PickCube 无障碍 71.66%，静态 3.25%、动态 1.31% | Table I；§IV-B1 |
| 两条常见路线（避障示范微调、CBF 逐步修正）的问题 | §I ¶4；§IV-B1 Safety–Task Trade-off |
| 每 8 步一个动作块、换算成相对末端位姿参考；Stem 输入（参考 8×8、本体 16 维、障碍 ≤3×11 维）、输出全部动作、无视觉 | §III-A；附录 -A1、-A2 |
| 段距离奖励、段索引只前进、允许绕行与等待 | §III-B；附录 -C |
| 教师多看目标物体位置、学生 PPO＋0.1·KL；课程三阶段；38.0＋23.7＋20.6M 转移/seed | §III-C–D；§IV-A Training details；附录 -B2–B3 Table VI |
| Normal：73.3/70.6/75.2 vs 71.7/61.4/74.5 | Table I |
| 参考偏移干预：15–20 cm，每方向 30 对，88/90 更贴近改后参考，成功 60–70% | §IV-B2；Fig. 4 |
| VLA 避障微调 RRT 示范、1,500 条最好、胡萝卜抓取失手 | §IV-A；§IV-B1；附录 -D2 |
| 散点 30 点（5 方法 × 6 设置）与六设置平均 52.8/23.3/23.7/17.1/6.1 | Table I（平均由我们算） |
| PickCube-静态：VLSA-ARM COLL 22.53% / SUCC 15.16% vs Stem 23.16% / 52.19% | Table I；§IV-B1 |
| 同 checkpoint、真值障碍、VLSA 每设置验证回合调参；每设置 3,200 回合 | §IV-A；附录 -D3 Parameter Tuning |
| VLSA 失败原因与“低碰撞来自早失败” | §IV-B1 |
| 消融：逐步对齐 30% vs 63%（静态 COLL 3.66%、SUCC 47.78%）；去蒸馏 14% vs 63%、碰撞 37% vs 15%；去参考 PickCube 全 0 | Tables II–IV；§IV-B2 |
| 真机：UR7e、两任务、15 次/任务/场景、50 条遥操作、AprilTag＋D455、区间 73–100%→20–40%、0–20%→47–60% | §IV-C；Fig. 5 |
| 限制：低维框、真值/AprilTag、无接触力安全、碰撞 8–34%、无形式保证 | §IV-C；§V；Table I |

## 自行绘制

- 机制图左侧场景为假想示意（非论文实验轨迹），右侧流程据 Fig. 2 与 §III、附录重绘。
- 散点按 Table I 数值绘制；“每任务各训一遍”依据 §IV-A（三任务同一流程）与 §IV-B2（消融在单任务上重训）的阅读判断。
