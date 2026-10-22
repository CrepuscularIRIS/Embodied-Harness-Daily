# embodied-v3 — Embodied-Harness-Daily

权重：G=15、M=20、X=20、E=45。当前仓库已迁至 `/home/lingxufeng/Embodied-Harness-Daily`，原目录名 `embodied-harness-radar` 不再作为本次定位依据。正式范围以仓库 `docs/EVIDENCE.md` 为准。

核心问题：**模型经由什么 harness 控制什么本体，成败怎样判定，改进来自 harness、策略还是额外预算/特权信息？**

收录 LLM/VLM/coding agent 经工具、感知/控制原语、冻结技能/VLA、记忆、验证与执行控制组成的具身 harness；也包括 harness 教师到学生的蒸馏、纠正、相关 RL、自我优化和评测。无 harness/教师关系的纯 VLA 不自动纳入；GUI 和非具身 RSI 分流。

| 轴 | 本领域的具体判断 |
|---|---|
| G | 具身感知、技能调用、闭环控制、停止/完成判断或学生训练的哪项瓶颈？明确本体和部署条件。 |
| M | 改动在 planner、tool、executor、verifier、memory、教师数据还是优化环？该操作怎样回应瓶颈？ |
| X | 训练与部署接口、teacher/student 信息权限、监控、hand-back 或技能前提是否说清？不对无关论文强求所有组件。 |
| E | 闭环/真机试验有没有任务和次数分母？同模型、任务和预算是否可比？教师特权、学生增益和验证器误差能否区分？ |

教师/学生论文按训练及部署的中心主张评价，不能把教师特权条件的成功算作学生部署能力。仿真和真机结果分别陈述，少量定性演示不能替代有分母的成功率。

证据等级沿用 offline / online / transfer，材料不够则 unknown；不因标题 generalist 或 sim-to-real 就直接判 transfer。可靠的负结果、安全/评测审计也可入选。

可按机制查现有领域卡：

- `patterns/main/external_verification_control.md`：外部验证与执行控制。
- `patterns/main/privileged_teacher_supervision.md`：特权教师监督。
- `patterns/main/learner_state_teacher_correction.md`：基于学生状态的教师纠正。
- `patterns/main/harness_effect_evaluation.md`：隔离 harness 的实际效果。

不要求每篇都是 RSI 式自我改进；只有论文声称留存收益时才检查选择、保存和后续使用链。
