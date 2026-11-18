# SOURCE — 2611.19198 Self-Calibrating VAA

## 论文信息
- 标题：Self-Calibrating Vision-Agent-Action: Deploying Pick-and-Place to New Robot Cells without Demonstrations or Fine-Tuning
- arXiv 2611.19198v1（2026-11-14 提交）。
- 阅读原文：research/fulltext/2611.19198.txt（FULLTEXT html 完整缓存）。
- 初筛记录：research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-16.jsonl（P3/confirmed/to_l3，卡 observe_act_interface + harness_effect_evaluation）。

## 核对结论
逐节与 L2 记录核对一致，无实质错误；corrections：0。

## 海报数字与断言映射（poster 区块 → 原文位置）
| 海报内容 | 原文出处 |
| --- | --- |
| 01 丢分诊断：8 因子（臂/爪/相机/镜头/光照/桌面/物体/基座 45°）2^(8-4) 分式设计 30 单元 | §III 分式设计与逐因子诊断（图 3）；换爪/转架为主导因子 |
| 01 条形示意：换爪 4 单元 64/71/35（冻结 VAA/VAA/最强 VLA GR00T）、转基座 2 单元 78/90/45（最强 π0.5） | 表 I 按组数字（gripper changed 56→71、frame rotated 78→90、Δ+36/++45）；最强 VLA 按组数字 |
| 02 三步自标定：命令映射 Δx≈JΔu；K/[R|t]/k₁ 桌面平整；测深抓取 | §IV-A 式 2 与图 2/5；VLM Qwen3.8 27B 标注＋Qwen3 30B 选目标 |
| 03 主结果 230/360（64%）冻结、268/360（74%）微调、76/360（21%）X-VLA | 表 I（18 单元 × 20 回合）；X-VLA 为该子集总分最强 |
| 04 表 II：X1 6/13/18、X2 0/10/16、X4 8/7/7、X5 0/5/14、X6 0/9/13，合计 10/44/68（各 /100） | 表 II 五个开发压力格（最强 VLA/冻结 VAA/VAA） |
| 04 备注：X4 未拉开（7 对 8） | 表 II X4 行 |
| 05 消融：full 50/60、复用训练标定 22/60（p<0.001，转架单元 0/20 对完整 19/20）、k₁=0 32/60、单目深度 20/60、oracle 44/60（p=0.07）、无探索 43/60 | 表 III（3 配对单元 × 20 回合，精确 McNemar 未校正，Holm 校正后主消融仍显著）；oracle 差 6 不显著 |
| 05 备注：k₁=0 损失几乎全在组合单元（16→1/20） | 表 III 注 |
| 06 两步链 54/60 对 4 个被测 VLA 0/60 | §V-C（LIBERO-Goal 中最可靠的两步链） |
| 06 失败分解 41 放置＋27 抓空＋19 换抓＋5 其他＝92；两任务占 40% | §VIII |
| 06 边界：Robotiq 2F-85 弧爪 0/20（VLA 0–6/20），不计入 18 单元 | §VIII（平行爪模型外） |
| 07 与 2610.01560 区分（那篇换 harness 提同模型，本篇不换模型、换单元） | 本文相关工作对比 |
| 8 个 LIBERO VLA 基线（X-VLA/π0.5/π0/GR00T/OpenVLA/SmolVLA/τ0/VLA-JEPA） | 表 I 对照组 |

## 示意图标注
- 01 区分组条形为按表 I 数字重绘（示意）；05 区消融条形按表 III 数字重绘（示意）。

## 展示缩窄（非 correction，仅记录）
全仿真（LIBERO-spatial）；refined VAA 微调用过开发单元、评设计单元时冻结版结果可见（开发污染）；5 个整单元与消融三单元均为开发格/设计子集非留出；标定是捆绑包非逐项因果；基线 RGB 无实测深度（传感器差，RGB-only VAA 消融 50→20/60 部分回应）；单 seed（参照重跑 OpenVLA 14/20 与 19/20、SmolVLA 16/20 与 12/20 波动）；链任务为挑选的两步、两任务占失败 40%；平桌＋平行闭合爪边界（弧爪 0/20）。
