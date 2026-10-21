# dev 阶段锚点修订记录 — embodied-v22-20261021-01

日期：2026-10-21。依据：c-dev-1/c-dev-2 双席初评 + Opus 聚合裁决（6 篇，3×accepted+score / 1×accepted+score / 1×accepted+score / 1×out_of_scope）。
本文件只记录锚点级澄清与执行先例，**不改权重**（G15/M20/X20/E45 与 E 子项 15/10/10/5/5 维持 SCORE_SPEC v2.2 初始提案）；holdout 不据本文件重评。

## E 五子项本领域锚点实例（冻结候选，待 holdout 一致性检验）

- **E.measurement**：4=闭环执行由环境真值判定+每任务试验次数与成功率完整（2609.27308 双本体真机+仿真）；2=闭环结果可读但分母/验证器有缺口或含特权通道（PhysMem 符号状态）；0=无成功率/基线测量（PEACE）。
- **E.causality**：4=同模型/任务/预算对照充分、强替代解释被消融检验；2=关键增益存在未分离的混杂（DROID 后训练、接口增量 +0.8）；0=无任何对照。
- **E.holdout**：4=构建期未用的本体/场景且增益保留（2606.12299 未见硬件任务 30 试）；2=开发任务与评测重叠或留出增益≈0；0=训练评测同批任务同本体（2606.12372）。
- **E.statistics**：4=重复试验+方差/失败分母完整；1-2=有试验数但无方差、失败不分解；0=not_reported（须记录查找范围）。
- **E.cost**：4=预算公平+实际成本披露；3=成本披露但部分环节缺失；2=调用预算可推算但特权信息通道未定价（PhysMem）；0=not_reported。

## 执行先例（对生产轮有约束力）

1. **特权信息通道**：模拟器符号状态（如 blocker/dependency）来源未写明时按特权处理，进 E.causality/E.holdout 扣分锚点，evidence_level 不给 transfer（PhysMem 先例）。
2. **scope 裁决**：无前沿 LLM/VLM/coding agent、教师为人类操作者、被控为学习型干预模块 → out_of_scope（2606.12372 先例；条件分保留在 conditional_score_if_scope_reversed 供宽读法复核，不入索引）。
3. **claim_type 歧义**：论文同时含基准与求解框架时按其自述中心主张定 type（2609.27308 → system_method）。
4. **来源循环卡**：领域卡引用被评论文本身时，匹配只作结构参照、不构成独立证据，不得作为任何 rating 依据（K204/K503/K504/K704 先例）。
5. **not_reported ≠ unknown**：完整材料+附录查过且记录查找范围才可 not_reported（rating 0）；材料有但被作者删节（如 PhysMem v6 任务提示词）按 unknown 处理并挂 needs_evidence。
6. **共有错误必须建 shared_error_corrections**：两席一致的结论仍需 Opus 复核（Tool-Aligned VLA 的 OpenVLA RoboTwin-SA 反向结果两席都漏）。

## 记录格式规范（两席统一，消除机械假差异）

- ratings 嵌套结构：`ratings.G/M/X` 与 `ratings.E.<sub>`（不写扁平 `E.<sub>` 顶层键）。
- 原卡子卡一律 `rs:` 前缀（裸 `C08` 视为格式错误）；领域卡 namespace=embodied、匹配上限 3 张。
- check_batch.py 已修复扁平 E 键兼容；扩展比较（expectations/domain/supporting）由 Opus 聚合覆盖，机器不重复判。

## 遗留（阶段末处理）

- 卡修订提案：K504 "from saved checkpoints" 措辞、来源循环标记、HiL-RL 范围规则条目化（在 c-dev-1/c-dev-2 aggregate records 中）。
- expectations 独立文件缺失（期望内嵌于 patterns/main/*.md）——校准报告记录，不阻塞。
- 2602.20323 v6 删节任务提示词可能存在于早期 arXiv 版本：仅当评审版本改变时处理。

## v2 修订（2026-10-21 第二轮，依据 round1_consistency.md 诊断；权重不变）

- **E.measurement 中间档细化**：成功/到达判据未定义、或全部结果为单次试验无重复 → rating ≤2；判据存在但分母不完整（部分任务有试验数、部分没有）→ 2；判据与分母皆无 → 0–1。依据：dev PEACE 先例（0 档）与 2606.12372（holdout 低档）同向延伸。
- **E.statistics 中间档细化**：无重复试验、无失败分解 → ≤1；有试验数但无方差/置信区间 → 1–2。
- 本版对 holdout 第二轮（a2 attempts）有约束力；a1 记录保留不回改。
