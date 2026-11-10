# SOURCE · 2611.08914

- 论文：HomeLoop: A Simulation Framework and Benchmark for Robot–IoT Coordination in Everyday Domestic Assistance and Safety，arXiv **2611.08914v1**（2026-11-06；Ramy ElMallah、Marc Bishara、Hyegang Kim、Yuxi Zhang 等，多伦多大学）。arXiv 仅 v1（export API 2026-11-10 查询）。
- 阅读原文：钉定缓存 `research/fulltext/2611.08914.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §2 与全部附录，§1/§3.9/§6.9 段尾截断）。§2 相关工作、截断段落与附录 A–G 补读自同版本 arXiv HTML `https://arxiv.org/html/2611.08914v1`（2026-11-10 取得，转换稿仅在 /tmp，不提交）。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-11.jsonl`（L2，P3 / confirmed / to_l3；F2,F4；judgment；主卡 external_verification_control / observe_act_interface）。入选：`selections/selection-012.md` #1。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-11-10）

通过，无 correction。L2 facts 与原文一致：六 VLM、20 任务、每模型 40 回合；Astra 族均衡分 61.9%、原始 24/40；19/20 任务两种子世界相同；推理时世界暂停；跨屋单模型 174 对，重加权 60.3 vs 42.0。L2 所记 GT 感知、脚本故障、延迟回放只作敏感性、成本权重为规范选择，均成立。

补读后的展示取舍（不改判断）：
- 标题“错做 42、漏做 16”取表 4 合计；一回合可同时计入两列，画报注明。
- “起火约 170 s”出自 §2（HAZARD 对比段）；“60 L ≈ 90 s”是我们按 §3.5 的 40 L/min 与附录 D 表 14 的 60 L 上限换算，画报标“我们计算”。
- §6.9 补读到：Gemma 在十栋别的房子里错做干预 15 次（主房屋 0 次），8 栋里 7 栋在住户做饭时关炉。因此“错做多于漏做”依赖模型与房屋，写入限制栏第 6 条（我们的读法）。
- 服务消融的“可行路线”为作者从检查项推导、未执行（附录 C），画报注明。

收录：EVIDENCE B 类（benchmark / 安全评测），被测对象就是 VLM 代理 harness（七个服务的原生工具调用控制机器人与联网设备）。全部仿真。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 框架组成、20 类设备、2,100 户型、五种本体 | Abstract、§3.1–3.6 |
| 警报只含类型 / 时间 / 来源设备；代理看不到检查、原因、故障、预算 | §3.4、§3.9 |
| 四个烟警任务的处置与检查名；按时限末或停手时判分 | 表 2、§4.2、附录 D 表 14 |
| 有限迹 LTL 检查（always / ever / never） | §4.2 |
| 第 ② 区错做 / 漏做 / 失败数 | 表 4 |
| 通过数（种子 0, 1）与族均衡分 | 表 3 |
| Gemma 20 次应叫急救只叫 1 次、从未关真漏水 | §6.2 |
| 第 ③ 区 6 真 / 8 良性干预数、仿真中位时间、推理耗时中位 | 表 5 |
| 40 次命令 39 次在任何图像之前；Astra 0.4–0.6 s 关炉、约 15 s 后认出住户 | §6.2–6.3 |
| 延迟回放只改变 1 个结局（Qwen 漏水超 60 L） | §6.3 |
| 起火约 170 s | §2 |
| 关图像 12→9、11→8；叫急救给熟睡住户 | 表 8、§6.6 |
| 显示价格 12→10、11→10；“最划算的选项” | 表 7、§6.5 |
| 无室内摄像头两模型都没过门铃误报 | 表 6、§6.4、附录 C |
| 十栋房子 60.3%→42.0%、错做 0→15、7/8 栋关炉 | 表 10、§6.9 |
| 限制 1–5 | §5、§7 Limitations |
