# Embodied-Harness-Daily（原 EH Radar — Embodied Harness）

`domain: embodied agent harness` · `scoring: sol-batch-v3` · `reel: 2026-10-22 第 1 期` · `license: MIT`

追踪前沿 LLM/VLM 或 coding agent 如何借助 harness 控制具身系统，覆盖机械臂、移动操作、导航、无人机和人形机器人。harness 由工具、冻结 VLA/技能、感知原语、记忆、验证和执行控制组成。本项目也收录 harness 教师轨迹蒸馏、on-policy 纠正、harness 内 RL、自我优化及其评测。无 harness/教师闭环的纯 VLA、GUI agent 和非具身 RSI 不在范围内，详见 [收录范围与证据等级](docs/EVIDENCE.md)。

核心问题：**模型通过哪一层 harness 控制什么本体？闭环成败如何判定？改进来自 harness、策略，还是额外预算/特权信息？**

## 流程

```
Grok Bots 定时收集 ──► 领域 card pattern 提取 ──► 四轴打分 ──► 高质量挑选＋原文核对 ──► Reel 中文海报
   inbox/               原15+31 ＋ embodied 领域卡    G/M/X/E 满分100   Opus 5.5                reel/<paper_id>/
```

| 步骤 | 做什么 | 产物 |
|---|---|---|
| 1 收集 | 追溯一手来源，收录机制/实验明确的候选，记录检索覆盖与排除理由，不打分 | `inbox/*.jsonl`、`inbox/*-run.md` |
| 2 模式提取 | 按 ResearchStudio Idea 的 card pattern 识别：原 15 主卡＋31 子卡简明索引，再映射 embodied 领域卡；无匹配记 `outside_taxonomy` | 每篇的 `patterns` 字段 |
| 3 四轴打分 | 每轴 0–4 档或 null，`screen_score = (15G+20M+20X+45E)/4` | `final/index.jsonl` |
| 4 挑选与核对 | 高分组内做编辑挑选，读该版本完整原文，逐个数字核对 | `final/selection.md`、`reel/*/verify.md` |
| 5 Reel | 核对通过后做中文海报，经视觉 QA 后才算 ready | `reel/<id>/poster.png`、`poster.pdf` |

### 四轴评分（profile `embodied-v3`）

| 轴 | 问题 | 权重 |
|---|---|---:|
| G：问题与 gap | 瓶颈是什么，与最近邻相比还剩下什么 | 15 |
| M：方法与 problem-fit | 实际改变了什么操作，为什么能对准该瓶颈 | 20 |
| X：机制与条件 | 所需信息、接口和执行条件能否重建 | 20 |
| E：证据支撑 | 已见结果与对照能在多大程度上支持核心主张 | 45 |

总分与 `claim_support`、`evidence_level` 分开记录。匹配到某个模式不加分。所有分数都是初筛分，不是权威审稿分。

## 模型分工

| 环节 | 模型 | 说明 |
|---|---|---|
| 候选收集 | **Grok Bots** | 定时更新，写入 `inbox/`，不打分、不做海报 |
| 全量打分 | **6.1 Sol** | 单模型批量简评，规则 `sol-batch-v3`；无第二初评席、无全量聚合 |
| 高质量挑选＋原文核对＋Reel 海报 | **Opus 5.5** | 在高分组内做编辑挑选，读原文核对数字与主张，制作并 QA 中文海报 |

## 当前状态（run `embodied-v3-20261021-01`）

- **全量评分 500 篇**：487 篇有效出分；11 篇材料不足记 `needs_material`，总分 null；2 篇判为 `out_of_scope`。
- **最高分组**：88.75 分（G4/M4/X4/E3）共 53 篇并列。Opus 5.5 把这 53 篇分成 13 个主题聚类做编辑挑选，从中定出 9 篇。
- **核对与制作**：9/9 原文核对通过，9/9 海报视觉 QA ready，替补未动用。核对后收窄的结论只写进海报和 `verify.md`，不改原分数。
- 本期海报索引见 [reel/README.md](reel/README.md)；选择过程见 [final/selection.md](research/v3/runs/embodied-v3-20261021-01/final/selection.md) 和 [reel/selection-opus.md](reel/selection-opus.md)。

| paper_id | 一句话机制 |
|---|---|
| 2204.01691 | 语言似然×技能可行性打分选择（SayCan，2022 经典参照） |
| 2609.34412 | LLM 只写实体/关系，编译器生成保留零空间的任务映射 |
| 2610.19600 | 按最早未恢复错误做诊断，再对固定 VLA 注入针对性干预 |
| 2510.20328 | 高层 VLM 输出子任务＋关键帧，用时间聚类记忆指挥低层 VLA |
| 2606.10577 | 把像素目标、按需深度、历史召回暴露为导航工具 |
| 2609.19906 | 区分源任务性能与实现库对新任务的参考价值 |
| 2608.11350 | 冻结规划器/执行器，只演化文本技能与上下文代码 |
| 2410.07166 | 用对象状态＋LTL 统一决策模块接口，并细分错误类型 |
| 2609.33807 | 把隐藏物理验证与 agent 的完成声明分开记录的闭环基准 |

## 持续维护

仓库处于积极维护中：已连续两天收集（collect）候选，分别是 2026-10-21 和 2026-10-22（+10 候选、2 条更新）；新候选会进入后续的评分与 Reel 期次。
诚信原则：缺材料记 null，不冒充低分；作者声称与材料支持分开记录（`claim_support` / `evidence_level`）；只发布核对通过且 QA ready 的海报。

## 目录结构

```
inbox/                                   Grok Bots 收集记录（每次一个 jsonl + run.md）
patterns/overview.md                     embodied 领域模式卡（17 主卡 / 58 子卡）
research/reference/researchstudio-15-31/ 原 15+31 方法卡冻结副本
research/v3/runs/embodied-v3-20261021-01/
  ├── run.md                             规则版本、模型、输入快照
  ├── batches/                           54 个材料批次＋无材料批次
  └── final/                             index.jsonl（500 篇记录）、selection.md
reel/                                    本期海报：<paper_id>/{poster.png,poster.pdf,SOURCE.md,QA.md,verify.md}
docs/                                    EVIDENCE（证据等级）、PIPELINE、MAINTAINING、agents/ 提示词
```

## Related awesome lists

The corpus harvests arXiv ids and section headings from these lists (snapshots and commits in
[`refs/lists/SOURCES.md`](refs/lists/SOURCES.md)). They are broader than this radar; go there for coverage.

- [harooos/awesome-coding-agents-for-robot-learning](https://github.com/harooos/awesome-coding-agents-for-robot-learning)
- [kairunwen/Awesome-Robot-Use-Agent](https://github.com/kairunwen/Awesome-Robot-Use-Agent)
- [chonghanqin/Awesome-Agentic-Robots](https://github.com/chonghanqin/Awesome-Agentic-Robots)
- [xwzhang221/Awesome-Agentic-Robot-Policies](https://github.com/xwzhang221/Awesome-Agentic-Robot-Policies)
- [dongqianyu99/Awesome-Agentic-Embodided-Systems](https://github.com/dongqianyu99/Awesome-Agentic-Embodided-Systems)
- [mindorigin150/awesome-fm-driven-embodied-agents](https://github.com/mindorigin150/awesome-fm-driven-embodied-agents)
- [wisdom-pan/embodied-agent-harness](https://github.com/wisdom-pan/embodied-agent-harness)
- [YennNing/Awesome-Code-as-Agent-Harness-Papers](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers)
- [lobehub/awesome-rsi](https://github.com/lobehub/awesome-rsi)

## Credits and license

MIT（见 [LICENSE](LICENSE)）。
- **Base pipeline** cloned from [CUA Radar](https://github.com/CrepuscularIRIS/cua-architecture-radar), itself cloned
  from [HarnessRSI Daily](https://github.com/CrepuscularIRIS/HarnessRSI-Daily), built on
  [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) (MIT).
- **Pattern cards**：方法卡来自 ResearchStudio Idea 原 15+31（保留原 LICENSE）；领域卡借助 Open Scientist（domain build `embodied-agent-harness` v1）归纳。
