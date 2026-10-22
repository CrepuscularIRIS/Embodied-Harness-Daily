# SOURCE · 2204.01691（SayCan）

- 版本：arXiv 2204.01691v2（材料标注 2022-04-04），https://arxiv.org/abs/2204.01691
- 读取材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2204.01691.txt`（html-full，正文+附录 A–E；私有缓存，不提交）
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl` paper_id=2204.01691（_batch b044，screen_score 88.75，claim_support=supported_in_material）
- 核对记录：`reel/2204.01691/verify.md`（Opus 5.5，pass）
- 呈现定位：经典参照（2022），非 2026 前沿。

## 画报断言 → 原文定位

| 画报内容 | 原文 | 定位 |
|---|---|---|
| “用吸尘器”式合理但不可执行的回答；LLM 不知道机器人能力和当前状态 | "You could try using a vacuum cleaner" is impossible if there is no vacuum... | §1 |
| 对固定技能文本打分 × 当前状态完成概率，argmax 执行，追加后循环至 done | p(c_i|i,s,ℓ_π) ∝ p(c_π|s,ℓ_π)p(ℓ_π|i)；Algorithm 1 | §3 |
| 指令示例 “I spilled my coke, can you bring me something to clean it up?” | Crowd-Sourced 族指令 | 附录 E.1 Table 6 |
| 提示含 17 个示例 | "the prompt used in this work, Listing 1, involved 17 examples" | 附录 D.3 |
| Can 输入为 RGB 观测 | "policies trained from an RGB observation" | §5 Fig. 6 图注 |
| pick：BC 执行 + RL 价值函数，clamp((v−0.2)/(0.5−0.2)) | v_max=0.5, v_min=0.2 | 附录 D.2 |
| find/go to：假设物体位置已知，按距离，d_max=100 m | "we assume the location of objects are known"；d_max=100, d_min=0 | 附录 D.2 |
| put down：运动规划；可行性恒 1.0 | "We assume place is always possible" | 附录 D.2 |
| done：可行性 0.1 | p_terminate=0.1 | 附录 D.2 |
| 已完成技能封顶屏蔽 | "set a cap for the affordances indicating that the skill has been completed" | 附录 D.2 |
| 101 条指令、7 个指令族；Embodiment 11 条、Long-Horizon 15 条 | Table 1 | §5 |
| PaLM 540B | "The LLM used is 540B PaLM" | §5 |
| 规划成功 = 3 名评审 2/3 认为计划可完成指令，不看执行 | Metrics | §5 |
| 全部：SayCan 84% / No VF 67% / Generative 74%（规划） | Total 行 | Table 2 |
| Embodiment：64% / 18% / 36%（规划） | Embodiment 行 | Table 2 |
| Long-Horizon：73% / 67% / 60%（规划） | Long-Horizon 行 | Table 2 |
| 执行：mock 74%；真实厨房 60%（规划 81%） | Mock Kitchen / Kitchen 列 | Table 2、§5.1 |
| BC NL 0%、BC USE 9%（执行） | No LLM 列 Total | Table 2 |
| No VF / Generative 只有规划列 | 表头 "No Affordance … Plan Plan" | Table 2 |
| 限制：技能报高价值却失败时难以反应 | "not easily able to react to situations where individual skills fail despite reporting a high value" | §8 |
| 只在当前决策步通过价值函数得到环境反馈 | Closed-Loop Planning 段 | §5.2 |
| 真实厨房参与技能 graduate 评测 | "graduated to the same evaluation protocol in the real kitchen, and then integrated into SayCan" | 附录 C.3 |
| 65% LLM 错误 / 35% affordance 错误；长程多为过早终止 | §5.1；Fig. 25 图注 | §5.1、附录 E.6 |
| 未见重复次数/置信区间 | 本刊阅读判断（材料中未找到） | — |

## 自绘与示意

- 机制图（双通道汇合）：结构依 §3、Algorithm 1、Fig. 5 图注重绘；五个候选技能的 Say/Can/乘积数值（0.38/0.41/0.12/0.06/0.03；0.92/0.05/0.90/0.95/0.10）为**说明用虚构示意值**，非原文 Figure 8 读数。
- 结果条形图：数值全部取自 Table 2，由本刊重绘。
- 无原论文插图（材料为纯文本缓存）。

## 未采用的作者表述

- §1 “grounding 使性能接近翻倍”：材料中无同指标的直接对应对照，未采用。
- §5.1 “相比 FLAN 错误减半”：仅规划错误近似成立（16% vs 30%），未采用。
