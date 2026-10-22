# Embodied-Harness-Daily（原 EH Radar — Embodied Harness）

`domain: embodied agent harness` · `scoring: sol-batch-v3` · `reel: 2026-10-22 第 1 期` · `license: MIT`

![pipeline](docs/assets/pipeline.svg)

追踪前沿 LLM/VLM 或 coding agent 如何借助 harness 控制具身系统，覆盖机械臂、移动操作、导航、无人机和人形机器人。harness 由工具、冻结 VLA/技能、感知原语、记忆、验证和执行控制组成；也收录 harness 教师轨迹蒸馏、on-policy 纠正、harness 内 RL、自我优化及其评测。无 harness/教师闭环的纯 VLA、GUI agent 和非具身 RSI 不在范围内。

核心问题：**模型通过哪一层 harness 控制什么本体？闭环成败如何判定？改进来自 harness、策略，还是额外预算/特权信息？**

## 从这里开始

| 内容 | 入口与状态 |
|---|---|
| 本期 Reel | [reel/README.md](reel/README.md)：9 篇核对通过的海报索引，每篇布局各异 |
| 评分记录 | [final/index.jsonl](research/v3/runs/embodied-v3-20261021-01/final/index.jsonl)：500 篇逐篇 JSONL |
| 选择过程 | [final/selection.md](research/v3/runs/embodied-v3-20261021-01/final/selection.md)＋[reel/selection-opus.md](reel/selection-opus.md) |
| 评分规则 | `sol-batch-v3`（run 记录见 [run.md](research/v3/runs/embodied-v3-20261021-01/run.md)） |
| 流程文档 | [PIPELINE](docs/PIPELINE.md)；[维护规则](docs/MAINTAINING.md)；[收录范围](docs/EVIDENCE.md)；[设计依据](docs/DESIGN_BASIS.md) |
| 模式卡 | [overview](patterns/overview.md)（embodied 领域 17 主卡/58 子卡）；[原 15+31 冻结副本](research/reference/researchstudio-15-31/) |
| Grok 收集 | [GROK_PROMPT](docs/agents/GROK_PROMPT.md)：只收有一手证据的候选，定时更新写 inbox/ |

## 模型分工

| 环节 | 模型 | 做什么 |
|---|---|---|
| 收集 | **Grok Bots** | 定时更新，写入 `inbox/`，不打分、不做海报 |
| 打分 | **6.1 Sol** | 单模型批量简评（`sol-batch-v3`）：card pattern 提取＋四轴 G/M/X/E，权重 15/20/20/45，满分 100 |
| 挑选＋核对＋海报 | **Opus 5.5** | 高分并列组内 13 聚类编辑挑选 → 逐篇读原文核对数字与主张 → 制作中文海报并视觉 QA |

四轴：G 问题与 gap / M 方法与 problem-fit / X 机制与条件 / E 证据支撑（权重最高）。分数是选读初筛分，不是审稿分；缺材料记 null 不冒充低分；作者声称与材料支持分开记录（`claim_support` / `evidence_level`）。

## 本期 Reel（2026-10-22 · 9 篇 · 核对 9/9 通过）

|  |  |  |
|---|---|---|
| [![](reel/thumbs/2204.01691.jpg)](reel/2204.01691/poster.png) | [![](reel/thumbs/2609.34412.jpg)](reel/2609.34412/poster.png) | [![](reel/thumbs/2610.19600.jpg)](reel/2610.19600/poster.png) |
| **2204.01691** 语言似然×技能可行性（SayCan 经典参照） | **2609.34412** LLM 写实体，编译器生成任务映射 | **2610.19600** 最早未恢复错误诊断→干预 |
| [![](reel/thumbs/2510.20328.jpg)](reel/2510.20328/poster.png) | [![](reel/thumbs/2606.10577.jpg)](reel/2606.10577/poster.png) | [![](reel/thumbs/2609.19906.jpg)](reel/2609.19906/poster.png) |
| **2510.20328** 高层 VLM 子任务＋关键帧记忆 | **2606.10577** 像素目标/深度/历史召回工具化 | **2609.19906** 源任务性能 vs 新任务参考价值 |
| [![](reel/thumbs/2608.11350.jpg)](reel/2608.11350/poster.png) | [![](reel/thumbs/2410.07166.jpg)](reel/2410.07166/poster.png) | [![](reel/thumbs/2609.33807.jpg)](reel/2609.33807/poster.png) |
| **2608.11350** 冻结策略，只演化技能与上下文代码 | **2410.07166** 对象状态＋LTL 统一接口基准 | **2609.33807** 隐藏物理验证 vs 完成声明 |

每篇目录含 `poster.png/pdf`、`SOURCE.md`（数字→原文定位映射）、`QA.md`、`verify.md`；可编辑源 `poster.html` 仅存本地。

## 当前状态（run `embodied-v3-20261021-01`）

- **全量评分 500 篇**：487 有效出分；11 篇材料不足记 `needs_material`（总分 null）；2 篇 `out_of_scope`。
- **最高分组**：88.75（G4/M4/X4/E3）×53 篇并列 → Opus 13 聚类挑选 9 篇，全部 supported_in_material。
- **核对结论**：收窄不改分——如 SayCan 两处作者表述无依据未上画报、2410.07166 LTL 统一仅对 G/Φ/Q 模块成立，详见各 `verify.md`。
- **机械校验**：54 批全部通过（ID 对应、档位范围、算术、evidence 存在性），零问题。

## 持续维护

积极维护中：Grok Bots 已连续两日收集（2026-10-21、2026-10-22 +10 候选），新候选进入后续评分与 Reel 期次；仓库与文档随流程演进定期更新（v2.2 双席流程已于 2026-10-21 停用并归档）。

## 目录结构

```
inbox/                                   Grok Bots 收集记录（每次一个 jsonl + run.md）
patterns/overview.md                     embodied 领域模式卡（17 主卡 / 58 子卡）
research/reference/researchstudio-15-31/ 原 15+31 方法卡冻结副本
research/v3/runs/embodied-v3-20261021-01/
  ├── run.md                             规则版本、模型、输入快照
  ├── batches/                           54 个材料批次＋无材料批次
  └── final/                             index.jsonl（500 篇）、selection.md
reel/                                    每期海报 <paper_id>/＋thumbs/ 缩略图＋索引
docs/                                    EVIDENCE、PIPELINE、MAINTAINING、agents/ 提示词
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
