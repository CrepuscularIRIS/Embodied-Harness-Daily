---
# 机器可读字段：CI 会校验这些 key 是否存在、取值是否在枚举内
id: slug-lowercase
title: "Full Paper Title"
authors: "First Author et al."
first_seen: YYYY-MM-DD          # arXiv v1 / OpenReview 首次公开日期
arxiv: "XXXX.XXXXXvN"           # 本卡实际读的版本；无则 null
openreview: null                # forum URL；无则 null
code: "https://github.com/owner/repo"   # 官方仓库；无则 null
code_commit: null               # 核查时的 SHA；未核查则 null
license: null                   # 仓库 LICENSE 原文类型；未确认则 null
venue: "arXiv preprint"         # 或 "ICLR 2027 submission" 等
tier: A                         # A=具身 harness / 学生训练 / harness 内 RL / harness 自我优化方法；B=benchmark、评测方法学、安全研究等直接贡献（见 docs/EVIDENCE.md）
platforms: [manipulation]       # 子集：manipulation|navigation|aerial|humanoid|mobile_manipulation|driving|general
components: [code_primitives]   # 子集：interface|perception_tools|code_primitives|learned_tools|verification|execution_control|memory|skills|harness_optimization|teacher_distillation|onpolicy_correction|rl|evaluation|safety|efficiency|multi_agent
evidence_level: offline         # offline|online|transfer —— 我们判定的、有证据支持的最高级
held_out: unclear               # yes|partial|no|unclear —— 评测任务/场景/本体是否与设计 harness、合成技能、建记忆、采教师数据、harness 搜索所用的隔离
budget_matched: unclear         # yes|partial|no|unclear —— 与基线的比较是否预算对等
leakage_risk: unclear           # low|medium|high|unclear
code_status: released           # none|announced|released|verified_run
checked: YYYY-MM-DD
---

## 一句话
它改了模型与本体之间 harness 的哪一部分（或学生 / 训练闭环的哪一部分），属于哪个模式卡（`Kxxx`），用什么证据支撑。

## 机制
本体与仿真/真机、模型观测到什么、通过 harness 调用什么（感知工具、代码原语、技能 / VLA 工具）、验证与执行控制、记忆、
学生训练或 RL 的信号，各一两句（只写论文涉及的部分）。如果有学习型成功检测器、停止检查器、VLM judge、reward model
或代替真实世界的模拟器，指出它在 agent 与真值之间的位置。

## 作者报告的证据
只转述作者的数字，并写清模型、任务与划分、闭环还是开环、仿真还是真机、每任务试验次数、交互预算。不跨论文比较数值。

## 我们的诊断
- **证据等级**：为什么是 offline / online / transfer（定义见 [docs/EVIDENCE.md](../docs/EVIDENCE.md)）。
- **留出与泄漏**：设计 harness、合成技能、建记忆、采教师数据或做 harness 搜索用了哪些任务/场景/物体，评测又在哪些上；
  特权信息（仿真状态、真值位姿）是否在评测时对系统可见。
- **验证器**：成功率若由学习型成功检测器、VLM judge、reward model 或代理模拟器判定，它是否对照模拟器真值、人工标注或真机试验校验过。
- **基线与预算**：是否有同一骨干换 harness 的对照、教师 / 未训练学生 / 蒸馏学生在同一 harness 下的对照；调用次数、步数、
  token、时长是否对等；失败或超时的回合怎么计。
- **最强的反驳**：一个最可能推翻主要结论的理由。

## 代码核查
读了哪些文件（固定 SHA）、确认了什么、没确认什么。没跑就写"未运行"。

## 相对已有工作的增量
和哪 1–3 篇最接近的工作比，真正新的部分是什么。

## 适合 / 不适合
谁今天能用它、接入代价是什么（需要哪些原语、传感器、特权信息、模拟器）；什么场景不该用。

## 一个值得验证的问题
一个具体、可检验的后续研究问题。

## 来源
- 论文链接（含版本）
- 代码链接（含 SHA）
