# 精选 Reel

2026-10-22，现有 Reel 和选题已撤下并保存在仓库外。当前没有可发布的新版成品。

新的 Reel 仅来自按领域 pattern 判据评分后入选、经 Opus 5.5 原文核对并完成实际视觉 QA 的论文。每期默认最多 9 篇，不为凑数制作。

## 本期 s001（embodied-full-v11-20261022，problem-core-v1.1）

| paper | 画报主题 | 版式 | 成品 |
|---|---|---|---|
| 2610.27350 | 动作时不再拒绝——安全诊断 | 双栏对照 | ✅ ready（QA passed） |
| 2411.04549 | GVL 验证信号——进度分数在测什么 | 消融对比 | ✅ ready（QA passed） |
| 2610.25114 | 自我改进收益拆解 | 收益成分拆解 | ✅ ready（QA passed） |
| 2510.20328 | MemER 该记什么 | 条件矩阵 | ✅ ready（QA passed） |
| 2610.15572 | AIDA 教师导航行为阶梯 | 递进阶梯 | ✅ ready（QA passed） |
| 2506.17811 | RoboMonkey 采样-验证-选择 | 流水线 | ✅ ready（QA passed） |
| 2311.13373 | 会犯错的 LLM 教师 | 阶段曲线 | ✅ ready（QA passed） |
| 2411.00081 | PARTNR 人机合作反直觉 | 网格+数据条 | ✅ ready（QA passed） |
| 2602.15875 | Fly0 只换目标接口 | 分层栈 | ✅ ready（QA passed） |

- 选择：91 篇 P3-confirmed 候选 → 同题去重 22 + 多样性截断 60 → 9 篇（选择记录见 run selections/selection-001.md）
- 制作与核对：Opus 5.5 逐篇原文核对（3 处展示缩窄记于各篇 SOURCE.md，无判断错误退回）、视觉 QA 实开渲染图
- `poster.html` 可编辑源被 .gitignore:193 忽略，保留本地；正式发布时按精确路径放行
- 数字与断言映射：各篇 SOURCE.md（节/表定位）