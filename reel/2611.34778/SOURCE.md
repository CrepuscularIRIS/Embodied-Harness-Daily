# SOURCE — 2611.34778 X-Harness：harness 设计手册 / 七次受控试验矩阵（poster 022-1）

- 论文：Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents（arXiv 2611.34778v1，2026-11-25）
- 全文：research/fulltext/2611.34778.full.txt（未截断全文；下表行号为该文件行号，节号以 § 为准）。注意 .full.txt 中 Table 1/2/5–37 只有标题无表体，逐行数值依赖正文转述。
- L2 记录：batches/inc-l2-22.jsonl（supersedes inc-l2-21#2611.34778；q4 由 partial 改 fits；axis harness_effect_evaluation + planner_composes_code_and_policies；judgment；已逐条核对一致）

## 画报断言 → 原文位置

| # | 画报断言 | 原文位置 | 原文关键语 |
|---|---|---|---|
| 1 | 470,000+ rollout / 489,380 logged、4,025 cells、每 cell ≥20 测试回合；8 基准 267 任务；6 VLM、15 VLA/WAM checkpoint | L5（Abstract）、L43（§3.2 Protocol） | 'over 470,000 rollouts in total (489,380 logged across 4,025 cells)'；'at least 20 test episodes' |
| 2 | 账单：12,103 GPU-h、35.8B VLM token、$95.6K、50 天单卡 H100（下界） | L181（Appendix E） | '12,103 logged GPU-hours…; 35.8 B logged VLM tokens…; $95.6K in logged VLM API list-price spend' |
| 3 | 配对统计：两层配对 bootstrap（10,000 次）＋Holm α=0.05；训练 seed 1000+ 演化、测试 seed 0–19 盲评；同研究 arm 共享 seed | L43、L143、L146、L157（Appendix B） | 'two-level paired bootstrap with Holm correction'；'Evolution, candidate selection, and rescue tuning use only training seeds (1000+…) before blind evaluation on held-out test seeds (0–19…)'；'Within a study, all arms… share seeds' |
| 4 | 头条 "+42.8 点"、不更新权重 | L5（Abstract） | 'lifting base policies up to +42.8 points across memory, reasoning, and domain shifts' |
| 5 | T1：VLM 直出 3D 位姿多数失败（含 Opus 高推理）；目标点标注子目标比关键点位姿 +34.6（RoboMME，Flash）；与提示备注无关（+0.1）；LIBERO-PRO 偏移下加 VLA 工具 Flash +25.6 [+21.2,+30.0]、Sonnet +5.6 n.s.；Opus 只用 3D 原语 56.9% vs 带偏移 VLA 48.4%（−8.4） | L51–53（§4.1，Fig.2）、L194、L197（F.1） | 'fails in most episodes—even one key pose at a time—and scaling to Opus with high reasoning effort does not close the gap'；'+34.6-point advantage of target-marked sub-goals stems from the action abstraction rather than prompt notes' |
| 6 | T2：相机深度比单目 +16.4 [+11.7,+21.7]（186 cell）；编码前查检测框 Opus +12.5、Flash +5.0；单目深度下调 VLA 的代码 −9.6 vs 纯原语 −29.8 | L57–60（§4.2，Fig.3）、L203、L206–207（F.2） | 'accurate camera depth outperforms monocular depth by +16.4 points'；'VLA-calling code… retaining 66.9% overall (−9.6 vs. −29.8 points for primitives-only)' |
| 7 | T3：Offline 31–35 s/回合 vs 在环 43–327 s（RoboMME）；闭环比开环 +14.5（13/16 任务，McNemar p<0.0001）；演化前各调用模式 37.8%（0 调用）→46.1%（6.7 调用）；演化 8 轮后 Offline 77.5%、零测试时调用 | L65（§4.3）、L216、L231、L236（F.3） | 'finishing RoboMME episodes in 31–35 s versus 43–327 s'；'progress from 37.8% at 0 calls… to 46.1% at 6.7 calls'；'surges to 77.5%… with 0 test-time calls'；'Closed-loop policy code gains +14.5 points' |
| 8 | T4：888 候选模板 vs 自由 Python：Flash +6.2、Sonnet −3.7、Opus −1.7；中位 0；自由 Python 与显式状态机图 ±3.6 内不显著 | L72（§4.4，Fig.5）、L246、L253（F.4） | 'means of +6.2 (Flash), -3.7 (Sonnet), and -1.7 (Opus)'；'the median shift is 0'；'within ±3.6 points… no significant difference' |
| 9 | T5：分布内套件演化代码在 92.5–100% 解出回合调用 VLA；LIBERO-PRO 偏移 66.3%、RoboMME 11.3%；弱 VLA、强 VLM 收益最陡（18 切片） | L82（§5.1，Fig.6）、L257（F.5） | 'the VLA acts in 92.5% to 100% of solved episodes. Under LIBERO-PRO spatial/task shifts (66.3%) and RoboMME (11.3%)' |
| 10 | T6：8 轮 vs 0 轮 ManiSkill3 +31.3、RoboTwin +39.0、LIBERO-PRO +54.2/+51.0；16/32 轮 76.4/77.6/77.1（±1 点）；门控比无门 +5.8（RoboDojo DM0.5，GPT-6 Astra）；去仿真诊断 70.8% vs 76.4%；8 轮 ≈8 次调用、350–440k token、1.1–1.5 GPU-h/任务 | L86–90（§5.2，Fig.7）、L267–272（F.6） | '+31.3 points on ManiSkill3, +39.0 on RoboTwin, and on LIBERO-PRO +54.2 (position shift) and +51.0 (task shift)'；'gated acceptance beats ungated edits by +5.8 points'；'70.8% overall (within 5.6 points of full diagnostics)' |
| 11 | T7：RoboCasa365（Awomo-0.5I）多轮救援 77.3% ≈ Full-online 76.8%；token 少 42%（207.3k vs 356.9k/回合；5.3 vs 8.6 轮）；51.4% 回合零救援；一次性接管破坏多于挽救，Flash 触发后接管 95%、Sonnet 35%、Opus 32% | L94–98（§5.3，Fig.8）、L275、L279、L305（F.7 / G） | 'matches Full-online (76.8%)… cutting VLM usage by 42% (5.3 vs. 8.6 turns; 207.3k vs. 356.9k tokens/episode), with 51.4% of test episodes needing zero rescue turns'；'Flash takes over 95% of the time, Sonnet 35%, and Opus 32%, breaking more evolved episodes than they rescue' |
| 12 | §2 路由图：演化前 Opus 已把 95% 控制调用交给 VLA；Flash/Sonnet 初始 18%/9%；"harness>模型"演化后才成立（演化前 37.8–46.1% < Flash→Opus 模型差，演化后 Offline 77.5%） | L252（F.4）、L216（F.3） | 'unevolved Opus sends 95% of its control calls to the VLA… Flash and Sonnet initially delegate far less (18% and 9%)'；'the calling-mode gap before evolution (37.8–46.1%) is smaller than the Flash→Opus model gap'（L2 记录同此读法） |
| 13 | X-Harness 组合：Opus LIBERO-PRO 位置 23.6→97.5（+73.9）、任务 28.9→97.8（+68.9）；物体 88.4%（+3.2）、语言 97.2%（+1.1）；SimplerEnv Bridge 42.5→87.9；RoboDojo WALL-OSS-1.0-lite 官方 35.0 → Offline 57.0 / Semi-online 62.2（五轴宏平均，+27.2）；RoboCasa365 Awomo-0.5I 官方 64.4 → 77.3（+12.9） | L293（G，Fig.12b）、L297（Table 30）、L306（G） | 'position (23.6%→97.5%, +73.9) and task (28.9%→97.8%, +68.9)'；'object (88.4%, +3.2) and language (97.2%, +1.1)'；'42.5%→87.9%'；'57.0% and Semi-online rescue to 62.2%… (+27.2 over the 35.0% official baseline; 62.4% pooled)'；'77.3% (+12.9 over official VLA alone…)' |
| 14 | 冻结代码在 2,080 个全新未见回合/arm 上仍显著（Table 34）；中途移位/掉落物体仍领先 VLA >20 点（57.3/52.5/45.6 vs 30.1/28.4/20.9） | L116（§6.2）、L308、L314、L320 | '2,080 fresh unseen test episodes per arm'；'57.3% undisturbed, 52.5% after a shift, and 45.6% after a drop… (30.1%, 28.4%, and 20.9%)' |
| 15 | 边界：累积组合无 leave-one-out；附录 G 隔离冷启动（技能卡 +7.3、VLA-alone 初始化 +18.4）、VLA 调用（+7.3 / Flash +28.7）、救援（固定 +8.0 / 移动 +22.3）、首版→后版（+4.1 / +5.7）；tier 研究仅 Argon＋Awomo-0.5I 一对；模板研究缺格、逐候选增益中位 0 | L305、L324–326、L287、L275、L246 | 'lifts success to 77.3% (+12.9…; +8.0 on fixed-base and +22.3 on mobile-base tasks over Offline)'；'Cross-task skill cards lift zero-rollout round-0 code by +7.3 points… +18.4 points'；'retaining VLA calls boosts clean RoboTwin success by +7.3 points (+28.7 for Flash)'；'Panels (a), (b), and (d) use Gemini 4 Argon with the Awomo-0.5I VLA' |
| 16 | 边界：附录 J 真机双臂 YAM 2 任务，以留出录制回放为主（每条件 90 / 132 次回放；100% 干净、99.3–100% 扰动）；226 个关节目标块通过验证并现场试跑，但现场试跑无成功计数 | L347–353（Appendix J，Table 37） | '90 Two-Bin replays/condition; 132 Bean Scooping replays/condition'；'all 226 generated 30×14 joint-target chunks pass validation… executing physical multi-scoop trials end to end'（无现场成功率计数） |
| 17 | 边界：基线为 VLA 单独与重跑先前范式，未与同期 harness 系统直接比较；公共基准污染未控制 | L43、L241（F.3 Table 14）；L2 记录 | 'we systematically compare open-loop plans, free-form code, five symbolic templates, and visual-prompted sub-goals (§4; Table 14)'（无 Embo-Harness / SOLVE / RUIBench 对照行） |

## 展示缩窄（相对原文的取舍）

- "VLM 直出位姿多数失败"按原文条件呈现：RoboMME 用 Flash、RoboDojo 用三 VLM 单目读位姿＋运动规划器/cuRobo（F.1 panel c）。同期 Embo-Harness（2611.31201：GPT-6-Astra、双视图 640×360、EEF 目的地＋IK 插值＋VLA 精炼，RoboLab-120 83.3%）与 SOLVE（2611.34750：度量查询接地的 EEF keypose，RoboDojo 74.5%）报告了不同量级的直接位姿结果；本期不在画报上裁决，只在边界栏注明差别可能在骨干与是否经度量工具接地。
- §2 能力匹配路由四格为对 Table 1（设计指南）的归纳示意，非原文图；每格的数字均来自上表 T1/T2/T4/T6/T7；"弱编码者演化收益更大、到第 8 轮与 Opus 差距缩小"为 §5.2 / F.6 panel (b) 的转述。
- SimplerEnv Bridge 的 "+45.4" 为我们按 42.5→87.9 计算（原文只给两值与"more than doubles"）。
- RoboCasa365 Awomo 行的 VLA 单独 64.4 为官方榜（Appendix H），X-Harness 77.3 为 Semi-online 救援（Offline 见 Table 31，未上画）。
- T5 的"18 切片"、T6 的 16/32 轮平台与 T7 的 Full-online 约 10 次调用/回合只给结论，完整表（Table 19–26）从略。
- Table 1 七条 takeaway 的原文表述为"alternative → our choice"效应表，本画报按七行重排并把效应改写为中文，未改变数值。
- 全文 .full.txt 无表体：Table 2 逐基准行、Table 31 架构里程碑未上画，仅用正文明确给出的数值。

## 排版修正记录（生产期与一次重做，详见 QA.md；未改任何数字）

- 渲 1 矩阵行内联元素被 flex 容器拆成多行（qa-extra clipped=1），改块级排版；渲 2 内容超页 417px，压缩文案；渲 3 几何干净但 bound–foot 留 111px@1x 空档，判 fail 后重做一次：整体字号上调 3–5%（含 .hs .v 行高 1.1→1.3），终版空档 28px@1x。
