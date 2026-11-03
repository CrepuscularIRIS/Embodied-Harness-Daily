# selection-007 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽，单席串行）；日期 2026-11-03
- 本仓第七期。前六期 30 篇（run embodied-full-v11-20261022 selection-001/002 共 18 篇；本 run selection-003–006 各 3 篇）不再重复入选，只用作同题/同卡对照。
- 候选池：本 run 最新记录中 P3 / confirmed / to_l3 共 6 篇，均出自 inc-l2-07（40799、41216、41844、42053、41044、41857）。无上期备选，无 P2 confirmed 编辑候选。
- 结果：入选 3 篇，3 张均 ready（每张首轮渲染不过、重做一次后通过）；与前期已选同卡重复 2（40799、42053）；多样性截断 1（41044，下期首选备选）；correction 0。
- 档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。未运行论文代码，未复现。

## 候选（6 篇）

| paper_id | 标题（简） | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2610.41857 | When the Simulator Fails, Not the Policy（SimuGuard） | P3 | judgment | F1,F2 | harness_effect_evaluation / external_verification_control | **入选 #1** |
| 2610.41844 | SketchMate: Agentic Geometric Reasoning for Zero-Shot Precision Insertion | P3 | capability | F0,F3 | observe_act_interface / planner_composes_code_and_policies | **入选 #2** |
| 2610.41216 | TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents | P3 | capability | F3,F1 | offline_harness_distillation / harness_self_optimization | **入选 #3** |
| 2610.41044 | Consensus Within, Competition Between（LLM 周界防御团队） | P3 | judgment | F1,F4 | multi_robot_llm_coordination | 多样性截断（下期首选备选） |
| 2610.40799 | CaPtain: Post-Training Code-as-Policy Robot Agents | P3 | capability | F0,F4 | harness_native_rl / planner_composes_code_and_policies | 与前期已选同卡重复 → 2610.35817（ZAP，s004）＋机制证据缺口 |
| 2610.42053 | REA: Routed Embodied Agent Runtime | P3 | capability | F2,F0 | external_verification_control / planner_composes_code_and_policies | 与前期已选同卡重复（执行监控/门控槽已饱和）＋主效应小、窗口混杂 |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2610.41857 | 评测方法学（B 类）：仿真基准结局归因 | 问题最清楚、证据最直接：把一次接触报告逐位追到回合结局，用单参数/单常数干预确认原因。RoboTwin 五个薄壁容器任务中 LingBot-VA 44 个失败有 40 个含接触伪影；根因为 PhysX 5.3.1 GJK 中不随尺度缩放的退化阈值，引擎外逐位复现 20 个假接触、换 5.4.0 阈值后全消且 4 个真穿透保留；同一改动下脚本示范含伪影 18→1、6→0，闭环 89(12)→98(0)。改变的是“仿真成功率里的失败归策略”这一研究判断，并给出改不了引擎时的区间报告法。前 30 张无仿真物理保真类画报；本池 41216、40799、42053 都在 RoboTwin/LIBERO 上报数，直接相关。 |
| 2 | 2610.41844 | VLM 智能体＋几何工具的精密操作接口 | 能力型问题：零样本、无 CAD/示范/训练的亚毫米、键向正确插接。同一 VLM、规划器、控制器下，移植的 ReKep/MOKA 0/69，草图 50/69，加抓后近看配准 61/69（误差中位 0.10 mm），留出 6 种新连接器 18/18；键向读错由几何纠正（严格 36→82，增 46 失 0）；同件复用 3.4 s 对 90 s 且成功持平。机制分工清楚（VLM 决定量什么、工具给数），与 s002 ReKep（2409.01652，自动约束 vs 人工参照）、s004 ThinkLocoManip（2610.34370，机身姿态工具化）、2602.15875 Fly0（目标接口）问题不同：本篇问的是精度从哪里来、对应关系由谁算。 |
| 3 | 2610.41216 | harness 自我演化 → 学生蒸馏 | 两个可检验主张中的第一个有干净对照：固定权重的教师、未参与演化的 DeepSeek、未训练 4B 三条线都随 harness 版本上升（+30.2/+30.6/+26.6），收益属于 harness 且跨规划器；第二个（学生贴着教师走）有支持但数据未配平，画报已分开写。去推理文本的单因素消融影响极不均匀（RoboTwin −0.4、LIBERO-PRO −19.3），如实展示。与 s005 RoboAuto（2610.36533，逐任务程序搜索）、s001 2610.25114（自我改进收益拆解）、s006 2610.39775（LLM 监督规则化）、s003 TILDE（2610.25376，教师接手状态蒸馏）对象不同：本篇问的是整套 harness 的演化收益能否换模型、换小模型保留。HarnessRSI 仓 selection-008 已入选同篇；三仓不共享画报，本仓独立核对制作，不构成本仓已有机制重复。 |

### 画报侧重（已制作）

- **2610.41857**：深色题带；单回合取证速度曲线（示意，只标 0.28 s 与 0.2→22 m/s）；SimuGuard 三件事；根因纵链（含三项放大设置）；失败构成条；只改常数对照表（注明 p=0.11、种子不完全配对）；区间数轴 [75.8, 98.5] 与四条假设；“限速≠修复”警示卡（90→50，附压力测试）；限制栏标明对 harness 的相关性是阅读判断。
- **2610.41844**：VLM/几何双泳道＋执行行；对数误差梯（含 0.2–0.45 mm 容差带与严格成功数）；旋转打分示意＋键向两组大数；结果与复用两张计数表；限制栏写明仅仿真无噪声深度、基线为移植版。
- **2610.41216**：两段接力带（含 296 项候选账本条）；四版本×四规划器折线＋读图表（固定权重线与学生线分开解读）；去推理文本发散条；零样本四列表；规划器算力三卡（注明只算规划器）。

## 排列、去重与多样性（编辑理由，均有原文依据）

1. 6 篇均为 P3/confirmed；q3：capability 4、judgment 2，不分先后，不按数值排序。
2. **与前期已选同卡重复：40799（CaPtain）→ 2610.35817（ZAP，s004）。** 两篇问同一件事：小型开放 VLM 在只暴露低层感知/几何/运动原语、无抓取宏与 VLA 的 harness 里，经仿真内 SFT→多轮 RL 学会操作（ZAP 同 harness base 8.3→SFT 58.3→RL 74.0；CaPtain 0→55.4→73.8，held-out 初始状态）。CaPtain 独有的部分是特权物理 critic 的逐请求信用分配，但原文没有等预算的 outcome-only RL 训练对照（§4.5、附录 H 只给离线梯度噪声尺度 9.0k→6.7k 回合与 critic AUC），critic 的必要性未被隔离——L2 已记此缺口；零样本迁移 RoboTwin 22.6%、RoboDojo 0.8%，真机两例无计数。按 PROBLEM_CORE §4 priority 下调理由“与已选论文内容重复”处理，不改记录；不列备选。
3. **与前期已选同卡重复：42053（REA）。** external_verification_control 槽已有 s002 REFLECT（2306.15724）、s003 Backtrack（2610.32941）、s005 Best-of-N（2610.37196）、s006 LOGIV（2610.40016）与 2610.39775。REA 独有的“非阻塞调度”问题成立（阻塞 advisor 闲置 2.62 s、约 20% 控制时间），但主效应小且条件混杂：路由记忆比全局最好单法 95.9 vs 94.7（+1.2，p=0.004），judge gate 在非挑选种子上 +3.1 而每成功用时 2.1×，+15.3 只在按 Fix 失败挑选的压力子集；RoboTwin VLA 研究为历史窗口/不同主机，真机与 RoboTwin 两夜相差 36 个场景。画报难给出“有完整对照条件的结果”。不改记录；不列备选。
4. **多样性截断：41044（周界防御 LLM 团队）。** 问题与证据可用（900 回合配对种子、95% CI；同一 consensus 内提高低价模型出价权限突破 +38 点，CI +30 到 +45），且多机器人协调卡在前 30 张中空缺。让位理由：(a) 具身性弱——平面双积分质点、抽象单位竞技场，队友状态与安全屏障用全局真值、已解决对手记录即时删除（§4.2–4.3）；(b) 没有无 LLM 的 CBAA 经典投标基线，“consensus 最好”可能主要来自外部拍卖协议本身（作者结论亦为“需要 LLM 之外的冲突消解协议”）；(c) 伪装实验每条件 5 个种子、照片为静态参考图。本期三篇已覆盖评测、接口、harness 演化三类，列下期首选备选；原文已核对，无需重做 L2。这里的具身性顾虑属阅读判断，不作 correction（EVIDENCE.md 收录范围含无人机与多机器人任务分配，L1/L2 判为收录不算错误）。
5. 入选 3 篇覆盖 F0、F1、F2、F3；judgment 1、capability 2；对象分别为仿真评测平台本身、单臂精密装配（仿真）、单/双臂通用操作 harness。41857 与 41216 都用 RoboTwin 2.0，但前者质疑该平台的结局记账，后者在其上报数——41216 的 RoboTwin-50 包含 41857 指出的薄壁容器任务，此为阅读联系，不改变 41216 的跨版本对照（同一引擎、同一 500 回合内的相对比较）。
6. later_work：6 篇均无 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标 v1（六篇缓存头均为 `FULLTEXT: html`，实际均为 core 裁剪版，缺相关工作与附录；41844 在 §1 末与 §3.6 有截断）。六篇均取得同版本 arXiv HTML（`https://arxiv.org/html/<pid>v1`，2026-11-03，转换稿仅在 /tmp，不提交）。

| paper_id | 读到范围 | 结论 |
|---|---|---|
| 2610.41857 | 正文 §1–6＋§2＋附录 A–D（Table 5–14） | 通过，无 correction。收录范围按 B 类评测方法学维持（理由见 reel/2610.41857/SOURCE.md：缺陷在引擎、脚本示范同样受影响，受审平台即本语料 harness 常用平台；与 C005-1 不同）。展示缩窄：89→98 注明 p=0.11 与种子不完全配对；修法 5.4.0 已有；精度单任务、无召回。 |
| 2610.41844 | 正文 §1–5（含 §2、§3.6 全文）＋附录 A–E | 通过，无 correction。展示缩窄：基线为移植版（附录 B 列出改动）且获实例掩码；复用任务按失败挑选；只靠形状匹配会选错插口（附录 C）。 |
| 2610.41216 | 正文 §1–5（含 §2）＋附录 A、B、D、E、F、G（附录 C 已发表结果协议未展开，画报不引用） | 通过，无 correction。展示缩窄：学生线与固定权重线分开解读；跨版本只在 RoboTwin、同组任务；保留 harness 非内化；真机无计数；算力只算规划器。 |
| 2610.41044 | 正文 §1–4（core 已含 §2 结果、§3 讨论前半、§4 方法前半）；HTML 已取得，附录与补充表未展开 | 无 correction。facts 一致（四个未伪造条件突破 15/32/29%；高权限 +38 点 CI 30–45；队友状态与屏障用真值；存活 161 中 113 仍在逼近）。 |
| 2610.40799 | 正文 §1–6；附录目录与附录 H（梯度噪声）核对 | 无 correction。facts 一致（held-out LIBERO host 55.4→73.8、strict 52.1→67.5、false finish 7.1→2.1；critic AUC .970/.904；RoboDojo 0.8%）。确认无等预算 outcome-only RL 训练对照，与 L2 biggest_gap 一致。 |
| 2610.42053 | 正文 §1–6 | 无 correction。facts 一致（3,000 回合 95.9 vs 94.7；590 回合 166 失败仅 6 次异常；阻塞闲置 2.62 s；judge 准确 .67 < always-done .75、done precision .905；重跑救 19%/毁 9%，压力子集 24%/5%）。 |

## Correction（退回 Sol 单篇修订）

本期无。六篇 L2 判断与原文一致；所有缩窄均为展示层面，已记入各篇 SOURCE.md。

## 待补与漏检抽查

- 待补（priority=high、未 confirmed，不在本期候选池，补齐后由 Sol 单篇 L2；见 progress.md 2026-11-02 12:17 班）：
  - inc-l2-07 pending_material：2610.41320、2610.41383、2610.41688、2610.42141（BioAgent 缺 LLM/VLM 闭环证据；LEXP / RoboArchitect 缺经验流协议）。
  - inc-l2-07 pending_experiment：2610.41868（P3）、2610.31518（补抽改判 P2→P3）。
  - 前期遗留待补项见 selection-006 与 progress.md，本期未变动。
- 漏检抽查：inc-l2-07 补抽 2610.31518，改判 P2→P3 / pending_experiment（漏检 1，待材料，未进本期候选池）；余欠账约 0（progress.md）。
- 下期备选：首选 2610.41044（理由见上第 4 条）。40799、42053 按同卡重复处理，不列备选。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2610.41857 | **ready**（第 1 次纵轴标题被裁、虚线压字、末框孤字、警示卡半空 → 重做一次后通过） | `reel/2610.41857/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2610.41844 | **ready**（第 1 次超出页面/PDF 2 页、标题孤字、容差标签被截 → 重做一次后通过；同轮修 360° 刻度与执行顺序措辞） | `reel/2610.41844/`：同上 |
| 2610.41216 | **ready**（第 1 次标题孤字、框内文字越界、纵轴标题压刻度、算力卡孤字、页底空白 → 重做一次后通过） | `reel/2610.41216/`：同上 |

- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（张数 30→33、增量 run 12→15 张、近三月表新增 3 行、“选择与制作”新增本期条目）；`README.md` 第 9 行本季漏斗统计行（追加 “6 P3-confirmed → +3 posters”，30 → **33 posters**），其余段落未动。
