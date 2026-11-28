# SOURCE — 2611.30550 Body and Soul / RoboHarness-Zero：零准备的 VLM 监督 harness（poster 022-3）

- 论文：Body and Soul: Decoupling Robotic Brain and Policy with RoboHarness-Zero（arXiv 2611.30550v1，2026-11-23）
- 全文：research/fulltext/2611.30550.txt（html 节选缓存，19 行长行；§3–§5 正文与 Table 2–7 表体完整，§4.7 末尾与附录不可见；下表行号为该文件行号，定位以节 / 表号为准）
- L2 记录：batches/inc-l2-20.jsonl（axis planner_composes_code_and_policies + harness_effect_evaluation；judgment；q4 fits；已逐条核对一致）

## 画报断言 → 原文位置

| # | 画报断言 | 原文位置 | 原文关键语 |
|---|---|---|---|
| 1 | 审计 Xiaomi-Robotics-1 的 893 个失败回合中的 193 个：43% 为决策错误（选错目标 24% + 丢了进度 19%），57% 为物理执行失败等 | L9（§1）、L12（§3.1） | 'After weighting…, we estimate that 43% of failures involve a decision error. The robot chooses the wrong target in 24% of failures and loses track of task order or progress in 19%' |
| 2 | 配对恒等式 S_H = b·r + (1−b)·s；b = 57.5%、r = 104/115 = 90.4%、s = 37/85 = 43.5% → 70.5%；不输给策略需 r ≥ 1 − (1−b)/b·s；原子任务阈值 91.5%（实测 96.6%），已见组合 80.0% vs 51.4%、未见组合 90.5% vs 28.6%；再丢 3 个就抹平原子增益 | L12（§3.2 Eq. 1）、L15（§4.5） | 'At the observed rescue rates, Eq. (1) gives a break-even retention of 91.5% on atomic tasks, against 96.6% observed… Three additional losses… would erase the atomic gain'；'retention reaches 80.0% against a 51.4% threshold on seen tasks and 90.5% against 28.6% on unseen tasks' |
| 3 | 机制：整句任务原样交给 VLA，VLM 自己列计划（无示范 / 记忆 / 脚本）；每 160 控制步（10 次 16 动作预测、8 秒仿真）看一次；当前阶段有进展 = 距离比上次最小值近 ≥2 cm 或 VLM 核实完成；停滞计数到 120 步触发复查；先改写指令，反复改写永不触发接管；同一子阶段两次已核实物理失败后才有有界接管（基座 / 躯干 / 夹爪走点），吃同一回合预算，抬手验证后交还；接口不给真值位姿 / 隐藏状态 / 子阶段标签 / 专家轨迹 | L12（§3.2–3.6） | 'A default window allows ten predictions, or 160 control steps'；'A fresh observation earns progress credit when the estimated distance falls at least 2 cm below its previous minimum'；'the stall window is 120 steps'；'Two verified physical failures on the same substage… make a bounded takeover available… Repeated rewording alone never triggers a takeover'；'A takeover draws from the same episode budget as the policy' |
| 4 | 主结果：200 配对回合 Xiaomi 单独 115/200（57.5%，榜单 57.4%）→ Astra 监督 141/200（70.5%），+13.0 [6.5, 19.5]；保留 104/115、救回 37/85；37 增 / 11 损，精确 McNemar p = 0.00022；Sol 监督 126/200（63.0%） | L6（Abstract）、L15（§4.2 Table 3） | 'The gain is 13.0 percentage points, with a 95% paired bootstrap confidence interval of 6.5–19.5 points… The 37 gains and 11 losses yield a two-sided exact McNemar p-value of 0.00022' |
| 5 | 组合任务贡献 26 个净增中的 23；已见组合 +17 / −7，未见组合 +15 / −2（占总增益一半）；原子任务只 +4 点；四批 50 回合 30→34、29→36、31→34、25→37 | L9、L15（§4.2）、L18（§5） | 'Composite tasks account for 23 of the 26 net additional successes. On seen compositions, the harness gains 17 scenes and loses seven. On unseen compositions, it gains 15 and loses only two'；'Xiaomi gains only four percentage points on atomic tasks' |
| 6 | 固定重发（无 VLM，每 160 步重发原指令）113/200（56.5%）；Astra 的 37 个增益中固定重发只复现 15 个：只观察 9/10、仅改写 3/12、涉及接管 3/15；22 个不可复现增益中 21 个含干预（9 改写、12 接管）；11 个配对损失在固定重发下也全败 | L15（§4.6 Table 7） | 'Fixed reissue solves 113/200 scenes (56.5%)'；'fixed reissue reproduces nine of ten observation-only gains, three of twelve gains with rewriting alone, and three of fifteen gains involving takeover… 21 of those 22 involve an intervention: nine rewrite the instruction and 12 involve takeover. All 11 scenes that Xiaomi solves alone but loses with Astra also fail under fixed reissue' |
| 7 | 一套规则五个冻结策略（同 50 回合子集、各用原生适配器与技能配置、每策略 975 次单独剖析回合）：RLDX-1 20→25（40→50%）、WorldDreamer 18→22（36→44%）、GR00T N1.5 13→17（26→34%）、π₀.₅ 8→12（16→24%）、Xiaomi 30→34（60→68%）；四个新策略只丢 59 个单独成功中的 1 个（GR00T）；RLDX-1 5 个救回全是未见组合、WorldDreamer 4/32、GR00T 5/37、π₀.₅ 4/42 且全含接管 | L6、L15（§4.3 Table 4） | 'RLDX-1 improves from 20 to 25 successes, WorldDreamer from 18 to 22, GR00T from 13 to 17, and π0.5 from 8 to 12… all five policies gain eight to ten percentage points… lose one of their 59 standalone successes'；'Profiling rollouts 975 per policy' |
| 8 | 按任务准备的 Harness VLA：在 RLDX-1 上发表增益 +29.2（Astra）vs 本 harness +10；迁到 Xiaomi：Harness VLA 29 vs 单独 30（−2.0），本 harness 34（+8.0）；未为 Xiaomi 重建记忆；作者声明不对其它系统排名 | L9、L15（§4.4 Table 5） | 'Harness VLA solves 29 scenes, Xiaomi alone solves 30, and our harness solves 34'；'We did not rebuild the memories for Xiaomi'；'Differences in scenes, task-specific preparation, and access to success feedback preclude a direct ranking' |
| 9 | 收益构成：37 个增益中 22 个策略生成全部动作（10 原指令 + 12 改写）；接管出现在另 15 个增益与 11 个损失的 9 个；接管占控制步 9.3%（21,182 / 227,198）；23 个增益可见"卡住→干预→同阶段完成"（12 仅语言、11 接管）；10 个只观察增益中固定重发解 9 个，不记功于 VLM | L15（§4.5 Table 6） | 'Xiaomi generates every robot action in 22 of the 37 harness-only successes: ten under the original instruction and twelve under revised wording. Takeover occurs in the other 15 gains and in nine of the 11 losses… 21,182 of 227,198 executed control steps (9.3%)'；'Twenty-three episodes meet this criterion: 12 with language alone and 11 with takeover' |
| 10 | 接管是短板：接管回合 20/65 成功 vs 仅改写 19/31；单独轨迹审计 35 次失败技能尝试中 22 次干预后仍未达目标，5 次交还后策略找不到目标；四个新策略救回 18/141（Xiaomi 同场景 6/20） | L9、L18（§5） | '20/65 episodes involving takeover succeed, compared with 19/31 involving rewriting alone'；'22 of 35 failed skill attempts still do not reach their goal after the harness intervenes'；'the harness recovers 18 of 141 standalone failures on the four new policies, against six of 20 for Xiaomi' |
| 11 | 开销与模型：每回合 71 次 VLM 请求；等待响应占回合墙钟 87%；Sol→Astra 救回 27.1→43.5%、保留 89.6→90.4%；Astra 15 个净增中 14 个来自策略单独失败的回合 | L15（§4.1、§4.5）、L18 | 'The 200 harness runs in the main result average 71 VLM requests'；'waiting for responses consumes 87% of episode wall time'；'Switching from Sol to Astra raises rescue from 27.1% to 43.5%, while retention rises only from 89.6% to 90.4%. Fourteen of Astra's 15 net additional successes thus come from scenes Xiaomi alone misses' |
| 12 | 边界：仅 RoboCasa365 仿真；72 个开发回合覆盖 47/50 任务，10 个评测回合与开发重合（剔除后 134/190 vs 108/190）；未逐个移除重写 / 接管 / 校准；未测无 VLM 的停滞触发重试、未同机重跑单独策略；四个新策略无无 VLM 对照；对 95% 成功率的策略需保留约 98% | L15（§4.1 Table 2、§4.6）、L18（§5） | 'Our 72 development episodes cover 47 of these tasks. Ten evaluation scenes match development episodes… Excluding them gives 134/190 harness successes versus 108/190'；'We did not test a stall-triggered retry without a VLM or repeat the standalone policy run on the same machine…, nor did we individually remove rewriting, takeover, or calibration'；'even rescuing 43.5% of its failures requires retaining about 98% of its successes to break even' |

## 展示缩窄（相对原文的取舍）

- §2 流转图（104 保留 / 11 弄丢 / 37 救回 / 48 两边都败）为按 Table 7 配对计数绘制的示意 Sankey，带宽按回合数等比；不是原文图。
- 五策略卡只给 50 回合子集的成功数与百分比，未上画每策略的 VLM 请求数（π₀.₅ 162 / 回合等）与适配器细节。
- §4 迁移条以"相对同场景策略单独的增益（点）"为尺度，Harness VLA 在 RLDX-1 的 +29.2 为其发表数字、本 harness 的 +10 为本文 50 回合测量；绝对成功率不可直接比。
- §4.7 轨迹审计（Sol 监督 80 个未见组合回合）只取 22/35 与 5 次交还失败两个数，逐技能表从略。
- 收益构成只取 22 / 15 / 9 / 9.3% / 23 五个数；Eq. 1 的推导与各任务类别阈值全表（Figure 5）从略。
- 画报题头"先数它保住了多少，再谈救回多少"为编辑修辞；全部数字均在上表可溯源。

## 排版修正记录（生产期，未改任何数字）

- 渲 1 内容超页 22px（overH=22）、SVG 条宽 640×460 过高 → 流转图等比缩至 U=1.7（640×396）、一处 SVG 标签缩短；固定重发大数字行高 1.2→1.3（overflowAny 3→0）。终版无溢出、无裁切、无空带。
