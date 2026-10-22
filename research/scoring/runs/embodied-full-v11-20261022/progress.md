# progress — embodied-full-v11-20261022

## L1（489/489，完成）

20 批 × 25 + fixmat-01（34 篇材料修复重评，旧行已清理）。枚举/封顶/ID 覆盖 0 错误。
- tiers：P3×303 / P2×170 / P1×4 / null×12；next：to_l2×482 / park×4 / exclude×3
- families：F0×233 / F3×205 / F2×166 / F1×113 / F4×76 / F5×58
- 材料缺陷：34 篇 l1 切分漏引言（数字编号 "## 1 Introduction"），修复重评后 P3 由少计上移

## L2（114/114，完成；6 批）

队列 = to_l2×97（high 优先截断）+ 漏检抽查×10（种子 20261023）+ pilot 遗留×7。
- 枚举/封顶/supersedes 0 错误；subcard_checks 463 项：holds 175 / partial 230 / unknown 36 / NA 13 / **fails 8** / challenged_with_evidence 1
- L2 最终 tier：P3×102 / P2×8 / P1×1 / null×3；next：to_l3×88 / to_l2×16（pending_experiment 或 pending_material）/ park×10
- **漏检抽查改判：2/10**（2501.11858、2602.15875，均 P2→P3 上移；方向与试点一致——L1 对材料受限论文偏保守）
- 相对 L1 改判共 12 篇（上移 11、待实验降级转 park 若干），L2 无推翻性问题判断

## 候选池（SELECTION 输入）

- **P3 confirmed to_l3：88 篇**（candidates-l3.json）
- 待补清单：needs_material×3（2509.01106、2511.00917、2505.23266 等 pending_material/high）+ pending_experiment×16
- audit 改判单列：2501.11858（P2→P3）、2602.15875（P2→P3）

## 增量：inbox 新论文

- Grok 三批 +25 已 ingest（corpus 1376 行）；全文材料抓取中，随后补 L1/L2（见 run.md 增量批）

## 用量（subagent tokens）

L1 全量 ≈ 2.9M（20 批 + fixmat）；L2 ≈ 0.8M（6 批）；pilot 已单列。

## 增量批（inbox +25，完成）

- L1 inc01：25/25（P3×16 / P2×9，全 to_l2；0 错误）
- L2 inc-l2-01：7 篇（to_l2×5 + audit×2）；4 篇 confirmed/to_l3、3 篇 park/pending_experiment；audit 改判 1/2（2610.27039 P2→P3）
- **最终候选池（P3 confirmed to_l3）：92 篇**（candidates-l3.json + candidates-l3-overview.json）
- 全 run 用量 ≈ 4.0M subagent tokens；L3/SELECTION 与 Reel 待用户授权后执行

## L2 第二波（用户解除预算限制，2026-10-22 晚）

- 范围：395 篇（high 溢出 222 + medium 173；2 篇仅摘要排除；pilot 3 篇 confirmed 补并入）
- 20 批（l2-07..l2-26）全部完成，枚举/封顶终查 0 错误
- **相对 L1 改判：上移 P2→P3 共 67 篇**（摘要差被全文纠正的主要效应）、下移 3 篇（含 1 篇 out_of_scope）
- L2 全量合计：516 篇记录；P3×391 / P2×118 / P1×3 / null×4
- **最终 to_l3 候选池：338 篇（含 l2-27 补齐 2 篇）**（s001 已用 9，可供 s002：327 篇）
- 用量：wave2 ≈ 2.9M subagent tokens（20 批）
