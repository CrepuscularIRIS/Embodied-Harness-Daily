# Embodied Harness：v3 单模型批量评分与 Reel 流程

当前：v3（`sol-batch-v3`）已于 2026-10-21/22 完成全量 500 篇评分并产出第 1 期 Reel（9 篇）。v2.2 双席流程已停用并归档（本地 `archive/`，不在远端）。
[设计依据](DESIGN_BASIS.md) · [收录范围与证据等级](EVIDENCE.md) · [维护规则](MAINTAINING.md) · [run 记录](../research/v3/runs/embodied-v3-20261021-01/run.md)

## 模型分工

| 环节 | 模型 | 说明 |
|---|---|---|
| 收集 | Grok Bots | [GROK_PROMPT](agents/GROK_PROMPT.md)；定时更新写 inbox/，不打分 |
| 打分 | 6.1 Sol（Claude Code type `sonnet`） | 单席批量简评，无第二初评席、无全量聚合、无校准冻结 |
| 挑选/核对/海报 | Opus 5.5（type `fable`） | 并列组聚类挑选 → 原文核对 → 海报制作与视觉 QA |

## 每期流程

1. **收集**：Grok Bots 写 `inbox/*.jsonl`；本地 `python3 research/ingest.py inbox/<batch>.jsonl` 核对来源/去重/入库。
2. **材料固定**：完整全文缓存（`FULLTEXT: html-full` 头；附录缺失去 PDF 补 `<id>_pdf.txt`）。裁剪文本只作索引，不冒充 full。
3. **批量打分**（6.1 Sol，CC 内置 Subagent 4–6 并发滚动）：按材料体量切批（预算约 550KB/批），每篇一次判断完成 card pattern 提取（原 15+31 简明索引＋embodied 领域卡）＋四轴 G/M/X/E（0–4 或 null）＋紧凑 JSONL。逐批 `check.py` 机械校验（ID 对应、档位、算术、evidence 存在性）。
4. **选题**（`final/selection.md`）：分数降序；高并列组交 Opus 13 聚类编辑挑选（不改分），contradicted/unresolved 进问题清单，needs_material 单列待补。
5. **核对**（Opus 5.5）：逐篇读完整原文，核对 Sol 记录的数字与主张；发现错误写 correction 退回 Sol 单篇修订；收窄结论只写 verify.md。
6. **Reel**：核对通过才制作，每篇布局各异；渲染后实际看图 QA，ready 才发布。成品 `reel/<paper-id>/{poster.png,pdf,html,SOURCE.md,QA.md,verify.md}`。

## 数据与边界

- `research/fulltext/review-runs/` 完整材料为本地忽略目录，不提交全文。
- 旧 v2 分数与批次不作为 v3 输入；不同 profile/版本分数不混排。
- `make check` 只做离线结构检查；旧 `make score` / `make board` 拒绝运行。
- 每篇只初评一次；失败只补对应记录，不重跑整批。改规则须新版本号并记录 supersedes。
