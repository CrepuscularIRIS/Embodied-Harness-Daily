# selection-008 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽，单席串行）；日期 2026-11-04
- 本仓第八期。前七期 33 篇（run embodied-full-v11-20261022 selection-001/002 共 18 篇；本 run selection-003–007 各 3 篇）不再重复入选，只用作同题/同卡对照。
- 候选池：8 篇 = 上期首选备选 2610.41044（inc-l2-07）＋ inc-l2-08 的 7 篇 P3 / confirmed / to_l3（01560、04255、04226、04080、02391、05058、00344）。无 P2 confirmed 编辑候选。
  - 记录核对：progress.md 2026-11-04 班把 inc-l2-08 的 7 篇写成 “…/05058/03850”；按 batches 最新记录，2611.03850 为 P2 / confirmed / **park**，第 7 篇应为 **2611.00344**（P3 / confirmed / to_l3）。本期按记录取 00344；progress.md 的 pid 笔误请总控更正（本席不改共享进度）。
- 结果：入选 3 篇，3 张均 ready（每张首轮渲染不过、重做一次后通过）；与前期已选同卡重复 2（04226、05058）；证据不足以展示 1（04255）；范围与代表性让位 1（02391）；暂停并退回 1（00344，correction C008-1）；另对未入选的 04226 记 correction C008-2。
- 档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。未运行论文代码，未复现。

## 候选（8 篇）

| paper_id | 标题（简） | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2611.04080 | FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation | P3 | capability | F4,F2 | observe_act_interface / external_verification_control | **入选 #1** |
| 2611.01560 | Democratizing Robot-Use Agents: A Unified Harness with Open Models | P3 | capability | F1,F4 | observe_act_interface / harness_effect_evaluation | **入选 #2** |
| 2610.41044 | Consensus Within, Competition Between（LLM 周界防御团队） | P3 | judgment | F1,F4 | multi_robot_llm_coordination | **入选 #3**（上期首选备选） |
| 2611.05058 | Do Agentic Policies Need to Look at Every Step?（几何抽象接口） | P3 | judgment | F1,F5 | observe_act_interface / planner_composes_code_and_policies | 与前期已选同卡重复 → 2610.41844（SketchMate，s007） |
| 2611.04226 | DiMuRe: Diagnosis-Guided Multilevel Recovery | P3 | capability | F2,F1 | external_verification_control / planner_composes_code_and_policies | 与前期已选同卡重复 → 2610.40016（LOGIV，s006）；另记 C008-2 |
| 2611.04255 | ActOR: Ambient AI Orchestration for Humanoids in ORs | P3 | capability | F4,F2 | observe_act_interface / external_verification_control | 主效应证据不足以给出完整对照的结果 |
| 2611.02391 | Late Autumn: LLM Agents Specialize a Multi-Robot Planner | P3 | judgment | F1,F3 | harness_self_optimization / harness_effect_evaluation | 范围与代表性让位（列下期备选） |
| 2611.00344 | SPARK: Self-Correcting Embodied Memory via Physical Re-Observation | P3 | capability | F2,F5 | harness_memory_skill_reuse / external_verification_control | **暂停，C008-1 退回 Sol** |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2611.04080 | 移动操作 harness：指令后按需定位＋执行闸门（真机） | 信息访问（F4）问题清楚：预建场景表示在指令未知时压缩信息，任务属性可能丢失。103 条查询、人工判定，预建最强 TextMap 68.0% vs 指令后回看原始帧 94.2%；分类型看，预建表示失分集中在“集合”“推理”。附录 Table 4 显示整扫描 VLM（Gemini 3.8 Flash 96.1%）同样胜过预建表示，**支持路线、削弱 Fido 流程本身**，画报据此缩窄。另有 Spot 真机 50 次（35 完成，失败 13/15 来自物理技能）与三项执行闸门小消融。前 33 张无“预建图 vs 按需取证”的画报；与 s007 SketchMate（精度从哪来）、s004 ThinkLocoManip（机身姿态工具化）问题不同。 |
| 2 | 2611.01560 | harness 效应：开放模型、无特权输入 | 判断“开放模型不会用机器人”的前提是否属于接口问题。最干净的对照是同一 Qwen3.8-Flash-Next、同 42 任务换四套 harness：Score 1.90 / 7.75 / 21.01 / 31.39；同一 harness 内的几何信息消融显示标定（不是模拟器深度）承载几何：31.39 → 9.13（去标定）vs 35.89（加深度）；去技能库仍 96.6%。与 s004 ZAP（2610.35817，小 VLM 在 harness 内训练）问题不同：本篇不训练，问的是零样本时接口与可部署信息带来多少能力。摘要头条“超过 Astra-RoboProbe”在抽样波动内且跨 harness，画报单独成卡打折。 |
| 3 | 2610.41044 | 多机器人 LLM 协调：架构与权限 | 上期首选备选兑现。多机器人协调卡在前 33 张中空缺；本池统计设计最严：主比较预先确定、共同随机数配对种子、按种子算区间。各自为政队与共识队只差拍卖消息开关，冲突消解被配对隔离（15% vs 29%，−14 点，−22 到 −6）；低价模型拿高权限 +38 点（+30 到 +45，探索性）。selection-007 的三条顾虑（抽象质点仿真、无纯 CBAA 基线、照片实验 5 种子）全部作为画报限制展示，不弱化。 |

### 画报侧重（已制作）

- **2611.04080**：信息双路线图（含压缩漏斗）；分组点图带耗时·费用列，把整扫描 VLM 放进同一张图；查询类型方阵（每类条数由百分比反推并注明）；编号闸门卡（三项消融各注样本与选样偏差）；真机分段结局条（18/17/13/2）。
- **2611.01560**：同模型四 harness 柱图＋Astra 参照，橙框标附录 G 抽样波动量级；harness 六项设计清单；几何信息三档阶梯；§4.2 失败类型表；“超过 Astra 要打折”对决卡；费用与到 25 分时间；模型胶囊带。限制栏写明真机 v1→v2 改动未解释。
- **2610.41044**：深色题带＋竞技场示意；三队拓扑卡（大数）；按入侵数分组条（差距集中在 4 架）；权限开关卡与表（标“探索性”，近前沿“只追平、没有更好”）；照片三行情形表。

## 排列、去重与取舍（编辑理由，均有原文依据）

1. 8 篇均为 P3/confirmed；q3：capability 5、judgment 3，不分先后，不按数值排序。
2. **与前期已选同卡重复：05058 → 2610.41844（SketchMate，s007）。** 两篇的机制是同一家族：VLM/LLM 只做符号与决策，度量交给本地标定几何工具（observe_act_interface “几何保留于校准工具”）。05058 对照很干净（同骨干、同传感执行、100 个留出布局；在线 50 对，Bridge 28/50 vs 12/50、搬塔 42/50 vs 15/50，图像附件 10.94 → 2.72），但上期刚以同一机制入选，接连两期同质；且其感知靠颜色分割＋规则形状先验（附录 C），几何组还多了算子与检查点，未拆出“文本符号”单因素（L2 已记）。按 PROBLEM_CORE §4 “与已选论文内容重复”处理，不改记录；不列备选。
3. **与前期已选同卡重复：04226 → 2610.40016（LOGIV，s006）。** 同一问题：扰动只破坏部分动作前提时保留仍有效的程序、只修失效部分。恢复/门控槽已有 REFLECT、Backtrack、Best-of-N、LOGIV、2610.39775。另外主结果 Local（77.65% vs 58.68%）的 L1/L2 分支是规则与 GraspVLA，**不含在环 LLM**；LLM 只在 Full 的终端改码里，且 Full 多了步数预算与提前交接，无法单独归因（作者亦承认）。再加 C008-2 所记的子集问题。不列备选。
4. **证据不足以展示：04255（ActOR）。** 两项核心对照都给不出“有完整对照条件的结果”：环境相机对照的成功率 80% vs 66.7%（局部不可见组）与 80% vs 73.3%（可见组）Wilson 区间重叠，作者自己写需更大样本，可信的只有探索次数 1.05 → 0.12；闭环对照的基线 Open-loop 在第一次技能失败即结束回合（重试与重规划一起去掉），是弱基线，闭环重规划本身已有 Inner Monologue 等先例。真机 20 次处置 14 次成功无对照。这是阅读判断，不作 correction：L2 的确认范围已窄到“不宣称环境相机单独因果增益”，档位依据（局部可见 → 现场环境观测的信息访问变化）成立。不列备选。
5. **范围与代表性让位：02391（Late Autumn）。** 研究判断有价值：隐藏种子评分＋强制提交评估生命周期，六条补丁在 20 个新种子上全胜 +22–63%，40/42 个迁移格为正，代码审查发现分数看不到的问题（880 ms 后另起 1 s 期限、蒙特卡洛重抽、最高 112× 规划算力）。让位理由：(a) 部署物是不含 LLM 的经典规划器、对象是网格 MAPF，具身性与 41044 同样抽象，本期多机器人位已给 41044；(b) 基线有停机判据 bug（只用 <1% 预算），收益部分来自“用掉闲置算力”，没有修好 bug 的廉价基线或等算力对照（L2 已记）。收录范围按“具身场景下的 harness 自我优化”维持（与 s005 RoboAuto、s004 FORCA 同为编码代理改机器人程序），不作 correction。**列下期首选备选。**
6. **暂停：00344（SPARK）**，见 C008-1。即便修订后维持 P3，记忆槽已有 MemER、LogLook，且已两次以“记忆槽饱和/离线问答评测”让位（s005 ReSight、s006 2610.38318），评测仍是固定问答集。
7. 入选 3 篇覆盖 F1、F2、F4；capability 2、judgment 1；对象分别为真机移动操作、仿真桌面双臂操作（RoboDojo）、多机器人仿真协调。01560 与 04080 主卡同为 observe_act_interface，但问题不同（harness 与可部署信息带来多少能力 vs 预建表示的信息损失），不算同题。
8. later_work：8 篇均无 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标版本。七篇缓存头均为 `FULLTEXT: html`，实际都是 core 裁剪版，缺相关工作和/或附录；八篇均取得同版本 arXiv HTML（2026-11-04，转换稿仅在 /tmp，不提交）。

| paper_id | 版本 | 读到范围 | 结论 |
|---|---|---|---|
| 2611.04080 | v1 | 正文 §1–5 全文（含 §2、§3.4.3）＋附录 A–B（Table 4） | 通过，无 correction。缓存未含附录 B Table 4（整扫描 VLM 96.1% ≥ Fido 94.2%），属材料缺口而非判断错误：它加强 Q1，不改档位；展示缩窄到“路线”。 |
| 2611.01560 | v2（另取 v1 对照） | v2 正文 §1–8＋附录 A–G；v1 全文逐段对比 | 通过，无 correction。展示缩窄：头条跨 harness 且在抽样波动内；v2 补写两项任务说明；真机分数 v1→v2 被改且未解释（不据真机下结论）；基线 harness 配置未写明。 |
| 2610.41044 | v1 | 正文 §1–4＋补充 S1–S5（Supp. Table 1–14、提示词） | 通过，无 correction。补充：权限对比为看结果后加入的探索性比较；各自为政队是配对消融；近前沿高权限分两次运行。 |
| 2611.05058 | v1 | 正文 §1–6＋附录 A–C | 无 correction。facts 一致（R1 Bridge 45.2 vs 21.2、Stack 57.2 vs 17.2；R3 Ring 38 vs 0；在线 28/50 vs 12/50、42/50 vs 15/50；Ring 77.2 s vs 115.8 s、101.3k vs 214.5k token；Bridge token 反增 15.1%）。 |
| 2611.04226 | v1 | 正文 §I–VIII＋附录 A–C | **C008-2**（见下）。其余 facts 一致（Local 310.20 步/5.47 s；Full 361.30 步/19.59 s；161/801 有独立故障标签）。 |
| 2611.04255 | v1 | 正文 §1–6＋补充 S1–S4 | 无 correction。facts 一致（40/60 → 48/60、Explore 1.05 → 0.12；28/60 → 50/60、5/60 → 31/60；真机 14/20，5 次感知失败）。 |
| 2611.02391 | v1 | 正文 §1–6、Limitations、附录 A–F | 无 correction。facts 一致（600 次正式评估、102 个新最好 diff；20 新种子全胜 +22–63%；40/42 迁移格为正，GPT 补丁在出库 80/20 下约 −6%；87×/112× 规划时间）。 |
| 2611.00344 | v1 | 正文 §1–7＋附录 A–D | **C008-1**（见下）。 |

## Correction（退回 Sol 单篇修订，保留原记录）

### C008-1 · 2611.00344（SPARK）· inc-l2-08

- 原判：q4_fit = `fits`，evidence_status = `confirmed`，P3 / to_l3。
- 问题：方法的两个关键部件（与查询无关的诊断、定向重访）没有被实验隔离，Q4 应为 `partial`。依据：
  1. 附录 C.1：退化后第一回合**每个被评估的簇都恢复不良**，因此批评器的 precision 按构造为 1.0、无法测量；全部标记也能得到召回 1.0。Table 3 的召回 0.800 不能说明诊断有选择力。
  2. §6.4 Table 4：同预算的非定向重访 +0.147 vs 定向 +0.154，非定向对照只用一个随机种子；Old Shipyard 上非定向更好（+0.400 vs +0.300）。
  3. §3.4.1、§6.1：重访**不带第一回合的人工退化**飞行（作者写明“一定程度恢复是预期的”）；§6.2 三种合并规则增益几乎相同（+0.294–0.296）。EQA 提升主要来自“去掉注入的退化再看一次”，L2 facts 也已写“问答改善主要靠新证据而非删除”。
  4. §6.5：多回合后 KB 持续膨胀（Old Shipyard 958 个对象 vs oracle 152；Downtown 1,142 vs 493），选择性合并的“修正”在长期不成立。
- 建议：q4_fit 改 `partial`；evidence_status 改 `pending_experiment`（缺：退化后仍有恢复良好区域的设定以测 precision、多种子等预算非定向对照、重访也带退化或换退化类型的对照）；next_action 由 Sol 按规则重定，不再进本期候选池。Q1–Q3 本席未见错误。
- 本席未改原记录，等待 Sol 单篇修订。

### C008-2 · 2611.04226（DiMuRe）· inc-l2-08

- 原判：P3 / confirmed / to_l3；q3_loss 写“按适用条件恢复可在保留进度时处理……**而不破坏原本成功回合**”；facts 以 801 例为主结果分母。
- 问题（事实范围，不一定改档）：
  1. 附录 B-A：801 例子集“在早期开发中选定，**未预登记为留出评测**”，排除的是 90 例 6 cm 接收区平移；附录 Table S6：在这 90 例上 Original 79/90，Local 67/90，Full 69/90，**恢复系统使原本成功的回合变少**。全 891 例仍为 549 → 689 → 725。
  2. 正文 §VI-A 只写“disturbed subset follows an earlier development selection”，摘要报告 801 例结果；L2 未记录被排除的负向子集。
  3. L2 已写“规则本地分支不是在环 LLM”；补充一点：主结果 Local（+18.98 点）全程不含在环 LLM，在环 LLM 只在 Full，且 Full 的额外步数与提前交接使 +4.24 点无法归因（§VI-A、附录 B-A，作者自述）。收录依据宜写明以 LIBERO-Disturb（B 类评测）及 Encore 程序为主。
- 建议：facts 与 q3_loss 改为同时报告 801 例与全 891 例，写明 6 cm 子集上的退化；biggest_gap 增加“开发选定子集、未预登记”。是否改档由 Sol 判断；本篇本期按同卡重复不入选，与此 correction 无关。

## 待补与漏检抽查

- 待补（priority=high、未 confirmed，不在本期候选池，补齐后由 Sol 单篇 L2；见 progress.md 2026-11-04 班）：inc-l2-08 pending_material 4 篇（2611.01112、2611.05320、2611.00180、2611.02497）。前期遗留待补项见 selection-007 与 progress.md，本期未变动。
- 漏检抽查：inc-l2-08 抽查名额 1、池 0，欠账约 2.2 滚存（progress.md）；本期无改判。
- 下期备选：首选 2611.02391（理由见上第 5 条）。05058、04226 按同卡重复，04255 按证据不足，不列备选；00344 待 C008-1 修订后再议。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2611.04080 | **ready**（第 1 次超出页面/PDF 2 页、路线框文字顶边、短任务用时误写 5.2 min（应为 2.5）、闸门栏孤字 → 重做一次后通过；同轮再改两处孤字） | `reel/2611.04080/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2611.01560 | **ready**（第 1 次页底空白约 290 px、波动标签伸入邻区、Astra 标签相撞、图注被裁 → 重做一次后通过；同轮再改一处短句） | `reel/2611.01560/`：同上 |
| 2610.41044 | **ready**（第 1 次拓扑说明被裁、扇区标签压线、照片表一格措辞超出原文 → 重做一次后通过） | `reel/2610.41044/`：同上 |

- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（张数 33→36、增量 run 15→18 张、新增 3 行、“选择与制作”新增本期条目）；`README.md` 第 9 行本季漏斗统计行（追加 “8 P3-confirmed → +3 posters”，33 → **36 posters**），其余段落未动。
