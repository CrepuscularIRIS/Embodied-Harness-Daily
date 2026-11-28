# SOURCE — 2611.31894 RESET：一次演示 → 可练习的世界（poster 022-2）

- 论文：RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments（arXiv 2611.31894v2，2026-11-24）
- 全文：research/fulltext/2611.31894.txt（html 节选缓存，19 行长行；§3–§5 正文与 Table 1–6 表体完整，下表行号为该文件行号，定位以节 / 表号为准）
- L2 记录：batches/inc-l2-21.jsonl（axis code_policy_trial_revision + external_verification_control；capability；q4 fits；已逐条核对一致）

## 画报断言 → 原文位置

| # | 画报断言 | 原文位置 | 原文关键语 |
|---|---|---|---|
| 1 | 真实任务无真值判分器与可重置练习环境；一次演示同时给出场景几何、终态判据与验证世界的物理参考，且与源机器人运动学解耦 | L6（Abstract）、L9（§1） | 'real-world tasks provide neither ground-truth success scorers nor resettable practice environments'；'a single successful real-world demonstration simultaneously provides a blueprint of the world, a success criterion, and a physical reference for verifying that world—all independent of the source robot's kinematics' |
| 2 | 97% 平均（50 个未见布局 × 8 任务，TEST 0–49）；零样本代码 27%（3 次均值 26.8%、最好 43%，Cubes 70/0/36%）；π₀.₅ 逐任务微调 31%（30.8%，6,000 步 / 100 条轨迹）；Diffusion Policy 50%（49.8%，同 100 条轨迹）；开环回放 8% | L6、L12（§3.1）、L15（§4.1–4.2 Table 1） | Table 1 行：Open-loop Demo Replay 8% / Zero-shot Code 27%（best 43%）/ π0.5 31% / Diffusion Policy 50% / RESET 97%；'Zero-shot code averages 26.8% with extreme variance (Cubes: 70/0/36%…)' |
| 3 | 三个零样本为 0 的任务 RESET 88–100%；独立重跑从零样本起步达 Build Tower 100%、Open Drawer 98%、Sweep 86% | L15（§4.2） | 'RESET reaches 97.0% overall and 88%–100% on the four tasks where zero-shot code scores 0%'；'Independent reruns from zero-shot starts reach 100% on Build Tower, 98% on Open Drawer, and 86% on Sweep' |
| 4 | 真机 223/280（80%）；三台固定底座 210/240（88%）；xTrainer 73/80、Franka 76/80、LIFT2 61/80、G1 13/40；仿真–真机结局一致 xTrainer 95%（80 次）、LIFT2 90% | L6、L15（§4.6 Table 5） | 'In total, 223 of 280 real-robot trials succeed (80%), and 210 of 240 (88%) on the three fixed-base robots'；'Simulation and the real robot give the same outcome in 95% of the 80 trials on xTrainer and in 90% on ARX LIFT2' |
| 5 | 跨本体仿真：Franka 96%、LIFT2 80%、G1 77%（源 xTrainer 97%）；G1 五指手在 Sweep 只有 32% | L15（§4.5、Table 5） | 'Dual-arm Franka and ARX LIFT2 reach 95.5% and 79.5%, and Unitree G1… reaches 77.3% (32% on Sweep…)' |
| 6 | 五段工序：Rebuild（首帧 RGB-D → 网格 / 桌面 / MuJoCo；终态几何关系＋静止条件 → 只读隐藏判据，人确认一次）；Examine（开环回放关节指令看接触复现；轮廓 IoU；质量 / 摩擦交给随机化）；Self-improve（任务图＋技能库，读每节点状态 / 失败原因 / 关键帧，改最早出错处，hold-out 更好才替换）；Execute（冻结、零 LLM 调用）；Transfer（世界、判据、布局分布、任务图笔记原样交付，只补 URDF / 标定 / 接触偏置） | L12（§3.3–3.6） | 'The scorer is then read-only and hidden from the controller, so practice cannot game it'；'Examine is a check that the world is usable, not a guarantee of fidelity'；'a revised program replaces the current one only if it succeeds more often on a separate set of hold-out layouts' |
| 7 | Rebuild 用 GPT-6 Astra、Self-improve 用 Claude Code（Claude Opus 5.5）；判据由人确认一次、只改了 Lift-Box | L15（§4.1） | 'Rebuild uses GPT-6 Astra…; Self-improve uses Claude Code with Claude Opus 5.5. A person confirms the success criterion once per task; this changed the criterion only for Lift-Box' |
| 8 | 布局扰动 ±3–6 cm / ±10°–180°；DEV 0–19 / hold-out 20–39 / TEST 0–49 seed 不相交，TEST 开发结束后只评一次 | L15（§4.1） | 'Each layout moves every task object by up to ±3–6 cm along each table axis and rotates it by up to ±10°–180°…'；'sealed Blind Test (TEST 0–49, evaluated once, after development ends…)' |
| 9 | 成本：2–8 轮、100–320 仿真回合、约 30M token / 任务 / 机器人；部署零 token | L15（§4.6） | 'Self-improve converges in 2–8 rounds, using 100–320 simulation episodes and about 30M LLM tokens per task and robot. Deployment uses no LLM tokens.' |
| 10 | 错的世界（Table 2，6 任务）：正确世界 0/6 打破、0/6 标出；放大 ×1.1–1.2 打破 12/18、标出 11/18（打破的 12 例中标出 9 例）；桌面 −2 cm 打破 3/6、标出 6/6（3/3）；相机偏移 0/6、标出 6/6；摩擦 ×0.3 打破 0/6、质量 ×3 打破 2/6、均 0 标出；Examine 不标正确世界、标出 16 个打破技能的几何缺陷中的 13 个，漏 3 个放大世界 | L15（§4.3 Table 2、Finding 3） | 'It flags no correct world and 13 of the 16 geometric defects that break a skill, including every lowered table… It misses three enlarged worlds, so it is a check, not a guarantee' |
| 11 | 隐藏失败：桌面低 2 cm 时零样本 Stack Cups 程序练习成功 98%，三次独立运行在正确世界只有 18–20%（正确世界练习 96%） | L15（§4.3 Finding 1、Table 3） | 'the zero-shot Stack Cups program happens to release at the right height and succeeds in 98% of practice episodes… In three independent runs the resulting program reaches only 18%–20% in the correct world, against 96% after practice there' |
| 12 | 判据精度：松判据 "carton on box" 给撞平纸箱的程序 100%，演示导出的直立判据 0% | L15（§4.2） | 'a loose text-translated criterion ("carton on box") scores a zero-shot program 100% for knocking the carton flat; the demonstration-derived upright criterion scores it 0%' |
| 13 | 随机化物理：Mug-Box 未见质量 ×3 从 10% 到 100%；3× 重的 Open Drawer 仍不解 | L15（§4.3 Table 4） | 'on Mug-Box this lifts success under an unseen mass ×3 from 10% to 100% (Tab. 4); the 3× heavy Open Drawer stays unsolved' |
| 14 | 消融（Table 6）：去 hold-out 门控 Mug-Box 100%（3 轮）/ Open Drawer 0%（8 轮）；只给结果不给节点日志与关键帧 12% / 0%；完整 3 / 5 轮 100% / 98% | L15（§4.4 Table 6） | 'removing node-level failure logs and keyframes… leaves performance at 12% and 0% after 8 rounds… Removing hold-out gating… still solves Mug-Box (100%) but stays at 0% on Open Drawer after all 8 rounds' |
| 15 | 共享的是世界和判据不是代码：Franka 5 个程序直接可用（94–100%），另 3 个 10% / 24% / 0% → 练习后 100 / 78 / 100%；LIFT2 源程序一个任务都不成，练习后平均 80%；只给世界＋判据从零起步 Mug-Box / Open Drawer 94 / 84%（继承任务图 84 / 70%）；G1 源程序只在 Apple 18%，练习后 77%，74 / 92%；技能复用 Franka 94.5% 相同、LIFT2 78.2%、G1 86.7% 自写 | L15（§4.5） | 'On ARX LIFT2 the source programs succeed on no task, and on Unitree G1 only on Apple (18%); after practice the two robots average 80% and 77%'；'94.5% of Dual-arm Franka's skill functions are identical to another robot's and LIFT2 reuses 78.2%, whereas Unitree G1 writes 86.7% of its skills from scratch' |
| 16 | 边界：只覆盖刚体 / 铰接 / 准静态扫掠；3× 重抽屉超出随机化；G1 真机 33%（同任务仿真 84%）因全身控制器移底座；π₀.₅ / DP 只有 100 条轨迹（作者承认偏少）；真机只执行冻结程序、不从真机失败改写 | L15（§4.6、§3.1）、L18（§5） | 'Unitree G1 succeeds in 13/40 trials on its four tasks (33%, against 84% in simulation on the same tasks)'；'100 trajectories are little data for fine-tuning a model as large as π0.5, which may explain its lower score'；'RESET currently targets rigid, articulated, and quasi-static sweeping tasks, not deformable cloth or dynamic throwing' |

## 展示缩窄（相对原文的取舍）

- 题头三个大数（97%、223/280、3 台）为 Table 1 / §4.6 / §4.5 的合并读数；"3 台零演示学会"指 Franka / LIFT2 / G1 在共享世界练习后的仿真均值 96 / 80 / 77%，真机分别 95 / 76 / 33%——G1 的真机落差写在边界栏与 §2 表内。
- Table 2 的"打破 / 标出"以取芯格示意：每格 = 一个任务–缺陷例（6 任务 × 该缺陷的世界数），实心赭 = 打破、斜纹青 = Examine 标出；"打破的 12 例中标出 9 例"为原文 "9/12"。
- Table 3（练习于缺陷世界再测正确世界）只上画 Stack Cups 桌面 −2 cm 一例（98% → 18–20%），Apple / Build Tower / Mug-Box 容忍行从略。
- §2 基线条的 π₀.₅ 与 Diffusion Policy 均为"在 100 条 RESET 成功轨迹上逐任务训练"的同条件对照，未与榜单上的通用策略比较。
- Table 5 的逐任务 8 列合并为每台机器人的仿真均值与真机成功数；"Franka 5 个程序可用 / 3 个 10 / 24 / 0%"为 §4.5 正文，非表格行。
- 消融只在 Mug-Box 与 Open Drawer 两任务、从 0% 零样本起步，画报如实标出。

## 排版修正记录（生产期，未改任何数字）

- 渲 1 内容偏短：bound–foot 间 317px@2x 空带，且题头底边距与章头间距合成 104px@2x 色带 → 增"拷过去的是世界和判据，不是代码"三卡条、收紧题头底距、整体字号微调；h1 与三个大数字行高 1.26 / 1.1 → 1.32 / 1.3（overflowAny 4→0）。终版无空带、无裁切、无溢出。
