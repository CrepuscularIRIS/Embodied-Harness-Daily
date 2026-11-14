# selection-015 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽，单席串行）；日期 2026-11-14
- 本仓第十五期。前十四期 50 篇不再重复入选，只用作同题/同卡对照。
- 候选池：8 篇，全部出自 inc-l2-14，按 batches 中最新记录均为 P3 / confirmed / to_l3（标题取自 `research/fulltext/<id>.txt` 文件头）。没有 P2 confirmed 的编辑候选。
- 结果：入选 **2 篇**。2611.16246 **ready**；2611.15651 原文核对通过，但**视觉 QA 重做一次后仍未通过，记 fail**，等待总控授权后再修，不进索引。不为凑数做第三张。本期 **correction 0**。
- 档位是问题评价，不是审稿结论；入选不表示方法或结果已被验证。未运行论文代码，未复现。

## 候选（8 篇）

| paper_id | 标题（简） | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2611.16246 | What Can a VLA Learn from the Agent That Calls It?（H2E） | P3 | capability | F4,F3 | offline_harness_distillation | **入选 #1**（A 类学生训练，ready） |
| 2611.15651 | Recover, Don't Just Continue（Embodied-Corrector） | P3 | capability | F2,F4 | learner_state_teacher_correction / offline_harness_distillation | **入选 #2**（A 类，核对通过；视觉 QA fail） |
| 2611.16009 | JustRUA: A Controlled Study of GPT-6 Robot-Use Agents | P3 | judgment | F1,F5 | harness_effect_evaluation / harness_memory_skill_reuse | 与前期已选同判断重复 |
| 2611.16872 | ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience | P3 | capability | F0,F3 | code_policy_trial_revision | 范围与代表性让位 |
| 2611.15964 | COMBS: Concealed Object Multi-modal Bayesian Search | P3 | capability | F2,F4 | external_verification_control / observe_act_interface | 证据不足以展示 |
| 2611.15317 | BiPOP: Partial-Order Planning for Bimanual Manipulation | P3 | capability | F1,F0 | llm_symbolic_solver_planning | 范围与代表性让位 |
| 2611.16671 | NSDL: Neuro-Symbolic Division of Labor for Multi-Robot Planning | P3 | judgment | F1,F2 | llm_symbolic_solver_planning / harness_effect_evaluation | 证据不足以展示 |
| 2611.15093 | Decide Before You Move（PreNav） | P3 | capability | F3,F4 | observe_act_interface / harness_memory_skill_reuse | 范围与代表性让位 |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2611.16246 | 学生训练：把 LLM 导航代理的成功会话改写成被调用 VLA 的监督，测试时撤掉代理 | 官方 REVERIE-CE val-unseen 全部 3189 回合、10 个未参与训练的场景：同场景、同配方、同 3000 步，只多 504 个会话，SR 43.2 vs 测地线微调 34.9 vs 基础 35.0（表 4）；完整版 44.9（+9.9，场景自助法区间 +3.9–16.3）。增益分解清楚：对基础 VLA，停止项 +11.6、到达项 −1.7（表 7）。它改变的判断是：从 harness 蒸馏不一定要把规划器缩小，可以直接训被调用的执行模型，前提是会话要改写成学生测试时的接口。与前期区别：2610.41216 蒸给 4B 规划器；2610.25376 TILDE 是教师接管学生失败状态。 |
| 2 | 2611.15651 | 学生训练＋harness 组件：用单因素扰动造失败数据，训练 8B 纠错脑输出 Judge–Cause–Sub–Fine，接入 GPT-5.5 写码 harness | 同一 GPT-5.5、同一函数/感知/任务/种子/预算，只换纠错者：十格全部高于未训练纠错脑（平均 +13.9），对 GPT-5.5 自纠 6 高 2 平 2 低（表 3）；真机 Piper 两种冻结 VLA 各 100 回合。问题清楚（诊断“哪个前提坏了”而不是重复失败），训练用“准确前缀打分、自生成前缀生成”处理部署时前缀失配。与前期区别：2610.40016 LOGIV 不训练、只修失效支持；2611.13039 是阶段监控；2306.15724 REFLECT 是零样本解释。 |

### 画报侧重

- **2611.16246（ready）**：白底题头＋俯视地图示意（标示意）；运动来源色带（表 1）；三规则卡；同配方三格大数（表 4）；100% 结局条（图 4）＋到达/停止分解桥图（表 7）；师生对照表（表 6，注明 63 会话模型）；消融点区间（表 8，Wilson 区间为我们计算）；深色双栏边界（OSR 下降、无偏航恢复、rank 在 val-unseen 子集选择、仅仿真、采集成本未报告）。
- **2611.15651（视觉 QA fail）**：浅紫题头＋四栏纠错记录卡（附录 E.1 改写）；数据工厂五站条；双前缀对照；表 3 三方点图带双差值列；图 5 斜纹柱图（加权整体为我们计算，π0 略降）；图 7 计数表＋红色“对照不等预算”警示框。

## 排列、去重与取舍（编辑理由，均有原文或记录依据）

1. 8 篇均为 P3 / confirmed。q3：capability 6，judgment 2，不分先后，不按数值排序。
2. **与前期已选同判断重复（1）：**
   - 16009 JustRUA：同一 RoboDojo 基准、同一 GPT-6 直接控臂 harness 路线，结论“报告的弱点多在 harness；几何信息贡献最大”与 2611.01560（“先排除接口，再谈模型；标定而非深度承载几何”）同判断；2611.08209 也已覆盖“更丰富界面的收益与花费”。另外它是自家 111 回合评测集上的逐步路径、每变体单次、非 factorial，行为计数由模型审视频（读 §1–2.5 与摘要/结论）。
3. **范围与代表性让位（3）：**
   - 16872 ACE-CaP-0：编码代理改程序的卡已有 2610.31841、2610.36533、2611.09030、2611.06863、2611.12177、2611.02391；本篇的新点“按需示范＋按需仿真”的每个条件都只有**一次开发运行**（§2 与结论自承），30 次评测只检验同一个程序的可靠性，不足以支撑“哪种经验获取方式更好”的展示结论；八任务 221/240 没有匹配基线（读全文）。
   - 15317 BiPOP：LLM→时间规划的符号求解路线，本仓已有 2611.12409、2610.41844 等；全部动作单位时长、效率是符号 makespan，真机 NICOL 只有端到端演示无次数（读缓存）。
   - 15093 PreNav：LLM 只离线调用一次给共现分数，harness 角色弱；同结构先验下对 SGM 的增益 +2.3 SR / +3.0 SPL（十类 +1.4、SPL 持平），无多种子区间（L2 facts 与缓存核对）。
4. **证据不足以展示（2）：**
   - 15964 COMBS：读全文（含缓存缺失的 §III-I–J、表 V）。最有 harness 意义的结果——“提示 LLM 可以停止时会放弃 12.3/22.4% 的在场目标，COMBS 为 1.6/3.2%”——所依赖的 “external LLM” **未写明是哪个模型、提示词未公开、无附录**；完备性定理要求 α=1 且每次探查揭示全部子节点，缺失判定的保证另需搜索条件独立；开容器为抽象动作（MP3D 打开即揭示全部内容）。L2 已把 Q1 记为 measured_own 而非 proof，判断不推翻，不退回。
   - 16671 NSDL：全部为符号回放打分（“Scoring is symbolic replay only”），证据等级 offline；L2 已按 B 类方法学收录并写明，画报需要的闭环结果不存在。
5. later_work：8 篇都没有 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标版本（均为 `FULLTEXT: html`、v1、core 裁剪版）。2026-11-14 查 arXiv abs，下列各篇都只有 v1；同版本 HTML 转换稿只放 /tmp，不提交。

| paper_id | 版本 | 读到范围 | 结论 |
|---|---|---|---|
| 2611.16246 | v1 | HTML 全文：§1–5、表 1–9、附录 A–D、图 3/4 SVG | 通过，无 correction。展示缩窄：主表与测地线微调步数不同（严格对照用表 4）、表 6 与表 8 是不同模型、rank 在 val-unseen 子集上选（记 online）。 |
| 2611.15651 | v1 | HTML 全文：§1–5、表 1–4、附录 A–G、图 5/7 SVG | 通过，无 correction。补读附录 G 发现真机对照不等预算（有纠错最多 10 次恢复，无纠错一臂重试规则未写、无未训练纠错脑对照）；π0 冻结 VLA 加权整体略降（我们计算）。均作展示缩窄，不推翻 Q4=fits（受控证据在表 3）。 |
| 2611.15964 | v1 | HTML 全文：§I–V、表 I–V（无附录） | 未入选（证据不足以展示，见上）。与 L2 facts 一致。 |
| 2611.16872 | v1 | HTML 全文：§1–6、表 1 | 未入选（让位）。与 L2 facts 一致（单开发运行、十次复位不含示范复位）。 |
| 2611.16009 | v1 | HTML §1–2.5 与摘要/结论（未读 §3–8 细表） | 未入选（同判断重复），去重理由不依赖 §3–8 细数。 |
| 2611.15317 / 16671 / 15093 | v1 | 缓存（core） | 未入选；排除理由所引事实在缓存中逐条核对。 |

## Correction

本期没有。补读发现（16246 的步数与 rank 选择口径；15651 的真机对照预算与 π0 整体略降；15964 的外部 LLM 未具名与定理条件）都不推翻问题档位、Q1–Q4 或 evidence_status。供 Sol 后续参考：15651 的 L2 子卡检查可补上“真机对照不等预算”一条（附录 G.3）；15964 若后续版本写明 LLM 与提示词，可单篇复核。

## 待补与漏检抽查

- 待补：本期没有新增。
- 漏检抽查：本期没有新的抽查改判。
- 下期备选：不指定。2611.15651 的画报只差版式修复，待总控授权后修一次并重新视觉 QA，通过后再记 ready 并进索引。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2611.16246 | **ready**（第 1 次：地图标签被裁、桥图负值标签重叠、页底留白 → 重做一次；重做轮内对一处 “−0.4” 标签做单行追加修复后通过，QA.md 如实记录） | `reel/2611.16246/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2611.15651 | **fail**（第 1 次：页面溢出、组名重叠、菱形被遮、图例压数 → 重做一次后仍溢出页底且 LIBERO-PRO 组名重叠；按规则停止） | `reel/2611.15651/`：poster.html · poster.png · poster.pdf（均为未通过版，勿发布）· SOURCE.md · QA.md |

- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（张数 50→51、增量 run 32→33 张、新增 2611.16246 一行、“选择与制作”新增本期条目）；`README.md` 本季漏斗统计行（追加 “8 P3-confirmed → +1 poster”，50 → **51 posters**）。2611.15651 未进索引。progress.md 未动（由总控写共享进度）。
