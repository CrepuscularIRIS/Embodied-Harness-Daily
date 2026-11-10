# SOURCE · 2611.08425

- 论文：Failure Prediction and Classification in Vision-Language-Action Models via Calibrated Latent Probing（VLA-Tug），arXiv **2611.08425v1**（2026-11-05；Michal P. Podolinsky、Yunhao Yang、Daniel Little 等，UT Austin、Tufts、UT Dallas）。arXiv 仅 v1（export API 2026-11-10 查询）。
- 阅读原文：钉定缓存 `research/fulltext/2611.08425.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §2、§5 与全部附录，§1/§4.2 段尾截断）。§5 与附录 A–E 补读自同版本 arXiv HTML `https://arxiv.org/html/2611.08425v1`（2026-11-10 取得，转换稿仅在 /tmp，不提交）。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-10.jsonl`（L2，P3 / confirmed / to_l3；F2,F3；capability；主卡 external_verification_control）。selection-011 第一备选，本期兑现。入选：`selections/selection-012.md` #3。

## 核对结论（Opus 5.5，2026-11-10）

通过，无 correction。L2 facts 与原文一致：14 次 LIBERO-X 运行、7 个误报目标；见过的任务上已认证运行全部兑现；未见任务误报兑现 40–86%、提前抓到兑现 57–90%；探针 6.6M、0.12 ms GPU / 0.9 ms CPU、动作块 400 ms；纠偏只是概念验证。L2 已修正 L1 的“86% 联合兑现”说法，正确。

补读附录后的展示取舍（不改判断）：
- 附录表 7：α=10% 时 LTT 在 14 次运行全部弃权（L2 写“4–7/14 abstain”，对应正文 α=15–50% 的说法）；可认证的 β 只有 15–65%。画报第 ② 区以“能承诺多少”为主体，把弃权与低 β 一起呈现。
- 表 7 两组兑现率分母不同：LTT 只算已认证运行，MC/FC 算全部 14 次；新任务、新组合两类划分的 3 次运行共享同一批未见任务。画报表头与正文注明。
- **附录 B.2：出错时刻与失败类型由 Gemini 3.5 Flash 看视频标注，原文未报告人工一致性。** L2 K804 已记“缺 §5 标注一致性，不能把便宜标注视为独立可靠真值”，补读证实这一缺口；附录 D.4 只检验了出错时刻整体后移的敏感性（真机上 SAFE-LSTM 会反超）。属 L2 已标的证据边界，不改档位，画报限制栏第 1 条写明。
- 摘要称“支持轻量纠偏、提高任务成功”，§6.5 与 §7 明说纠偏为启发式、未评估；画报第 ④ 区按演示读。
- 表 3：VLA-Tug 在未见任务六设置中四个最好；新任务划分 SAFE-MLP 42.3 最好（L2 未提，补齐）；真机领先 0.7 点为我们按表 3 计算。
- 附录 B.1：真机校准集只有 12–14 个成功回合，LTT 无法认证，表 7 只覆盖 LIBERO-X。

收录：被监控对象是冻结 VLA，环里没有 LLM/VLM harness；按 EVIDENCE B 类“成功/失败检测器”收录（selection-011 已作此判定）。价值在于为 harness 的交还与门控提供可校准的触发信号；画报题签写明“冻结 VLA，无 LLM 在环”。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 探针结构、6.6M 参数、取 π0.5 第 18 层 / GR00T-N1.7 第 16 层 | §4.1 |
| 已有方法多只校准 FPR、多不按出错时刻评 | §1 |
| LTT 同时认证 FPR ≤ α 与 TPR_early ≥ β，δ=0.1 | §4.2、§6.2、附录 A.3 |
| 出错时刻定义（沿用 Gu 等 2025） | §3.1、附录 B.2 |
| 四种标注策略；出错前全段最好，出错后标正例最差 | §4.1、附录 D.4 表 9 |
| 第 ② 区阶梯与表格 | 附录 D.1 表 7 |
| MC 在见过任务上误报兑现 57–71% | §6.2、表 7 |
| 第 ③ 区六组面积 | 表 3 |
| 新组合 +14%、新技能 +30%（相对 SAFE-LSTM） | §6.1 |
| 后移出错时刻时真机 SAFE-LSTM 反超 | 附录 D.4、表 11 |
| 前三类命中最多比多数类高 44% | Abstract、§6.3 |
| 训练 6.8 s、校准 <2 ms、0.12 ms / 0.9 ms、54 ms、400 ms | §6.4 |
| 3,180 条标注回合；真机 8 任务 399 回合、Kinova＋GR00T | Abstract、附录 B.1 |
| 纠偏为启发式演示、未评估；设想由专家模型（如 VLM）调用恢复工具 | §6.5、§7 |
| Gemini 3.5 Flash 标注 | §5、附录 B.2 |
| 真机校准集 12–14 个成功、LTT 无法认证 | 附录 B.1、D.1 |
