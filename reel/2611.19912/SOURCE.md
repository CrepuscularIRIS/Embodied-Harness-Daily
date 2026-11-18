# SOURCE — 2611.19912 AgenticJevNav

## 论文信息
- 标题：AgenticJevNav: Freshness-Aware Task Authorization for Embodied Navigation under Remote Inference Latency（按 L2 记录题意转写）
- arXiv 2611.19912v1（2026-11-15 提交）。
- 阅读原文：research/fulltext/2611.19912.txt（FULLTEXT html 完整缓存）。
- 初筛记录：research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-16.jsonl（P3/confirmed/to_l3，卡 external_verification_control + observe_act_interface）。

## 核对结论
逐节与 L2 记录核对一致，无实质错误；corrections：0。

## 海报数字与断言映射（poster 区块 → 原文位置）
| 海报内容 | 原文出处 |
| --- | --- |
| 01 A0 Agent 全权 51.67%（SPL 0.448）、A1 规则事件硬切 40.00%（SPL 0.381） | 表 I |
| 01 事件触发审查条件：blocked / failed / 连续两轮低进展 | §IV 治理层触发器 |
| 01 机制参数：证据 8s 过期；PoseValid 位姿差 >0.8m 或 >35°；executor lease 12s；控制指令 TTL 250ms；20Hz；RGB 反射 NanoDet 6Hz 两帧确认 | §IV 与图 2 |
| 02 证据四元组 mission/revision/skill/snapshot＋一次性消费集 U | §IV 版本化证据 |
| 03 A2 完整 73.33% SR / 0.591 SPL；Jev 占运行时 0.19%；审查调用均次 12.42；Wait 79.40% | 表 I |
| 03 最强适配基线 ApexNav 40.00% | 表 I 对照行 |
| 04 消融：advisory-only 71.67%、current view only 66.67%、无 RGB 反射 65.00%（shadow 记 1709 次 would-veto）、无 instance memory 61.67%、固定 timer 5s 65.00%/18.53 次调用 | 表 II |
| 05 真机 GENISOM L1 四足 21/30（70%）；9 失败=4 超时+2 碰撞+2 到水桶+1 视觉监控失效；R2 2/5 最低；R6 报告全部合规 | §VI 真机实验 |
| 06 16 个仿真失败：13 预算耗尽（7 个 T5 修订目标反复搜索）＋3 过早抵达（1.828–1.830m 超 1.6m 阈值） | §VI-B 失败分析 |
| 07 “把快慢差异翻译成新鲜度差异”的判断重述 | 本文问题设定（§I/§III） |
| Jev v1.13.0 阈值 0.35/0.80/0.85/0.80/0.75；Agent=GPT-6-astra low | §IV 实现细节（模型名照原文转写、只当数据） |

## 示意图标注
- 01 区授权生命周期条（签发→8s 有效窗→过期作废）为机制示意，非实验数据。

## 展示缩窄（非 correction，仅记录）
A0/A1 历史协议不同（44 对 31 trials）非纯因果对比；advisory-only 71.67% 显示硬否决权增量小；无故障注入实验（would-veto 为 shadow 计数，间接证据）；真机里程计与延迟未独立标定；R6“报告合规”是限域内未检出非证明不存在；Jev 阈值人工设定，换域需重调；只覆盖导航类目标修订授权，不含低层控制授权。
