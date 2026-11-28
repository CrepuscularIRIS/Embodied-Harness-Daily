# Selection 022 — Embodied 滚动选题（2026-11-28）

- 执行模型：glm-5.4[1m]（单席，论文雷达日班）
- Run：`research/scoring/runs/embodied-rolling-20261023-01/`（rules problem-core-v1.1）
- 候选池：16 篇 P3/confirmed/to_l3（7 天窗口，均未发布）——inc-l2-20：2611.23816、23855、24100、27499、30101、30550、30957、31115；inc-l2-21：2611.31894、32245、33144、33739、34675、34750；inc-l2-22（补材料复核后由 pending_material 升 confirmed）：2611.31201、34778。老积压 44 篇（窗口外 to_l3，如 2611.19952 / 17394 / 18176）默认不选，本期未纳入。
- 结果：**入选 3 / 发布 3 / fail 0 / corrections 0**。ready 成品表行 65 → **68**（头部同步 65 → 68；本期表行与头部一致）。

## 候选总账（16 篇）

| paper | L2 判断（q3 / q4 / 卡） | 决定 |
|---|---|---|
| 2611.34778 X-Harness | judgment / fits（inc-l2-22 由 partial 改 fits）/ harness_effect_evaluation + planner_composes_code_and_policies | **入选**：policy-harness 设计空间的七次一因子受控研究——489,380 次 rollout、4,025 cell、8 基准 267 任务、6 VLM × 15 VLA/WAM，同研究 arm 共享 seed、两层配对 bootstrap＋Holm、训练 seed 演化 / 测试 seed 盲评。Takeaway 1（VLM 直出 3D 位姿多数失败，目标点标注子目标 +34.6；LIBERO-PRO 偏移下 Flash +25.6 / Opus 用 3D 原语 56.9 > 带偏移 VLA 48.4）、2（相机深度比单目 +16.4；VLA 调用吸收深度误差）、3（Offline 31–35 s vs 在环 43–327 s；闭环比开环 +14.5）、4（模板 Flash +6.2 / Sonnet −3.7 / Opus −1.7）、5（分布内 92.5–100% 解出回合直接委托 VLA）、6（8 轮 +31.3～+54.2；回归门 +5.8）、7（Semi-online 多轮救援 77.3 ≈ Full-online 76.8，token 少 42%；一次性接管破坏多于挽救）；X-Harness 不更新权重 LIBERO-PRO 位置 / 任务 23.6→97.5、28.9→97.8，2,080 未见回合 / arm 仍显著。harness_effect_evaluation 卡在库仅 26613 一张，覆盖面收益最大；边界如实上画（累积组合无 leave-one-out、tier 研究仅 Argon＋Awomo 一对、未与同期 harness 系统直接比较、附录 J 真机以录制回放为主无现场计数） |
| 2611.31894 RESET | capability / fits / code_policy_trial_revision + external_verification_control | **入选**：一次真实演示 → 可接触世界 ＋ 从终态导出的冻结只读、对控制器隐藏的成功判据；Examine 用演示回放与轮廓 IoU 验世界；hold-out 门控自改进；冻结代码零 LLM 部署；世界＋判据原样交给零演示的目标机器人。50 个封存未见布局 × 8 任务 97% vs 零样本代码 27% / 逐任务微调 π₀.₅ 31% / DP 50%；缺陷注入（放大 10–20% 打破 12/18、桌面低 2 cm 练习 98% 但正确世界 18–20%、Examine 标出 16 个打破技能的几何缺陷中的 13 个）；松判据 "carton on box" 100% vs 演示导出判据 0%（"Checker is a weak proxy"的直接反例库）；真机 4 台 223/280（80%），源程序直接拷到 LIFT2 0 任务成功、共享世界练习后 80%。external_verification_control 卡在库仅 25179 / 22761 两张；代码自改进簇（34675 / 33144 / 33739）中唯一真机跨 4 本体且评测与开发布局分离者。边界：G1 真机 33%、π₀.₅ / DP 仅 100 条轨迹、单 agent、Examine 漏 3 个放大世界、真机不从真机失败改写 |
| 2611.30550 Body and Soul | judgment / fits / planner_composes_code_and_policies + harness_effect_evaluation | **入选**：零任务准备、规则固定的 VLM 监督 harness——整句递给冻结 VLA、VLM 自列计划、每 160 步看当前子阶段进展、停滞 120 步先改写指令、同一子阶段两次已核实失败才有界接管再交还；配对协议共享初始状态 / 随机数 / 时域，Eq. 1 保留–救回分解：200 回合 Xiaomi-Robotics-1 57.5%→70.5%（保留 104/115 = 90.4%、救回 37/85 = 43.5%，McNemar p=0.00022）；同规则给 4 个冻结策略各 +8–10 点、59 个单独成功只丢 1；按任务准备的 Harness VLA 任务记忆迁到更强策略为 −2.0（29 vs 30）；无 VLM 固定重发对照只复现 37 个增益中的 15 个。挑战"harness 需按任务 / 策略定制"与"A planner on top always helps"两条常用做法，与 22584（InteractVLA 双向接口）、14115（安全层）机制不同轴；与本期 34778 互为对照（34778：harness 要匹配能力；本篇：零准备规则可跨 5 策略，但原子任务盈亏保留阈值 91.5% vs 实测 96.6%）。边界：仅 RoboCasa365、开发覆盖 47/50 任务、重写 / 接管 / 校准未逐个消融、接管回合 20/65 成功 |
| 2611.31201 Embo-Harness | judgment / partial / harness_effect_evaluation + observe_act_interface | 同月同题簇去重 → 34778：RoboLab-120 83.3 vs 57.1、真机 15/20 vs 7/20 成立，但全文 Table 1–7 无方差 / 区间 / 配对检验，Table 5 EEF destination +5.0 与 Table 6（20 任务 × 1 次）在噪声量级；前向继承只在前缀上测；harness 实验仅 GPT-6 家族；20 任务开发子集在 RoboLab-120 评测集内、Table 2 基线为已发表数字未同骨干重跑。与 34778 §4.1 "VLM 直出位姿多数失败"的张力（骨干 / 分辩率 / 是否经 IK＋VLA 精炼）记于 34778 SOURCE.md，本期不裁决 |
| 2611.31115 RUIBench | judgment / fits / observe_act_interface + harness_effect_evaluation | 同月同题簇去重 → 34778：6 动作抽象 × 2 交互形式（13 接口）仅换 RUI 使 Claude Code 45.3→80.7、两前沿 agent 平均差 2.1 点、82.1%/70.9% 失败回合以完成声明结束——结论扎实，但接口轴与 34778 的 T1（动作层级）/ T4（代码形式）/ T7（调用时机）重叠，34778 覆盖 6 VLM × 15 VLA 并有配对统计；验证缺口判断在库已有 08209 / 26613。主文无区间、真机 5 任务单臂 |
| 2611.34750 SOLVE | capability / fits / observe_act_interface + harness_memory_skill_reuse | 让位（下期首选备选）：稀疏有序 6-DoF EEF keypose ＋ query_points 度量收据，RoboDojo 官方 74.5 vs 最佳条目 56.4、真机 UR12e 16 任务 85 回合 88%，结果强；但 observe_act_interface 卡在库已 5 张（01560 / 23070 / 26376 / 26414 / 22584），harness_memory_skill_reuse 槽饱和；keypose/次上限 1 vs 5 成功率相同（69.8 / 68.2）——"有序序列"贡献在调用效率而非成功率。与 34778 T1 的接地之争（度量查询接地 vs 单目读位姿）记于 34778 SOURCE.md |
| 2611.34675 RoboEvo² | capability / fits / harness_self_optimization + offline_harness_distillation + learner_state_teacher_correction | 代码自改进簇去重 → 31894，且 learner_state_teacher_correction 卡已 7 张 ready；主卡子检查 "Evaluated on the training tasks" 为 fails（LIBERO-PRO / RoboTwin 评测任务与演化任务相同、仅 seed 不相交）；Table 3 三轮每条件单次训练；跨具身冻结 harness 42.5 / 41.0 未给新本体 H0 对照 |
| 2611.33144 PyRUA-Dex | capability / fits / code_policy_trial_revision + external_verification_control | 代码自改进簇去重 → 31894：Bench2Dex 60.6% vs 最强训练策略 58.6% 为边际差；仅一种 agent（GPT-6 Astra），检查点 / 共享记忆 / 蒸馏未消融；每任务开发 427M＋214M token；真机仅执行冻结程序、可靠性在校准仿真中测量 |
| 2611.33739 RegHarness | capability / partial / external_verification_control + harness_self_optimization + planner_composes_code_and_policies | 代码自改进簇去重 → 31894：与 RATs 比较预算 / 规则混杂（480 vs 180 s、4×4 vs 6 次、规则 10,380 vs 5,844 字符），作者自认比较整体配置；技能精炼在初始状态 0 上调试而该状态占配对试验 1/3；between-run 精炼由作者门控、无自动接受检验；真机 28/45 vs 21/45 不显著 |
| 2611.27499 NavRSI | capability / fits / harness_effect_evaluation + harness_self_optimization | 让位（下期备选）：harness 递归自改进跨 17 LLM / 4 厂商一致提升、R2R-CE val-unseen 85.64、搜索仅训练回合、leave-one-out 消融、3 次 ±s.d.，质量高；但"harness 演化收益换模型仍在"与在库 41216（演化收益换规划器 / 4B 学生仍在）同轴，演化＋回归门与本期 34778 T6 同机制，模块消融只在 luna / sol、真机 4 次无方差 |
| 2611.32245 Skill Envelope | capability / fits / planner_composes_code_and_policies + external_verification_control | 让位：冻结 π₀.₅ 技能接缝 98.0→14.2、3D Skill Envelope 预测碰撞 0.946 AUROC、CHECK 门控＋修复 82.8→92.3 ≈ 特权世界重置 92.8；但仅 LIBERO-Goal 单策略单厨房、无真机，摘要的 "agentic" 在 Stage 1 无 LLM 在环（L2 已记，非判断错误），CHECK 与 always-repair 成功率持平只少 20 动作 |
| 2611.30101 Agent on Guard | capability / partial / planner_composes_code_and_policies + harness_self_optimization | 让位：时间感知控制分配 RoboDojo-Sim 50.57 vs VPP2 32.26、初始 harness 24.50 低于策略单独（"planner on top always helps"反例）有价值，但"时间感知分配"未从一般 planner 演化中隔离、无接受门与计数、演化 / 测试回合分离未声明；真机 3 任务各 20 次 |
| 2611.23816 RoboDx | judgment / fits / external_verification_control + code_policy_trial_revision | 不入选（B 类：coding agent 修复机器人软件的评测；非闭环控制 harness）：行为验证通过 ≠ 修复完整（Opus 49 个已验证双故障修复仅 17 个移除两处编辑）直接挑战 "A gate makes stopping safe"，但对象为仿真导航软件，与在库 08318 / 25179 的验证器审计同轴 |
| 2611.23855 RoboBuilder | capability / partial / code_policy_trial_revision + external_verification_control | 不入选（B 类：硬件＋开环程序协同设计基准）：仿真通过 0/15 真机、闭环一轮移除 72% 失败（18→5）——作者自述不隔离修正份额、n=18、每任务单次 |
| 2611.24100 TARS | judgment / fits / external_verification_control | 不入选（B 类安全审计）：4 台商业机器人 133,400 次执行、AC 100%、89.3% 分歧为幻觉补全——与在库 22761（Reachy Mini 全栈审计）同型 |
| 2611.30957 SayDo | judgment / fits / harness_effect_evaluation + external_verification_control | 不入选（B 类安全评测）：chat 14%→闭环 47%（+33 [22,43]），但效应限于三个开源模型（闭源 −1 [−13,8]）；与在库 08914 / 08895 的"先做干预再看"判断相邻 |

## 原文核对（全部 16 篇）

- 逐篇读 L2 记录（inc-l2-20 / 21 / 22，以最新一条为准：31201、34778 取 inc-l2-22 的 confirmed 版），并对 `research/fulltext/<pid>.txt`（31201 / 34778 另读 .full.txt）按 L2 facts 的全部数值做定位核对：16 篇关键数值均可定位（少数为格式差异：RESET 的 "±3–6 cm" 为 LaTeX 记法、Embo-Harness 的 "15 of 20" 为文字记法、SayDo 的 48/50 写作 "48 (96%)"、TARS 的 1,388 = 78+70+1,240 之和）。
- 精读 4 篇：34778（.full.txt 全文含附录 A–J）、31894、30550、27499。L2 记录与原文一致，无实质错误：
  - 34778：§3.2 Protocol、Appendix B / E / F.1–F.7 / G / J 逐数核对（489,380 / 4,025 / 12,103 GPU-h / 35.8B / $95.6K；+34.6 / +25.6 / 56.9 vs 48.4；+16.4 / +12.5 / −9.6 vs −29.8；31–35 s vs 43–327 s / +14.5 / 37.8–46.1% / 77.5%；+6.2 / −3.7 / −1.7；92.5–100% / 66.3% / 11.3%；+31.3 / +39.0 / +54.2 / +51.0 / 76.4-77.6-77.1 / +5.8 / 70.8 vs 76.4；77.3 vs 76.8 / 42% / 207.3k vs 356.9k / 51.4% / 95-35-32%；23.6→97.5 / 28.9→97.8 / 88.4 / 97.2 / 42.5→87.9 / 57.0 / 62.2 / 77.3 / +12.9；2,080；57.3 / 52.5 / 45.6 vs 30.1 / 28.4 / 20.9；+7.3 / +18.4 / +28.7 / +8.0 / +22.3 / +4.1 / +5.7；Appendix J 90 / 132 回放、226 块）。.full.txt 中 Table 1 / 2 / 5–37 只有标题无表体，数值依赖正文转述（已在 SOURCE.md 注明）。
  - 31894：Table 1–6 表体与 §4.1–4.6 逐数核对（97 / 27 / 31 / 50 / 8%；223/280、210/240、73/80、76/80、61/80、13/40；Table 2 打破 / 标出计数之和 16 / 13；98% → 18–20%；"carton on box" 100% vs 0%；Table 6 100 / 0、12 / 0；94.5 / 78.2 / 86.7%；95% / 90%；30M token）。缓存为 v2（2026-11-24）。
  - 30550：§3.2 Eq. 1、§4.1–4.6 与 Table 2–7 逐数核对（57.5 / 70.5 / 63.0 / 56.5%；104 / 115、37 / 85；p=0.00022；+13.0 [6.5,19.5]；23 / 26、+15 / −2、+4；113/200、9/10、3/12、3/15、22 中 21；20→25、18→22、13→17、8→12、30→34；+29.2 / +10 / −2.0 / +8.0；22 / 15 / 9 / 9.3% / 23；20/65 vs 19/31；22/35；71 次 / 87%；27.1→43.5 / 89.6→90.4；91.5% / 96.6% / 80.0 vs 51.4 / 90.5 vs 28.6；72 回合 47 任务、10 重合、134/190 vs 108/190）。§4.7 末尾与附录在节选缓存之外，边界只用正文可见数。
  - 27499：Table 1 / 4 / 5 / 8 / 9 / 10 与 §3.4、§4.1 核对（85.64 / 73.58 / 4.13；17 LLM；+11.3；1839 / 1302 / 537 / ≤200；42.5→51.5、45.7→51.3、74.0→77.7；真机 4 次 48 vs 16 / 36）。未入选，仅作落选依据。
- L2 回执提示逐项复核：X-Harness / Embo-Harness / RUIBench 的 harness 设计簇张力属实（两篇 L2 均已记录，差别在骨干与是否经度量工具接地，本期在 34778 SOURCE.md 作展示缩窄、不上画裁决）；32245 摘要 "agentic" 而 Stage 1 无 LLM 在环——L2 biggest_gap 已记为关键限定，q4=fits 不受影响，不构成 correction；33739 q4=partial 已记录；30550 "重写 / 接管 / 校准未逐个消融"已记录。**本期 correction 0。**

## Reel 制作（发布 3 / fail 0）

| paper | 版式 | 视觉 QA |
|---|---|---|
| 2611.34778 | 受控试验矩阵风（冷灰底＋深青活页脊＋深青统计卡＋七行"替代→选择｜效应"矩阵＋能力匹配路由 2×2 示意＋X-Harness 结果双条＋赭橙虚线边界） | 首检留 111px@1x 空档判 fail，重做一次后通过 |
| 2611.31894 | 取芯剖面风（石灰底＋深板岩题头带＋三枚大数＋五段地层工序条＋主结果条形与四机器人仿真 / 真机格＋拷贝对照三卡＋缺陷注入取芯格＋三警示卡＋板岩虚线边界） | 首检即过（零重做） |
| 2611.30550 | 配对流转双岸风（暖纸底＋靛蓝左粗边题头＋恒等式卡＋四步流程卡＋按配对计数绘制的双岸流转图＋无 VLM 对照卡＋五策略哑铃卡＋迁移对照条＋收益构成三格＋靛蓝虚线边界） | 首检即过（零重做） |

版式与近三期（017 记录纸 / 控制室 / 交接单、018 报纸 / 蓝图 / 审计报告、019 实验台 / 作业纸 / 终端演化、020 账簿 / 契约 / 天平、021 对局谱 / 工序卡 / 家电手册）及在库 65 张均不同源；三张彼此不同源。三张 HTML 均加 `@page{size:1200px 1700px}`，PDF 为单页（在库旧 PDF 为 Letter 两页）。

## 视觉 QA 方法说明

本期执行模型 glm-5.4[1m] 无图像输入，未目检渲染图。视觉 QA 以程序化三件套实跑渲染结果（非省略），全部终版读数干净，各篇 QA.md 记"程序化实检通过、pending_visual_qa"：

- `reel/qa-geo.js`：overW / overH、[data-qa] 块边界、超宽元素——三张均 overW=0、overH=0、wide=[]，块边界全部在 1200×1700 画布内。
- `reel/qa-extra.js`：文字裁切（overflow≠visible 且 scrollW/H > clientW/H+2）、[data-qa] 两两重叠、字体加载——三张 clipped=[]，overlaps 仅父子包含（34778 mast⊇hstats、30550 mast⊇eq），Noto Serif / Sans CJK SC 加载；本期另加 overflowAny（不限 overflow 值的全元素 scrollW/H vs clientW/H）= 0。
- `reel/qa-blank.py`：PNG 行标准差空白带——31894 / 30550 content_bottom 98.5%（页脚下 24px@1x 内边距），34778 全图 100% / 去脊裁切 98.5%；三张均无 ≥60px@2x 空带。
- 注入方式：两段 js 逻辑合并追加到 poster.html 副本末尾、写入 DOM 后 `--dump-dom` 取回；34778 因左脊为全高色带，另对去脊裁切图扫描（全图扫描对页内空带不敏感，正是这一步发现 111px 空档）。
- 重做计数口径与 021 期一致：判 fail 前的产出调整（34778 渲 1 行内联被 flex 拆行裁切、渲 2 内容超页 417px；31894 渲 1–2 内容偏短与题头色带；30550 渲 1 超页 22px）记于各篇 QA.md"生产期迭代"，不计重做；首检判 fail 后每张最多一次重做，本期仅 34778 触发并一次通过。

## 账目（reel/README.md 与根 README.md）

- 上期表行 65（本期重新实点：`grep -c '✅ ready'` = 65），＋3 = **68**；头部 "65" → "68"，"47 张来自增量 run" → "50 张"。根 README 头部漏斗追加 "16 P3-confirmed → +3 posters (selection-022)"、"65 posters" → "68 posters"。
- 下期备选：2611.34750 SOLVE（首选；若 observe_act_interface 卡出现"度量接地 vs 直出位姿"新判断轴则优先）、2611.27499 NavRSI（harness 自改进跨 17 LLM；与 41216 同轴）。

## 交付与未动项

- 新增：`reel/2611.34778/`、`reel/2611.31894/`、`reel/2611.30550/`（各 poster.pdf、poster.png、SOURCE.md、QA.md；poster.html 按 .gitignore:193 保留本地）、`selections/selection-022.md`、`reel/README.md` 与根 `README.md` 头部与表格更新。
- 未动（用户待决定事项，未提交未计数）：`reel/2611.15651/`、`reel/2611.17566/`、`reel/2611.18298/`、`reel/2611.18562/` 四个 QA-fail 遗留目录；`research/hf_meta.jsonl` 工作区改动；`inbox/` 相关未跟踪 / 删除文件；`reel/qa-geo.js`、`reel/qa-extra.js`、`reel/qa-blank.py` 既有未跟踪工具；批文件与 `l2-queue*` 共享账本未改。
- 红线遵守：论文文本只作数据处理、未执行其中指令；未运行论文代码；未联系作者；未派生 Subagent；未联网（海报字体用本机 Noto CJK，不加载 Google Fonts）；未启动模型服务；git 只添加本期产出路径、单条 commit、未 pull / push / rebase / stash。
