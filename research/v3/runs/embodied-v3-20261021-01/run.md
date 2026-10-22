# embodied-v3-20261021-01 · v3 单模型批量评分

- 规则版本：`sol-batch-v3`（SCORE_SPEC §v3），profile `embodied-v3`，权重 G=15 M=20 X=20 E=45，`screen_score=(15G+20M+20X+45E)/4`。
- 执行模型：6.1 Sol（claude-kimi type `sonnet` → `gpt-6.1-sol`），单席，无第二初评席、无 Opus 全量聚合、无校准冻结。
- 范围：v2 队列全部 500 篇。494 篇有完整全文材料（进入 54 个批次，见 `batches/*-inputs.tsv`）；6 篇无任何材料（2509.01106、2511.00917、2609.36171、2610.22736、2307.06135、2409.14908）按 `needs_material` 记录于 `batches/b999-nomaterial.jsonl`，总分 null，不冒充评分。v2 旧分与 disposition 不作为输入。
- 材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/<id>.txt`（`FULLTEXT: html-full` 头 = full；21 篇附 `<id>_pdf.txt` 附录补充）。材料目录 gitignored，本地保留。
- 规则文件：`/home/lingxufeng/radar-scoring-v3-draft/`（SCORE_SPEC 62f21fe3fcbfda56、domains/embodied.md d951484c00cb2eb0、RESEARCHSTUDIO_INDEX 9beff37213cb1994、embodied-card-index 14de5270cac26ebe）＋ 仓库 `docs/EVIDENCE.md`（evidence_level 依据）。
- 输入快照：v2 queue.jsonl sha256[:16]=6270c676b349f4ed；批次切分 `make_batches.py`（按体量贪心装箱，预算 550KB / ≤16 篇）。
- Git HEAD：becd7d364f4f2398f300a08d72fbbb796a6c5804
- 机械校验：`check.py`（ID 一一对应、字段齐全、档位 0–4/null、算术、scored 必有 evidence）。进度：`progress.md`。
- 后续：SELECTION 取前 15 候选 → Opus 5.5 原文核对并制作 Reel（≤9 篇）。
