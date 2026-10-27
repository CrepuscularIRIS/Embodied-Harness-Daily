# selection-004 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽）；日期 2026-10-27
- 本仓第四期。前三期 21 篇（run embodied-full-v11-20261022 selection-001/002 共 18 篇；本 run selection-003 共 3 篇）不再重复入选，只用作同题/类型对照。
- 候选池：本 run 最新记录中 P3 / confirmed / to_l3 共 9 篇（inc-l2-03：32348，上期第一备选；inc-l2-04：34370、34108、33487、33446、35817、34649、33718、34151）。无 P2 confirmed 编辑候选。
- 结果：入选 3 篇，3 张均 ready（其中 2 张经总控授权的额外单行修复轮后通过）；同题去重 4；与前期已选重复 1；多样性截断 1；correction 1（退回 Sol，未入选篇）。
- 档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。未运行论文代码，未复现。

## 候选（9 篇）

| paper_id | 标题（简） | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2610.35817 | Pretraining Knows What, Simulation Teaches How（ZAP） | P3 | capability | F3,F1 | harness_native_rl / observe_act_interface | **入选 #1** |
| 2610.34370 | ThinkLocoManip | P3 | capability | F0,F3 | observe_act_interface / planner_composes_code_and_policies | **入选 #2** |
| 2610.32348 | LogLook | P3 | judgment | F1,F5 | harness_memory_skill_reuse / harness_effect_evaluation | **入选 #3** |
| 2610.33446 | MOTIO | P3 | capability | F3,F1 | code_policy_trial_revision / planner_composes_code_and_policies | 同题去重 → 34370 |
| 2610.33487 | ReSight | P3 | capability | F3,F4 | harness_memory_skill_reuse / harness_self_optimization | 同卡去重 → 32348（下期记忆/自优化槽首选备选） |
| 2610.33718 | RoboJev | P3 | judgment | F2,F3 | external_verification_control / harness_effect_evaluation | 同题去重（judge 对内较弱） |
| 2610.34151 | Execution Logs Sway VLM Judges | P3 | judgment | F2,F4 | external_verification_control / harness_effect_evaluation | 暂停：correction C004-1；同题对内本属保留篇 |
| 2610.34108 | RoboDuo | P3 | capability | F2,F0 | external_verification_control / planner_composes_code_and_policies | 与前期已选重复 → 2610.32941（s003） |
| 2610.34649 | RobotAgentBench | P3 | judgment | F1,F0 | harness_effect_evaluation / external_verification_control | 多样性截断 |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2610.35817 | harness 内 RL，仿真→真机/新本体 | 同一 27B 模型在同一工具 harness 里，只在 40 个仿真任务上用自采成功轨迹 SFT＋GRPO 补“运动”：真机 10 任务 Base 5/30 → 29/30；同一 Astra 只换 harness 11/30 → 29/30（Table 3、附录 Table 6）。两条单因素对照分别回答“模型训练”与“harness”各贡献多少；仿真 Franka 新本体 55.9%。前 21 张无 harness_native_rl 类型。 |
| 2 | 2610.34370 | 全身控制工具化的腿足移动操作 harness | 把机身速度/姿态作为 LLM 可调用工具，执行—检查—重排循环；真机五个长任务 54/70 vs plan-then-act 26/70（Table II）；去掉姿态工具地面抓取 18/20 → 0/20（Table III）。前 21 张无腿足/移动操作本体（Fly0 为无人机、AIDA 为导航）。 |
| 3 | 2610.32348 | harness 记忆与其评测方法 | 上期第一备选。同代码同执行器只换记忆：成功 237 vs 234，但 token 40.5k vs 71.3k、图像 46 vs 114；学习型执行器下 104 = 104、分歧 14 个中 12 个由执行器决定；Table 9 逐回合原因显示笔记记忆 19 次失败中 13 次属“记住/看到”。改变的是“只看总成功率比较记忆设计”的做法。闭环（仿真）证据。 |

### 画报侧重（已制作）

- **2610.35817**：训练/部署流程带；“模型 × harness”两因素格（5/30、29/30、29/30、11/30，未测格留空）；逐任务 10×5 热格；仿真训练阶梯；时间/费用条；Franka 条（标“仍在仿真、对照为排行榜”）；§5 单次演示条（标“无成功率”）。
- **2610.34370**：4 域 11 工具格（运动域高亮）；plan-then-act vs 边想边做循环示意；五任务逐次方块图（每格一次真机试验）；消融、干扰、户外三张小方块图。注明 Avg 77.0/77.1/73.0 口径、消融沿用主表试验、plan-then-act 技能配置未说明。
- **2610.32348**：记忆分工三栏（系统记/模型挑/对照）；两执行器大数字对照；成本条；分歧回合原因方块账本（Table 9）；组件消融表。不写成功率提升。

## 排列、去重与多样性（编辑理由，均有原文依据）

1. 9 篇均为 P3/confirmed；capability 5、judgment 4，并列不分先后，不按数值排序。
2. **同题去重：2610.33446（MOTIO）→ 2610.34370。** 二者都是 LLM/编码智能体为腿足/人形本体组合全身控制能力（共享 planner_composes_code_and_policies）。保留 34370：真机五任务 70 次试验、三个基线、消融和干扰实验（Tables II–V）。MOTIO 真机只有两段各一次的连续执行（101.75 s、98.41 s，§4.1 Table 1），无一次性代码/经典控制器/无视觉基线；螺丝残差 269.44 → 64.58 μm 是 MuJoCo 仿真反馈（§3.3、§5.2），而摘要与 Fig. 9 图注写作 “physical refinement”；共享策略 18/18 是在开发任务上（§6）。问题也不完全相同（人类视频 → 机器人程序），但在 3 篇上限下不并列。
3. **同卡去重：2610.33487（ReSight）→ 2610.32348。** 同属 harness_memory_skill_reuse。两者问题不同（ReSight：证据已在记忆里但工具做不了所需计算，由编码智能体离线探索并蒸馏成工具；LogLook：规划器的工作记忆由谁记、看什么），按 SELECTION.md 同卡保留一篇。保留 32348：其结论来自闭环执行（RoboMME 800 回合、256 回合配对），且是上期已核对的第一备选。ReSight 证据扎实（冻结工具在未参与探索的 81–90 回合 37.5 → 65.8%，去掉探索只到 46.4%，Table 4），但评测是记忆问答：附录 C.4 写明真机评测时 “Robot motion is disabled”，下游导航只在附录 E.4 以图示展示、无计数；按 docs/EVIDENCE.md 属 offline 级。另与 s001 MemER（记忆）、2610.25114（自我改进归因）类型相邻。列下期记忆/自优化槽首选备选。
4. **judge 同题对：2610.33718（RoboJev）与 2610.34151。** 同属 external_verification_control，都问 VLM judge 的信号能否当作成功/进度真值。34151 的受控干预更直接（同帧只换一行日志，有中性句与重复调用对照、倒序一致性筛选，§3 Table 1），本应保留；但其 Q2 判断存疑，按规则暂停并退回（C004-1）。33718 作为保留篇证据偏弱：同输入跨域 AUROC 差 −0.0092，CI [−0.0218, 0.0026] 含 0，仅单次训练（§5.2、§5.4），公开测试集开发时已被查看（§3.3），训练标签来自同时作为基线的前沿模型（附录 C.1）；且 s001 已有 GVL（2411.04549）占验证信号槽。故本期两篇均不入选。
5. **与前期已选重复：2610.34108（RoboDuo）→ 2610.32941（s003 Backtrack）。** 同为冻结 VLA 一次尝试失败后的外部检测＋恢复（external_verification_control / K202），同在 LIBERO-Long 上报提升。RoboDuo 另需训练 atomic VLA 与 judge，且无等时长重跑完整 VLA 的对照（§4，L2 已记）；Backtrack 已有两倍步数对照。按 PROBLEM_CORE §4 priority 下调理由“与已选论文内容重复”处理，不改记录。
6. **多样性截断：2610.34649（RobotAgentBench）。** 问题成立（操作分数高≠能自主发现任务与恢复，Table 1–2）；但与已选的 EmbodiedEval（2501.11858）、RoboCerebra（2506.06677）同为“benchmark 揭示能力鸿沟”类型，架构比较同时改变多部件、无配对区间（§3.1–3.3），RSI 只报第 10 轮。3 篇上限下让位于填补新类型的 35817、34370 与已排队的 32348。
7. 入选 3 篇覆盖 F0、F1、F3、F5；capability 2、judgment 1。
8. later_work：9 篇均无 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标 v1（九篇缓存头均为 `FULLTEXT: html`，实际均为 core 裁剪版）。为满足“读完整原文及必要附录”，九篇均补读同版本 arXiv HTML（`https://arxiv.org/html/<pid>v1`，2026-10-27 取得，转换稿仅在 /tmp，不提交）。

| paper_id | 读到范围 | 结论 |
|---|---|---|
| 2610.35817 | 正文＋附录 A–E（Table 6 逐任务） | 通过，无 correction。附录 A 确认仿真中策略不读物体位姿真值（L2 K703 Operation 的待核项可视为成立）；真机任务从 RoboLab-120 任务表复刻、与训练同族；17× 为自托管折算对 API 账单。 |
| 2610.34370 | 正文全文（无附录） | 通过，无 correction。Avg 77.0 为合计 54/70=77.14% 的写法（任务平均 73.0%），L2 已注意；§III-D 关键帧定义补齐；消融“Ours”沿用主表试验；plan-then-act 是否有技能未说明。 |
| 2610.32348 | 正文＋附录 A–C | 通过，无 correction（与 selection-003 一致）；Table 9 逐条加总与 §4.2 文字一致。 |
| 2610.33446 | 正文全文（HTML 无补充材料 S1–S7） | 无 correction。§6 现可读：BC 2/10 → D7 10/10 是逐步开发接口的过程，18/18 为开发任务，L2“不据摘要 18 任务确认蒸馏贡献”成立；摘要/Fig. 9 “physical refinement” 与正文“simulation feedback”不一致，L2 facts 已按仿真记。补充材料 S1–S7 未获取（needs_material，仅影响画报，不影响本期去重）。 |
| 2610.33487 | 正文＋附录 A–E | 无 correction。L2 facts 一致；真机 12/30 → 30/30 中 3 个任务即探索任务本身，未参与探索的 3 个任务为 9/15 → 15/15（Table 5），L2 合并报告但已在 K401 注明新楼层/新查询；记忆问答、真机评测时运动关闭（附录 C.4）。 |
| 2610.33718 | 正文＋附录 A–D | 无 correction。facts 一致。P2→P3 的“诊断阅读”依据偏弱（CI 含 0、单次训练），属阅读判断，不作 correction。 |
| 2610.34151 | 正文＋附录 A | facts 一致；**Q2 判断存疑 → correction C004-1**。 |
| 2610.34108 | 正文全文（文中所称附录未见于 HTML） | 无 correction。facts 一致；真机切换规则与 GPT-6 Astra 判定见 §4.4，附录未获取，不影响去重。 |
| 2610.34649 | 正文＋附录 A–D | 无 correction。facts 一致；附录 D 给出四个行为指标的操作定义。 |

## Correction（退回 Sol 单篇修订；保留原记录，不改批次文件）

**C004-1 · 2610.34151（inc-l2-04 记录）**

- 原判：Q2 `open_failure`，P3 / `confirmed` / to_l3；L2 已注明 “首版前 Xu[10] 已在 video-generation verifier 做过日志攻击”，以“机器人 progress 与标注/反序条件”为同条件缺口。
- 问题：按 PROBLEM_CORE §3 Q2，`vertical_port` 指“只换了应用对象，问题约束、机制和可用能力都没变”。原文自述为移植：§1 “Xu [10] showed that execution logs sway the verifiers of video-generation agents. We carry this diagnosis to robot progress judges.”；§5 小标题 “The diagnosis transfers.”。干预方式（帧固定、只变日志文本）与 Xu [10] 相同（§2）；“提示缓解以召回为代价”也已见于 Khalifa et al. [4]（§2）。机器人场景新增的只有片段长度/位置与标签相关的混杂及相应的倒序一致性筛选（§3 Primary measure），这是测量控制，不是问题约束的改变；可写日志进入机器人 judge 的部署频率作者明言未测（§5 Limitations）。
- 影响：若改判 `vertical_port`，按封顶规则最高 P1，`next_action` 不再是 to_l3。
- 建议：Sol 单篇复核 Q2。若维持 `open_failure`，需写明机器人场景具体改变了哪条约束（候选：进度方向判定这一任务形式、逐区间挑选的完成声明攻击），并说明为何不属于 vertical_port。本条依据为原文自述与引文，不否认该文的测量价值；未运行代码。
- 本期处理：该篇暂停，不入选；correction 不影响本期成品。

## 待补与漏检抽查

- 待补（priority=high、未 confirmed，不在本期候选池，补齐后由 Sol 单篇 L2）：
  - pending_material：2610.26659（缺附录 A/B 与场景/目标数冲突）；2610.32208（缺附录 B–D 续采样策略、恢复样本数）；2610.32633（缓存截断于 §4.2，缺 §§4.3–6）；2610.30587（C003-1 退回后 needs_material：CRR 计数口径）。
  - pending_experiment：2610.30197、2610.30478、2610.31427、2610.31613（Table IV 0.72 vs 0.78 冲突）、2610.35051（缺独立最终留出与 rollout 账单）、2610.34527（缓存缺 §6 主要结果，sim/real 预算不匹配）。
  - medium 待补（参考）：2610.31013、2610.31518、2610.32554、2610.32776。
- 本期补读中顺带发现的材料缺口（非候选池阻塞）：2610.33446 补充材料 S1–S7、2610.34108 文中所称附录均未出现在 HTML，未获取。
- 漏检抽查：inc-l2-04 已补抽 2610.33044（维持排除，改判 0/1）；本期无新抽查改判结果；累计欠账约 1.2 篇（progress.md）。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2610.35817 | **ready**（第 1 次渲染溢出/裁切，重做一次后通过） | `reel/2610.35817/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2610.34370 | **ready**（第 1 次溢出/标签压线，重做一次后仍有 1 处“感知”框文字溢出 → 记 fail；总控授权额外一轮单行修复后第 3 次渲染通过） | `reel/2610.34370/`：同上 |
| 2610.32348 | **ready**（第 1 次限定语断行/成本图过小，重做一次后限定语仍断行 → 记 fail；总控授权额外一轮单行修复后第 3 次渲染通过） | `reel/2610.32348/`：同上 |

- 额外修复轮由总控 2026-10-27 授权（仅此一轮），每张只改一行文字；改动与复看记录见各篇 QA.md。
- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（表头张数 21→24、近三月表新增 3 行、“选择与制作”新增本期条目）；`README.md` 第 9 行本季漏斗统计行（21 → 24 posters），其余段落未动。
