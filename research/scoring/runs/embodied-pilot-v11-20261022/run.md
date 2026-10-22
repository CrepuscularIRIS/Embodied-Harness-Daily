# embodied-pilot-v11-20261022 · problem-core-v1.1 试点

- 规则版本：`problem-core-v1.1`（commit 731a93c；PROBLEM_CORE/SOL_BATCH_PROMPT/SELECTION/OPUS_REEL_PROMPT 三项目共用）
- 性质：**试点（PROBLEM_CORE 第 9 节），全量前必做；用户 2026-10-22 指令"全部按照这个重新跑"**
- 执行模型：6.1 Sol（claude-kimi type `sonnet` → `gpt-6.1-sol`），CC 内置 Subagent；单初评席，无第二席/无聚合/无校准门槛
- 范围：10 篇试点样本（pilot-sample.json），覆盖 F1/F2/F4/F5/F0 ≥5 族、1 篇诊断/审计（2311.11183）、1 篇 vertical_port 候选（2412.04453）、2 篇 abstract-only（2509.01106、2511.00917）、1 篇单一来源卡论文（2610.15572，K505 唯一来源）
- 材料：L1 = 摘要+引言切分（materials/<id>-l1.txt，sha256 见 pilot-sample.json；8 篇 abstract_intro、2 篇 abstract）；L2 用 materials 完整全文的关键段（同 v22 缓存目录，不重新下载）
- 输入清单线索：research/scoring/runs/embodied-v31-20261022-01/queue.jsonl（材料固化快照，仅作路径/版本来源，其数值规范已停用不作输入）
- **L2 预算**：to_l2 上限 2 篇（L1 的 20%）+ 试点特别要求的漏检抽查 ≥3 篇（从 P0/P1、F0、needs_material、park 随机抽，随机种子 20261022，标 audit_sample=true）→ L2 总计 ≤5 篇，单批
- L1 批：1 批 10 篇（试点规模即一批）
- 卡片版本：patterns/ 于 731a93c 固定；卡片来源 hash 由 worker 按文件自取
- 试点验收（用户人工）：漏检（低档抽查中被改判数量）、L2 推翻 L1 的数量、实际用量
- 产出：batches/l1-b01.jsonl（L1）、batches/l2-b01.jsonl（L2）、progress.md、pilot-report.md
