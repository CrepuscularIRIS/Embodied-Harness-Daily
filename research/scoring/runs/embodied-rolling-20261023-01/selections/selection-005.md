# selection-005 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽）；日期 2026-10-28
- 本仓第五期。前四期 24 篇（run embodied-full-v11-20261022 selection-001/002 共 18 篇；本 run selection-003、selection-004 各 3 篇）不再重复入选，只用作同题/类型对照。
- 候选池：本 run 最新记录中 P3 / confirmed / to_l3 共 7 篇（inc-l2-04：33487，上期第一备选；inc-l2-05：36533、36143、37196、36852、37533、37378）。无 P2 confirmed 编辑候选。
- 结果：入选 3 篇，3 张均 ready（每张首轮渲染不过、重做一次后通过）；与前期已选同卡重复 1；暂停并退回 1（correction C005-1）；证据不足 1；多样性截断 1。
- 档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。未运行论文代码，未复现。

## 候选（7 篇）

| paper_id | 标题（简） | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2610.36533 | RoboAuto | P3 | capability | F2,F3 | code_policy_trial_revision / external_verification_control | **入选 #1** |
| 2610.37196 | How Much Can Best-of-N Help a WAM? | P3 | judgment | F2,F1 | sample_verify_select | **入选 #2** |
| 2610.37533 | Which Hand Was Late? | P3 | judgment | F4,F2 | external_verification_control / privileged_teacher_supervision | **入选 #3** |
| 2610.37378 | VLA-Stem | P3 | capability | F0,F4 | external_verification_control / privileged_teacher_supervision | 多样性截断（下期首选备选） |
| 2610.33487 | ReSight | P3 | capability | F3,F4 | harness_memory_skill_reuse / harness_self_optimization | 与前期已选同卡重复 → 2610.32348（s004）、2510.20328（s001）；上期顾虑未解除 |
| 2610.36143 | Program-Level Adversarial Co-Adaptive Self-Play | P3 | judgment | F3,F2 | code_policy_trial_revision / harness_self_optimization | 证据不足以支撑展示（单谱系案例研究） |
| 2610.36852 | When Black-Box Robot Policies Fail | P3 | capability | F4,F2 | external_verification_control | 暂停：correction C005-1（收录范围） |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2610.36533 | 编码智能体程序搜索的物理知识与主动诊断 | 把对象级物理知识（含“现场测什么、怎么测”，不存数值）、场景实测、逐阶段验证与自设实验放进程序搜索。累加消融 5.2 → 19.2 → 38.4 → 91.2（5 任务，Table 12）；同一 LIBERO-90 知识库换仿真器与双臂本体 RoboTwin 24.5 → 91.5（Table 14），真机未见长任务阶段完成分 98.6 vs ASPIRE 11.3。与前期 FORCA（2610.31841，修订回路缺力觉证据）、2610.25114（自改进收益拆解）、2512.02002（文本模拟反馈）问题不同：本篇问的是跨任务保留的物理理解与主动实验，而非单一感知通道或反馈来源。 |
| 2 | 2610.37196 | 测试时选择的余量测量（评测方法学） | 用逐字节分支＋重复续跑＋留出神谕，说明单续跑神谕把续跑运气算进候选质量：RoboCasa 复现 O¹ +10.2 点、留出 +0.9 点；17 次续跑下可选份额 24–52%（Cosmos）。据此做“先判是否偏离、再选方向”的门控选择器，冻结后预登记闭环 76.9 → 81.6、未见任务 62.6 → 69.8，并如实报告 24 项预登记中 8 项不支持。与 s002 RoboMonkey（2506.17811，同卡 sample_verify_select）问题不同：本篇衡量并修正该类方法所依赖的上界本身，按 SELECTION.md 第 4 条“仍有独立价值”保留。 |
| 3 | 2610.37533 | 失败诊断器的可观测性与 VLM 读出 | 失败原因由机构轨迹定类，逐通道同一探针：单手传感器主要读自己那只手的延迟（交互效应 +0.811），工具手晚且推力不足时被动观测上限恰为 0.500；Qwen3-VL 状态探针 ≥0.956 而答案中位 0.497/0.604，读出方向与探针方向 cos≈0。改变的是“诊断器给什么观测、怎么检查 VLM 答案”的判断。与 s002 REFLECT（2306.15724，失败解释→纠正）、s001 GVL（2411.04549，进度信号）不同：本篇问的是可辨识性与“知道但不说”。 |

### 画报侧重（已制作）

- **2610.36533**：基线三类失败 → 三组件对应带；分阶段搜索流程（验证器/审计员/自设实验/预算计入）；套件哑铃图逐行标“复现/引用”并画 π0.5；累加消融热格；RoboTwin、真机（阶段完成分、人判）、token 三联。注明 π0.5 布局 98.0、18/83 设置低于 ASPIRE。
- **2610.37196**：两种神谕网格示意（假想数据）；份额区间条；结构化余量点线（Streaming 未通过）；闭环斜率图（含物体布局 −1.3）；24 项预登记记分牌。
- **2610.37533**：双臂-门示意上挂各通道 AUC 标签；三层“在哪可读”卡；修复对比条（升级＝神谕＝不诊断全上 297，加力次数不同）；VLM 两向量示意＋AUC 表。

## 排列、去重与多样性（编辑理由，均有原文依据）

1. 7 篇均为 P3/confirmed；capability 4、judgment 3，并列不分先后，不按数值排序。
2. **36852 与 37533 是否同题：不按同题处理。** 二者都属“诊断决定修复”，但问题不同：36852 是冻结 RL 行走策略（URMA）输入端的传感器故障归因与输入替换（§2，Fourier 步态代理＋岭回归贡献分解），37533 是双臂协作失败中“哪只手晚”的可辨识性与 VLM 读出（§3–6）。故障对象（传感器读数 vs 两臂相对时序）、诊断器（结构化代理 vs 逐通道探针/VLM）、结论类型（能力 vs 判断）都不同。36852 未入选的原因是收录范围存疑（C005-1），不是同题去重。
3. **与前期已选同卡重复：2610.33487（ReSight）。** 上期顾虑复核后未解除：§4.4 与附录 C.4 写明真机评测时 “Robot motion is disabled during evaluation; answers and cited historical evidence are scored”，下游导航只在附录 E.4 以图示展示、无计数；GOAT-core/OC-NaVQA/FindingDory 均为记忆问答（按 docs/EVIDENCE.md 属 offline 级）。证据本身扎实（冻结工具在未参与探索的 81–90 回合、真机未参与探索 3 任务 9/15 → 15/15，Table 5），但 harness_memory_skill_reuse 卡已有 s001 MemER 与 s004 LogLook 两张，按 PROBLEM_CORE §4 priority 下调理由“与已选论文内容重复”处理，不改记录；不再列首选备选。
4. **证据不足：2610.36143。** 问题成立（局部恢复不等于对自适应对手的持续稳健），但原文为每域一条八代谱系的案例研究（§4.1 Table 1、§5）：驾驶每攻击一场、无 defense-only/attack-only 对照；人形 90 次相应联合回合仅 11 次到达；57 次冻结对手测试是开发用，无历史攻击回归矩阵。画报无法给出“有完整对照条件的结果”。另：相关工作中 CodeClash、FAMOU、COvolve、RvB、SysEvolve 已做攻防程序共演化，本文自述差别是“围绕现有机器人栈、固定任务与仿真”（§2），L2 的 Q2 `new_bottleneck` 依据偏弱——属阅读判断，不作 correction。
5. **多样性截断：2610.37378（VLA-Stem）。** 证据较完整（仿真每设置 3,200 回合，六个受约束设置平均 52.8% vs 调参后 VLSA 23.7%；真机每任务/场景 15 次，Fig. 5），无 correction。让位理由：(a) 本期 37196 已占“冻结策略外加一层”类型，前期 Backtrack（2610.32941）同为冻结 VLA 外部模块；(b) 安全槽已有 Safety Chip（2309.09919，动作拦截）与 2610.27350；(c) Stem 为逐任务 PPO＋特权教师蒸馏（每 seed 约 82.3M transitions，§IV-A），更接近策略学习而非 harness 组件；真机数字仅以图表给出。列下期首选备选，原文已核对，无需重做 L2。
6. 入选 3 篇覆盖 F1、F2、F3、F4；capability 1、judgment 2。37196 与 37533 都含“表示里有信息、读出头没用上”的发现（价值头 vs 想象未来；VLM 答案 vs 状态），但对象与问题不同（候选排序 vs 失败归因），画报机制图与版式已区分。
7. later_work：7 篇均无 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标 v1（七篇缓存头均为 `FULLTEXT: html`，实际均为 core 裁剪版；37533 缓存在 §4.3 截断）。七篇均补读同版本 arXiv HTML（`https://arxiv.org/html/<pid>v1`，2026-10-28 取得，转换稿仅在 /tmp，不提交）。

| paper_id | 读到范围 | 结论 |
|---|---|---|
| 2610.36533 | 正文＋附录 A–F | 通过，无 correction。附录 A.2 Table 2 补齐预算（45/55/11 rollouts，换视角与实验计入）；附录 B.8 补齐 token。展示缩窄：L2 子卡 R05 称“复现 CaP baselines 使用相同 Opus 4.6”，实际只有 LIBERO-PRO Long 与 LIBERO-Plus 为复现，其余基线取自原论文（附录 A.4）；CaP-Agent0 无搜索阶段、在测试场景内最多改 10 次。不影响档位。 |
| 2610.37196 | 正文＋附录 A–G | 通过，无 correction。附录 A：24 项预登记 16 支持 / 8 不支持，部分在已知前序结果后登记；附录 G：未见任务仅机器人初始态类别，任务内状态×方向排序器 +1.9 vs 完整 +2.5。 |
| 2610.37533 | 正文 §1–7＋附录 A–B | 通过，无 correction。L2 边界项（§5–6 未核）已补读并核实；展示缩窄：“不诊断全上”同为 297（Table 2），诊断收益在加力次数而非修好数。 |
| 2610.37378 | 正文全文（附录 -A–-D 未细读，非入选篇） | 无 correction。L2 facts 一致（52.8% / 23.7%；去蒸馏 14% vs 63%；逐步对齐 30% vs 63%；真机 47–60% / 20–40%；82.3M transitions）。 |
| 2610.33487 | 正文＋附录 C.4、E（复核上期顾虑） | 无 correction。上期顾虑未解除（见上第 3 条）。 |
| 2610.36143 | 正文全文（无附录） | 无 correction。facts 一致（40 场 18/16/6；176 次正式评估，90 次相应联合回合 11 到达；57 次冻结对手开发测试）。 |
| 2610.36852 | 正文全文（无附录） | facts 一致；**收录范围存疑 → correction C005-1**。 |

## Correction（退回 Sol 单篇修订；保留原记录，不改批次文件）

**C005-1 · 2610.36852（inc-l2-05 记录）**

- 原判：q4 `fits`，P3 / `confirmed` / to_l3；card_anchor 写“本文是可用于具身系统的外部诊断/修复工具（B 类），不是新的 LLM harness”。
- 问题：按 docs/EVIDENCE.md，收录对象是包住前沿 LLM/VLM 的具身 harness 及“可直接用于这类系统”的 B 类贡献。原文中：被监控的是冻结的多本体 RL 行走策略 URMA（§1），诊断器是 Fourier 步态＋岭回归的结构化代理（§2 Eq. 1），全文无 LLM/VLM、无 agent loop；方法核心依赖周期步态相位（20 个相位 bin、前左足触地重置相位，§2），对非周期的 VLA 操作不直接适用；作者自述 “Extension to manipulation and vision–language–action policies also remains open”（§4）、“robot foundation model and hardware validation remain open”（摘要）。同一批次 Sol 对 2610.37547（冻结 ACT＋残差后训练）以“不自动纳入 B 类工具来绕过明文纯 visuomotor 排除”判为 out_of_scope，两条判据未对齐。
- 影响：若改判范围外，`next_action` 应为 exclude，不进入 L3 候选池；若维持收录，需写明它“可直接用于”哪一类 LLM/VLM harness 组件，以及为何与 37547 的排除理由不同。
- 本条依据为原文自述与 EVIDENCE.md 文字，不否认该文的诊断方法价值（同条件 GBM 代理 R² 相近却几乎不能诊断，Table 1）；未运行代码。
- 本期处理：该篇暂停，不入选；correction 不影响本期成品。

## 待补与漏检抽查

- 待补（priority=high、未 confirmed，不在本期候选池，补齐后由 Sol 单篇 L2）：
  - 本班新增 pending_material：2610.36013（缓存在 §4.2 截断，缺 §4.3–4.4 领域专家与 MOPD 目标、学生采样状态、教师访问条件，及附录 9–10 数据分割与预算；补齐后可判断 on-policy 整合是否对准跨域干扰，决定能否 confirmed）。
  - 前期遗留（见 selection-004 与 progress.md）：pending_material 2610.26659、2610.32208、2610.32633、2610.30587；pending_experiment 2610.30197、2610.30478、2610.31427、2610.31613、2610.35051、2610.34527。
- 漏检抽查：inc-l2-05 已补抽 2610.37547（维持排除，改判 0/1）；本期无新抽查改判结果；累计欠账约 0.8 篇（progress.md）。
- 下期备选：2610.37378（VLA-Stem，原文已核对）。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2610.36533 | **ready**（第 1 次框内文字溢出、注释右端被裁、标签压点 → 重做一次后通过） | `reel/2610.36533/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2610.37196 | **ready**（第 1 次标题限定语单独掉行、两处底注被裁 → 重做一次后通过；剩余：页底留白约 130 px） | `reel/2610.37196/`：同上 |
| 2610.37533 | **ready**（第 1 次标签压格、引线穿标签、数值断行、箭头压字 → 重做一次后通过） | `reel/2610.37533/`：同上 |

- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（表头张数 24→27、“6 张来自增量 run”→9 张、近三月表新增 3 行、“选择与制作”新增本期条目）；`README.md` 第 9 行本季漏斗统计行（追加 “7 P3-confirmed → +3 posters”，24 → **27 posters**），其余段落未动。
