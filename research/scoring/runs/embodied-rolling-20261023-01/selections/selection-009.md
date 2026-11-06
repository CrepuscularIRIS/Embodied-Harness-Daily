# selection-009 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽，单席串行）；日期 2026-11-05
- 本仓第九期。前八期 36 篇（run embodied-full-v11-20261022 selection-001/002 共 18 篇；本 run selection-003–008 各 3 篇）不再重复入选，只用作同题/同卡对照。
- 候选池：8 篇 = inc-l2-09 最新 L2 记录中全部 P3 / confirmed / to_l3（06863、06768、06881、06475、06434、06653、05567、06453），与 progress.md 2026-11-06 06:17 班一致。无 P2 confirmed 编辑候选（00405 为 P2 / park，无编辑理由）。
  - 不在本期池：上期首选备选 2611.02391；C008-2 修订后维持 to_l3 的 2611.04226（progress.md 记“下期候选”）。均按总控派发的池范围不讨论，留待总控决定是否并入下期。
- 结果：入选 3 篇，3 张均 ready（每张首轮渲染不过、重做一次后通过）；与前期已选同卡重复 1（06768）；范围与代表性让位 2（05567、06475）；证据不足以展示 2（06881、06653）。本期 **correction 0**。
- 档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。未运行论文代码，未复现。

## 候选（8 篇）

| paper_id | 标题（简） | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2611.06863 | Rethinking Self-Repair in Code-as-Policy Agents | P3 | judgment | F1,F2 | code_policy_trial_revision / harness_effect_evaluation | **入选 #1** |
| 2611.06434 | EviSeek: Evidence-Centric Agentic Framework for Active EQA | P3 | judgment | F2,F5 | harness_memory_skill_reuse / observe_act_interface | **入选 #2** |
| 2611.06453 | Beyond Infraction Scores: Failure-Boundary Profiles | P3 | judgment | F2,F3 | harness_effect_evaluation / external_verification_control | **入选 #3**（B 类评测方法） |
| 2611.06768 | PyRUA-REAL: Embodied RSI in the Real World | P3 | capability | F3,F1 | code_policy_trial_revision / harness_self_optimization | 与前期已选同卡重复 → 2610.31841（FORCA，s003）、2610.36533（RoboAuto，s005） |
| 2611.06653 | Detecting Silent Action-Interface Mismatch | P3 | capability | F2,F1 | observe_act_interface / external_verification_control | 证据不足以展示（离线回放、外部数据全部未过门槛） |
| 2611.06881 | VABAR: Variational Automation Benchmark | P3 | judgment | F3,F0 | harness_effect_evaluation / code_policy_trial_revision | 证据不足以展示（参考解跨实现不稳、无区间） |
| 2611.05567 | MESA: Compositional, Semantic, Spatial Generalization | P3 | judgment | F3,F1 | harness_effect_evaluation | 范围与代表性让位（列下期备选） |
| 2611.06475 | RoboCasa-Mem: Environment and Process Memory | P3 | judgment | F4,F2 | harness_memory_skill_reuse / harness_effect_evaluation | 范围与代表性让位（记忆槽） |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2611.06863 | 代码即策略：重试收益归因（对照研究） | F1 归因问题最干净的一篇：同一 252 个首轮失败、同模型同解码同重试上限，只换反馈来源。对再抽样 +17.1 [9.9, 24.2]（固定 token 预算下仍 +15.9/+14.7）；换成别的回合、不同标签的反馈（627/627 均为不同标签，附录 B.3）或每任务一段固定模板，点估计 86.1 均不低于本次失败模板 85.3。另有 700 新场景“第一次就给指导”与反例（nut insertion −15.0 [−27.5, −2.5]）。前 36 张里代码修订卡已有 REFLECT、2512.02002、FORCA、RoboAuto，均把执行反馈当有效信号；本篇正是检验这一前提，问题不同。与 s005 的 2610.37196（Best-of-N 上界多为续跑运气）同属“收益是不是采样”，但对象（代码修复反馈 vs VLA 选择器）和卡片不同。 |
| 2 | 2611.06434 | 主动具身问答 harness：证据需求驱动采集与保留 | 不训练、同骨干、同动作接口与 30 步上限，Qwen +7.1 [5.2, 9.0]、Gemini +3.7 [2.0, 5.4]（3,436 题配对），调用与 token 同时下降。消融把在线收益定位到“需求”（去需求 46.6，基线 45.6），固定轨迹重答把证据板与同容量选择性保留分开（−5.1/−5.3）。前期记忆类两次以“离线问答评测”让位（s005 ReSight、s006 38318）；本篇是在线主动取证，问题是“动作是否取得并留住回答证据”，与 MemER、LogLook（记什么、谁挑看）不同题；与 s008 的 04080（预建表示 vs 指令后回看）同属信息访问但机制不同（主动交互取证 vs 回看已录扫描）。展示时用我们按表 1 计算的分题型贡献，写明增益集中在空间关系与感知定位、度量比较两骨干都退步。 |
| 3 | 2611.06453 | 评测方法：承诺/能力两条曲线与认证标签 | 本池判断最硬的反例：堵死走廊上硬闯的 SimLingo 驾驶分 52.2 高于每次都停的代理（37.8–40.6）；BridgeDrive 驾驶分第 4、决策准确率垫底。仓储导航两个微调版通过更多却在堵死处 0/15 停（发布版 15/15），平均 DA 反而上升。外部验证/STOP 门控槽现有画报都只报单一成功或安全分，本篇给出可复测的“停没停”和“过没过”分开计量法。收录范围：被测对象均无 LLM/VLM harness，按 EVIDENCE B 类评测方法学收录（先例 s007 的 2610.41857），画报顶部与限制栏明示，迁到 harness 门控标为阅读判断。 |

### 画报侧重（已制作）

- **2611.06863**：提示词组成色条＋同行恢复率条（标出唯一被替换的反馈块）；四行判决表；700 新场景“首轮 / 重试补上”两段堆叠条带 token 列；边界键值表（nut insertion、温度 0.2、32B、改写与批评、7 设定汇总）；作者评测清单。限制栏写明“未检出 ≠ 等效”、两个对照同时改生成指令、标签未人工审计。
- **2611.06434**：深色题带；出处链示意（需求→子任务→意图→证据板＋答题条，含基线停止规则）；分题型贡献双条图（我们按表 1 计算）；在线/固定轨迹两栏消融数阶；用量表（Gemini 步数增加标红）；EXPRESS-Bench 表（Fine-EQA 有据正确率更高标红）。
- **2611.06453**：警示斜纹题带；Charger 边界尺（承诺/能力双条＋橙色缺口，按原文边界值重绘）；堵死宽度驾驶分柱条＋12 格结局计数；驾驶分 vs DA 名次连线；仓储微调前后对照表；对向车流须等窗口计数条。

## 排列、去重与取舍（编辑理由，均有原文依据）

1. 8 篇均为 P3 / confirmed；q3：judgment 6、capability 2，不分先后，不按数值排序。
2. **与前期已选同卡重复：06768（PyRUA-REAL）→ 2610.31841（FORCA）、2610.36533（RoboAuto）。** 同为编码代理靠真实/仿真执行反馈反复改机器人程序并沉淀技能；s007 的 41216 亦在 harness 自我优化位。证据也不足以给出“有完整对照条件的结果”：真机 91.1% 是跨程序版本的开发期累计（§4.3.1 作者自述非单一冻结程序可靠性）；唯一受控对照（§4.5 B/BS/BVJ 15.3/45.8/54.2%）每格只有一次开发会话，且 BS 含真值物体状态；reviewer、显式规格、技能库三项比较都是顺序阶段或含额外探索（§4.4、§4.6 作者自述）；RoboDojo 对比是不同或未说明种子的报告值，引言 84.82% 与正文 84.42% 不一致（L2 已记）；人工曾建议 SigLIP 并协助误接触诊断（§5）。RSI 仓 selection-010 亦未选，本席独立判断结论相同。不改记录，不列备选。
3. **证据不足以展示：06653（动作接口错配检测）。** 问题清楚（形状与值域合法但轴、符号、极性错配），但全部证据是 LIBERO 回放上的离线检测：坏动作从未执行（后继状态属于原动作，§3.1），匹配 FPR 为事后曲线（§4、§5.2），DROID、HYDRA 三任务、短时延、小偏移、精确修复和仿真缓解全部未过各自门槛（§6 表 2），xArm 只有一个任务；回路中没有 LLM/VLM harness。能展示的结论只到“同一数据约定内的离线诊断”，不足以做一张 harness 画报。阅读判断，不作 correction：L2 已把确认范围限定为“B 类离线接口审计”，档位依据（问题成立且开放）不受影响。不列备选。
4. **证据不足以展示：06881（VABAR）。** 基准设计对本领域最贴题（编码代理＋技能库＋同栈人写参考图），但表 II 的主结果没有区间或配对说明；人写参考图在 Newton 与 Isaac Lab-Arena 两个实现间差别很大（Syringe L2 63.0 vs 40.0、Cable Routing L2 46.7 vs 5.0、Tool Sorting L1 47.1 vs 20.0，§VII-D 作者归因于纹理、场景与光照），与其“可重复”设计目标尚未对上；GaP 自动生成图的开发与留出、所用反馈未写明；GaP 对裸 Claude Code 同时加了 harness 与技能库（作者自述未拆）；失败归因表无干预。阅读判断，不作 correction（L2 已把这些列入 biggest_gap，Q1–Q4 依据不变）。等后续版本补区间与开发隔离再议，不列本期备选。
5. **范围与代表性让位：05567（MESA）。** 研究判断扎实（四条可控泛化轴、匹配 ID/OOD、语言跟随率 L = S/(S+D)、RoboArena 名次大体一致），但主体是 VLA 微调基准；与 harness 相关的只有附录 B.7 一行零样本 GPT-6.1-Sol 工具调用 harness（每任务 10 次、常规 50 次），本身不是受控对象。本期 B 类评测位给了 06453（反例更直接、可迁到停止门控）。**列下期首选备选**，若届时池中缺评测方法类可兑现，画报须以 VLA 基准为主体、harness 行只作旁注。
6. **范围与代表性让位：06475（RoboCasa-Mem）。** 行为条件评测（后续合法目标由机器人自己的早先动作决定）是新的评测条件，但记忆槽已有 MemER、LogLook，且本期 06434 已占信息获取与保留位；HMAP 是示范监督训练的分层策略（Qwen3-VL-4B 规划器＋π0.5），增益集中在隐属性回忆（TempReport .22→.86），两个多任务调度任务所有方法 SR 为 0，真机只有 1 个任务各 10 次；§5.3 累加消融不能把 24% 对 16% 全归记忆（L2 已记）。不列备选。
7. 入选 3 篇覆盖 F1、F2、F3、F5；q3 均为 judgment（capability 两篇分别按同卡重复与证据不足落选，非按类型排除）。对象分别为仿真桌面代码策略、仿真主动问答（含导航变体）、驾驶与仓储导航评测。三篇主卡不同（code_policy_trial_revision / harness_memory_skill_reuse·observe_act_interface / harness_effect_evaluation·external_verification_control），不算同题。
8. later_work：8 篇均无 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标版本。8 篇缓存头均为 `FULLTEXT: html`、v1，均为 core 裁剪版。入选 3 篇另取同版本 arXiv HTML（2026-11-05，转换稿仅在 /tmp，不提交）补读缺失节与全部附录；未入选 5 篇按缓存正文核对 L2 facts 与落选理由（落选理由所引数字均在缓存正文内）。

| paper_id | 版本 | 读到范围 | 结论 |
|---|---|---|---|
| 2611.06863 | v1 | 缓存 §1、§3–6＋HTML §2、附录 A–D | 通过，无 correction。附录 B.3 补足 L2 所缺 fallback 比例（627/627 不同标签，无 fallback）；附录 A.3 的开发选定、标签未人工审计写入限制栏。 |
| 2611.06434 | v1 | 缓存 §1、§4–6＋HTML §2、附录 A–J | 通过，无 correction。附录 D 确认主比较同时改规划、保留、答题上下文与停止方式，写入限制栏；分题型贡献为我们按表 1 计算并在 SOURCE.md 标明。 |
| 2611.06453 | v1 | 缓存全部＋HTML §2、§3.3–3.4、§4.4、Limitations（该版无附录） | 通过，无 correction。§3.4 认证流程与 L2 判断一致；收录按 B 类评测方法，理由记于其 SOURCE.md。 |
| 2611.06768 | v1 | 缓存 §1、§3–5（§4.8 尾与附录缺） | 无 correction。facts 一致（88.7→98.7%；B/BS/BVJ 15.3/45.8/54.2%；新任务 40.0 vs 21.3%；84.42 vs 引言 84.82）。 |
| 2611.06653 | v1 | 缓存 §1–6、§10（§6 后半、§7–9 缺） | 无 correction。facts 一致（2.5% 匹配 FPR 召回 46.08/60.96/65.66；定位 95.81/94.62；实际 FPR 2.63/3.22/2.85）。 |
| 2611.06881 | v1 | 缓存 §I、§III–VIII（§VIII 尾缺） | 无 correction。facts 一致（Newton gear 人写 100/90、GaP 70/60、裸 Claude 0/0；GaP 高于裸 Claude 11/12，余下 1 格 Tool Hanging L2 并列 10.0，与表 II 一致）。 |
| 2611.05567 | v1 | 缓存 §1、§3–6 | 无 correction。facts 一致（π0.5 BiMESA 48.7%、Category 18.6%；GPT-6.1-Sol 42.8% 每任务 10 次）。 |
| 2611.06475 | v1 | 缓存 §1、§3–6（附录 A–C 缺） | 无 correction。facts 一致（HMAP 平均 SR .24 vs .16；TempReport .86 vs .22、条件回忆 .90 vs .41；累加 .20/.34/.40/.46；真机 8/10 vs 2/10）。 |

## Correction

本期无。未入选 5 篇的落选均为阅读判断（同卡重复、证据不足以展示、范围与代表性），不涉及 L2 字段错误。

## 待补与漏检抽查

- 待补（priority=high、未 confirmed，不在本期候选池，补齐后由 Sol 单篇 L2；见 progress.md 2026-11-06 06:17 班）：2611.06654（pending_material：缺方法后半与 §5，LLM/VLM 链路未确认；若确认只是纯 VLA 离线 RL/权重合并按 EVIDENCE 排除）；2611.06184（P3 / pending_experiment：缺同 Astra/历史条件的固定间隔或 always-replan 实跑、监控 FP/FN）。前期遗留待补项见 selection-008 与 progress.md，本期未变动。
- 漏检抽查：inc-l2-09 名额 1、池 0，欠账约 3.3 滚存（progress.md）；本期无改判。
- 下期备选：首选 2611.05567（理由见上第 5 条）。06768 按同卡重复、06653 与 06881 按证据不足、06475 按记忆槽让位，均不列备选。02391、04226 不在本期池，由总控决定是否并入下期。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2611.06863 | **ready**（第 1 次页底空白约 135 px、参考线标签挤在刻度旁 → 重做一次后通过；同轮再改两处孤字） | `reel/2611.06863/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2611.06434 | **ready**（第 1 次箭头压字、消融标签孤词、左卡底部空白约 90 px → 重做一次后通过） | `reel/2611.06434/`：同上 |
| 2611.06453 | **ready**（第 1 次超出页面/PDF 2 页、边界尺两行相挤且标签压条 → 重做一次后通过；同轮再改一处断行与页脚边距） | `reel/2611.06453/`：同上 |

- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（张数 36→39、增量 run 18→21 张、新增 3 行、“选择与制作”新增本期条目）；`README.md` 第 9 行本季漏斗统计行（追加 “8 P3-confirmed → +3 posters”，36 → **39 posters**），其余段落未动。
