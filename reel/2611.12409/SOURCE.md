# SOURCE · 2611.12409

- 论文：Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation，arXiv **2611.12409v1**（2026-11-09；Cuzzocrea、Iannotti、Rossini、Laurenzi、Tsagarakis，IIT HHCM / Genoa）。arXiv HTML 仅见 v1（2026-11-11 取得）。
- 阅读原文：钉定缓存 `research/fulltext/2611.12409.txt`（头标 `FULLTEXT: html`、v1；core 裁剪版，缺 §II 与表 III 的完整内容）。§II 相关工作、表 I–IV、参考文献 [19] 补读自同版本 arXiv HTML `https://arxiv.org/html/2611.12409v1`（2026-11-11 取得，转换稿只放在 /tmp，不提交）。论文没有附录。
- 初筛记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-12.jsonl`（L2，P3 / confirmed / to_l3；F2,F0；capability；主卡 external_verification_control / planner_composes_code_and_policies）。入选：`selections/selection-013.md` #2。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-11-11）

通过，无 correction。L2 facts 与原文一致：CENTAURO 真机九场景各 20 次、同一初始布置；箱子并排 / 易碎箱 / 长程三个场景，无执行意识 0%，加执行意识后 85 / 70 / 50%；抓瓶失败的恢复查询 3 → 1.1、每回合 10 → 8.1；GPT-5.2 骨干 5%。L2 Q4=fits（同骨干三配置分层对照）成立。

补读后的展示取舍（不改判断）：
- L2 写“缺 TableIII 完整表、validator 误报漏报”。完整表 III 其实有模块列，验证模块每次调用的“正确”比例为 89–100%，但原文没说明正确与否由谁判定，也没有把误报和漏报分开。L2 判断的实质（验证器没有误报/漏报审计）仍然成立，画报第 05 区如实写出这个数字及其局限。缺口来自缓存裁剪，不退回。
- 参考文献 [19] 是同一作者在 ICRA 2026 研讨会上的前作 “Execution-aware task planning for language-conditioned bimanual manipulation”，可以确认是同一研究的早期版本。按 PROBLEM_CORE Q2，本文的各个版本不用于判定 prior_solved；L2 保守处理是对的。画报限制栏写明“执行意识规划”已在前作发表，本文的新增部分是分级验证与恢复。
- 分级验证对成功率的额外贡献较小（75→85、35→50、85→95，其余持平），主要收益是少用查询；画报照此写，不把 0→85 记在验证器名下。
- 并行调度的 40% / 11% 节省是单次示例，而且只计机械臂运动（§IV-B3），画报写明。
- 第 01 区的场景图是我们依据 §III-B/C 与图 4 画的示意（图 4 的易碎箱是“蓝绿压在白箱上”，示意改成并排，用来说明侧面阻挡），已标“示意，重绘”。

收录：EVIDENCE A 类。VLM（Gemini Robotics-ER 1.6）在环负责感知、规划、调度与验证，调用抓、放、推等原语，在真机双臂上闭环执行。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 六个面标上空间与 IK 可达性、记录挡住它的物体；夹持需要一对相对的面；挪开距离用同一间隙阈值 | §III-A、§III-B、§III-C |
| CAD＋FoundationPose 估 6D 位姿；VLM 给出符号关系 | §III-B |
| 三值验证、不确定时重建场景图、读前后场景图与尝试历史；repeat / modify / replan 分别花 1 / 2 / 3 次查询 | §III-E；表 II；图 5 图注 |
| 恢复决策平均查询 1.1 / 1.5 / 2.0 / 2.1 / 2.8 / 2.8，二值验证器总是 3 | 图 5 |
| 抓瓶失败 10 → 8.1、推动失败 10 → 9.1 | §IV-B1；表 III |
| 九场景三配置成功率与本文配置的查询数 | 表 III |
| 堆叠箱三者都 100%；并排时直接抓、20 次全失败 | §IV-B1 |
| 三配置共用骨干、指令、原语、低层 | §IV-B 开头 |
| 骨干对比 73.3% / 41.9 s、80.0% / 91.4 s、5.0% / 34.6 s；GPT-5.2 败在规划 | 表 IV；§IV-B4 |
| 规划时延 5.79–31.78 s、长程规划正确率 67%、验证正确率 89–100% | 表 III 模块列；§IV-B2 |
| 并行：60→36 s、108→96 s，单次示例、只计运动 | 图 6；§IV-B3 |
| 长方体近似、基座固定、同一初始布置 | §III-A；§IV-A；§V |
| 前作 [19] | §I；参考文献 [19] |
