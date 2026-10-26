# selection-003 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽）；日期 2026-10-26
- 本仓第三期。前两期 18 篇（run embodied-full-v11-20261022，selection-001/002）不再重复入选，只用作同题/类型对照。
- 候选池：本 run 最新 L2 记录中 P3 / confirmed / to_l3 共 5 篇（inc-l2-02：25376；inc-l2-03：31841、32348、32941、30587）。无 P2 confirmed 编辑候选。
- 结果：入选 3 篇；同题去重 1；多样性截断 1；correction 1（退回 Sol，未入选篇）。
- 档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。未运行论文代码，未复现。

## 候选（5 篇）

| paper_id | 标题 | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2610.25376 | TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models | P3 | capability | F3,F2 | learner_state_teacher_correction / offline_harness_distillation | **入选 #1** |
| 2610.31841 | FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation | P3 | capability | F0,F4 | code_policy_trial_revision / observe_act_interface | **入选 #2** |
| 2610.32941 | If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs | P3 | capability | F0,F2 | external_verification_control | **入选 #3** |
| 2610.30587 | Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents | P3 | capability | F0,F2 | external_verification_control | 同题去重 → 2610.32941；另记 correction |
| 2610.32348 | LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners | P3 | judgment | F1,F5 | harness_memory_skill_reuse / harness_effect_evaluation | 多样性截断（下期备选） |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2610.25376 | 学习者状态纠正→蒸馏 | 让冻结 π0.5 教师在学生偏离处真正执行纠正，把“纠正之后的状态”放进训练；同池数据逐项加入、同额外 30 回合对比人类示范、同一组 12 个错误状态（BC 4、OPD 5、TILDE 8、教师 9），三种对照分别回答哪部分有用。填补 selection-002 明确空缺的 learner_state_teacher_correction 槽。 |
| 2 | 2610.31841 | 编码智能体的感知通道 | 同一编码智能体、同技能库与预算，只拿走腕部力/力矩通道：真机抽屉 10/10 vs 4/10、门 10/10 vs 1/10，手持擦拭 93% vs 21%；力既进 100 Hz 控制回路，又作为两次执行间改写“力反馈逻辑本身”的证据。与前期代码修订篇（2610.25114 收益归因、2512.02002 反馈来源替代）问题不同：本篇问的是修订回路缺哪类物理证据。 |
| 3 | 2610.32941 | 冻结策略的返回-重试恢复 | 不收恢复数据、不改权重，只用策略自身特征上的小报警头触发“倒放已实现手臂增量”再交还；两倍时间对照、5 种子、留出种子、三种 VLA 与第二基准，LIBERO-Long 提升 +7.40/+1.60/+7.08 pp，并如实报告低阈值自适应回走 −1.92 pp。前期失败相关入选（REFLECT 解释→纠正、GVL 进度信号）均不涉及此机制。 |

### 画报侧重（已制作）

- **2610.25376**：顶部三种状态分布示意；三面板置信区间点图（附录 Table 12）；12 错误状态方阵；同额外回合数据源柱图；AutoDAgger vs HG-DAgger 对比条。限定 4.1× 为得分、2× 只计接管后恢复段、真机 12/27/30 次区间宽。
- **2610.31841**：门把手两条开发记录双泳道（Table V、Fig. 9）；冻结后 5 项真机结果表；敲方块迭代数单列（无对照）；成本格。限定一条开发链、力与诊断同时改变、人负责场景。
- **2610.32941**：触发—回走—交还机制时间带；LIBERO 森林图（含留出种子点）；恒等式 Δ=cF−bS 与套件热格（三处负值）；π0.5 阈值×规则森林图（−1.92 标红）。限定仅仿真、物体不复位、无随机/定时回走对照。

## 排列、去重与多样性（编辑理由）

1. 5 篇均为 P3/confirmed；capability 4、judgment 1，二者并列不分先后，不按数值排序。
2. **同题去重：2610.30587 → 2610.32941。** 两篇同属 external_verification_control / K202（监控触发介入，恢复后交还原执行者），都问“何时由监控信号把控制交给恢复机制、何时交还”。保留 32941：问题更窄更清楚（冻结策略、无新数据、无第二模型），证据更直接（5 种子 CI、留出种子、两倍步数对照、负结果）。30587 阈值在评测实例上扫描、单次运行，且其关键的“等云预算”对照受 CRR 口径问题影响（见 correction）。二者机制确有差异（30587 是双执行器间的权限转移与延迟权衡），但在本期 3 篇上限下不并列入选。
3. **F0 占比：** 去重后 F0 仍有 31841 与 32941 两篇。二者机制类型不同（编码智能体的物理信息通道 vs 冻结 VLA 的返回-重试），且各自填补前 18 篇未覆盖的类型，故保留两篇 F0，记此编辑理由，不改记录字段。三篇合计覆盖 F0、F2、F3、F4。
4. **多样性截断：2610.32348（LogLook）。** 问题成立且是本池唯一 judgment 篇；但其两条主线与已入选篇重合：“记什么、谁来记”属 s001 MemER（2510.20328）同卡记忆槽，“执行器失败掩盖上层差异”与 s002 RoboCerebra（2506.06677）的分层归因判断同型。其直接证据主要是成本（token 40.5k vs 71.3k、图像 46 vs 114）与失败构成（other 12 vs 4，作者非盲分类、未检验），成功率本身不可区分、单组件删除未见正向 SR 贡献。三篇上限下让位于填补新类型的 25376/31841/32941。下期记忆/评测槽首选备选；原文核对通过（见下），无需重做 L2。
5. later_work：5 篇均无 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标 v1（五篇缓存头均为 `FULLTEXT: html`，实际均为 core 裁剪版，L2 记 `material: core`）。为满足“读完整原文及必要附录”，补读同版本 arXiv HTML（`https://arxiv.org/html/<pid>v1`，2026-10-26 取得，仅本地临时文本，不提交）。

| paper_id | 核对 | 结论 |
|---|---|---|
| 2610.25376 | 正文＋附录 A–C、Tables 1–15 | 通过，无 correction。附录 B.1 补到真机 20 条 rollout 门控结局判别（准确 85%），仍非接管时机误报/漏报；附录 CI 为按试次 bootstrap、非种子方差——L2 缺口判断成立。缓存与 HTML 表号不同（缓存 “Table 2” 对应 HTML Table 1/2），已在 SOURCE.md 注明。 |
| 2610.31841 | 正文＋§II、全部图注（无附录） | 通过，无 correction。Fig. 9 图注确认门把手第 18–20 次为重复执行终版程序，与 Table IV 17 轮一致。 |
| 2610.32941 | 正文＋§2、附录 A.1–A.8 | 通过，无 correction。附录 A.3 确认两倍步数单独只 +2.3–3.7 pp；A.1 选配置样本小（作者自述）；A.6 特权复位 vs 实际倒放。L2 所记“初始状态划分未说明、无随机/周期回走对照”在附录中仍未补。 |
| 2610.30587 | 正文＋§II、图注（无附录） | **发现 L2 漏检的内部不一致 → correction C003-1（下）**。不影响 P3 问题档位判断。 |
| 2610.32348 | 正文＋附录 A–C（含 Table 6 任务说明消融、Table 10 实现细节） | 通过，无 correction。L2 facts（237/256 vs 234/256、失败 15/4 vs 10/12、token 40.5k vs 71.3k、Table 3 56/58/61/58、learned executor 104/104）与原文一致；附录 Table 6：去掉完成判据 other 失败 4→11、去掉全部说明 89.1%，支持 L2“任务说明来自基准成功代码”的限定。 |

## Correction（退回 Sol 单篇修订；保留原记录，不改批次文件）

**C003-1 · 2610.30587（inc-l2-03 记录）**

- 原判：P3 / `confirmed` / to_l3；subcard K202 “监控所需输入…投机请求也计入 cloud request ratio”判 holds，并以 §IV-C 等云预算随机/周期对照作为确认依据。
- 问题：CRR 的计数口径与方法描述在算术上不相容，L2 未核出。§IV-A：Habitat 上 critic 每步调用（k=1），“All cloud executor requests, including speculative requests, are included in N_C”；Algorithm 1 第 7–8 行在每个 critic 步同时发出一次云端请求（本地控制时为投机请求，云控制时为实际请求）与一次本地提案。按此每步至少 1 次云请求与 1 次本地请求，Habitat 上 CRR 应 ≥50%；Table I 报 CARE 在 Habitat 的 CRR 为 24.4%。Fig. 5 又称默认配置启用投机执行（“removing speculation costs 0.05 s at P50…”）。
- 影响：Fig. 4(a) 在 Habitat 失败子集上“同 CRR 下 CARE 88.4–93.0% vs 随机/周期 74.4–79.0%”是 L2 确认 Q4 的关键证据；若 CARE 的实际云调用被低估，所谓“匹配预算”可能不成立。另有阈值在评测实例上扫描（§IV-A）、单次运行，L2 已记。
- 建议：Sol 单篇复核 CRR 定义与 Algorithm 1/§IV-A 的关系（可能是作者未写清投机请求只在部分步骤发出，或 Table I 与 Fig. 4 采用不同口径）；在澄清前 `evidence_status` 宜改 `pending_material`，P3 问题档位不因此下调。本条以原文自身陈述的算术推断为据，未运行代码。
- 本期处理：该篇本已按同题去重不入选；correction 不影响本期成品。

## 待补与漏检抽查

- 待补（priority=high、未 confirmed，不在本期候选池，补齐后由 Sol 单篇 L2）：沿用 progress.md——2610.26659（pending_material，缺附录 A/B 与场景/目标数冲突）；2610.32208、2610.32633（pending_material，缺附录章节）；2610.30197、2610.30478、2610.31427、2610.31613（含 Table IV 0.72 vs 0.78 冲突）、2610.32554、2610.32776（pending_experiment）。本期未新增，另加 C003-1 退回的 2610.30587。
- 漏检抽查：本 run 欠账未清（progress.md 记下班补抽 1 篇），本期无抽查改判结果。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2610.25376 | ready（视觉 QA 通过；第 1 次渲染溢出/重叠，重做后通过） | `reel/2610.25376/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2610.31841 | ready（第 1 次溢出/折行，重做一次后通过） | `reel/2610.31841/`：同上 |
| 2610.32941 | ready（第 1 次溢出/标签重叠，重做一次后通过） | `reel/2610.32941/`：同上 |

- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（表头说明、近三月表新增 3 行、“选择与制作”新增本期条目）；`README.md` 第 9 行本季漏斗统计行（18 → 21 posters，其余段落未动）。
