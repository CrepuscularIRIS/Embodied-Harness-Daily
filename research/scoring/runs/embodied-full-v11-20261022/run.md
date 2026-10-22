# embodied-full-v11-20261022 · problem-core-v1.1 全量 L1

- 授权：用户 2026-10-22"可以去跑全量了, 6.1 sol"（试点 embodied-pilot-v11-20261022 已人工验收通过）
- 规则版本：`problem-core-v1.1`（commit 472aff1 时点；PROBLEM_CORE/SOL_BATCH_PROMPT/SELECTION 三项目共用）
- 执行模型：6.1 Sol（claude-kimi type `sonnet` → `gpt-6.1-sol`），CC 内置 Subagent，单初评席
- 范围：489 篇（v31 queue 500 − 试点已评 10 − out_of_scope 1）；试点 10 篇的 v1.1 记录复用，不重跑
- 批次：20 批 × 25 篇（自默认 20 放宽到 25：L1 材料为摘要+引言切分，实测每篇 3–6KB、批输入 ~100–150KB，Sol 上下文充裕；放宽依据 PROBLEM_CORE 第 5 节写入本记录）
- 并发：6（默认 4，试点无限流，按 SOL_BATCH_PROMPT 升至 6；滚动补位）
- L1 材料：materials/<id>-l1.txt（摘要+引言，切不出引言则 abstract；sha256 见各批 inputs.tsv 与 l1-pool.json）
- **L2 预算**：to_l2 ≤ 97 篇（489 的 20%；进入顺序 high→medium）+ 固定抽查 10 篇（P0/P1、F0、needs_material、park，随机种子 20261023，标 audit_sample=true）；另并入试点遗留 to_l2 的 5 篇（引用 pilot L1 记录）
- 卡片版本：patterns/ 于本 run 固定（不改卡匹配论文）
- 产出：batches/f01..f20 .jsonl；progress.md 滚动；阶段 checkpoint 本地 commit
- 全量 L1 完成后：总控机械核对 → L2 排队分批（10–20 篇/批）→ L2 workers → SELECTION 候选 → Opus 5.5 核对与 Reel（另行授权）
