# 2611.26376 UniCraft — 数字与断言映射

- 论文：*Alignment Drives Reuse: Cross-Embodiment Skill Unification via Enforced Action Contracts*，arXiv 2611.26376v1（2026-11-19）。全文缓存 `research/fulltext/2611.26376.txt`。
- L2 记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-19.jsonl`（P3/confirmed/to_l3，capability，main/observe_act_interface + harness_memory_skill_reuse + harness_self_optimization）。核对无判断错误，correction 0。

## 断言 → 原文映射

| 画报断言 | 原文位置 |
|---|---|
| 6 本体、3 基准（LIBERO-PRO 90 + RoboCasa365 50 + RoboTwin 2.0 hard 40）、300 任务-本体对、3 epoch×6 batch | §4.1 实验设置；L2 anchor §4 |
| 3 agent model（GPT-6 Astra/Gemini 3.8 Flash/DeepSeek-V4.1-Flash）各 2,700 rollouts、同案例同序同预算 | §4.1；L2 paper_evidence（同案例同序同预算 2700 rollouts/model） |
| episode-local 统一几何帧 + R_tcp 工具朝向（approach/jaw 轴由目标携带非设备隐含） | §3.1 |
| Action a=(σ,F,φ)、谓词作用于设备测得值、"issued but not achieved is a failure"、替换测得值为指令值即违约 | §3.1 |
| set_gripper 两原生绑定（LIBERO 定向命令 vs RoboTwin 归一化关节目标）同谓词同判 | §3.1 |
| 逐案非回归门控 Δ_c≥0∀c 且至少一例 >0（否则比执行步数） | §3.2 |
| 修订保留率 Astra 38.7%（12/31）、Gemini 40%（12/30）、DeepSeek 39.3%（11/28） | §4 "retained 38.7% (12/31)…40% (12/30)…39.3% (11/28)" |
| E1→E3 unseen 场景：LIBERO-PRO 9–28pp、RoboTwin 10.8–13.3、RoboCasa 3.1–14.4（vs 每本体独立技能基线） | §4.3 |
| 表2：UniCraft(Astra) LIBERO-PRO 86（X-VLA 96，但其 RoboTwin ckpt 仅 10%）/ RoboTwin 89.25（跨 4 evaluated embodiments）/ RoboCasa 37.50（π₀.₅ 10.63） | §4 表2 及 "X-VLA leads on LIBERO-PRO, achieving 96% versus 86%…RoboTwin-specific checkpoint achieves only 10%, while UniCraft reaches 89.25%…37.50% on RoboCasa365, compared with 10.63%" |
| 冻结 Astra 库 zero-shot ARX-X5 74.0（学习期 88.5，保留 83.6%，差 14.5pt 归可达性/接触几何） | §4.4 |
| robosuite 11 任务族 2K：Sol 67.3 / Astra 66.7 / Terra 48.0 / DeepSeek 32.7 / Gemini 28.0 / MiniMax 24.7 | §4.4 表3 |
| RoboDojo 42 任务 210 rollouts 均值 54.8%（Memory 组最好 76.7%、Precision 62.5%、Open 55.0%） | §4.4 "Overall success is 54.8% (115/210)…Memory performs best (76.7%)" |
| 组件使用 pick() 54–64%、move_to() 81–96% | §4.4 组件统计 |
| 失败四因（能力缺/后续动作使子目标失效/推不出可动部件响应/精细对齐不可靠） | §4 失败分析 |
| Gemini Composite-Unseen 23.75→17.50→21.25（通过门控的修订仍 held-out 回归；验证集≠全集保护） | §3.2/§4（L2 partial 条目原文） |
| 2K→4K：Astra 66.7→83.3、Sol 67.3→75.3、Terra 48.0→62.0；MiniMax 请求预算耗尽 40.7–56% | §4 图（"Increasing the horizon from 2K to 4K improves Astra from 66.7% to 83.3% and Sol from 67.3% to 75.3%"）；L2 记录 |
| 边界：adapter 每本体人工实现（task-independent、ARX-X5 无目标任务反馈调参）；修订间隔 150 未调参；辅助件不对等（SAM2.1 vs SAM3+Contact-GraspNet+Molmo）；Composite-Seen 0–15% 跨三模型 | L2 partial 两条 paper_evidence；§4.1 披露 |
| 画报示意：保留率三横条按 38.7/40/39.3 绘制；违约三步 23.75→17.50→21.25 为原文数字排布，非原图 | 自绘 |

## 展示缩窄

- 表2 只取 UniCraft(Astra) 一行与 X-VLA/π₀.₅ 对照；Gemini 77%（LIBERO-PRO）未展示，方向一致。
- robosuite 表按 2K 步列出；Terra 4K（62.0）未展示，画报注记"长任务更好"以 Astra/Sol 为据。
- "跨本体复用靠执行契约"为论文题名（Alignment Drives Reuse…Enforced Action Contracts）的转述，非我们的额外推断。
