# 2606.10577 核对记录（Opus 5.5 核对席）

- 结论：**核对通过（pass）**，可制作。
- 版本：arXiv 2606.10577v3（2026-06-09），《AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness》。
- 材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2606.10577.txt`（FULLTEXT: html-full，含摘要、§I–VI、表 I–V 正文；图 2–8 只有图注无图像；无 `_pdf.txt`）。已全文通读。未运行论文代码。
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl`，paper_id=2606.10577，batch b018，screen_score 88.75，G4/M4/X4/E3，claim_support=supported_in_material，evidence_level=transfer。

## 五项核对

| 项 | 材料实际支持 | 定位 |
|---|---|---|
| 问题 | 零样本 VLN-CE 中 VLM 通过学习的航点预测器行动：动作空间受限于候选；深度只喂给预测器、VLM 拿不到具体位置的度量距离；记忆靠累积文本/图像历史，撑满上下文。 | §I 第 2–3 段 |
| 实际改动 | 冻结 VLM，暴露四个工具 {query_depth, recall, move_to, stop}。move_to(k,u,v,reason) 选像素→深度反投影→方位/距离（减停止裕量、截断 ρ_max）→矩形区域障碍检查，失败返回 Reselect；query_depth 返回像素深度+5×5 邻域 min/mean/median；recall(p,k) 从图像缓存取过去决策点某视角 RGB。上下文每步重建为 指令+当前 RGB+BEV 图+最近 6 步 (reason, action) 记录；VLM 不直接收深度图。 | §III-A–D，式 (1)–(9) |
| 关键结果（仿真） | Habitat，R2R-CE val_unseen 同一 100 回合协议，同骨干对比（基线为作者复现，标 ∗）：Gemini-3.7-Flash 76/66.50 vs SmartWay 54/47.95（SR/SPL）；Gemini-2.5-Pro 58/42.91 vs 52/41.70；GPT-5.5 55/48.41 vs 44/35.04。 | 表 I，§IV-A |
| 组件消融 | 仅在 Gemini-3.7-Flash 上：航点预测器替换动作工具 66/57.73；去深度工具 60/47.14；深度图替换深度工具 69/55.79；去召回 64/47.47；去推理文本历史 63/48.49；换为任务进度文本 64/52.56；去 BEV 70/59.46；累积全部历史图像 66/54.05。 | 表 III、表 IV |
| transfer（真机） | 35 回合，Unitree Go2W 四足 + 全向四轮两平台，均 4×RealSense D435 + LiDAR + FAST-LIO；局部规划 TEB / SCAN-Planner。骨干 GPT-5.5。总体 SR：SmartWay(12 视角原地旋转采集) 22.9% / 本法 1 视角 37.1% / 4 视角 54.3%；NE 3.74/3.16/2.51 m。按百分比反推分母：实验室 9、办公室 17、广场 9（合计 35），总体成功 8/13/19 回合。同平台、同路线、同指令、同评估设置。 | §IV-B，表 V |
| 基线 | 主基线 SmartWay（航点预测器 + 累积历史），同 VLM 复现；真机只比 SmartWay（作者称仿真中最强可复现基线）。 | 表 I；§IV-B |
| 成立条件 | 100 回合单次运行、无方差/种子报告；消融只在一个骨干；工具调用次数仅图 4 给出、正文无数值，未报告调用/延迟成本与基线对齐；依赖 RGB-D 深度与 SLAM 构建的 BEV；真机表未按平台拆分。 | §IV；图 4 图注；表 V |

## transfer 主张分开陈述

- 仿真：Habitat R2R-CE，有分母（100 回合）与同骨干对照。
- 真机：有分母的成功率（35 回合，三类场景）与同平台同指令对照，支持“真机零样本可用且优于 SmartWay”；但未按平台拆分，故“两平台上分别成立”材料不能直接确认，画报只写“两平台合计 35 回合”。
- 图 7 中 >200 m 室内到室外长程任务、读标牌任务为**定性演示**（另见补充视频），不计入成功率，画报标“定性”。
- 视角数不对等：SmartWay 12 视角 vs 本法 1/4 视角（1 视角时本法信息更少仍更好）。

## 与 Sol 记录的差异

无实质差异，不需 correction。Sol 三条 evidence 数字与表 I/III/IV/V 一致；caveat（100 回合选择风险、调用成本未控制）与材料一致。补充收窄：
1. 消融只在 Gemini-3.7-Flash 上做，“组件有效”不自动推广到其他骨干。
2. 真机 35 回合未按两平台拆分；Sol 写“覆盖两平台”准确，但不应读成每平台各自有成功率。
3. “跨骨干持续增益”（图 5）只覆盖 Gemini 系列内 2.5-Pro→3.7-Flash 的对比，正文另有图号笔误（文字写 Fig. 6 实指 Fig. 5），画报不展示此外推。

## 作者声称 vs 材料支持

- “SOTA 零样本”：材料支持到同 100 回合、同骨干复现基线比较；非全集 val_unseen。
- “优于训练方法 LightNav-0”：表中 LightNav-0 为作者复现（∗），且非同骨干比较，画报不展示。
- “失败分析：停止类失败减半、航点类失败消除”：图 8 仅图注，无数值，画报不引用具体比例。
