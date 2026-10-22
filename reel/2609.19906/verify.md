# 2609.19906 核对记录（Opus 5.5 核对席）

- 论文：Learning and Transferring Closed-Loop Robot Software，arXiv 2609.19906v1（2026-09-17）
- 材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2609.19906.txt`（FULLTEXT: html-full，24 行/33 KB，摘要、§I–VI、Tables I–III 全文通读；无 `_pdf.txt`；图 1–3 仅有图注、无图像）
- Sol 记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl`，paper_id=2609.19906，batch b024，screen_score 88.75，claim_type=system_method，claim_support=supported_in_material，evidence_level=online
- 核对日期：2026-10-22；未运行论文代码

## 结论：核对通过（pass），展示时需缩窄措辞

Sol 记录的问题、动作、数字、caveat 均与材料一致。论文核心区分（源任务性能 ≠ 对新任务的参考价值）有一组可检验的同条件对照支撑：Initial4 与 Best4 指向**同四个源任务的同一份档案的两个阶段**，目标侧示范、观测、模型、用例、会话上限、改进规则共享，三次独立运行。但该证据只在“条件平均”层面成立：没有逐份参考的归因，特化解释未经检验（作者自述）。

## 逐项核对

| 项目 | 材料实际内容 | 定位 |
|---|---|---|
| 问题 | 源任务上优化后的整份闭环实现（观测处理+状态管理+条件分支）是否也更适合作为新任务的参考；担心优化加入的分支过度特化 | Abstract、§I、§II-B |
| 实际改动 | 编码代理（gpt-6-astra，high）从 10 条示范生成代码→用 Train 轨迹/结果/错误迭代改写至第 5 代→按 Validation 成功率选出→存入档案（代码+资产，不含源日志）；新任务只读档案、不指定源-目标配对、不自动复制 | §III-B/C、式(2)(3)、§IV-A |
| 源侧结果 | 四源任务同 30 个 Test：首个可执行代码 28.3%（34/120）→ 迭代 64.2%（77/120）；四任务均提升（10→17、1→21、8→23、15→16 /30） | Table I A 栏、§IV-B |
| 源侧基线 | 同代理在线控制 51.7%（平均 52.6 次模型调用/回合）；BC-Transformer-10 9.2%；公开多任务模型 GR00T N1.5 62.5%、π0.5 58.3%、π0 37.5%、DP 20.0%（作者标为输入/训练条件不同的参考比较） | Table I、§IV-B |
| 迁移对照 | 9 目标（Near 4/Intermediate 2/Far 3）× 3 次独立运行 × 10 Test：无参考 45.2±10.3%（122/270）、Initial4 41.5±10.5%（112/270）、Best4 57.0±7.8%（154/270）；三列计数已逐格相加核验 | Table III、§IV-D |
| 关键区分证据 | Best4>Initial4 在三次运行的九任务均值上都成立，平均 +15.6pp；逐任务三运行均值 6 胜 1 平（OpenCabinet）2 负（TurnOffMicrowave 23→18/30、CoffeeSetupMug 3→0/30）；Initial4 不优于无参考 | Table III、§IV-D |
| 目标侧条件 | 5 条共享示范、5 次 Train 回放、改进 1 轮（代码报错时修复重跑再多 1 轮）、无目标 Validation 选择、冻结后 10 个共享 Test；每会话 30 分钟/80 次 API；Full 观测 | §IV-D |
| 观测消融 | Full 65.0% → RGB only 22.5%；去 GT-Geom 35.0%（−30pp）；去 3D 67.5%、去接触 70.0%（单次运行，作者说明不说明“去信息有益”）；预算与 Table I 不同 | Table II、§IV-C |
| 分支计数 | 参考实现 if/elif 总数 622→741（+19.1%），TurnOnMicrowave 138→225；作者明确说不能单凭此证明特化 | §IV-D |
| 局限（作者自述） | 仅仿真；源档案在三次运行中固定，源侧获取方差未评估；部分任务运行间方差大；目标改进轮数单一 | §V |

## 与 Sol 记录的差异

无需退回的错误。补充边界（不改分，用于缩窄画报措辞）：
1. 15.6pp 为三次运行差值的均值；由表中均值直接相减为 15.5pp，属四舍五入差，画报按原文 15.6 引用并注明来源。
2. 参考价值只能在“条件平均”层面读出：代理自由选择参考哪份实现，论文未报告每个目标实际用了哪份代码，因此不能把某个源实现单独定位为“高源分低参考价值”。画报矩阵的点是“目标任务 × 参考条件”，不是单个技能。
3. Best4 并非逐任务都优于无参考：PickPlaceCounterToCabinet 17<19/30，水龙头与咖啡杯持平；逐任务 3 次运行标准差最高达 52pp（每运行仅 10 个 Test），逐任务差异不宜强断言。
4. 计算量不等（报错触发的修复与重跑）、Table I 中 Full 观测含仿真真值几何分割（GT-Geom），这两点 Sol 已在 E 理由与 caveat 写明。
5. evidence_level=online 判定合理：同本体、同模拟器、同厨房操作任务族，目标任务仍用自身示范与 Train 反馈改进，不满足 docs/EVIDENCE.md 的 transfer 条件；画报中“迁移”一词仅指论文的跨任务参考，不作 transfer 等级主张。

## 关键证据定位

- 方法与数据隔离：§III-A/B/C，式(1)–(3)
- 源侧优化：Table I、§IV-B、Fig. 2 图注
- 观测消融：Table II、§IV-C
- 源性能 vs 参考价值：Table III、§IV-D（逐任务胜负、分支计数）
- 限制：§V；结论措辞“The advantage is not uniform”：§VI
