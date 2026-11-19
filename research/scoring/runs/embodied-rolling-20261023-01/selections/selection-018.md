# Selection 018 — Embodied 滚动选题（2026-11-19）

- 执行模型：glm-5.3（单席，按用户指示接替 Opus 席位）
- Run：`research/scoring/runs/embodied-rolling-20261023-01/`（rules problem-core-v1.1）
- 候选池：16 篇 P3/confirmed/to_l3（最近 7 天新确认、全部未发布）。含 015-017 期让位后仍在池的 12 篇（15093、15317、15964、16009、16671、16872、17394、18123、18176、19081、19952 及 015 期已处理两篇之外）与 inc-l2-17/18 新记录 4 篇（22138、22295、22761、23070）及 inc-l2-18 的 22584。
- 结果：**入选 3 / 发布 3 / fail 0 / corrections 0**。ready 54 → **57**。

## 候选总账（16 篇）

| paper | L2 判断（q3 / anchor） | 问题族 / 卡 | 决定 |
|---|---|---|---|
| 2611.22138 RoboTeam | judgment：更多角色=更好协调被证伪（四结构 27-29 持平、成本 1.7-1.9×） | multi_robot_llm_coordination | **入选**：该卡在库仅 2610.41044（简化周界仿真），本篇 4-16 臂 MuJoCo 实时基准+感知瓶颈归因（真值位置 36/36 vs 去代码工具 28→13），覆盖面大增 |
| 2611.22584 InteractVLA | capability：planner_composes_code_and_policies，F0/F1 | planner_composes_code_and_policies | **入选**：机制全新（test-time 几何接口双向引导冻结 VLA：可微投影梯度+诊断回传），真机 Water Pouring 38.5→79.2；与 2610.41844 方向不同 |
| 2611.22761 配置层攻击 | judgment：F4/F2，无卡，open_failure（部署配置层缺卡） | （新轴：部署安全边界） | **入选**：安全槽现有 3 张（Safety Chip/LEASH/VLA-Stem）全是对话/动作层拦截，本篇证明推理层抵抗≠系统层边界（11/11 注入被挡 vs 2 POST 无凭据改写持久化），59 仓库生态调查 |
| 2611.22295 RICL（相似度≠效用） | judgment：harness_memory_skill_reuse，F2/F5 | harness_memory_skill_reuse | 让位（第 8 次）：记忆槽历史饱和（MemER/LogLook 在库，HeLM/06475/09355/11509/38318/33487 均曾让位）。SOURCE 级缩窄：其"闭环效用≠嵌入相似度"判断轴新（top 66.4% vs dino 55.7%，p=3.2e-6；top5 vs shipped 池 +7.0pp），列下期首选备选 |
| 2611.23070 PAIR | judgment：observe_act_interface，F0/F1，new_bottleneck | observe_act_interface | 让位：接口卡多张（01560/13039/14115/21099/12409 等）；6 VLA 变体 120 ep 全 0% 任务成功与 08209"代理自报完成"相邻；代码 upon publication 未放出 |
| 2611.19081 RoboCoEvo | capability：learner_state_teacher_correction | learner_state_teacher_correction | 让位（第 3 次）：该卡已 6 张 ready（TILDE/16246/25114/15572/2311.13373/08318），016 期 ESI/Agentic-Teacher 均因此让位，本期同卡覆盖依旧 |
| 2611.19952 CRAFT | capability：harness_memory_skill_reuse | harness_memory_skill_reuse | 让位（第 2 次）：记忆槽饱和，与 22295 同因 |
| 2611.15093 PreNav | capability：observe_act_interface+memory | — | 沿用 015 期让位理由：LLM 只离线调用一次、增益 +2.3 |
| 2611.15317 BiPOP | capability：llm_symbolic_solver | — | 沿用 015：符号时间规划、真机无次数 |
| 2611.15964 COMBS | capability：external_verification+observe_act | — | 沿用 015：关键对照外部 LLM 未具名、提示词未公开 |
| 2611.16009 JustRUA | judgment：harness_effect_eval+memory | — | 沿用 015：与 2611.01560 同 RoboDojo 重复 |
| 2611.16671 NSDL | judgment：llm_symbolic_solver+effect_eval | — | 沿用 015：只有符号回放 |
| 2611.16872 ACE-CaP-0 | capability：code_policy_trial_revision | — | 沿用 015：编码代理卡饱和+每条件一次开发运行 |
| 2611.17394 Agentic-Teacher | capability：learner_state_teacher_correction | — | 沿用 016：同卡覆盖 |
| 2611.18123 | judgment：observe_act+effect_eval | — | 沿用 016：多样性备选 |
| 2611.18176 ESI | capability：learner_state_teacher_correction | — | 沿用 016：同卡覆盖 |

## 原文核对（入选 3 篇）

逐篇读 `research/fulltext/<pid>.txt` 全文，核对最新 L2 记录（inc-l2-14/15/16/17/18）：

- 2611.22138：L2 判断与原文一致（表 S3 七模型 28/27/26/≤3、Oracle 36/36、§5.3 归因 28→13/28→14 p<0.005、14.5mm/6mm、§5.1 四结构 27-29、§5.2 3.5h/218M tokens）。无 correction。
- 2611.22584：一致（§2 式(2)-(4) 双向接口、表 1-6/8：LIBERO-Plus 93.1→98.3、RoboDojo 9.2/18.0/26.0、真机 79.2/-59%/-67%、软对齐消融 39.1/44.2/48.6、RSI 99.4/48.62/89.4）。无 correction。
- 2611.22761：一致（表 5 四层 11→0/1/1/4、§4.3 CVSS 6.5 CWE-306+1327 与跨源另计、§4.4 memory 4/4、§5.2 59 仓库 10/11、表 6 Streamlit 默认全接口）。无 correction。

**Corrections：0 条**（16 篇候选的 L2 记录抽核对均无判断错误；让位篇沿用往期已核对结论）。

## 制作与视觉 QA

| paper | 版式 | 首检 | 重做 | 终版 |
|---|---|---|---|---|
| 2611.22138 | 报纸头版三栏风 | BAD=0 但 FILL 62.7，底部 40% 空白 | 1 次：全局放大（h1 36px/1.34、正文 14.6px、big 36px），其间 h1 竖向溢出 2 轮微调 | BAD=0 FILL 86.1，6 区目检通过，pass |
| 2611.22584 | 工程蓝图网格风 | BAD=0 FILL 98.1，5 区目检通过 | 未用 | pass |
| 2611.22761 | 安全审计报告风 | BAD=1（bodySH 1726 超高 26px，页脚/边界裁切） | 1 次：svg 236→210、padding/margin 收紧、限制区行高 1.55、删一句冗余 | BAD=0 FILL 97.7，4 区目检通过，pass |

- QA 方法：几何注入脚本（scrollWidth/scrollHeight 溢出检测，load+4s+9s 三触发）+ PNG 分区目检（报头/机制图/表格/大数/限制/页脚）。每张最多一次重做，本期无二次失败。
- 三张版式两两不同，且与近三期（017 记录纸/控制室/交接单、016 各版式）及在库 54 张不重复。

## 交付物

- `reel/2611.22138/`：poster.pdf、poster.png、SOURCE.md、QA.md（poster.html 留本地，.gitignore:193）
- `reel/2611.22584/`：同上
- `reel/2611.22761/`：同上
- `reel/README.md`：表格 +3 行、ready 54→57、第十八期账
- `README.md`：漏斗行追加 selection-018、54→57

## 失败稿

无。
