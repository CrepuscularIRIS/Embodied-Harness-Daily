# 收录范围与证据等级

## 收录范围

**具身智能体 harness（Embodied Agent Harness）**：把前沿 LLM / VLM（包括 coding agent）包在一层 harness 里——接口与动作调用、感知与控制原语工具、作为工具调用的冻结 VLA / 技能 / 学习型策略、记忆、验证与反馈、执行控制——去控制具身系统（机械臂操作、导航 / VLN、无人机、人形机器人、移动操作），在仿真或真实世界中完成任务；以及：

- harness 本身：接口与观测设计、感知工具、代码调用原语、技能库、验证器与监控、交还（hand-back）、记忆；
- 学生训练：用 harness 或教师轨迹训练小型 VLM / VLA 学生（SFT、on-policy 蒸馏、DAgger 式或首错纠正）；
- harness 内的 RL，或面向在 harness 中运行的策略的教师引导 RL；
- 具身场景下的 harness 自我优化、技能库 / playbook 演化；
- 评测：benchmark、环境、评测方法学与安全研究。

- **A 类**：论文提出新的 harness / agent loop、学生训练方法、harness 内 RL 或 harness 自我优化，并在闭环环境中验证。
- **B 类**：可直接用于这类系统的贡献，例如 benchmark / 环境 / gym、评测方法学或对照实验研究、LLM 控制机器人的安全研究、成功检测器、数据集或工具。
- **不收录**：
  - 没有 harness、agent loop、也不做教师-harness 蒸馏的纯 VLA / visuomotor 策略；
  - 没有具身对象的 GUI、浏览器、computer-use agent（见姊妹项目 CUA Radar）；
  - 非具身的 harness / scaffold 自我改进、没有具身对象的 coding agent RL（见姊妹项目 HarnessRSI Daily）；
  - 只顺带提到机器人的通用 LLM / VLM 工作、没有闭环交互的通用 VLM benchmark；
  - 线束（wire / cable harness）、测试框架（test harness）等同名不同义的工作。

## 证据等级

| 等级 | 需要的证据 |
|---|---|
| `offline` | 只有开环 / 静态的动作准确率、计划文本评分、轨迹回放，或定性演示 |
| `online` | 闭环、由执行结果判定成功：在模拟器中按环境检查成功（LIBERO、RoboTwin、BEHAVIOR、VLN-CE、ObjectNav、AirSim 等），或真机试验并给出每个任务的试验次数与成功率 |
| `transfer` | 在构建 harness、技能、记忆或教师数据时未使用过的本体、模拟器或场景集上取得闭环成功；或 sim-to-real 并给出真机试验次数；或跨 ≥2 个本体 / 任务族（如操作与导航、机械臂与无人机）取得闭环成功 |

判定规则：

1. **按证据判，不按自称判。** 论文自称 "general-purpose" 或 "embodiment-agnostic" 不等于 `transfer`；演示视频不是计数的试验。
2. **开发用过的任务不能当留出集。** 设计 harness、合成技能、构建记忆或 replay card、采集教师数据、做 harness 搜索时用过哪些任务、场景或物体，在这些上的提升最高只能判为 `online`。
3. **学习型验证器要单独审计。** 如果成功率是由学习型成功检测器、停止 / 完成检查器、VLM judge、reward model、接受门控，或代替真实世界的模拟器判定的，必须看它是否对照模拟器真值、人工标注或真机试验校验过。
4. **作者自称与我们的判定分开写。** frontmatter 里的 `evidence_level` 是我们的判定。
