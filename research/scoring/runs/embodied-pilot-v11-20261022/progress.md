# progress — embodied-pilot-v11-20261022

## L1（批 l1-b01，10 篇，完成）

| paper | status | 族 | q1 | q2 | tier | priority | next |
|---|---|---|---|---|---|---|---|
| 2311.10678 | assessed | F3 | measured_own | open_failure | P3 | high | to_l2 |
| 2505.07815 | assessed | F2,F0 | asserted | open_failure | P2 | medium | to_l2 |
| 2311.13373 | assessed | F0,F2 | asserted | open_failure | P2 | medium | to_l2 |
| 2310.10021 | assessed | F0,F3 | measured_own | open_failure | P3 | high | to_l2 |
| 2307.04738 | assessed | F0 | asserted | open_failure | P2 | medium | to_l2 |
| 2311.11183 | assessed | F2 | counterexample | open_failure | P3 | high | to_l2 |
| 2412.04453 | assessed | F3,F0 | asserted | open_failure | P2 | medium | to_l2 |
| 2610.15572 | assessed | F4,F3 | measured_own | open_failure | P3 | high | to_l2 |
| 2509.01106 | needs_material | F0 | asserted | unknown | null | medium | to_l2 |
| 2511.00917 | needs_material | F0,F3 | asserted | unknown | null | medium | to_l2 |

机械核对：ID 对应 ✓、枚举 ✓、封顶规则 ✓、facts 定位 ✓（0 错误）。

## L2（批 l2-b01，5 篇 = to_l2 2 + 抽查 3，完成，种子 20261022）

| paper | 入选方式 | L1 tier | L2 tier | evidence_status | next | 备注 |
|---|---|---|---|---|---|---|
| 2311.10678 | to_l2 | P3 | P3 | confirmed | to_l3 | BOSS 迁移结论收窄 |
| 2505.07815 | to_l2 | P2 | **P3** | pending_experiment | to_l2 | 全文给出自身测量；verifier 真值/误放行率仍缺 |
| 2310.10021 | audit | P3 | P3 | confirmed | to_l3 | 维持 |
| 2412.04453 | audit | P2 | **P3** | confirmed | to_l3 | 改判 |
| 2509.01106 | audit | null | null | pending_material | to_l2 | 仅摘要，缺方法/最近邻/打断实验 |

subcard_checks 35 项：5 holds / 19 partial / 8 unknown / 3 NA / 0 fails。

## 汇总指标

- 漏检抽查：3 篇抽 3，改判 1（2412.04453 P2→P3，上移）；to_l2 名额内另 1 篇上移（2505.07815）
- L2 推翻/修正 L1：2/5（均为上移；无下移）
- 候选池（P3 confirmed，to_l3）：2311.10678、2310.10021、2412.04453（3 篇）
- 用量：L1 119,722 subagent tokens（10 篇）；L2 153,404（5 篇）
- 阻塞：2509.01106/2511.00917 补材料（引言/方法/打断实验）；2505.07815 补 verifier 真值对照证据
