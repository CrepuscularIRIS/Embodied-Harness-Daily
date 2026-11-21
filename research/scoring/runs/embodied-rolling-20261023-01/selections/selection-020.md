# Selection 020 — Embodied 滚动选题（2026-11-21）

- 执行模型：glm-5.3（单席，按用户指示接替 Opus 席位）
- Run：`research/scoring/runs/embodied-rolling-20261023-01/`（rules problem-core-v1.1）
- 候选池：9 篇 P3/confirmed/to_l3（7 天窗口，均未发布）。
- 结果：**入选 3 / 发布 3 / fail 0 / corrections 0**。ready 60 → **63**。

## 候选总账（9 篇）

| paper | L2 判断（q3 / anchor） | 问题族 / 卡 | 决定 |
|---|---|---|---|
| 2611.25179 SimAudit | judgment：success checker 本身是弱代理信号（challenges_measurement） | external_verification_control | **入选**：审计 3 基准（RoboTwin 2.0/RoboCasa365/RoboDojo）142 任务的 success checker——61 缺陷/49 任务（40 phantom+21 silent），五因分解（proxy signal 16/missing condition 17/unstated requirement 15/loose geometry 10/transient success 3）；管线 Read→Guess→Stage→Review（probe 物理可达、未写 probe 的 VLM 四档审核、2/3 被拒、50 被拒样本人工抽查）；Verified checker 重评 9 policy 排名不变但差距失真（RoboTwin 全降、RoboDojo 全升 VPP +9.1、flip 率可超净变化）。该卡在库仅 2411.04549（+2610.37196 相邻），机制面新：把"外部验证"拉到基准自身判定层 |
| 2611.26376 UniCraft | judgment：跨体复用的成立条件是执行契约对齐 | harness_memory_skill_reuse + observe_act_interface + harness_self_optimization | **入选**：issued vs achieved 契约（完成谓词作用于设备测得值，替换为指令值即违约；set_gripper 两原生绑定同谓词同判）+ episode-local 统一几何帧 + 逐案非回归门控；180 任务×6 本体=300 对、3 agent model 各 2700 rollouts 同案同序同预算；冻结 Astra 库 zero-shot 跨 ARX-X5（74.0，学习期 88.5）与 4 新 agent model；违约账（Gemini 23.75→17.50→21.25 门控放行仍 held-out 回归）与失败四因完整。"契约+冻结库跨体迁移"判断轴与记忆槽让位诸篇不同 |
| 2611.26414 ZeroVLN | judgment：导航能力可以外挂在接口层而非权重层（condition_split） | observe_act_interface + harness_native_rl | **入选**：同骨干同 34.4k episodes 受控组，语义工具接口+联合 RL 零 SFT——SAGE-3D/R2R/RxR 51.3/52.7/51.4 vs NaVILA 23.5/46.5/48.7 vs DualVLN 21.2/15.4/17.7 vs Direct Tool 39.5/19.0/10.2；权重位移 0.01497% vs 3.21/7.67%，12 通用视觉基准保留 59.16%（底座 59.47%，两 SFT 基线≈0）；Answer 前缀探针证明损伤在参数层非指令遵循（62.00 vs 62.86）。"接口适应 vs 权重量适应"双重量化最干净 |
| 2611.19952 CRAFT | judgment：稀疏反馈下纠正适用范围 | harness_memory_skill_reuse + external_verification | 让位（第 4 次）：与 22295 同记忆槽，上期 22295 已以更强对照证据（paired ep+exact McNemar）入位；scope ladder 与 150 站点预注册质量高，列下期备选 |
| 2611.23070 PAIR | judgment：接口可用性≠运动能力 | observe_act_interface | 让位（第 3 次）：代码 upon publication 仍未放出；接口卡在库 5 张（01560/13039/14115/21099/12409+22584）；6 VLA 120 ep 全 0% 任务成功证据受演示量混淆。Matter 协议资产独特，列下期备选 |
| 2611.17394 Agentic-Teacher | capability | learner_state_teacher_correction + code_policy_trial_revision | 沿用 016/019 让位：该卡已 7 张 ready（TILDE/16246/25114/15572/2311.13373/08318/19081），表1 handle misalign 22→0% 与 §4.3 raw→filter 95% 证据直接但机制与在库高度重叠 |
| 2611.18176 ESI | capability | learner_state_teacher_correction + harness_self_optimization | 沿用 016：同卡覆盖 |
| 2611.26196 EmbodyAgent | capability：后训练栈 0→14→84/100 | offline_harness_distillation + harness_native_rl + teacher_seeded_sparse_rl | 不入选：单 suite 单 run（±3.7pt SE）无组件消融；error 自增强循环 5→63-69 而成功仍升（滞后指标）的监控+罚项修复观察有价值，证据链不足以支撑海报级断言 |
| 2611.26613 AgentRoboCritic | capability：动作级 intent 申报+归因 | harness_effect_evaluation | 不入选：49.8% 成功 episode 含被修复失败与恢复不对称证据好，但 12844 标注仅 400 人工验证、归因链承袭 critic 自身误差（79.25/κ0.497）且无 CI——证据链薄于在库卡 |

## 原文核对（入选 3 篇）

逐篇读 `research/fulltext/<pid>.txt` 全文，核对 L2 记录（inc-l2-19）：

- 2611.25179：L2 判断与原文一致（142 任务→568 候选状态→183 预测命中→61 缺陷/49 任务；表1 RoboTwin 31=20幻+11静 proxy 主因（读 gripper command 而非手指实际状态）、RoboCasa 18=17+1、RoboDojo 12=3+9 全 unstated；Read/Guess/Stage/Review 管线与 VLM 四档审核 2/3 被拒、50 被拒样本人工抽查；两位独立标注者确认 61；Verified checker（物理状态+条件对齐+持续 1 秒）1233 expert episodes 全过；表2 重评 9 policy：π₀.₅ 46.2→42.3、X-VLA click bell 95→20 单任务、LingBot-VA 93.1→90.0 全保、RoboCasa 全降、RoboDojo 全升 VPP 30→39.1/StarVLA-QwenOFT 0.9→5.5；排名不变、GR00T 100%/30% 两档差距拉大、VPP 逼近领先、flip 率超净变化；mouse 21cm/双瓶例 §3.2/§1）。无 correction。
- 2611.26376：一致（§4.1 6 本体 3 基准 300 对、3 agent model 各 2700 rollouts 3 epoch×6 batch；§3.1 R_tcp 与 a=(σ,F,φ) 谓词作用于测得值、"issued but not achieved is a failure"；§3.2 门控 Δ_c≥0∀c 且>0≥1；保留率 38.7=12/31、40=12/30、39.3=11/28；E1→E3 unseen 9-28pp/10.8-13.3/3.1-14.4；表2 UniCraft(Astra) 86/89.25/37.5 vs X-VLA 96（RoboTwin ckpt 仅 10%）/π₀.₅ 10.63；冻结 ARX-X5 74.0（88.5，保留 83.6%）；robosuite 2K Astra 66.7/Sol 67.3/Terra 48/Gemini 28/DeepSeek 32.7/MiniMax 24.7；RoboDojo 54.8=115/210 Memory 76.7；pick 54-64%/move_to 81-96%；Gemini 23.75→17.50→21.25；2K→4K 66.7→83.3/67.3→75.3/Terra 48→62、MiniMax 请求耗尽 40.7-56%）。无 correction。
- 2611.26414：一致（表1 受控组同骨干同 34.4k episodes 四行全对；NaVILA-SAGE 500K 46.0<51.3；权重位移 0.01497/3.21/7.67；保留 59.16 vs 59.47、两 SFT≈0；Answer 探针 62.00 vs 62.86、两基线≈随机；OSR/SPL 权衡 66.7/64.6 vs 51.8/55.6 与 29.2/28.1 vs 41.8/43.0；消融：只训 expert 无提升、只训 brain 先升后降、轨迹级优于 round 级、去 first-arrival 严重退化；奖励四组件；execution-prefix h=4）。无 correction。

**Corrections：0 条**（9 篇候选的 L2 记录核对均无判断错误；让位篇沿用往期已核对结论）。

## 制作与视觉 QA

| paper | 版式 | 首检 | 重做 | 终版 |
|---|---|---|---|---|
| 2611.25179 | 复式账簿风（米色账本纸+绿/红双色账+五因横条+深墨绿大数+琥珀边界+金斜章） | BAD=0，content_bottom 100%（唯一空带为报头/管线卡间纸底间隙）；事实核对中发现一处 note 措辞歧义（易误读为 π₀.₅ 与 GR00T 间差距），修正后重渲染——事实措辞修正不计入重做 | 未用（视觉） | 4 分区目检通过，pass |
| 2611.26376 | 契约文书风（米白契约纸+靛蓝条款卡+圆形红章"冻结技能库"+当事人卡+违约记录红框+签署栏） | BAD=0，content_bottom 100%（空带仅顶部留白） | 未用 | 4 分区目检通过（含 rowspan 冻结库表），pass |
| 2611.26414 | 深色天平双轨对照风（深蓝黑底+橙/蓝双色轨+天平双盘+语义接口工具带+受控对照表+权重位移三卡+保留三格+消融账+权衡卡） | BAD=0，content_bottom 99.7%（空带为顶部留白与天平/接口带间深底间隙）；渲染前修一处 CSS 笔误（`#d8a globalThis89`→`#d8a989`），未产生可见缺陷不计入重做 | 未用 | 4 分区目检通过，pass |

- QA 方法：几何注入脚本（scrollWidth/scrollHeight 溢出+分区 marks）+ PNG 空带扫描（行标准差<6）+ PIL 分区目检。每张最多一次重做，本期三张首版均过、零重做。
- 三张版式两两不同，且与近三期（017 记录纸/控制室/交接单、018 报纸/蓝图/审计报告、019 实验台/作业纸/终端演化）及在库 60 张不重复。

## 交付物

- `reel/2611.25179/`：poster.pdf、poster.png、SOURCE.md、QA.md（poster.html 留本地，.gitignore:193）
- `reel/2611.26376/`：同上
- `reel/2611.26414/`：同上
- `reel/README.md`：表格 +3 行、ready 60→63、第二十期账
- `README.md`：漏斗行追加 selection-020、60→63

## 失败稿

无。
