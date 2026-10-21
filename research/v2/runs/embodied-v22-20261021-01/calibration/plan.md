# 校准抽样计划 — embodied-v22-20261021-01

抽样池：material_ready=307 篇（screen A/B 线索 + 完整 HTML 全文缓存）。4 篇 abstract-only 缓存（2509.01106, 2511.00917, 2609.36171, 2610.22736）标 needs_fulltext 不入池。
分层代理：screen_kind（system/method → system_method/component_training 候选；benchmark/dataset/empirical → evaluation_resource 候选）
+ 全文大小三档（≥32KB / 26–32KB / <26KB，按缓存分布定档）。
实际 claim_type 由两席逐篇判定，抽样只保证材料多样性。evaluation 类全文仅 3 篇，claim_type=evaluation_resource 的校准覆盖有限，在校准报告如实记录。
确定性：各池按 (ft_size, paper_key) 排序后等距取样；dev 与 holdout 互斥。

## dev（6 篇，c-dev-1，用于锚点修订）
- 2602.20323 2602.20323v6 [A/method] 32012B
- 2606.12299 2606.12299v2 [A/method] 35477B
- 2606.12372 2606.12372v1 [A/method] 26015B
- 2605.13119 2605.13119v2 [A/method] 28684B
- 2609.27308 2609.27308v2 [A/benchmark] 17576B
- 2606.00104 2606.00104v1 [A/method] 14949B

## holdout（12 篇，c-ho-1/c-ho-2，不调参）
- 2503.02465 2503.02465v2 [A/system] 15224B
- 2610.15572 2610.15572v1 [A/method] 23190B
- 2609.39915 2609.39915v1 [A/method] 25431B
- 2512.10394 2512.10394v2 [A/system] 26725B
- 2609.26360 2609.26360v1 [A/method] 27744B
- 2503.10069 2503.10069v2 [A/method] 28852B
- 2608.16978 2608.16978v1 [A/method] 30203B
- 2602.19983 2602.19983v2 [A/method] 31597B
- 2601.18492 2601.18492v1 [A/method] 34873B
- 2608.18227 2608.18227v1 [A/empirical] 18366B
- 2609.31760 2609.31760v1 [A/empirical] 19185B
- 2609.29091 2609.29091v1 [A/method] 16926B
