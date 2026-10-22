# Embodied-Harness-Daily（原 EH Radar — Embodied Harness）

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

## 新评分：先 gap / 模式 / 期望，再核主张证据

[方法依据](docs/DESIGN_BASIS.md)借鉴 ResearchStudio Idea 与 Open Scientist；[逐篇工作表](research/REVIEW_WORKSHEET.md)记录改了什么、怎样保留、提升是否被支持。

| 轴 | 权重上限 |
|---|---:|
| G：Gap 与问题位置 | 15 |
| M：方法质量与 problem-fit | 20 |
| X：机制执行与模式条件 | 20 |
| E：主张的证据支撑 | 45 |

权重是待校准提案。G/M/X/E 总分与 claim_support、evidence_level 分开；匹配模式不直接加分，无审稿仍用有来源的审稿期望。
[动态选题](docs/REEL_SELECTION.md)：先过最低分，再控制篇数，默认一期最多 9 篇；不足可少做，调阈值不改原分数。
只有入选论文交给 ResearchStudio Reel 做画报，展示只包含成品 QA 通过的精选。

## claude-kimi / Claude Code 批量评分

先复制 [启动指令](docs/agents/START_CC.md)；[总控提示词](docs/agents/LOCAL_SCORING_PROMPT.md)可直接交给 claude-kimi（Claude Code）：每批默认5篇、每轮并行2批，6.1 Sol＋Sonnet 5.5 独立初评，Opus 5.5 逐篇聚合，轮次验收后继续，最后由总控提交。
每篇必做 [原15+31识别与领域映射](research/PATTERN_PROTOCOL.md)；固定原卡已随仓库提供，不能混用原卡与领域卡 ID。
[GLM 5.3 Reel 提示词](docs/agents/REEL_PROMPT.md)只处理入选名单。model type 已配置，直接沿用；本次只写文档，未启动批次，评分规则仍待校准。

## 当前工作边界

Grok 找候选并写 inbox → 本地核对来源/去重/入库 → Claude Code 读完整材料、做小样本校准 →
冻结 rubric 后重新评分 → 动态阈值与数量筛选 → 入选论文重做 Reel。

- 原有 `research/fulltext/` 是经过裁剪的历史文本缓存，不保证覆盖附录；新打分必须核对材料完整性。
- 原有 `research/screen.jsonl`、`research/patterns/assignments.jsonl` 是历史分档/适配线索，不能直接代替新的判断。
- 建议 CC 安装 Open Scientist，支持 gap 诊断、模式/期望维护与独立审阅；日常评审使用冻结资产，缺口才返回研究循环。
- `make check` 只做离线结构检查。旧 `make score` / `make board` 和旧脚本入口会明确拒绝运行。
- inherited arXiv digest 的关键词相关性分数不属于论文质量分数，见 [digest 用法](archive/2026-10-21-reset/docs/digest-pipeline.md)。

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
