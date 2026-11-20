# Selection 019 — Embodied 滚动选题（2026-11-20）

- 执行模型：glm-5.3（单席，按用户指示接替 Opus 席位）
- Run：`research/scoring/runs/embodied-rolling-20261023-01/`（rules problem-core-v1.1）
- 候选池：13 篇 P3/confirmed/to_l3（015–018 期让位后仍在池的复用候选 + 上期让位的 22295/23070）。7 天窗口内均未发布。
- 结果：**入选 3 / 发布 3 / fail 0 / corrections 0**。ready 57 → **60**。

## 候选总账（13 篇）

| paper | L2 判断（q3 / anchor） | 问题族 / 卡 | 决定 |
|---|---|---|---|
| 2611.22295 RICL | judgment：闭环效用选示范 vs 嵌入相似度（challenges_barrier） | harness_memory_skill_reuse | **入选**（兑现 selection-018"下期首选备选"承诺）：记忆槽让位 8 次后，以新判断轴入选——pool-swap 岭回归 φ̂ 证明相似度检索与随机无差（dino 55.7 vs random 55.5）、闭环效用 +10.8pp p=3.2e-6，失效机制（区分场景不区分目标）与边界（池=10 增益消失、split-half 0.14）完整 |
| 2611.18123 空间先验 | judgment：LLM 输出坐标文本似然≠真实空间密度 | observe_act_interface + harness_effect_evaluation | **入选**：接口分工证据新——纯重排序鉴别率 0.191（文本效应与几何效应同量级）、贴墙结构缺失（p=0.274）、提示词直接翻转"先验"（B-walls 斜率变号）；"LLM 出关联、不出几何先验"对导航系统设计有直接约束力 |
| 2611.19081 RoboCoEvo | capability：程序化检测/恢复随策略更新 | learner_state_teacher_correction + harness_self_optimization | **入选**（破例，说明）：该卡已 6 张 ready、本文让位 3 次（017/018 期同卡均让位）。本次入选理由：表3 是该卡迄今最直接的"纠正必须随学生演化"证据——旧程序复用检测率 94–97→54–72、恢复 ≤47%，agent 修订后回 93–96/71–83；表4 消融给出 FM 共享程序一致性（0.758 vs 独立恢复 0.267）与增广成本账（GPU 147→36h）。机制重叠在"纠正教师→蒸馏"主题，新增点是"每轮重写程序适配漂移失败分布"的结构性证明，与 6 张在库卡互补而非重复 |
| 2611.23070 PAIR | judgment：接口可用性≠运动能力（new_bottleneck） | observe_act_interface | 让位（第 2 次）：代码 upon publication 未放出；接口卡在库多张（01560/13039/14115/21099/12409）；6 VLA 120 ep 全 0% 任务成功与 08209"代理自报完成"判断相邻。其 Matter 协议仿真资产（84 设备/物理面板-API 双向耦合）与通道选择实验（面板可见性>API 延迟）是独特增量，列下期备选 |
| 2611.19952 CRAFT | judgment：稀疏反馈下纠正适用范围 | harness_memory_skill_reuse | 让位（第 3 次）：与 22295 同记忆槽，本期 22295 已以更强的对照证据（paired ep + exact McNemar）覆盖该卡；其 scope ladder（记忆×规则×开放层指数加权）与 150 站点预注册确证（新情景 +0.074[0.042,0.108]）质量高，列下期备选 |
| 2611.15093 PreNav | capability | observe_act_interface+memory | 沿用 015 期让位理由：LLM 只离线调用一次、增益 +2.3 |
| 2611.15317 BiPOP | capability | llm_symbolic_solver | 沿用 015：符号时间规划、真机无次数报告 |
| 2611.15964 COMBS | capability | external_verification+observe_act | 沿用 015：关键对照外部 LLM 未具名、提示词未公开 |
| 2611.16009 JustRUA | judgment | harness_effect_eval+memory | 沿用 015：与 2611.01560 同 RoboDojo 重复 |
| 2611.16671 NSDL | judgment | llm_symbolic_solver+effect_eval | 沿用 015：只有符号回放 |
| 2611.16872 ACE-CaP-0 | capability | code_policy_trial_revision | 沿用 015：编码代理卡饱和 + 每条件一次开发运行 |
| 2611.17394 Agentic-Teacher | capability | learner_state_teacher_correction | 沿用 016：同卡覆盖；本期 19081 已以更直接的漂移证据入选该卡 |
| 2611.18176 ESI | capability | learner_state_teacher_correction | 沿用 016：同卡覆盖；同上 |

## 原文核对（入选 3 篇）

逐篇读 `research/fulltext/<pid>.txt` 全文，核对最新 L2 记录（inc-l2-14–18）：

- 2611.22295：L2 判断与原文一致（表1：top 66.4/dino 55.7/random 55.5/bottom 43.8，+10.8pp p=3.2e-6；§3 pool-swap 岭回归 φ̂，60 池 |S|=5、init 0-9 拟合/10-49 评测不相交、40 paired ep/格/任务 exact McNemar；§5.2 goal:9 最近邻 57.5% 属他任务、任务内 Spearman 0.10；§4.2 池 3/5/10→+12.9/+11.8/+0.7、shipped top5 +7.0 p=0.006、相似度 curation −6.8；表2 六条被推翻假设；§4.3 split-half 0.14、best-of-ten 2/3；§6 单 checkpoint 单 port、真机未测、170 GPU-h）。无 correction。
- 2611.18123：一致（§5.1 表2 纯重排序 0.191、堆叠/换位 0.945-0.996、Keep-Drop +0.070/+0.145、切向/法向 +0.181/+0.251 浴室~0；§5.2 图5 频率 Spearman 0.75/0.67 对照 -0.03/-0.09、图6 贴墙超额真实 +0.146→−0.163、Qwen SD 比 10.58 p=0.274、Gemma 秩相关 0.00、图7 B-walls 斜率 −0.188/−0.661；§5.3 图8 生成先验省 0.036-0.077/0.015-0.069、真实先验的 14-32%/10-23%；§3 限制：2 模型 4 房型、闭集 18/14、ScanNet 7-26% 四墙完整）。无 correction。
- 2611.19081：一致（表1：BEHAVIOR Q 0.40→0.49→0.56 Succ 0.23→0.34、RoboTwin 79→93%、RoboCasa 79→91%、自恢复 0.18→0.54、目标 FM 失败占比 0.19→0.06；表3 旧程序 94-97→54-72 恢复 ≤47%、修订后 93-96/71-83；表4 success-only 0.633→0.642、独立恢复 0.267、共享程序 0.758、+增广 0.84、token 3366M→261M GPU 147→36h；§3 held-out ≥70% 接受、DAgger 1:1；§5 只学成功恢复示范）。无 correction。

**Corrections：0 条**（13 篇候选的 L2 记录抽核对均无判断错误；让位篇沿用往期已核对结论）。

## 制作与视觉 QA

| paper | 版式 | 首检 | 重做 | 终版 |
|---|---|---|---|---|
| 2611.22295 | 深色数据实验台风 | BAD=0 但 fill 约 42%（内容止于 css 722、底空 978px） | 1 次：全局放大（h1 44、正文 14、svg 238 viewBox、big 46、gap 18），中途超 269px 后两轮微调收口；期间发现截图参数坑：--window-size=2400,3400+dsf=2 会让画布只占 PNG 左上 1/4（误判塌陷），正确为 1200,1700+dsf=2，已记入 QA.md | BAD=0 bodySH=1700 满幅，6 区目检通过，pass |
| 2611.18123 | 横纹作业纸风 | BAD=0 但 ft 底 1513/1700，底部空约 187px（fill 89%） | 1 次：全局放大（h1 47、lede 18、表格 14.2、大数 45、gap 26）后超 57px，两轮微调（大数 48→45、gap 23、ft padding 9）收口 | BAD=0 bodySH=1700，内容满幅，6 区目检通过，pass |
| 2611.19081 | 深蓝绿终端演化风 | BAD=0，fill≈96%（ft 底 1642/1700） | 未用 | 首版即过，6 区目检通过，pass |

- QA 方法：几何注入脚本（scrollWidth/scrollHeight 溢出检测 + 分区 marks 定位）+ PNG 空带扫描（行标准差<6 判空）+ PIL 分区目检（报头/机制/表格/大数/限制/页脚）。每张最多一次重做，本期无二次失败。
- 三张版式两两不同，且与近三期（017 记录纸/控制室/交接单、018 报纸/蓝图/审计报告）及在库 57 张不重复。

## 交付物

- `reel/2611.22295/`：poster.pdf、poster.png、SOURCE.md、QA.md（poster.html 留本地，.gitignore:193）
- `reel/2611.18123/`：同上
- `reel/2611.19081/`：同上
- `reel/README.md`：表格 +3 行、ready 57→60、第十九期账
- `README.md`：漏斗行追加 selection-019、57→60

## 失败稿

无。
