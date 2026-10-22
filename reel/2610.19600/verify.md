# 2610.19600 核对记录（Opus 5.5 核对席）

- 论文：Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System，arXiv 2610.19600v1（2026-10-14）
- 材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2610.19600.txt`（FULLTEXT: html-full，含正文 §1–7 与附录 A–L，已全文通读；无 `_pdf.txt`）
- Sol 记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl`，paper_id=2610.19600，batch b041，screen_score 88.75，claim_support=supported_in_material，evidence_level=transfer
- 核对日期：2026-10-22；未运行论文代码（作者称代码将发布，材料中无可复现产物）

## 结论：核对通过（pass）

Sol 记录的问题、动作、关键数字、证据等级与 caveat 均与材料一致，未发现需退回的错误。transfer 主张成立，但需按“设计迁移、低层重训”的口径陈述（Sol caveat 已写明）。

## 逐项核对

| 项目 | 材料实际内容 | 定位 |
|---|---|---|
| 问题 | 子任务 VLA 原子任务 80%，组合成长程移动操作仅 19%；问“长程失败究竟断在哪” | Abstract、§4.1 |
| 实际改动 | 冻结同一子任务 VLA（StarVLA QwenPI，Qwen3-VL-4B+DiT-B），只在规划器侧加：示范技能卡、按需视觉回忆、check_stance 距离分级+底盘修正、末端局部修正 | §5、Appendix B.2、D |
| 诊断方法 | 100 集基线，81 失败；3 次重规划内补回视为已恢复；取最早未恢复且阻断完成的错误为主因；仿真状态仅离线诊断用；3×Codex 候选+3 人复核；粗类 30 集 κ=0.86（26/30），细类盲评 30 集 κ=0.79（24/30） | §4.2、Appendix C、Tables 5–6 |
| 失败分布 | 规划 17（21.0%）/导航与底盘 21（25.9%）/局部操作 43（53.1%） | Figure 2 文字、Table 11 行合计 |
| 主结果（同条件对照） | 留出 seed：Harness VLA 改编基线 18% → 完整系统 49%，20 任务×5 seed=100 集配对；Δ+31pp，95%CI[21,41]，McNemar p<0.001；同一 VLA checkpoint、同一规划器 Kimi K3、匹配 planner/retry 预算 | Table 1、§6.1/6.3、Table 9 |
| 逐步积累 | 19→25→29→40→47（开发 seed）；仅 +Base 一步 CI[3,19] 不含 0；+Demo[0,12]、+Memory[−2,10]、+EEF[0,14] 不足以单独强断言（作者自己也这样说明） | Table 8、Appendix E.1 |
| 干预-失败对应 | 被修复集的原失败类：技能库 8（规划 5）、记忆 7（规划 4）、底盘 15（导航 11）、末端 10（操作 9）；作者声明是 episode 级而非一一因果 | Table 10 |
| 瓶颈后移 | 完整系统 53 失败中操作 47/导航 5/规划 1；12 个基线前段失败转为操作失败 | Table 11、Appendix G |
| transfer：仿真 | BEHAVIOR-1K 5 任务×20 匹配集=100：π0.5 7、Harness VLA 14、Ours 37；低层 VLA 用 BEHAVIOR 训练数据重训，干预设计不变；未报告配对检验；5 任务的选取理由未说明 | §6.3、Appendix I、Table 14 |
| transfer：真机 | Astribot-S1，2 任务×10 次=20：π0.5 端到端 4/20、agentic 基线 5/20、完整系统 13/20（6/10、7/10）；π0.5 在 500/300 条真机示范上微调；无显著性检验；真机上距离阈值是否重估未说明；Figure 7 仅为定性演示，不计入成功率 | Appendix J、Table 15 |
| 局限（材料自述） | check_stance 只看距离，不检查关节限位/IK/全身碰撞；剩余失败集中于错误放置、搬运掉落、碰撞扰动 | §5.3、§6.2、Appendix G |

## 与 Sol 记录的差异

无实质差异。补充两点边界（不改分，仅供展示时缩窄措辞）：
1. Sol evidence 写“细类盲评 κ=0.79”——该 30 集取自多个配置的失败集（隐藏配置），并非只来自基线；不影响结论。
2. Sol E 理由“额外模型调用成本未量化对齐”成立：Table 1 只匹配 planner/retry 预算，Gemini 3.5 Flash（离线技能卡）、Qwen3.8-27B（回忆）、Grounding DINO+SAM 的调用开销与时延均未报告。
3. 迁移证据中真机仅 20 次、两任务、无统计检验；BEHAVIOR 无配对检验。画报按“作者报告的有分母成功率”陈述，不写成显著迁移。

## 关键证据定位

- 诊断规则：§4.2、Appendix C.1
- 留出主结果：Table 1、Table 9（Held-out Baseline→Full）
- 组件证据：Table 8、Table 9、Table 10、Table 16–18
- 迁移：Table 14（BEHAVIOR-1K）、Table 15（真机）
- 参数：Table 7 / Appendix D.3
