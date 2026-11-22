# 2611.26613 AgentRoboCritic — 数字与断言映射

- 论文：arXiv 2611.26613v1（2026-11-19）。全文缓存 `research/fulltext/2611.26613.txt`。
- L2 记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-19.jsonl`（P3/confirmed/to_l3，capability，harness_effect_evaluation 主卡 + observe_act_interface 子查，new_bottleneck，material=full）。核对无判断错误，correction 0。

## 断言 → 原文映射

| 画报断言 | 原文位置 |
|---|---|
| 对 GPT-6 Astra 数值动作直控（无原语）做动作级批评，12 个操作基准 | 摘要 / §1 |
| 代理每动作随附局部意图 g_t（无意图工具调用被 harness 拒绝）；批评者见（任务 G、g_t、前后帧+提起帧）判结局与失败模式 | §3 方法 |
| 失败谱：Choice 仅 0.2%（任一基准 ≤3.3%）；Grasp 为 9/10 非触觉基准首位；3/5 Grasp 失败在闭合段（毫米级深度/侧偏）；空夹爪续行 9.5%；handover/release 1.5% | §4 失败分析 |
| 场景换谱：UniVTAC/OpenViTac → Alignment；RoboDojo 杂乱 → Interference；LIBERO-MAX/StaB → Incomplete motion | §4 |
| 49.8% 成功回合含 ≥1 局部失败（一半成功靠恢复达成）；1–2 局部失败仍 40.3% 成功 vs 无失败 75.1%；38.9% 失败 ≤10 动作内恢复、57.7% 至回合末；恢复率×官方 SR Pearson 0.81 | §4 恢复分析 |
| 恢复不对称：Incomplete/Grasp/Interference 大多可恢复，Alignment+Effect 仅 1/3 且加动作不缩差 | §4 |
| Table 1（400 动作人工金标，34% 成功/66% 失败）：Astra 结局 79.25%/κ0.497、失败模式 80.68%/κ0.600、综合 71.25%；Cost 列=测试集整体推理花费（美元）：Astra $26.06、Fable 5.2 $26.52；复检接受评注计入后与人工一致率 >90%（结局/失败模式均是）；Fable 5.2 78.25/72.73/71.00 | §5 Table 1 及其表注（Inference costs on the test set are reported in US dollars） |
| 去掉局部意图 → 25.25/25.00/24.50，多数标"不可验证"（同一动作依意图可读作未伸到/对歪/抓空）——意图使动作级批评良定义 | §5 Table 1 对照 |
| Muse-Glimmer-30B 在 12,844 标注动作微调（episode 级切分）：失败模式 32.58→74.24%、综合 34.75→67.75%；同一 400 动作测试集推理花费 $0.79（vs Astra $26.06，>30× 便宜） | §5 Table 1 |
| 边界：12,844 为自动标注、人工金标仅 400 动作；归因承袭批评者自身误差；恢复与归类统计无 CI | §5/§6 局限；L2 已记 |
| 画报示意：谱面（棋盘格+落子①–⑤）为自绘示意，落点位次无数据含义 | 自绘 |

## 展示缩窄

- Table 1 只列 Astra 与 Fable 5.2 两行、四指标；GPT-6.1 Sol（74.50/62.12）与开源未微调（32–63% 失败模式）未展开。
- 失败模式归类词表（七式）中"空夹爪续行 9.5%""handover 1.5%"为原文报告数值，其余各模式占比未逐条列出。
- $26.06/$0.79 原文按"每千动作"计（26.06/0.79 美元每条→千条放大），画报按原文口径标注。