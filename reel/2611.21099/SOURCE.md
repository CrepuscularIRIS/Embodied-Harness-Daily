# SOURCE — 2611.21099 ForceHarness

## 论文信息
- 标题：ForceHarness: Force-Grounding API-Only Frontier Models for Contact-Rich Manipulation（按 L2 记录题意转写）
- arXiv 2611.21099v1（2026-11-16 提交）。
- 阅读原文：research/fulltext/2611.21099.txt（FULLTEXT html 完整缓存）。
- 初筛记录：research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-16.jsonl（P3/confirmed/to_l3，卡 observe_act_interface + external_verification_control）。

## 核对结论
逐节与 L2 记录核对一致，无实质错误；corrections：0。

## 海报数字与断言映射（poster 区块 → 原文位置）
| 海报内容 | 原文出处 |
| --- | --- |
| 01 真机 FR3 无腕力传感器，6 任务 × 10 ep：Astra 直出 2/60（3.3%）→ ForceHarness 54/60（90%）；Sol 47/60 | 表 3 |
| 01 分任务：wipe 1→8、screw 0→9、peel 1→9、USB 0→8、bottles 0→10、soft/hard 0→10（各 /10） | 表 3 分任务行 |
| 02 三层：力标定（腕 F/T 或关节扭矩反解 w=(Jᵀ)⁺τ_ext；tare-at-rest/settle-read/report-changes）；12 个自终止力原语 5 组（move_until_contact/push/slide/search/insert/wiggle/screw/press_turn/lift/pull 等），导抗控制 v=clip(k·f(F_d−F_u))；物理翻译（质量 m=\|F̄z\|/g、摩擦 μ=\|F̄t\|/F̄n 带 σ 传播，无任务阈值） | §III 与图 2 |
| 03 真机六任务表（同表 3 分任务数字） | 表 3 |
| 04 ForceBench（10 seeds）：Astra 70.0→87.5、Sol 65.0→87.5、Fable 75.0、最强训练策略 35.31；Drawer Pull 0/10→10/10 为主要分离点 | 表 4 |
| 05 HiddenPhys（7 任务 × 20 seeds，各藏一物理变量 Weight/CoM/Wipe/Stack/Peg/Latch/Lock）：Astra＋FH 135/140（96.4%，0 damage）；专家 136/140；Astra 直出 87/140；训练策略 65–83/140，damage DP 20/π0.5 24/ForceVLA 29 | 表 5 |
| 05 分布偏移（4 任务 80 trials）：FH 75→69 对专家 77→68；训练策略 −17%~25% | 表 5 shift 段 |
| 06 反馈形式消融（小模型，同 primitives/seeds）：raw success 0.63/decision 0.57；L2 0.70/0.70；decision 0.70/0.85（p=0.023）；Sol raw/decision 已 1.00；one-shot CaP 23%→77%，逐 turn 91% | 表 6 与 §V 消融 |
| 07 “接触快于决策→闭环必须下沉到非模型层”的判断重述 | §I 问题设定＋§VI 讨论 |

## 示意图标注
- 04 区 ForceBench 条形为按表 4 数字重绘（示意）。

## 展示缩窄（非 correction，仅记录）
ForceBench 8/10 seeds 用过该基准调参（两任务事后修订）存在调参泄漏，evaluator 缺 release/clearance 检查；真机 instructions 含过程性提示（soft/hard 除外）；handle damage 0 非完备安全（只统计把手类）；训练策略基线无同款 guard，damage 对比非同条件；12 原语为人工模板，覆盖接触类任务；物理翻译假设准静态，动态接触未验证。
