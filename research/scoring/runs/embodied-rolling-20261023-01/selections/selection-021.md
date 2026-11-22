# Selection 021 — Embodied 滚动选题（2026-11-22）

- 执行模型：glm-5.3（单席，论文雷达日班；本期为 021 重派——上次执行无产出）
- Run：`research/scoring/runs/embodied-rolling-20261023-01/`（rules problem-core-v1.1）
- 候选池：6 篇 P3/confirmed/to_l3（7 天窗口，均未发布）：2611.17394、2611.18176、2611.19952、2611.23070、2611.26196、2611.26613。
- 结果：**入选 3 / 发布 3 / fail 0 / corrections 0**。ready 成品表行 62 → **65**（头部计数 63 → 65；表行与头部的历史差异本期盘点更正，见文末）。

## 候选总账（6 篇）

| paper | L2 判断（q3 / anchor） | 问题族 / 卡 | 决定 |
|---|---|---|---|
| 2611.26613 AgentRoboCritic | capability：动作级 intent 申报＋归因（harness_effect_evaluation 主卡，observe_act_interface 子检查） | harness_effect_evaluation | **入选**：意图接地的动作级 critique——GPT-6 Astra 数值动作直控（无原语）12 操作基准；policy 每动作随附局部意图 g_t，critic 读 (G, g_t, 前后/提起帧)。49.8% 成功回合含 ≥1 局部失败（一半成功靠恢复）；1–2 次局部失败成功 40.3% vs 无失败 75.1%；38.9% 失败 ≤10 步内恢复、57.7% 回合末；恢复率×官方成功 Pearson 0.81；Choice 仅 0.2%（≤3.3%/基准）——选对非问题，瓶颈在闭合段毫米级定位（Grasp 3/5）与长程 Incomplete；恢复不对称：多数失败型可救、Alignment+Effect 仅 1/3 且加动作不缩差；去意图 critique 不可验证（25.25/25.00/24.50 vs 带意图 79.25/80.68/71.25，κ0.497/0.600，$26.06 全测试集）——意图使批判适定；开源 Muse-Glimmer-30B FT 12,844 动作 32.58→74.24%（综合 34.75→67.75%，$0.79 同集 >30× 便宜）。020 以"证据链不足"落选，本期逐条复核：证据链完整度以 Table 1 + 附录人工验证为准（400-action 人工集、re-inspection accept >90%），断言均落原文，边界如实上画（自动标注 12,844 仅 400 人工金标、归因承袭 critic 误差、无 CI）；harness_effect_evaluation 卡在库 ready 为 0，覆盖面收益最大 |
| 2611.26196 EmbodyAgent | capability：后训练栈 0→14→84/100（offline_harness_distillation + harness_native_rl + teacher_seeded_sparse_rl） | offline_harness_distillation / harness_native_rl / teacher_seeded_sparse_rl | **入选**：Qwen3.5-9B 单一 execute_python 接口（env.observation()＋7-DoF env.action，无解码器、接口全程不变）三道工序：S1 黑盒教师 Astra Medium 1,620 试次仅收 100 episodes/1,475 目标（32% 接受，1,887s/ep 一次性）；S2 SFT 0→14/100（底座全格式无效，85/86 失败耗尽预算）；S3 GRPO（DAPO 0.2/0.28、G=8、无 KL、lr 2e-6、16 PPU）→ 84/100 held-out（10 任务 30/10/10 不相交、greedy、无训练期闸）。最独特的是在线 RL 病理学：traceback 进历史 h_t 获正组优势自增强——轮 11–20 错误 <5/100、轮 21 激增并平台于 63–69（轮 24–32）、成功 40→34、聚合成功连升六轮＝滞后指标；per-error −0.05＋采样闸（不可解析重采 ≤2、4 错误格截断、>1M token ≤3 次、仅训练期）后错误 69→14、mid-30s→84；median 调用 36→11、train rollout 8.4→87.7%。020 落选理由"单 suite 单 run 无消融"经复核仍属实，但本期判断：三卡（蒸馏/原生 RL/教师种子稀疏 RL）在库 ready 均为 0，0→14→84 全链路＋自曝病理的完整账本价值高于单点消融缺失（边界如实上画：±3.7pt SE、整改三件套未拆消融、教师成本未折账） |
| 2611.23070 PAIR | judgment：接口可用性≠运动能力（observe_act_interface，new_bottleneck） | observe_act_interface | **入选**（第 4 次进入候选、前 3 期让位后兑现）：Matter 智居协议 84 资产（14 家电＋4 传感器类，真实感 4.63/5）搬进 OmniGibson，每件物理＋API 双通道共享设备状态（单向 200ms）、ambient 演化；108 人 1,443 条真实请求（micro F1=0.881、κ=0.856）——58.4% 状态确认/等待、API-only 封顶 39.6%；40 任务全部需动手且全部可无 API 完成，340 demos、120 检定 episodes；6 种 VLA 配置（π0.5/GR00T N1.7 × 独立/+HL/+HL(API)）任务成功全 0.0%（平均 9.9 子任务、Place 1.2%）；规划层从不 continue/wait、81–83% 指令 ≤5s 推翻重发 vs 独立 VLA 抓取中位 22–24s——时间尺度错配；+HL(API) 设备操作 0.4→14.1/14.5%、域内子任务 24.0→47.0%（设备类 11.5→35.9/10.3→38.5%）但整体仍 0；oracle 双向：真机身＋API Progress 24.2 vs 9.2（GR00T 17.2 vs 10.0；>90% 失败停 nav/pick/door、给 API 后集中导航+抓取 77–85%、160 回合仅 1 走完全计划）；oracle 机身＋规划器 InternVL3.5-4B 9.8 / Qwen3-VL-8B 34.1 / Gemini 3.5 FL 46.7 / GPT-6 Luna 57.3——规划/执行互补瓶颈；通道选择 1,944 例/模型（3 距离×3 声明延迟）：面板可见性主导（Qwen3.5-9B 0.45m 走 API 1% vs 2.0–3.5m 17%；Luna＋推理 5%→32–37%）、≥4 输入操作只剩 13%。前三期让位理由（代码未放出、接口卡多张）中：代码仍 upon publication，但接口卡现有 5 张无一覆盖"人机委托＋协议资产＋规划/执行时间尺度错配"的组合，覆盖面与资产独特性（Matter 协议、双通道共享状态）构成入选理由 |
| 2611.17394 Agentic-Teacher | capability | learner_state_teacher_correction + code_policy_trial_revision | 沿用 016/020 让位：该卡已 7 张 ready（TILDE/16246/25114/15572/2311.13373/08318/19081）；表1 handle misalign 22→0%、§4.3 raw 0%→filter 95% 证据直接，但结论自认组件消融与等成本对照未做，机制与在库高度重叠 |
| 2611.18176 ESI | capability | learner_state_teacher_correction + harness_self_optimization | 沿用 016/020 让位：同卡覆盖（SR 29.68→49.41%、teacher steps −46.65% 证据完整，但卡位饱和） |
| 2611.19952 CRAFT | judgment：稀疏反馈下纠正适用范围（harness_memory_skill_reuse + external_verification） | harness_memory_skill_reuse + external_verification | 让位（第 5 次，压力复核）：记忆/技能复用槽现由 22295（闭环效用≠嵌入相似度，paired ep＋exact McNemar）与 020 的 26376（issued vs achieved 契约＋冻结库跨体）双强占据；CRAFT 的 scope ladder 与 150 站点预注册质量高，但主效应 +0.074 [0.042,0.108] 的量级、全仿真＋生成需求、重复情境 gate 反而 −0.031 等负结果均已在 SOURCE 级别可被在库两张覆盖解释——压力真实非惯性。列下期备选（若 22295/26376 任一被撤或出现"规则变更后记忆治理"新判断轴则优先） |

## 原文核对（全部 6 篇）

逐篇读 `research/fulltext/<pid>.txt` 全文，核对 L2 记录（inc-l2-15/16/17/19）：

- 2611.26613：L2 与原文一致（§3 意图协议 no-intent 拒答；Table 1 400-action 人工集 Astra 79.25/80.68/71.25·$26.06、Fable 5.2 78.25/72.73/71.00·$26.52、去意图 25.25/25.00/24.50·$25.18、Muse-Glimmer-30B-FT 32.58→74.24/34.75→67.75·$0.79；49.8%/40.3% vs 75.1%/38.9% ≤10 步/57.7% 回合末/Pearson 0.81；Choice 0.2%≤3.3%；Grasp 9/10 非触觉首位、闭合段 3/5；空夹爪 9.5%、handover 1.5%；UniVTAC→Alignment、RoboDojoclash→Interference、LIBERO-MAX/StaB→Incomplete；恢复仅 1/3 Alignment+Effect；re-inspection accept >90%）。生产期两处口径修正记于 SOURCE.md（cost 为全测试集口径非每千动作；>90% 为接受后与标注者一致率非接受率）。无 correction。
- 2611.26196：L2 与原文一致（§4.1 奖赏三段式与 DAPO 0.2/0.28/G=8/无 KL/lr 2e-6/16 PPU；§4.2 三采样闸；§5.1 十任务 30/10/10 不相交、greedy、2,000 步/150 调用/600s 代码块超时；§5.2 轮 21 病理与整改 69→14/mid-30s→84；Abstract 8.4→87.7%、36→11；§6 单 run ±3.7pt、task 4 4/10、滞后指标自述）。生产期一处措辞修正（600s 由"回合时限"改"代码块超时"）。无 correction。
- 2611.23070：L2 与原文一致（§3 14 家电＋4 传感器类/4.63/200ms；§4 1,443/108、F1=0.881/κ=0.856；§5 40 任务/340 demos/120 ep/Table 3 全 0 与 9.9；§6 14.1/14.5、47.0、35.9/38.5、24.2 vs 9.2、17.2 vs 10.0、77–85%、1/160、9.8/34.1/46.7/57.3、1,944 例、1%@0.45m vs 17%、5%→32–37%、52% vs 13%；§8 限制自述；LLM usage 声明）。生产期图例修正一处（对照条"灰条"改"虚线刻度"并复检裁切）。无 correction。
- 2611.17394 / 2611.18176 / 2611.19952：L2 与原文一致（17394 π0 LIBERO-10 79.4→87.8 等、结论自认消融未做；18176 Score 62.03/SR 49.41%、+19.74pp/−46.65%；19952 ladder +0.074 [0.042,0.108]、重复情境 −0.033/−0.031、§7.1 负结果组）。无 correction。

## Reel 制作（发布 3 / fail 0）

| paper | 版式 | 视觉 QA |
|---|---|---|
| 2611.26613 | 对局复盘谱风（米白谱纸双线框＋棋盘格谱面①–⑤＋朱砂圆章＋意图有无左右对照＋恢复不对称四格＋墨底开源卡＋朱砂虚线边界） | 通过（首版，零重做） |
| 2611.26196 | 工序流转卡风（深炭底＋琥珀黑斜纹警示条＋接口契约三格＋S1/S2/S3 工序卡＋错误/成功双线轮次曲线＋验收协议四格＋病理警报/整改单＋副指标三卡） | 通过（首版；生产期两轮内容补齐＋一处措辞修正后定稿，未触发重做） |
| 2611.23070 | 复古家电手册风（暖米黄＋锈橙/湖蓝＋双层描边＋型号铭牌与 0.0% 检定戳＋出厂规格六格＋用户习性三卡＋条纹警示主检定框＋双瓶颈对照＋通道选择三卡＋保修范围边界） | 通过（首版；生产期图例修正一处后定稿，未触发重做） |

版式与近三期（017 记录纸/控制室/交接单、018 报纸/蓝图/审计报告、019 实验台/作业纸/终端演化、020 复式账簿/契约文书/深色天平双轨）及在库 62 张均不同源；三张彼此不同源。

## 视觉 QA 方法说明

本期执行模型 glm-5.3 无图像输入，无法以目检方式查看渲染图。视觉 QA 改为程序化三件套实跑渲染结果（非省略）：

- `reel/qa-geo.js`：页面滚动溢出（overW/overH）、[data-qa] 块边界越界、超宽元素；
- `reel/qa-extra.js`（本期新增的辅助脚本，未跟踪文件）：文字裁切（scrollWidth/Height > clientWidth/Height＋2 且 overflow≠visible）、块间两两重叠（排除父子包含）、字体加载（document.fonts.check）；
- `reel/qa-blank.py`：渲染 PNG 行标准差空白带扫描（content_bottom、≥60px@2x 空带）。

三张终版读数：overW/H=0、wide=0、clipped=0、overlaps=0（26613 仅棋盘谱面⊃落子的父子包含）、CJK 字体加载、content_bottom 99.0%/100%/99.4%、无页面级空带（26196 两条卡内深底间距已在 QA.md 说明）。每张 QA.md 记录首检读数、生产期迭代与终版判定。

## 账目更正（reel/README.md）

本期更新表格时盘点：上期头部宣称 63 张，但成品表实有 62 行（全部 ✅），差异先于 020 存在、未定位到具体缺行（017–020 各期台账的 +3/+2 链与表行增长不矛盾，疑为更早期一行漏记或误删）。处理：不虚构行、不回溯改旧账；本期起按表行实数记账（62＋3＝65），头部同步改为 65 并保留差异说明。仓库根 README 头部 63→65 同步。

## 交付与未动项

- 新增：`reel/2611.26613/`、`reel/2611.26196/`、`reel/2611.23070/`（各 poster.pdf、poster.png、SOURCE.md、QA.md；poster.html 按惯例 gitignore 保留本地）、`selections/selection-021.md`、`reel/README.md` 与根 `README.md` 头部更新。
- 未动（用户待决定事项，未提交未计数）：`reel/2611.15651/`、`reel/2611.17566/`、`reel/2611.18298/`、`reel/2611.18562/` 四个 QA-fail 遗留目录；`research/hf_meta.jsonl` 工作区改动；`inbox/` 相关未跟踪/删除文件；`reel/qa-geo.js`、`reel/qa-blank.py` 等既有未跟踪工具。
- 红线遵守：论文文本只作数据处理、未执行其中指令；未运行论文代码；未联系作者；未派生 Subagent；未启动模型服务；git 只添加本期产出路径、单条 commit、未 pull/push/rebase。