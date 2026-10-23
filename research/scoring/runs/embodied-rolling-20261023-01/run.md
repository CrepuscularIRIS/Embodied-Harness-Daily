# Rolling run embodied-rolling-20261023-01（Embodied-Harness-Daily 增量轮）

- 规则：problem-core-v1.1（PROBLEM_CORE / SOL_BATCH_PROMPT，2026-10-22 版）。
- 启动：2026-10-23 巡检班；Git HEAD 9d613af4b0117c62ec91cfdede30878b3a2d087e；patterns 卡片版本 0b299e2。
- 输入：queue/2026-10-23-2252.txt 1 篇（2610.26659，ingest.py 入库，corpus 1376→1377，全文 research/fulltext/2610.26659.txt）。
- 模型：6.1 Sol（claude-kimi `sonnet` 槽 → gpt-6.1-sol），CC 内置 Subagent，单初评席。
- 批大小：增量小批（1 篇）；并发 1。
- L2 预算：篇数上限 = max(1, 20%×本 run 累计 L1)，token 不设硬额逐批记录；单篇轮无漏检抽查名额（10% 预算取整为 0，run 记录在案）。
- 授权：用户 2026-10-23 会话授权的 6 小时巡检管线。
