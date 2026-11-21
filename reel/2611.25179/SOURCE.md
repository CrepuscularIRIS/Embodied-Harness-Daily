# 2611.25179 SimAudit — 数字与断言映射

- 论文：*Phantom Success, Silent Failure: SimAudit — Auditing Success Checkers in Robot Manipulation Benchmarks*，arXiv 2611.25179v1（2026-11-18）。全文缓存 `research/fulltext/2611.25179.txt`。
- L2 记录：`research/scoring/runs/embodied-rolling-20261023-01/batches/inc-l2-19.jsonl`（P3/confirmed/to_l3，capability，main/external_verification_control）。核对无判断错误，correction 0。

## 断言 → 原文映射

| 画报断言 | 原文位置 |
|---|---|
| 3 基准 142 任务、568 候选状态、183 预测命中、61 缺陷/49 任务 | §1 贡献段；§4.2 表1（Defects 61，Tasks with a defect 49） |
| 40 幻影成功 / 21 静默失败 | §1；§4.2 表1 "By direction of the error" |
| 分基准：RoboTwin 20幻+11静、RoboCasa 17幻+1静、RoboDojo 3幻+9静 | §4.2 表1 |
| 五因：proxy 16 / missing 17 / unstated 15 / loose 10 / transient 3 | §4.2 表1 "By primary cause" |
| 缺条件/宽松几何/瞬时即判全部产生幻影成功；多余要求全部静默失败；代理信号双向（10幻/6静） | §4.2 末段 "The cause of a defect fixes its direction" |
| RoboTwin 主因代理信号（读 commanded gripper 而非手指状态）；RoboCasa 多记（吸管横搭杯沿算入杯）；RoboDojo 少记（静默全是多余要求） | §4.2 表1 后三段 |
| "仿真成功率虚高"对 RoboDojo 是反的 | §4.2 "holds for RoboCasa365, holds in part for RoboTwin 2.0, and is reversed for RoboDojo" |
| 管线 Read（指令/代码分开描述防污染）→ Guess（≤4 假设）→ Stage（probe 用基准自身 motion 构造状态、跑未修改 checker、teleport 悬空/穿模不计）→ Review（未写 probe 的 reviewer 只看指令+多视角帧+判定、四档标注、仅 valid 计入、约 2/3 被拒） | §3.2 四段 |
| 修复三步：测物理状态（gripper 施力而非指令值）、条件对齐指令（补缺/删多余）、要求成功持续 1 秒 | §3.3 |
| Verified checker 放行 1,233 expert episodes + 61 缺陷回归套件 | §3.3 Validation |
| 两位独立标注者确认全部 61 缺陷；50 个被拒候选随机抽查无漏真缺陷 | §4.3 Precision / Effect of the review stage |
| 重评 π₀.₅@RoboTwin 46.2→42.3（Δ−3.9，幻影占原成功 10.2%、静默 1.6%、flip 5.6%） | §4.4 表2 |
| GR00T N1.5(30%)@RoboCasa 37.7→33.8（−3.8，12.2/1.2/5.4） | §4.4 表2 |
| VPP@RoboDojo 30.0→39.1（+9.1，幻影 0、静默占原失败 13.0、flip 9.1） | §4.4 表2 |
| StarVLA(QwenOFT)@RoboDojo 0.9→5.5（+4.5） | §4.4 表2 |
| click bell：π₀.₅ 保不住任何成功（夹爪停在铃上方未接触）；LingBot-VA 全保、X-VLA 95%→20% | §4.4 图4 段与 "The same defect does not affect all policies equally" |
| 三基准排名均不变；RoboCasa 上 GR00T 两档差距拉大（30% 档掉更多）；RoboDojo 上 VPP 逼近领先、甩开 StarVLA(QwenPI)；flip 率可超净变化 | §4.4 末两段 |
| 边界：审计召回无上界（每任务≤4 假设、无缺陷总量 ground truth、被拒候选抽查仅 50 样本）；重评单次无 seed 方差、排名结论弱 | L2 subcard partial 两条（§3/§4.4 对应） |
| 画报示意：五因横条为按表1数值绘制（16/17/15/10/3 比例），非原图 | 自绘（标注"示意"性质于画报脚注可追溯） |

## 展示缩窄

- "判分器验证了专家演示，验证不了策略会走到哪"（页脚）为我们的读法，依据 §1 "Expert demonstrations can establish that a success checker accepts a reference execution… A learned policy can reach states outside those covered by the demonstrations"。
- 重评表只选 5 行（表2 全 16 行），选择覆盖两方向（降/升）与最极端值（X-VLA click bell 95→20 单任务对照）；未展示的行方向一致。
