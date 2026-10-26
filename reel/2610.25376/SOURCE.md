# SOURCE · 2610.25376

- 论文：TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models，arXiv **2610.25376v1**（2026-10-18）
- 阅读原文：钉定缓存 `research/fulltext/2610.25376.txt`（头标 `FULLTEXT: html`、v1；实为 core 裁剪版：引言含 `[...]`，缺相关工作、附录、Fig. 3/4 数值与 Table 2/6 数值）。附录与表格数值补读自同版本 arXiv HTML `https://arxiv.org/html/2610.25376v1`（附录 A–C、Tables 1–15）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-02.jsonl`（L2，P3 / confirmed / to_l3；F3,F2；capability）；入选：`selections/selection-003.md` #1。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-26）

通过，无 correction。L2 facts（共享 30 回合池；12 错误状态 4/5/5/8/9；Table 3 额外人工示范 29.2/54.6/48.3 vs AutoDAgger 63.9/80.6/69.2；4.14× 为得分倍数；2.23–2.60× 为接管后恢复用时比）与原文一致。

材料补充（不改 L2 判断，只缩小 L2 所记缺口）：
- 附录 B.1 Table 11：真机 20 条 rollout（学生 10、教师 10）人工判定结局，监控系统准确 85%、P 88.9%、R 80%。这是回合结局判别，仍不是接管时机的误报/漏报，L2 关于“真机时序触发误报、漏报和延迟未报告”的判断成立。
- 附录 Table 12–15 给出按试次 bootstrap 的 96% 区间（非训练种子方差），L2“未报告训练种子方差”成立。
- 附录 A.1：学生自行完成的回合也被丢弃；学生/教师 T_fail 分别为 6/14、3/8、2/6 s。
- 表号差异：缓存正文把恢复评测与数据规模写作 “Table 2”，HTML 中分别为 Table 1、Table 2；跨架构与监控验证在 HTML 中为 Table 5、Table 6。画报按 HTML 表号标注。

展示边界：标题标注“真机 3 任务 · 单轮采集”；“最高 4.1×”明确为细粒度得分；“2× 更快”限定为接管后恢复段；跨架构只写 LIBERO 仿真。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| OPD 只在学生状态给教师标签、教师动作不被执行、看不到后续状态 | §1；§3.4 |
| Robometer 不做任务微调；每 ≥1 s 监控；ε_p=0.05、θ_s=0.5；T_fail 学生 2–6 s；T_succ 判恢复成功；恢复失败丢弃；学生完成的回合丢弃 | §3.3 Eqs. 4–6；附录 A.1、Table 7 |
| 学生：π0.5 同结构、PaliGemma 初始化、动作专家从零、无动作预训练；动作空间蒸馏 | §4.1；§3.4 Eqs. 7–9 |
| AgileX PiperX；示范 200/100/100；测试 12/27/30 次；共享 30 条 AutoDAgger 回合池 | §4.1；附录 A.2 |
| 七种方法三任务得分及 96% 区间（教师、BC、离线蒸馏、OPD、恢复 BC、恢复蒸馏、TILDE） | 附录 Table 12（对应 Fig. 3、Fig. 4）；方法定义附录 Table 10 |
| 3.07× / 2.18× / 4.14×；摘要“up to 4.1×” | §4.2；Abstract |
| 得分为分阶段 0/0.5/1 平均×100 | 附录 A.2 |
| 12 个错误状态：教师 9、TILDE 8、OPD 5、离线蒸馏 5、BC 4 | §4.3；HTML Table 1 |
| 同额外 30 回合：人类示范 vs AutoDAgger（蒸馏/不蒸馏两组） | §4.3 Table 3；附录 Table 13 |
| 叠毛巾 30/60/90 回合：63.9 → 65.3 → 77.8；教师 87.5 | §4.3；HTML Table 2 |
| HG-DAgger vs AutoDAgger：恢复用时、恢复成功率、下游得分 | §4.3 Table 4；附录 Tables 14–15 |
| 真机门控 85% / P 88.9% / R 80%；LIBERO-10 recall 0.841 | 附录 B.1 Table 11；HTML Table 6 |
| SmolVLA 学生 LIBERO-10：64.6% → 79.6% | §4.3；HTML Table 5 |
| 单轮采集、依赖监控与教师可恢复性、任务范围有限 | 附录 C |

## 自绘与示意

- 顶部“三种状态分布”路径图为自绘示意，非原文 Fig. 1。
- 点图、12 格方块与柱图由原表数值重绘；方块只表示成功个数，不对应具体错误状态（原文未逐状态列出）。
- 未运行论文代码，未复现实验。
