# SOURCE · 2611.06863

- 论文：Rethinking Self-Repair in Code-as-Policy Agents: What Drives Retry Success?，arXiv **2611.06863v1**（2026-11-04；Siddharth Aphale、Ayushman Singh）
- 阅读原文：钉定缓存 `research/fulltext/2611.06863.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §2 相关工作与附录 A–D）。§2 与附录 A–D 补读自同版本 arXiv HTML `https://arxiv.org/html/2611.06863v1`（2026-11-05 取得，转换稿仅在 /tmp，不提交）。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-09.jsonl`（L2，P3 / confirmed / to_l3；F1,F2；judgment）；入选：`selections/selection-009.md` #1。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-11-05）

通过，无 correction。L2 facts（252 失败 Compiled 85.3 / Resample 68.3，+17.1 [9.9, 24.2]；对 Different-Label 与 Fixed Task Template 均 −0.8；Static-from-Start 92.4 vs 89.6、Holm p = 0.13；nut insertion −15 pp）与原文一致。

L2 记“Different-Label 的 fallback 比例未在缓存附录展开”：附录 B.3 写明主评测所选 627 条记录**全部**与对应观测失败标签不同（无 fallback），此材料加强对照，不改档位。附录 A.3 另记：Fixed Task Template 在开发集选定，首次留出比较属探索性；生成指令中性化后才做主评测；泛化问题在核心结果后修订（该研究的设定与分析在生成前固定）；失败标签只在脚本故障上审计。均写入画报限制栏。

展示缩窄：标题只说“不一定来自读懂这次失败”“点估计相同”，不说等效；第 5 行（看旧程序改写）与“第一次就给”都注明同时改了生成指令。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 冻结 Qwen2.5-Coder-7B、robosuite Panda、特权状态、无图像、每次重置原场景、最多 5 次重试 | §3.1；附录 A.1 |
| 252 评测失败 / 40 开发失败，初始程序按 hash 区分；159 个组合中 24 个与开发共享 | §3.1；附录 A.1、A.3 |
| 14 标签规则判定 → MUST/NEVER 模板，逐次累积、最新在前、去重、长度上限 | §3.2；附录 B.1；表 1 |
| 解码参数、768 词反馈上限 | 附录 A.2 |
| 五种条件的提示词组成 | §3.3；附录 B.3 表 A2 |
| 恢复率 68.3 / 85.3 / 86.1 / 86.1 / 21.4 | §4.1–4.2、§4.4；表 2 |
| 627 条选中记录全部标签不同 | 附录 B.3 |
| 配对差值与区间 +17.1 [+9.9, +24.2]、−0.8 [−6.3, +4.8]、−0.8 [−6.7, +5.2]、+63.9 [+56.7, +70.6] | 表 2 |
| 固定 token 预算 +15.9（2,000）/ +14.7（5,000） | §4.1 |
| Reflection 56.0 vs 同期 Resample 70.6；Reflection Repair 25.0、Direct+Compiled 21.4 vs Compiled 89.7（原指令） | §4.4；附录 C.1 |
| 700 新场景：首轮 19.3 / 36.9；总成功 73.1 / 89.6 / 90.1 / 92.4；token/成功 3,623 / 2,578 / 2,564 / 2,087 | §4.3；附录表 A4 |
| “靠重试补上”的浅色段 = 总成功 − 首轮成功（53.8 / 70.3 / 70.8 / 55.5） | **由表 A4 两列相减**，原文未直接列 |
| Static-from-Start 对 Compiled +2.9 [0.0, +5.7]，Holm p = 0.13 | 附录 C.2 |
| nut insertion 82.5 vs 97.5（n = 40），−15.0 [−27.5, −2.5]；Other-Episode 62.5 | §4.5；附录 C.3 |
| 温度 0.2 抬起位姿偏移 −19.6（90% CI [−28.6, −10.7]） | §4.5；附录 C.3 |
| 32B 堆叠 52/55 两法相同 | §4.5；附录 C.3 |
| 7 设定 354 失败：+18.1 [+13.3, +22.9]；对 Other-Episode +2.3 [−1.1, +5.6] | §4.5；附录 C.3 |
| DeepSeek-Coder-6.7B、开门任务低于纳入门槛 | 附录 C.3 |
| 评测清单五条 | §5、§6 |
| 限制栏各条 | §6；附录 A.3 |

## 自绘与示意

- 第 1 区的提示词色块为自绘示意（只示意组成，不是原文图）；柱长、第 3 区堆叠条按原文数值绘制。未使用原文图片。
- “读法 / 判读”标签为我们的阅读判断。未运行论文代码，未复现实验。
