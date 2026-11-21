# 2611.26414 ZeroVLN — 数字与断言映射

- 论文：arXiv 2611.26414v1（2026-11-19）。全文缓存 `research/fulltext/2611.26414.txt`。
- L2 记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-19.jsonl`（P3/confirmed/to_l3，capability，main/observe_act_interface + harness_native_rl；partial F0/F3）。核对无判断错误，correction 0。

## 断言 → 原文映射

| 画报断言 | 原文位置 |
|---|---|
| 骨干 Qwen3.6-35B-A3B + 12 层 flow-matching 动作专家（视觉编码器 Qwen3.5-4B） | §3 架构 |
| 语义工具接口 run_action_head(target,where,plan) / turn / stop(reason) 替代几何目标预测；stop 必须给理由 | §3.1 接口定义 |
| SFT 使 12 通用视觉基准 59.47%→≈0（NaVILA/DualVLN 两基线） | 摘要/§4 通用能力保留实验 |
| request-grounded 锚定：brain 冻结在线 rollout 收自身请求，特权语义规划器用 mesh 语义图+训练期几何接地为可达局部目标；execution-prefix 监督只对已执行前 h=4 步算 loss（抗训练-执行失配） | §3.2 |
| 联合 agentic RL：轨迹级 RLOO 优势同更新两策略；奖励=终局成功+首次到达+有界距离进展（proximity potential）+信息发现（新发现深度验证实体），缓解全失败时梯度退化 | §3.3 |
| 表1 受控组（同骨干同 34.4k episodes）：SAGE-3D/R2R/RxR SR 51.3/52.7/51.4（ZeroVLN）vs NaVILA 23.5/46.5/48.7 vs DualVLN 21.2/15.4/17.7 vs Direct Tool 39.5/19.0/10.2 | §4 表1 |
| 已发布 NaVILA-SAGE（500K episodes）46.0 < ZeroVLN 51.3（1/14 数据） | §4 跨发布对照 |
| 权重位移 0.01497% vs DualVLN 3.21% / NaVILA 7.67% | §4 权重位移分析 |
| ZeroVLN 训练后 12 基准 59.16%（底座 59.47%） | §4 保留实验 |
| 强制 Answer: 前缀直接读选项 token 概率：NaVILA/DualVLN≈随机，ZeroVLN 62.00 vs 底座 62.86——损伤在参数层非指令遵循 | §4 探针实验 |
| OSR 66.7/64.6 更高（vs 51.8/55.6）但 SPL 29.2/28.1 更低（vs 41.8/43.0）——探索恢复换路径效率 | §4 权衡 |
| 消融：只训 expert 无提升；只训 brain 先升后降（请求-专家失配）；轨迹级 RLOO 优于 round 级（到达即奖励致 SR 降）；去 first-arrival 严重退化 | §4/§5 消融 |
| 边界：全部对比在单一 backbone；接口收益是否随骨干变化未验证；token/延迟成本未报 | L2 partial（F0/F3）；§6 局限 |
| 画报示意：天平双盘、权重位移 track 上的 pin 位置为示意自绘（比例按 0.015/3.21/7.67 相对摆位） | 自绘 |

## 展示缩窄

- 表1 只列 SR 三列与权重位移；OSR/SPL 放入"代价一"卡片（未列全 6 指标）。
- Direct Tool 权重位移记作"—（0）"（零训练，原文无位移数值）。
- 通用能力保留 12 基准为聚合数字，未逐基准展开。
