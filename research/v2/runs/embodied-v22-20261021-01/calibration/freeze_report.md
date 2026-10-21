# 校准报告（两轮未过，批量停止）— embodied-v22-20261021-01

日期：2026-10-21。结论：**一致性验收未通过，按 SCORE_SPEC 校准/冻结/实施边界第 5 条停止批量评分。rubric 未冻结，无有效排名，无 Reel 选择。**

## 验收目标（SCORE_SPEC）

留出 ≥8 对可评分论文，双席（6.1 Sol / Sonnet 5.5）总分中位差 ≤5，且 ≥90% 对差 ≤10。

## 两轮结果（12 对，c-ho-1 + c-ho-2）

| 轮 | anchors | 中位差 | ≤10 比例 | 超差对 |
|---|---|---|---|---|
| r1（a1） | v1 | 3.75 ✓ | 10/12 = 83.3% ✗ | 2503.02465 (18.75)、2512.10394 (15.00) |
| r2（a2） | v2（E.measurement/E.statistics 细化） | 8.125 ✗ | 9/12 = 75.0% ✗ | 2609.31760 (18.75)、2503.02465 (12.50)、2503.10069 (11.25) |

两轮均未达 90% 阈值；第二轮中位差恶化。r1 的问题对 2512.10394 收敛到 8.75，但 2609.31760 从 8.75 恶化到 18.75，且出现新超差对。

## 诊断

1. **锚点细化收敛了它针对的形态，放大了相邻形态的分歧**：anchors v2 的"结果报告不完整→E.measurement≤2"使 2512.10394 类论文收敛，但负结果/单次实验论文（2609.31760：123 轮 RSI 失败报告）在"负结果的证据价值如何计分"上两席产生更大分裂（sol 60 vs son55 78.75）。
2. **中间档论文的方差是模型内在的**：≥10 差的对在两轮间不稳定（r1 超差对与 r2 仅部分重叠），说明差异不是某个固定盲点，而是两席对 0–4 中间档的落点噪声。锚点文字细化不足以约束。
3. **方向不一致**：2503.02465 两轮均 sol>son55，2609.31760 r2 sol<son55——不存在可通过整体偏置校正的系统性方向。
4. 聚合质量本身无恙：两轮 24 个聚合记录全部 accepted_final、无未解分歧、hash/算分全部通过；Opus 在两轮均发现并记录了两席共有错误。失败模式集中在**双席初评一致性**，不是流程完整性。

## 已完成且保留的工作

- dev 6 篇 + holdout 12 篇（两轮）双席原件、聚合 final records、resolutions、共有错误修正——全部按 BATCH_CONTRACT 落盘，hash 可验。
- final/index.jsonl 当前持 17 条 accepted_final 记录（dev 6 + holdout r2 11 + out_of_scope 1），**标注为 calibration 来源，不构成冻结 rubric 下的有效分数**，不得用于 Reel 选择。
- anchors.md v2、两轮一致性原始数据、5 类机械工具（check_batch/update_state/make_batch/fetch_fulltext_v2/dispatch 脚本）。
- 材料资产：494/500 篇完整未裁剪全文（research/fulltext/review-runs/…/materials/，gitignored）。

## 停止后的选项（需用户决策，日常评审不得自行改 rubric/门槛）

A. 接受更高方差：与维护者商定放宽门槛（如 ≥80% ≤10 + 中位 ≤6），按当前 anchors v2 冻结进入生产——门槛变更需显式授权并记录。
B. 结构性约束而非文字锚点：把 E 子项改为逐事实核对清单（not_reported 判定表）压缩中间档自由度，再做一轮校准（新一轮 dev+holdout，非旧对重用）。
C. 引入人工 gold：用户/维护者标定 8–12 篇的 G/M/X/E 档位作参照，校准两席。
D. 换双席配置（如 sol↔其他模型）重新校准——模型内在方差或随席位组合改变。

## 过程备忘

- 模型路由：sonnet type=gpt-6.1-sol、haiku type=claude-sonnet-5-5[1m]、fable type=claude-opus-5-5[1m]，全部内部 Subagent 派发（用户纠正后统一）。
- 首派 a1 因旧全文缓存为裁剪版作废（留档 a1-invalidated-cropped-material），重抓 494 篇完整 HTML 后重新固定输入包。
- expectations 文件存在于 .forge/domains/embodied-agent-harness-v1/profile/expectations.json（sha256 db5ce019a8741274…），a2 阶段起被 worker 引用；生产轮应预先固定进 manifest。
- 两席 domain_cards hash 计算方式不一致（同一文件两种定义）——生产派发词需固定 hash 定义（taxonomy.json+conditions.json+overview.md 拼接序）。
- 1 次 API stream 中断重试成功（c-ho-1 sol）；无 contamination 事件。
