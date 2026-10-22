# SOURCE · 2610.25114

- 论文：Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds，arXiv **2610.25114v1**（2026-10-18）
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2610.25114.txt`（FULLTEXT: html-full，含正文 §1–§10 与附录 A–F；无 `_pdf.txt` 版本）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3）；入选：`selections/selection-001.md` #3（自我改进归因）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过。L2 facts（8/8、R−C 10.2、I−C 8.7、R−I 1.5、p=.125；148/150、147/150；$384/7≈$55、$278、366 slot-hours）与原文一致；subcard_checks 的限定（全仿真、无正式直接控制基线、三 lineage 仅单任务 3 次、继承组保留自身练习）均有原文依据。

展示边界：标题已限定“仿真 · 单任务 · 3 个 campaign”。“尝试选择”不是第二实验的差值成分（三条谱系共享选择规则，§7.4），画报将其单列并引用第一实验的 best-of-k 结果，未把它画成第三个数值柱。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 三成分定义：selection / inheritance / development feedback；三谱系 rewrite、inherit-only、repair；差值含义 | §3.3 |
| R0 两份初稿、R1 ≤10 轮、冻结哈希、R2 冻结后抽 100 布局、≥95 且 0 安全中止、R3 复用 | §3.3、§4、§5、Table 12 |
| RoboTwin 2.0、aloha-agilex、clutter（≤10 干扰物）、RTX 5090 | §4、§6 |
| 主作者 Claude Code 2.1.284（claude-opus-5-5）；Codex CLI 0.160.0（gpt-6-astra）5 campaign 无对照 | §6；§7.5 |
| 第二实验：stack_bowls_three、3 campaign、45 隐藏验证布局、轮数匹配、预注册 2026-10-10 | §4；§7.4；附录 E |
| R−C +10.2（15.8/6.3/8.5）；I−C +8.7（12.5/5.3/8.4）；R−I +1.5（3.2/1.0/0.1）；均 3/3 同号，单侧 p=0.125，不称显著 | §7.4 Tables 7–8 |
| 继承组保留自身练习、知道是否替换（1 比特）、单任务单作者产品 | §4；§9 |
| best-of-k Learn(k)：−2,+2,+1,+2,+0,+0,+7,+2；隐藏集最佳版本 repair 5 / control 3；重写方差 4/45–44/45；“可靠性而非更高上限” | §7.4 |
| 第一实验 8/8、p=0.004、每轮平均 +6.4 布局；比较中含保留起点的优势 | §7.4 Table 6；§4 |
| 复用：3 技能 × 50 布局；纯代码 148/150（98.7%，95.3–99.6）；DeepSeek-flash 147/150（98.0%，94.3–99.3）；200 次决策 0 无效；逐技能表与中止 | §7.6 Table 9 |
| 调用者 $0.00028–0.00054/回合；$384/20 campaign → $55/冻结技能；第二实验 $278；366 slot-hours 未计价；无正式直接控制基线 | §7.7；§5 |
| 7/20 campaign 冻结、4/7 任务、$4.29–8.22；5/7 来自初稿 | Abstract；§7.1 |
| write-once：默认减 write-once 验证基线 −3.4 分（p=0.77）；最小可检出约 14 分 | §7.3 |
| stack_bowls_three 0/9、成功 78–95、中止 3–16/100；128 开发布局 3 次仍未过 | Abstract；§7.1–7.2；Table 3 |
| 0 中止/100 回合只能界定到 3.6% | §7.2 |
| 仅仿真、无真机、3 技能 1 调用者 | §8 Threats；§9 |

## 自绘与示意

- 顶部流程条为自绘示意。
- 瀑布图柱值与点值转录自 Tables 7–8，不是论文原图。R−I 三个单 campaign 值（已四舍五入）平均为 1.43，原文报告 +1.5（应为未舍入值的均值），画报按原文并在页脚注明。
- 未运行论文代码，未复现实验。
