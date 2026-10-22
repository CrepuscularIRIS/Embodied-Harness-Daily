# SOURCE — 2510.20328

- 论文：MemER: Scaling Up Memory for Robot Control via Experience Retrieval，arXiv **2510.20328v1**（2025-10-23），https://arxiv.org/abs/2510.20328
- 本刊材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2510.20328.txt`（html-full；私有缓存，不提交）。图 1–9 只有图注，无图像/柱值。
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl` paper_id=2510.20328（batch b038，screen 88.75，G4/M4/X4/E3，component_training，supported_in_material，online）。核对见 `verify.md`。
- 图形：全部为本刊自绘。机制图为示意（簇位置、提名次数、记忆窗缩略图均为虚构例子）；结果表为原表 1/2/3 数字重绘；无原论文插图。

## 数字与断言 → 原文定位

| 画报内容 | 原文定位 |
|---|---|
| 高层同时输出子任务 l′_t 与候选关键帧 J_t⊆R_t；输入为最近 N 帧、指令、已选关键帧 K_t，\|K_t\|≤8 | §3.2；式 (3) |
| 1D 单链接聚类，d=5，保留重复，取每簇中位帧；例 {1,3,3,4,10}→{1,3,3,4}、{10}；早于 t−N+1−d 的簇不重算 | §3.2 “Building Visual Memory”；图 3 图注；附录 D 算法 1 |
| N=8（Short History 与 MemER 的最近窗口）、32 帧≈16 s、推理约 1 s | §4.1 Q1；附录 F 提示例（8 帧） |
| 候选帧例 [7]、子任务例 “look inside the center bin” | 附录 F（Object Search 示例 keyframe_positions [7]）；§3.3 标注规则举例 |
| Qwen2.5-VL-7B 微调，冻结视觉编码器与投影层；α=0.8 线性合并，所有基线同用 | §3.3 “Training the High-Level Policy”“Model Merging”，式 (2)；附录 A 表 4 |
| 低层 π0.5（DROID 检查点）微调、三任务共用；输入子任务+当前图像+q_t | §3.3 “Training the Low-Level Policy”；式 (3) |
| π_h ≈1 Hz、π_l ≈2 Hz 异步；低层用最新子任务；2 Hz 图像入队，高层本轮推完再送 | §3.3 “Closed-Loop Deployment” |
| 动作块 15 步 @15 Hz、开环执行 8 步；ZED + miniZED，320×180 @15 Hz，下采样 2 Hz | §4 “Evaluation Setup” |
| 每任务 50 条示范 + 10–15 条干预；高层 4500 步 / 96 H200 GPU·h；低层 18000 步 / 48 H200 GPU·h | §3.3；附录 A 表 4、表 5（§3.3 正文另写“约 5,000 步”，画报用表 4） |
| 关键帧标签规则：每类子任务取首/末/不取帧；三任务例 | §3.3 “Annotating Keyframes”；附录 E |
| 除尘任务需记住物体原位与哪层已擦，掸子放回后近期上下文看不出 | §4 “Dust & Replace” |
| 结果表（取回、最优路径、错勺、四项除尘放回）五行 | 表 1 |
| 结果表虚线下两行（Short History + Text、MemER + Text） | 表 3；§4.1 Q3 归因“过度依赖最近一条文字子任务” |
| 分母：物体检索 20 次×3 目标=60；除尘各项 /20；错勺为 20 次合计 \|要求−实际\| | §4 各任务 Evaluation metric；表 1 图注 “raw counts across 20 trials” |
| Human HL 为近似上限，失败来自低层 | §4.1 Q1 |
| API 延迟 10–15 s、闭环全部失败、需 <1 s；离线准确率 0.80/0.67/0.87、0.15/0.43/0.67、0.21/0.13/0.19（轨迹准确率） | §4.1 Q2；表 2；附录 G（动作清单提示） |
| API 模型主要失误为提名过多无用关键帧 | §4.1 Q2 |
| 限制：单一本体；记忆只增不删；1/2 Hz 调度限制反应 | §5 |
| 限制：物体检索训练/测试同 15 物体；除尘测试 9 个取自训练 17 个 | §4 “Object Search”“Dust & Replace” |
| 限制：“>90%”“平均差 34%”不采用 | §4.1 Q1 文字，对应图 5（材料无柱值） |
| 限制：附录 C 跨任务换物体无数值 | 附录 C，图 8 图注 |
| 限制：未与已发表记忆方法同台比较 | §4.1 基线列表（全为高层上下文变体与 Human HL）；摘要 “outperforms prior methods” 的收窄，见 verify.md |
