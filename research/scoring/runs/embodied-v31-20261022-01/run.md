# embodied-v31-20261022-01 · v3.1 领域 pattern 批量评分

- 规则版本：`sol-domain-v3.1`，profile `embodied-v3.1`，权重 G=15 M=20 X=20 E=45，`screen_score=(15G+20M+20X+45E)/4`。
- 与 v3 的关键区别：**只用本领域卡**（`patterns/main/`＋`patterns/sub/`，17 主卡/58 子卡）；原 ResearchStudio 15＋31 不作为分类层。评分路径强制：论文操作 → 相关领域 pattern → 读卡取 1–3 条关键判据（card_checks，verdict=met/partial/unmet/unknown/challenged_with_evidence）→ 论文证据 → 四轴评分。
- patterns 字段：`primary`/`subcards`/`supporting`/`status`(matched/unassigned/uncertain)/`reason`，全部 `embodied:<card-id>`。
- 执行模型：6.1 Sol（claude-kimi type `sonnet` → `gpt-6.1-sol`），CC 内置 Subagent，4 并发起滚动补位（稳定后按 SOL_BATCH_PROMPT 可升至 6–8）。无第二席、无全量聚合、无校准。
- 范围：500 篇（旧 v2 队列全量，旧分数不作输入）。494 篇有完整全文材料 → 54 个体量制批次（预算 550KB/≤16 篇）；6 篇无任何材料 → `batches/b999-nomaterial.jsonl` 记 needs_material（总分 null，不冒充）。
- 材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/<id>.txt`（`FULLTEXT: html-full` 头 = full；21 篇附 `<id>_pdf.txt` 附录补充）。gitignored，本地保留。
- 输入快照：`queue.jsonl`（自 d9496e0^ 固化，sha256[:16]=6270c676b349f4ed）。
- 规则文件：`research/scoring/`（SCORE_SPEC 7abbb6ae9e5cd7fd、PROFILE 78b419638c958deb、PATTERN_INDEX fd12faf155c28a4b、SOL_BATCH_PROMPT 8c81549af9d0d375、SELECTION e56249ded5a9fbf6）＋ `docs/EVIDENCE.md`（612b7df7eec04add）。
- Git HEAD：d9496e001d321845a823d0735bda93cf8349c908
- 机械校验：`check.py`（ID 对应、字段、patterns/card_checks 结构、档位、算术、evidence）。进度：`progress.md`。
- 后续：SELECTION 候选 ≤15 → Opus 5.5 原文核对 → Reel ≤9 篇。
