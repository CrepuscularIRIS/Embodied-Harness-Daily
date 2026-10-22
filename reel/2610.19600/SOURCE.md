# SOURCE · 2610.19600

- 原文：Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System，arXiv **2610.19600v1**（2026-10-14），https://arxiv.org/abs/2610.19600
- 阅读材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2610.19600.txt`（html-full 全文+附录 A–L；私有缓存，不提交）
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl`（paper_id=2610.19600，batch b041，screen_score 88.75，supported_in_material / transfer）；入选：`reel/selection-opus.md` C3
- 核对：`reel/2610.19600/verify.md`（pass）
- 图形：全部为本刊据原文文字/表格自绘的示意（HTML/SVG），无原论文插图；未运行论文代码。

## 数字与断言 → 原文定位

| 画报位置 | 数字/断言 | 原文 |
|---|---|---|
| 标题/顶栏 | 原子任务 80%、长程 19%、20 个移动操作复合任务、100 集 | Abstract；§4.1；§4.2 |
| 顶栏参照 | 子任务独立 0.8 连乘平均 41.0% | Appendix H “Reference from error compounding” |
| ① | VLA 每次调用 350 控制步后交回规划器 | Appendix B.1 |
| ① | 3 次重规划恢复窗口；成功 19、失败 81 | §4.2；Appendix C.1 |
| ① 示例（抓取空抓→放置失败归因抓取） | 原文举例的示意化（具体子任务名为本刊示意） | §4.2；Appendix C.1 |
| ② | 取最早未恢复错误；仿真状态仅离线诊断 | §4.2；Appendix C.1 |
| ② | 3×Codex 候选 + 3 名人工；30 集 26 集一致，Fleiss κ=0.86 | §4.2；Appendix C.1；Table 5 |
| ② | 规划 17（21.0%）/导航与底盘 21（25.9%）/操作 43（53.1%） | Figure 2 说明；Table 11 行合计 |
| ③ 规划 | 技能卡（任务目标、子任务顺序、关键帧、完成判据），评测前固定；≤256 候选帧取 16 帧，仅过去观测 | §5.1–5.2；Appendix D.1–D.2；Table 7 |
| ③ 交接 | d≤0.75m 可达；0.75–1.00m 边缘 → approach_xy ≤0.25m 朝向不变；>1.00m → goto_stance，A*，栅格 0.05m，障碍膨胀 0.10m | §5.3；Appendix D.3；Table 7 |
| ③ 接触 | Grounding DINO+SAM，点云中位数，表面法向，单次 ≤0.30m | §5.3；Appendix D.3 |
| ③ 底栏 | 子任务 VLA 冻结、同一 checkpoint | §5；§6.1；Appendix B |
| ④ 恢复 | 技能卡 8（5/1/2）、记忆 7（4/1/2）、底盘 15（0/11/4）、末端 10（0/1/9）；episode 级非一一因果 | Appendix E.3；Table 10 |
| ④ 后移 | 完整系统 53 失败：规划 1/导航 5/操作 47；规划→操作 6、导航→操作 6 | Table 11；Appendix G |
| 结果左 | 留出 18%→49%，+31pp，95%CI[21,41]，p<0.001（n01=33,n10=2） | Table 1；Table 9 |
| 结果左 | 20 任务×5 留出 seed；同一 VLA；Kimi K3；planner/retry 预算匹配；官方评测器；McNemar+分层 bootstrap | §6.1；§6.3；Appendix E |
| 结果左 森林图 | +Demo 19→25 +6[0,12]；+Memory 25→29 +4[−2,10]；+Base 29→40 +11[3,19]；+EEF 40→47 +7[0,14] | Table 8 |
| 结果右 BEHAVIOR | π0.5 7、Harness VLA 14、Ours 37（/100；5 任务×20）；低层用 BEHAVIOR 数据重训 | Appendix I；Table 14 |
| 结果右 真机 | π0.5 4/20、agentic 基线 5/20、完整 13/20；分任务 2→6、3→7；500/300 条示范微调 π0.5 | Appendix J；Table 15 |
| 限制 1 | 不检查关节限位、IK、全身碰撞；剩余失败为错放、掉落、碰撞扰动 | §5.3；§6.2；Appendix G |
| 限制 2 | 开发集与诊断同一批 100 集；单组件 CI 含 0/贴近 0 | §6.1；Table 8–9 |
| 限制 3 | 额外模型（Gemini 3.5 Flash、Qwen3.8-27B、GDINO+SAM）开销未报告 | §5；Appendix D（无成本表）；本刊阅读判断 |

## 本刊阅读判断（非作者主张）
- “迁移的是干预设计，不是零样本策略迁移”“只证明本系统干预有效，不证明诊断驱动优于其他设计流程”——来自 Sol caveat 与本次核对。
- 真机/BEHAVIOR “未报告显著性/配对检验”——材料中无对应统计。
