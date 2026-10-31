# SOURCE · 2610.40016

- 论文：LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks，arXiv **2610.40016v1**（2026-10-29）
- 阅读原文：钉定缓存 `research/fulltext/2610.40016.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §II 相关工作与附录 A–B）。全文含 §II、附录 A（Algorithm 1–2）、附录 B（Table A1）补读自同版本 arXiv HTML `https://arxiv.org/html/2610.40016v1`（2026-10-31 取得，转换稿仅在 /tmp，不提交）。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-06.jsonl`（L2，P3 / confirmed / to_l3；F2,F0；capability）；入选：`selections/selection-006.md` #1。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-31）

通过，无 correction。L2 facts（π0.5 RoboTwin 干净 56→72、扰动 32→60，BiCoord 39→50、31→48；真机 12/30→17/30 且未注入扰动；消融去 Graph Gate 60→48、去依赖追踪 60→52、全量重规划 54、重复有效动作 0.2→1.6、去不确定处理 R 72→59）与原文一致。L2 Q2 已把开放点限定为“观察驱动的持续条件有效性＋保留后继计划”，并承认经典 plan monitoring/repair 在先，判断成立。

展示缩窄（不改判断）：
- 与三个改造基线的 P 差距只有 2–5 点（每格 100 回合、单次评测），画报写明“小差距”，不写“显著优于”。
- 去 State Gate / Node Gate 的具体数值只在 Fig. 5，正文无数，画报不画、只文字注明“也下降”。
- 真机 17/30 写明“未注入扰动”，不作为扰动恢复率。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 搭桥例：支座被碰移、已完成动作的支持失效；完成状态与支持有效性分开 | §I ¶1、¶3；Fig. 1 |
| 节点＝PDDL 算子；条件支持边、资源边；“因果”指 PDDL 条件支持 | §III-A；§III-B Task graph construction |
| State / Node / Graph Gate 的检查内容；证据不足补观察，最多 3 次，仍不定→UNRESOLVED 停止 | §III-C；§IV-A Implementation details |
| 局部修复：从 GOAL 经保留动作反推 g_rep → LAMA-first → VAL 验整条 → 扩大范围；不保证最小/完备 | §III-C Repair planning；附录 A-B Algorithm 2 |
| 每格 100 回合（10 任务 × 10 初态，各一次）；骨干逐任务微调；三个基线为 PDDL 改造版 | §IV-A；附录 B Table A1 |
| 六行 P 值（骨干 / 最好的改造基线 / LOGIV） | Table I |
| 干净设置三骨干平均 71.67→82.33、42.33→57.67 | §I 末段；§IV-B（由 Table I 复算一致） |
| 消融 P：60 / 48 / 52 / 54 / 57；去依赖追踪改动节点 24.6%、干净 72→61；重复有效动作 0.2→1.6；R 72→59（去不确定）、72→62（去 VAL） | §IV-C 正文 |
| 真机三任务计数、平台、同 checkpoint/示范/匹配布局、未注入扰动、作者归因与“区间宽” | §IV-A；Table II；§IV-B Real-world |
| 预算：GPT-4o 512 tokens/调用，每失败最多 3 轮修复、4 次 VLM 调用；规划 30 s、VAL 5 s | §IV-A Implementation details |
| 限制：扰动为每任务固定类型/触发点；R 分母各方法不同；无时延；作者自述限于所评任务 | §IV-A Evaluation metrics；§V |

## 自行绘制

- 机制图为据 Fig. 1 与 §III-B–C 重绘的示意（节点名、边标签为说明用），不是论文实验图。
- 点线图为按 Table I 数值绘制；“最好的改造基线”为我们逐格取三基线最大值。
