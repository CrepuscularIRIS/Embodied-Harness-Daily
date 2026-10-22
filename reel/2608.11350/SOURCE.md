# SOURCE · 2608.11350

- 原文：Self-Evolving Embodied Agents via Skill-Harness Evolution（SHAPER），arXiv **2608.11350v2**（2026-08-11），https://arxiv.org/abs/2608.11350
- 阅读材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2608.11350.txt`（html-full，正文 §1–5 + Appendix A.1–A.4；私有缓存，不提交）。附录 Figure A1–A13 的工件正文在缓存中不可见，只用到其图注。
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl`（paper_id=2608.11350，batch b048，screen_score 88.75，G4/M4/X4/E3，supported_in_material / online）；入选：`reel/selection-opus.md` C7
- 核对：`reel/2608.11350/verify.md`（pass）
- 图形：同心环、条形图、表格均为本刊据原文文字/表格自绘（HTML/SVG），非原论文插图；未运行论文代码。生成脚本只做弧线几何计算，内容与数字均已写入 `poster.html`。

## 数字与断言 → 原文定位

| 画报位置 | 数字/断言 | 原文 |
|---|---|---|
| 标题/副标题 | 冻结规划器与执行器，演化文本技能 + 上下文构造代码 | Abstract；§1；§3.1 式(1) |
| ① 问题 | 无权重/示范/奖励、无可编程机器人 API、固定动作接口下的免训练适配 | Abstract；§1 第 2–3 段 |
| ③ 外环 · 规划器 | Qwen3.6-27B，θ 冻结；评测时所有变体同一规划器 | §3.1 式(1)；§4.1 Models |
| ③ 外环 · 执行器 | VLABench 官方 π0（OpenPI）/ ESI 固定动作 API；φ 冻结；动作接口与输出解析器固定 | §3.1；§4.1 |
| ③ 外环 · 优化器 | 同一冻结权重、单独提示词充当优化器 | §1；§3.3 式(4) |
| ③ 内环 · s | 规划器提示词中的过程指导：场景检查、分解、子目标、恢复、终止 | §3.1 |
| ③ 内环 · h | Python `build_context`，选择并格式化轨迹历史 | §3.1；Appendix A |
| ③ 核心 | 只优化 c=(s,h)；输出验证最高的 c* | §3.1 式(2)；§3.3 末段 |
| ③ 读箭头 | 规划器读 s 与 h(τ<t)；h 读历史（观测、命令、执行结果、报错） | §3.1 式(1)；§3.2 元数据 |
| ③ 写① / 写② | 先演化 s（h=种子），再演化 h（s=选中技能）；顺序固定 | §3.3 式(5)；§4.1；Appendix A.3.1 |
| ③ 沙箱 | 必须定义上下文函数，禁 import、文件读写、动态执行，超时拒绝 | §3.3 |
| ③ 反馈回路 | 回合级判官 (o_t,y_t,a_t,o_{t+1}) → 回合摘要 → 文本梯度 Γ → 优化器 | §3.2 式(3) |
| ③ 回路说明 | 固定验证集打分，beam top-K；宽 3、分支 2、4 轮，minibatch 4 | §3.3 式(6)；§4.1 Optimization protocol |
| 左上卡 | VLABench 800 留出：Seed 28.25 → SHAPER 34.50；仅技能 33.50；仅 harness 30.50 | Table 2；§4.2 |
| 右上卡 | ESI 231 题 micro 32.5 → 41.1 → 49.8；macro 31.2 → 38.6 → 42.9；GPT-5 PS 40.3 全集、非配对 | Table 3；§4.3 |
| 左下卡 | Specular Reflection 20→60（n=20）；Spatial Relations 37.3→54.9（n=51）；Enumerative 33.3→27.8（n=18）；Action Sequencing 40→20（n=5） | Table 3；§4.3 Category-level |
| 左下卡 单例 | 旧 h 只留最近 5 帧 RGB，30 步（右 15/左 12/前 3）答 not sure；新 h 保留第 1 步反射帧，答 middle | §4.3 Figure 4 及正文 |
| 右下卡 | $2.25 / $2.83 API 等价；Qwen3.6-27B 列表价 CNY 3/18 每百万 token，7.2 汇率；含 rollout/判官/摘要/优化，不含评测与仿真/GPU | §4.4；Appendix A.4 |
| 右下卡 | 15 训练 + 24 验证 episode / 10 + 10 题，与评测集不重叠 | §4.1 |
| ④ 条形图 | 10 行 Overall：23.25 / 24.00 / 21.38 / 22.00 / 24.38 / 23.50 / 28.25 / 33.50 / 30.50 / 34.50 | Table 2 |
| ④ split 表 | Direct VLA、Seed、Skill、Harness、SHAPER 的 C1–C4 | Table 2 |
| ④ split 说明 | C1 同域、C2 新目标类别、C3 新任务形式、C4 两者皆新；作者自定义，各 5 类×40=200 集 | Table 1；§4.1 |
| ④ 不可加和 | 技能之上 +1.00（+0.5/+2.5/0.0/+1.0）；harness-only C3 46 vs 50；作者称完整配置非独立效应 | §4.2 Artifact ablations |
| ④ 条件 | ≤10 规划轮、≤400 环境步；SFT 用同 15 条训练集 | §4.1 |
| ④ 另 | C3：Seed 40.0 < Direct VLA 45.0 | Table 2（本刊读表） |
| ⑤ 限制 1 | 单次演化、无重复/方差；作者称 descriptive | §4.2–4.3 用语；材料中无重复运行（本刊核对） |
| ⑤ 限制 2 | TTS 采样数未报告；SFT 调执行器、无规划器 | §4.1 Compared methods（本刊核对） |
| ⑤ 限制 3 | 两基准各自演化；ESI 无 harness-only；跨本体与真机留作未来工作 | §4.1；Table 3；§5 |

## 本刊阅读判断（非作者主张）
- "技能之上的 +1.0 点无法与噪声区分""10.5 点差混入有无规划器""SHAPER 另用 24 条验证 rollout"——来自 Sol caveat 与本次核对，作者未如此表述。
