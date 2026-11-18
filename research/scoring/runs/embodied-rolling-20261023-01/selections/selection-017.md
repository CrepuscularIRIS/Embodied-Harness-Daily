# selection-017 — 论文雷达日班（rolling 增量第十七期）

- 执行模型：glm-5.3（单席，用户 2026-11-17 指示）
- 日期：2026-11-18
- 候选池：inc-l2-16 的 5 篇 P3/confirmed/to_l3（全部未消费）
- 结果：入选 3、发布 3、fail 0；ready 51 → 54
- corrections：0

## 候选表

| paper | Q3 判断 | 族/卡 | 决定 |
|---|---|---|---|
| 2611.19081 RoboCoEvo | capability（q2_open=open_failure；已核对 ESI 2611.18176 §3–6，不判 prior_solved） | harness_self_optimization + learner_state_teacher_correction | 让位：同卡覆盖。learner_state_teacher_correction 卡已有六张 ready（TILDE 2610.25376、2611.16246、2610.25114、2610.15572、2311.13373、2611.08318），上期 2611.18176 ESI 与 2611.17394 Agentic-Teacher 均因此让位；本期机制仍为“失败驱动程序改写→DAgger 式回灌”的教师-学生自改进主线，与在库重复压力最大的候选 |
| 2611.19198 Self-Calibrating VAA | capability（open_failure） | observe_act_interface + harness_effect_evaluation | 入选并发布。跨单元自标定命令-几何映射：任务前动一动、看指尖，量出 J/K/[R|t]/k₁ 再抓，18 换爪/转架单元 64%→74%、最强 VLA 21%；与在库 2611.01560（换 harness 提同模型）同向但对象不同（本篇不换模型、换单元），无同卡机制重复 |
| 2611.19912 AgenticJevNav | capability（open_failure，constraint_conflict） | external_verification_control + observe_act_interface | 入选并发布。远程推理延迟下的授权新鲜度与版本化证据：事件触发审查＋8s 请求年龄＋一次性消费，51.7%→73.3%、真机四足 21/30；“验证还成立吗”在 L2 卡上是新增失效模式视角，与现有 ready 无重复 |
| 2611.19952 CRAFT | judgment（open_failure） | harness_memory_skill_reuse + external_verification_control | 让位：记忆槽历史饱和。harness_memory_skill_reuse 主题在库已多（MemER/LogLook 在库；HeLM/06475/09355/11509/38318/33487 均以记忆槽饱和让位）；诊断强（受控决策实验、分层收益归因清楚），列备选 |
| 2611.21099 ForceHarness | capability（new_bottleneck，constraint_conflict 补 measured_own） | observe_act_interface + external_verification_control | 入选并发布。API-only 冻结前沿模型的力闭环：力标定＋12 自终止导抗原语＋物理翻译，真机 3.3%→90%、HiddenPhys 135/140 与专家同水平；“接触快于决策→闭环下沉非模型层”是 observe_act_interface 卡的速度差实测注脚；与现有 ready 无同卡机制重复 |

## 原文核对

五篇全部读取全文缓存（research/fulltext/2611.{19081,19198,19912,19952,21099}.txt），逐节核对 L2 记录（batches/inc-l2-16.jsonl）的问题判断、数字与机制描述。

| paper | 核对结论 |
|---|---|
| 2611.19081 | 一致。核心数字（表 1/2/3/4：检测 0.97→Reused 0.54→Revised 0.96 等、消融 0.633/0.425→0.84/0.58、261M tokens/36 GPUh）与机制链核对无误 |
| 2611.19198 | 一致。表 I/II/III、链任务 54/60、92 失败分解、Robotiq 弧爪 0/20 边界外均核对无误 |
| 2611.19912 | 一致。表 I/II、真机 21/30 与 9 失败分解、16 失败分析（3 premature＋13 budget-ended）均核对无误 |
| 2611.19952 | 一致。表 1/2/3（Ladder +0.074 [0.042,0.108] 等、RQ4 换规则 0.298 vs 0.317）、scope ladder 机制均核对无误 |
| 2611.21099 | 一致。表 3/4/5/6（2/60→54/60、87.5、135/140、decision 0.85 p=0.023）与三层机制均核对无误 |

## Corrections

None（0）。五篇 L2 记录未发现实质错误。

非 correction 的展示缩窄（记入各篇 SOURCE.md）：19081 Table1 round2 换 detector 跨轮 FM 率不同尺度、缺多 seed、消融仅一任务、无真机、261M tokens 不含开发测试 GPUh（本篇让位未制 Reel，缩窄记录于此）；19198 全仿真、微调开发污染、开发格非留出、捆绑包非因果、RGB 传感器差、单 seed、链任务挑选；19912 A0/A1 协议差、advisory 增量小、无故障注入、真机未标定、R6 限域；19952 offline 受控实验、Popper seed 未控、集成 pilot 无统计功效（让位未制 Reel）；21099 ForceBench 调参泄漏、evaluator 缺检查、instructions 过程性提示、damage 非完备、baseline 非同 guard。

## 制作与 QA

三张均中文、版式各异，渲染用仓库既有工具链（google-chrome headless PNG 2400×3400＋单页 PDF）。视觉 QA 实开渲染图检查（几何注入脚本＋read_image 整图与放大目检）。

| paper | 首检问题 | 重做（各一次） | 终版 |
|---|---|---|---|
| 2611.19198 | h1 两行实际高度 92px 超 clientHeight 84px（overflow 下裁下缘） | 字号 32→31、行高 1.32→1.30、加 padding-bottom | BADCOUNT=0，目检过 |
| 2611.19912 | 几何 0 违规但内容只到 2515/3400（fill 74%），底部空白 442 CSS px，视觉不平衡 | 全局放大 22 处（h1 34px、正文 14–15px、区块 padding 等） | BADCOUNT=0，fill 91.3%，目检过 |
| 2611.21099 | 02 区三卡横排导致 .col/.sec/.pr 三层横向文本溢出（sw 667/cw 557） | .pr 三列改单列纵排，字号微调 | BADCOUNT=0，fill 90.4%，目检过 |

## 失败稿

无。本期三张重做后均通过，0 fail。

## 交付物

- reel/2611.19198/：poster.pdf、poster.png、SOURCE.md、QA.md（poster.html 留本地，.gitignore 规则）
- reel/2611.19912/：同上
- reel/2611.21099/：同上
- reel/README.md：表格 +3 行、头部 ready 51→54、历史账本 +1 条
- README.md：漏斗行追加 selection-017，总数 51→54
