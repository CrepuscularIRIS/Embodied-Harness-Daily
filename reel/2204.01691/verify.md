# 2204.01691 核对记录（Opus 5.5 核对席）

- 论文：Do As I Can, Not As I Say: Grounding Language in Robotic Affordances（SayCan）
- 版本：arXiv 2204.01691v2（材料标注日期 2022-04-04；附录 A：v1→v2 加入 PaLM 结果、抽屉/CoT/多语言、LLM 规模消融）
- 材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2204.01691.txt`（FULLTEXT: html-full，正文 §1–§8 + 附录 A–E 全部覆盖；无 `_pdf.txt`，图像不可见，仅有图注文字）
- Sol 记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl`，paper_id=2204.01691，_batch=b044，screen_score 88.75，claim_support=supported_in_material

## 结论：核对通过（pass）

Sol 记录的 move / gap / 三条 evidence / caveat 均与原文一致，未发现需要退回的分数理由错误。

## 逐项核对

| 项 | 原文实际 | 定位 |
|---|---|---|
| 问题 | LLM 生成的计划语义合理但不适配机器人能力与当前场景（"用吸尘器"例） | §1、§3 Connecting LLMs to Robots |
| 实际改动 | 不做生成；对固定技能文本求 LLM 似然 p(ℓ|i)，乘以价值函数给出的当前状态完成概率 p(c|s,ℓ)，argmax 执行，追加到提示循环至 done | §3、Algorithm 1 |
| 任务/分母 | 101 条指令、7 个指令族；mock kitchen（技能训练环境）+ 真实办公厨房；15 物体、5 个位置 | §5、Table 1 |
| 模型 | PaLM 540B（消融：PaLM 8B/62B、FLAN 137B） | §5、Table 3、Table 7 |
| 指标 | 规划成功 = 3 名评审 2/3 认为技能序列能完成指令（不看执行）；执行成功 = 3 名评审看真机执行 2/3 通过 | §5 Metrics |
| 主结果 | mock 规划 84% / 执行 74%；真实厨房 81% / 60% | §5.1、Table 2 |
| 基线 | No VF（只取 LLM 最高分）规划 67%；Generative（生成后 USE 投影）规划 74%；BC NL 执行 0%；BC USE 执行 9% | Table 2 |
| 关键分族 | Embodiment（11 条）：SayCan 64% vs No VF 18% vs Gen 36%（规划） | Table 2 |
| LLM 替换 | FLAN-SayCan 规划 70% / 执行 61% | Table 3 |
| 错误归因 | 规划错误中 65% 来自 LLM、35% 来自 affordance；长程失败多为 LLM 过早终止 | §5.1、Fig. 25 图注 |
| 实现条件 | pick：BC 策略 + RL 价值函数，归一化 clamp((v−0.2)/(0.5−0.2))；go to/find：假设物体位置已知，按距离给分（d_max=100 m）；place：运动规划，affordance 恒为 1.0；terminate 恒为 0.1；已完成技能被封顶屏蔽 | Appendix D.2 |
| 留出性 | 技能在 mock 站迭代后"graduate"到真实厨房同协议评测再集成，真实厨房非独立留出 | Appendix C.3 |
| 作者自述限制 | 技能报高价值却实际失败时系统难以反应；只在当前决策步通过价值函数获得环境反馈 | §8、§5.2 Closed-Loop Planning |

## 与 Sol 记录的差异 / 补充（不改分，仅缩窄展示口径）

1. 无差异性错误。Sol 的 caveat"规划消融增益不能当执行增益"成立：No VF / Generative 在 Table 2 只有 Plan 列。
2. 补充：作者 §1 称"grounding 使性能接近翻倍"，在材料中无与之直接对应的同指标对照（规划 84% vs 67%/74% 不是翻倍；翻倍量级只出现在 Embodiment 族 64% vs 18%，n=11，或与 BC 基线比较）。画报不采用"翻倍"表述。
3. 补充：§5.1"相比 FLAN 错误减半"仅对规划错误近似成立（16% vs 30%），执行错误为 26% vs 39%。画报不采用。
4. 补充：附录 D.3 正文写 0 例时无终止要求成功率 54%，Table 5 为 52%，原文内部不一致；不影响主结论，画报不使用。
5. 增益在指令族间不均：Structured 族 SayCan 93% = No VF 93%、低于 Gen 100%；Long-Horizon 73% vs 67%/60%。增益主要集中在 Embodiment 族。
6. 材料中未见每条指令重复次数或置信区间（抽屉任务 Table 8 出现 0.17/0.83 等分数，主表无），统计不确定性无法评估。

## 画报展示口径

- 按"经典参照（2022）"呈现，不写成前沿。
- 结果只用 Table 2 规划成功率同条件三方对比（同 101 条、同 PaLM 540B、同评审规则），执行率单列并标注无去 VF 执行对照。
- Can 通道明确只有 pick 是学习得到的 affordance，导航/放置为启发式或常数。
- 机制图数值为示意，非原论文 Figure 8 读数。
