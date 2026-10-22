# SOURCE — 2606.10577

- 论文：AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness，arXiv **2606.10577v3**（2026-06-09），https://arxiv.org/abs/2606.10577
- 阅读材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2606.10577.txt`（html-full 全文缓存，私有，不提交）。图 2–8 仅有图注，画报中无原论文插图。
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl` paper_id=2606.10577（batch b018，screen_score 88.75，supported_in_material / transfer）。核对见 `verify.md`。
- 未运行论文代码；所有数字为作者报告值。

## 数字 / 断言 → 原文定位

| 画报位置 | 内容 | 原文 |
|---|---|---|
| 标题、导语 | 不选预测航点，暴露动作/深度/记忆为工具；上下文 = 指令＋当前 RGB＋BEV＋最近六步理由；几何检查退回重选 | 摘要；§III-A 式 (1)(2)；§III-C；§III-D 式 (8) |
| 问题条 | Open-Nav / SmartWay / EvoNav 依赖训练的航点预测器；三个瓶颈：动作空间受限、深度不显式暴露、历史累积 | §I 第 2–3 段 |
| 动作卡 | move_to(k,u,v,reason)；理由作为记忆记录；反投影式 (5)；ρ = min(ρ_max, max(0, ‖p‖−m))；矩形区 𝓡(θ,ρ) 无障碍点才 Safe；越界/深度无效拒绝；Execute / Reselect；成功即结束本步 | §III-A、§III-C 式 (5)–(7) |
| 动作卡示意图 | 像素准星、俯视矩形区、障碍点 —— **示意** | 据 §III-C 自绘 |
| 动作卡消融 | 换回航点预测器 SR 76→66，SPL 66.50→57.73 | 表 IV |
| 深度卡 | query_depth 批量像素 (k,u,v)；返回米制深度 d_i＋5×5 邻域 min/mean/median；不移动机器人；VLM 不直接收深度图；触发例：走廊是否通、门是否比障碍近 | §III-A、§III-B 式 (3)(4)；§I |
| 深度卡示意值 | 1.6 m / 5.2 m / 2.3 m 为**示意值**，非原文数据 | 自绘 |
| 深度卡消融 | 去掉 60/47.14；改为深度图输入 69/55.79（SR/SPL） | 表 IV |
| 召回卡 | recall(p,k) 取图像缓存 C_t[p,k]，追加到当前提示；BEV 节点编号即召回索引；下一步上下文重建不含历史图，需再次召回；用例：走过头后回溯 | §III-D 式 (9)；图 6 图注（Episode 116） |
| 召回卡消融 | 去掉 64/47.47（表 IV）；累积全部历史图像 66/54.05（表 III） | 表 III、表 IV |
| 反馈带 · 回路 | query_depth / recall 返回证据给下一轮且同一步可多次调用；move_to / stop 成功则终结本步 | §III-A |
| 反馈带 · 六步文本历史 | 最近 6 步 (r_j, a_j)；去掉 63/48.49；换任务进度记录 64/52.56 | §III-D 式 (8)；表 III |
| 反馈带 · BEV | 轨迹、决策点索引、SLAM 障碍/可通行；去掉 70/59.46 | §III-D；表 III |
| 反馈带 · 几何拒绝 | 身高范围障碍点投影，𝓡 内无点则 Safe，否则 Reselect；“原文未单独消融”为我们的阅读判断 | §III-C 式 (7)；表 III/IV 无此行 |
| 仿真结果图（据表 I 重绘） | SR：GPT-5.5 44→55；Gemini-2.5-Pro 52→58；Gemini-3.7-Flash 54→76。SPL：35.04→48.41；41.70→42.91；47.95→66.50。增量 +11/+6/+22 为相减所得 | 表 I；§IV-A |
| 仿真条件 chips | Habitat；R2R-CE val_unseen 同一 100 回合协议；SmartWay 为作者同 VLM、同设置复现（∗）；单次运行无方差（材料未报告重复/种子，为我们的阅读判断） | §IV-A；表 I 脚注 |
| 真机结果图（据表 V 重绘） | SR%：实验室 44.4/55.6/66.7；办公室 17.6/35.3/47.1；广场 11.1/22.2/55.6；总体 22.9/37.1/54.3；总体 NE 4 视角 2.51 m | 表 V |
| 真机分母（反推） | 实验室 9、办公室 17、广场 9 回合（合计 35，与 §IV-B 一致）；成功回合 4/5/6、3/6/8、1/2/5、8/13/19——由百分比反推，原文未直接给出分场景回合数 | 表 V；§IV-B“35 real-world episodes” |
| 真机条件 chips | Go2W 四足＋全向四轮；4×D435＋LiDAR＋FAST-LIO；同平台/路线/指令/评估；SmartWay 12 视角原地旋转采集，本法 1/4 视角；表 V 未按平台拆分；>200 m 室内→室外任务仅图 7 定性演示 | §IV-B；表 V；图 7 图注 |
| 限制 1 | 100 回合子集、无方差；真机每场景 9–17 回合 | §IV-A；表 V（反推） |
| 限制 2 | 每回合调用次数仅图 4 示意，无数值与基线成本对齐 | 图 4 图注；§IV-A“VLM cores”段 |
| 限制 3 | 表 III/IV 均为 Gemini-3.7-Flash；Gemini-2.5-Pro SPL 42.91−41.70 = 1.21 | 表 III、IV、I |
| 限制 4 | 依赖对齐深度、SLAM-BEV、TEB/SCAN-Planner；“仍受 VLM 决策质量限制” | §III-A、§III-D、§IV-B；§V |

## 未采用的作者主张

- “优于训练方法 LightNav-0”：非同骨干、LightNav-0 为作者复现，未展示。
- “跨 Gemini 骨干持续增益”（图 5，正文误写为 Fig. 6）：仅三代 Gemini 内比较，未展示。
- 图 8 失败分析比例：仅图注无数值，未展示。
