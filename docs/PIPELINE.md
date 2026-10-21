# 现行流程：收集 → 本地阅读 → 校准 → 重评 → Reel

状态：旧路线已退役；候选收集/入库工具保留；新评分是待校准设计。本次整理不调用付费评审模型，不批量重评。

1. **Grok 收集**：按 [GROK_PROMPT](agents/GROK_PROMPT.md) 读标题、摘要与官方论文/项目页。只把机制和研究对象清楚、能回到一手来源的候选写入 inbox。
   高质量线索不等于高分；负结果、审计和 benchmark 同样可收，不能靠热点/演示/转述充数。
2. **本地核对**：读 [inbox 格式](../inbox/README.md)，验证 ID、标题、版本与来源相符，去掉同论文改名/多来源重复。
   对新 arXiv ID 可运行 `python3 research/ingest.py inbox/<batch>.jsonl`。脚本保留旧的截取文本抓取，结果只作为阅读索引。
   该脚本会跳过 corpus 已有 ID；版本更新保留在 inbox 并人工核对新版本，不能以“nothing new”认定已处理。
   无 arXiv ID 的论文/技术报告留在 inbox 单独处理，不假造 ID。确认所有行都有处理结果后再移动 inbox 到 processed。
3. **材料检查**：固定版本并取完整正文、附录、补充实验；为每份材料保存 URL、hash 与覆盖范围。
   旧 HTML 截取去掉了附录并有字符上限，不能据此认定论文“未报告”。缺材料 → `needs_fulltext`，不评分。
4. **Claude Code 小样本校准**：使用 [LOCAL_SCORING_PROMPT](agents/LOCAL_SCORING_PROMPT.md)。现有卡片只作机制参考，旧分数不输入。
   按 [SCORE_SPEC](../research/SCORE_SPEC.md) 校准规则和同一版本材料，先记录引用，再逐项判断，最后计算。
5. **冻结后重评**：记录 rubric 哈希、校准报告及通过的证据。实现并验证新版确定性评分器后，评审新批次到 `research/v2/judgments/`；
   任何得分必须能从同一批次的证据重算，重复 ID/version 要明确 supersedes，不用“后写文件覆盖”隐式决定。
6. **展示与 Reel**：新发布器只读经审核的 v2 结果。先做三篇不同机制的样片，经核对后再扩展。
   按 [REEL_PROMPT](agents/REEL_PROMPT.md) 给每篇设计可解释机制的叙述与图；不按旧高分清单批量套版。

## 数据位置

| 内容 | 位置 |
|---|---|
| 现有原始语料与全文缓存 | `research/corpus.jsonl`、`research/fulltext/`（后者本地） |
| 已完成模式卡与机器可读定义 | `patterns/`、`research/patterns/taxonomy*.json`、`conditions.json` |
| 历史分档/适配线索 | `research/screen.jsonl`、`research/patterns/assignments.jsonl`；未经新流程认可 |
| 新版评审工作 | `research/v2/`；当前只有说明，尚无新分数 |
| 退役产物 | `archive/2026-10-21-reset/`；索引和哈希清单在内 |
| 当前展示入口 | `papers/README.md`、`reel/README.md`；当前为空榜/待重做 |

## Open Scientist 的位置

已有模式卡与期望条目是有用的来源索引，不能把它们的存在等同于评分可靠。
其 `paper_practice` / `paper_limitation` 表示论文惯例/作者局限，不可改称“实际审稿共识”。
目前 Embodied 本地 profile 明确说没有 reviews/labels，现有权重不是经验标定得到的。

**建议 CC 安装用于后续 rubric 研究、独立审阅和卡片维护，但不是日常打分的必需依赖。**
本次只读取已安装 Open Scientist 的说明与现有领域 profile 来评估适配，不创建新 study，不重新构建领域。
冻结后的规则与证据记录可以直接交给 Claude Code；只有要改领域结构或研究判据时再进入 Open Scientist 研究循环。

## 已停用的入口

`research/score.py`、`build_board.py`、双席 merge/batch、旧 calibration、monitor 和 Reel 生成入口已改成明确失败的退役提示。
旧源码在归档中保存。不存在“v2 打分已完成”或“重做 Reel 已完成”的状态。
