# EH Radar — Embodied Harness

前沿 LLM/VLM 或 coding agent 通过工具、冻结 VLA/技能、感知原语、记忆、验证和执行控制组成 harness，控制机械臂、移动操作、导航、无人机或人形机器人；也包括 harness 教师轨迹蒸馏、on-policy 纠正、harness 内 RL、自我优化及其评测。无 harness/教师闭环的纯 VLA、GUI 和非具身 RSI 不在本项目范围内。

核心问题：**模型通过哪一层 harness 控制什么本体，闭环成败如何判定，改进来自 harness、策略还是额外预算/特权信息？**

> **2026-10-21 重置：旧分数、榜单、Reel 和双席评审批次已归档，全部退出当前展示。**
> 模式卡与来源保留。当前没有有效的新版分数；v2 权重是待校准的设计草案，不是已验证的论文质量量尺。

## 从这里开始

| 内容 | 入口与状态 |
|---|---|
| 模式卡 | [overview](patterns/overview.md)，17 张主卡、58 张子卡；保留原有逆向产物 |
| 原始语料 | `research/corpus.jsonl`，本次盘点 1,351 条；收录不等于判定通过 |
| 新打分设计 | [SCORE_SPEC](research/SCORE_SPEC.md)：本领域权重、等级与待校准边界 |
| 本地 Claude Code | [LOCAL_SCORING_PROMPT](docs/agents/LOCAL_SCORING_PROMPT.md)：逐篇读全文与校准 |
| Grok 收集 | [GROK_PROMPT](docs/agents/GROK_PROMPT.md)：只收有一手证据的候选 |
| 新流程 | [PIPELINE](docs/PIPELINE.md)；[维护规则](docs/MAINTAINING.md)；[收录范围](docs/EVIDENCE.md) |
| Reel 重做 | [REEL_PROMPT](docs/agents/REEL_PROMPT.md)：先做单篇机制叙述，再设计图解 |
| 整理记录 | [RESET](docs/RESET_2026-10-21.md)；[旧产物归档](archive/2026-10-21-reset/README.md) |

## 新评分的权重草案

| 维度 | 分值 | 本项目重点 |
|---|---:|---|
| 结果与测量可信度 | 25 | 模拟器执行真值或计数的真机任务结果；逐任务试验数、成功判据、人工接管、重置和失败分母清楚。视频仅是线索。 |
| 因果归因与对照 | 20 | 固定 frontier backbone 替换 harness；学生方法比较 teacher/base/distilled student 在同一 harness 下；逐项消融工具、反馈、记忆和控制。 |
| 留出与外推 | 15 | 留出任务、场景、物体或本体；检查开发/技能挖掘/教师采集重叠。sim-to-real 主张需真机计数，跨本体主张需独立闭环证据。 |
| 统计与失败分析 | 15 | 真机少量试验的不确定性、随机种子/配对统计、碰撞/接管/超时、恢复与安全边界；不以一次演示代表稳定性能。 |
| 预算公平与成本 | 10 | 同传感器、特权状态、动作空间、交互/重试预算；纳入教师采集、训练、失败 episode、调用和硬件时延。 |
| 机制清晰度与模式执行 | 10 | 说明 model–harness–embodiment 接口、观测、工具/原语、状态、完成检测、执行门控与 hand-back；区分仿真和真机配置。 |
| 可迁移研究价值 | 5 | 说明迁移到另一任务/本体所需的控制接口、传感器、技能和工程改动；代码存在与运行验证单列。 |

分数回答“论文自身的主张被怎样的证据支持”；它不预测录用，也不等同于新颖性。
证据覆盖率、适用主张类型、模式适配、代码状态和阅读优先级单列。三个领域的数值不跨榜比较。

## 当前工作边界

Grok 找候选并写 inbox → 本地核对来源/去重/入库 → Claude Code 读完整材料、做小样本校准 →
冻结 rubric 后重新评分 → 通过证据审核的论文逐篇重做 Reel。

- 原有 `research/fulltext/` 是经过裁剪的历史文本缓存，不保证覆盖附录；新打分必须核对材料完整性。
- 原有 `research/screen.jsonl`、`research/patterns/assignments.jsonl` 是历史分档/适配线索，不能直接代替新的判断。
- Open Scientist 适合维护模式卡、研究问题与证据要求；日常打分不依赖完整研究循环。
- `make check` 只做离线结构检查。旧 `make score` / `make board` 和旧脚本入口会明确拒绝运行。
- inherited arXiv digest 的关键词相关性分数不属于论文质量分数，见 [digest 用法](docs/digest-pipeline.md)。

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

MIT (see [LICENSE](LICENSE)).
- **Base pipeline** cloned from [CUA Radar](https://github.com/CrepuscularIRIS/cua-architecture-radar), itself cloned
  from [HarnessRSI Daily](https://github.com/CrepuscularIRIS/HarnessRSI-Daily), built on
  [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) (MIT).
- **Pattern induction** with the Open Scientist plugin (domain build `embodied-agent-harness` v1, kept locally).
- **Corpus sources:** the nine lists above (arXiv ids and section headings only).
