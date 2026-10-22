# 问题族映射：Embodied-Harness-Daily

配合 [PROBLEM_CORE.md](PROBLEM_CORE.md) 使用，版本 `problem-core-v1`，初版映射，尚未试点。依据为各主卡“Cognitive barriers”与“Failure modes”两节。本表只用于检索和归组；判断 Q2、Q3 时必须引用卡片原文，不能只引本表。

| 主卡 | 问题族 | 卡片中的锚点要点 |
|---|---|---|
| [code_policy_trial_revision](../../patterns/main/code_policy_trial_revision.md) | F1、F3 | 执行反馈而非视觉评审承载大部分收益；换一个同预算的编码代理即失效 |
| [external_verification_control](../../patterns/main/external_verification_control.md) | F2 | STOP 门控在成功区域外放行，停止仍是主要残余失败 |
| [harness_effect_evaluation](../../patterns/main/harness_effect_evaluation.md) | F1 | 固定模型时 harness 改动的影响大于固定 harness 时模型改动 |
| [harness_memory_skill_reuse](../../patterns/main/harness_memory_skill_reuse.md) | F5 | 累积全部图像会降低成功率，多张历史图像引入陈旧上下文 |
| [harness_native_rl](../../patterns/main/harness_native_rl.md) | F1 | 同一训练方法在不同控制流下收益相反 |
| [harness_self_optimization](../../patterns/main/harness_self_optimization.md) | F1、F3 | 弱接收方自我改进失败，强教师改进才有效；提议代理只测过一种 |
| [learner_state_teacher_correction](../../patterns/main/learner_state_teacher_correction.md) | F2、F5 | 教师数据加倍无明显收益；成功过滤的演示远不如经验证的纠正 |
| [llm_symbolic_solver_planning](../../patterns/main/llm_symbolic_solver_planning.md) | F1、F5 | 强结果中搜索由求解器完成；模糊或单机器人任务上形式层无增益 |
| [multi_robot_llm_coordination](../../patterns/main/multi_robot_llm_coordination.md) | F1、F5 | 协商在外部基准上与已有协调器持平；增加角色反而降低奖励 |
| [observe_act_interface](../../patterns/main/observe_act_interface.md) | F1、F5 | 强制结构帮助弱模型、对强模型中性，但可选工具仍提升最强骨干 |
| [offline_harness_distillation](../../patterns/main/offline_harness_distillation.md) | F1 | 保留 harness 的小学生模型接近教师，去掉规划器则差距拉大 |
| [on_policy_distillation_objectives](../../patterns/main/on_policy_distillation_objectives.md) | F4 | 只用动作级教师信号（argmax 重标注）平台最低且熵坍缩 |
| [planner_composes_code_and_policies](../../patterns/main/planner_composes_code_and_policies.md) | F1、F5 | 组合、持久状态与选择性反馈未分开；规划器叠加在普通 VLA 上反而有害 |
| [privileged_teacher_supervision](../../patterns/main/privileged_teacher_supervision.md) | F3、F4 | 估计专家输入优于像素 BC，但仅限特权是固定状态向量时 |
| [sample_verify_select](../../patterns/main/sample_verify_select.md) | F2、F5 | 换一个已发表的验证器反而低于不验证；多种反思信号不可叠加 |
| [teacher_seeded_sparse_rl](../../patterns/main/teacher_seeded_sparse_rl.md) | F1 | 从零成功率直接 PPO 多数任务仍为 0，BC 初始化的 RL 停滞 |
| [trained_vlm_vla_hierarchy](../../patterns/main/trained_vlm_vla_hierarchy.md) | F1、F5 | 未适配机器人的前沿规划器不如微调的小 VLM；分离纠正器不如联合训练 |
