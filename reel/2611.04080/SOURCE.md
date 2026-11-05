# SOURCE · 2611.04080

- 论文：FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation，arXiv **2611.04080v1**（2026-11-02；Agarwal、Shen、Chintalapudi 等 9 人）
- 阅读原文：钉定缓存 `research/fulltext/2611.04080.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §2 相关工作、§3.4.3 尾段与附录）。全文含 §2、§3.4.3 与附录 A–B（含 Table 4）补读自同版本 arXiv HTML `https://arxiv.org/html/2611.04080v1`（2026-11-04 取得，转换稿仅在 /tmp，不提交）。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-08.jsonl`（L2，P3 / confirmed / to_l3；F4,F2；capability）；入选：`selections/selection-008.md` #1。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-11-04）

通过，无 correction。L2 facts（103 查询 Fido 94.2 / TextMap 68.0 / find_objects 47.6；29.5 s·3.1¢ 对 8.5 s·1.4¢；20 次失败重放 9/6/2；Spot 35/50、17 次恢复后成功、15 次失败中 13 物理技能）与原文一致。

L2 因缓存裁剪未见附录 B Table 4：把整份扫描逐帧交给独立 VLM，Gemini 3.8 Flash 精确匹配 96.1%（16.7 s、3.2¢）、GPT-6 Astra 93.2%，均与 Fido 相当或更高；作者自称两者是同一类方法。这一材料**加强**了 Q1（指令后回看原始帧胜过预建表示），不改变档位；但削弱“Fido 代理流程带来准确率”的读法。画报按此缩窄：结论只到“路线”，并在正文和限制栏写出 Table 4。

其他展示缩窄：真机无基线；闸门消融样本 5–20 且条件互异；裁判只在已失败样本上评估；静态场景假设；RB-Y1 仅演示。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 预建表示在指令前把场景压成嵌入或描述，缺任务属性 | §1 ¶3–4；§2 Semantic scene representations |
| 初始带位姿 RGB-D 扫描、机器人已定位、场景只被机器人改变 | §3.1 |
| find_objects：SAM 3 分割、深度反投影、Qwen3-VL-8B 核对、5 cm 体素合并 | 附录 A |
| Fido 拟查询、检视候选、改写重查；输出 id、3D 位置、尺寸、视角 | §3.3 |
| 前提与运动学检查、站位采样与拒绝 | §3.4.1–3.4.2 |
| 独立裁判 Gemini 3.6 Flash，前后两图，success/failure/uncertain | §3.4.3 |
| 103 查询、4 扫描、148 目标、人工判定；各方法 Exact 与耗时、费用 | §4.1 Table 1；附录 B |
| 整扫描 VLM：Gemini 3.8 Flash 96.1、Astra 93.2；Set 85.2 vs 92.6 | 附录 B Table 4 及文字 |
| 查询类型百分比 | Table 1、Table 4 |
| 每类条数 23/20/22/27/11 | **由百分比反推**（所有方法的百分比均整除一致），原文未直接列出 |
| 失败重放 9/20、6/20、2/20；从裁判判失败并人工确认的样本中选 | §4.2.1；Table 2a |
| 采样器 5/5 vs 2/5、5/5 vs 1/5 | §4.2.2；Table 2b |
| 代价工具 +9.8%、+12.3%，p=.039/.020，10 对指令 | §4.2.3；Table 2c |
| Spot 13/16、12/18、10/16；均用时 2.5/4.5/8.7 min；585 技能调用、1,045 工具调用 | §4.3 Table 3 及文字 |
| 18 次一次成功（35−17）、17 次恢复后成功、13 物理技能、2 定位或推理 | 摘要；Fig. 3 说明；§4.3 |
| 25 个任务需推断目标，定位只错 1 次；41% 墙钟时间在 LLM 调用，约 20 次 × 7 s | §4.3 |

## 自绘与示意

- 顶部“两条信息路线”为自绘示意；点图、类型方阵、结局条由原表重绘。未使用原文图片。
- 未运行论文代码，未复现实验。
