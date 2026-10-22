# SOURCE — 2609.34412

- 论文：From Language to Task Maps: Compiling Semantic Relations While Preserving Task-Relevant Freedom，arXiv **2609.34412v1**（2026-09-28），https://arxiv.org/abs/2609.34412
- 阅读材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2609.34412.txt`（html-full 全文缓存，私有，不提交）。图 1–3 仅有图注，画报中无原论文插图。
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl` paper_id=2609.34412（batch b045，screen_score 88.75，supported_in_material / online）；入选见 `reel/selection-opus.md` C2。核对见 `verify.md`。
- 未运行论文代码；所有数字为作者报告值。

## 数字 / 断言 → 原文定位

| 画报位置 | 内容 | 原文 |
|---|---|---|
| 标题副句 | 定性关系只约束部分相对位形，展开成完整位姿会引入非预期约束、产生表示性冲突 | 摘要；§I 第 2–3 段 |
| 问题三联（示意） | 线平行 dim 𝓑=2，只看方向，平移与绕轴转动保留；线重合 dim 𝓑=4，轴向平移与自旋保留；“线重合给插入留轴向平移” | 表 II；§I“line coincidence leaves axial translation available to an insertion policy” |
| 问题第三格（示意） | 完整位姿目标锁住未指定自由度 → 冲突 | §I“Replacing such relation-specific objectives with full-pose targets constrains freedoms…” |
| 左栏 JSON（示意） | ALN red.bottom↔yellow.top，plane coincidence；carry={RA,ALN}，seat={ALN,EC}；RA/EC 绑定原文未给，标“绑定略” | §III-A 堆叠例 |
| 左栏“U 无 / 不写” | 𝒰 仅含用户说出的距离角度；抓取位姿、IK 分支、碰撞间隙、控制器度量在落地/执行期解析 | §III-A，式 (1) 后与式 (2) 后段落 |
| 左栏 E1 条形 | 共享语义 41/60 vs 41/60；关键接口错误 19/60 vs 58/60 | 表 III，§IV-B2 |
| 左栏 E1 条件 | 120 次调用，gpt-5.6-sol，180 s，无种子/温度；oracle 预先固定；3 次超时计入分母；非能力差异；非闭环成功率 | §IV-B1；§IV-B2 |
| 中脊 | 类型校验，非法规格产生诊断而非任意目标位姿 | §III-A“invalid specifications are rejected with diagnostics… rather than an arbitrary target pose” |
| 右栏步骤 1 | 平面重合：法向＋有符号间隙残差，d*=0，保留平面内位姿，dim 𝓑=3；C_type 不产生数值 | 表 II；§III-A |
| 右栏步骤 2 | C_ground：𝒦、标定机器人模型、q0/o0 → X_s⁰, X_r⁰, z_γ | 式 (2) |
| 右栏步骤 3 | x_γ = coeff_I(N(O(X̂_s, X̂_r)))；残差与 Jacobian 同一映射求导 | 式 (7)；§III-C |
| 右栏平面图（示意） | 同一对平面：法向对齐 dim 2（平移、绕法向转动等价），平面重合 dim 3 | §III-B 堆叠例 |
| 右栏步骤 4 | J_γ v=0 ⇒ vᵀJᵀMJv=0，拉回后不加权 | 式 (9)、(10) |
| 右栏 E2 卡 | 8 形式×8 构型=64；阈值 1e-8 / 1e-6；秩与 dim 𝓑 一致；仅局部 | §IV-C1，表 IV |
| 结果条形图（据表 V 重绘） | 关系 2.91[2.90,17.68] / 锁 65.67[59.74,87.68]；4.57[4.44,4.63] / 75.58[75.38,75.75]；0.95[0.92,0.96] / 21.19[21.19,21.20]（mm，中位数[最小,最大]） | 表 V |
| 结果增量 | +62.76 / +71.00 / +20.24 mm | §IV-C2 正文。注：按表 V 中位数相减 Cutting 得 71.01，采用原文 71.00 |
| 任务名对应 | Align–insert=螺母插入；Align–traverse=切割；方向对齐–进度=堆叠搬运；锁定坐标=配合轴/路径切向/竖直轴 | 表 V；§IV-C2 |
| 结果条件 chips | MuJoCo 模拟 Panda；5 匹配种子；锁定组全部停滞终止；关系组 1 次螺母停滞（计入区间）；锁定下横向 ≤3.30 mm、刀面 0.24°、方向 ≤0.74°；力余弦 −1.000 | §IV-A；§IV-C2 表 V 后段落 |
| 限制 1 | 只加一个多余位姿约束，不与一般完整位姿控制器比较 | §IV-C2 末句 |
| 限制 2 | 仅局部、每关系保证；不含全局可行、相位收敛、闭环稳定 | §III-E；§V |
| 限制 3 | 世界描述给定实体/可供性；感知缺失与指代歧义未评估；19/60 语义错误需校验器 | §V；§IV-B2 末句 |
| 限制 4 | 单一模拟 Panda；跨机器人、真实接触、未见组合、重复采样未评估 | §V；§IV-C3 |

## 绘图说明
- 问题三联、左栏 JSON、右栏平面图、中脊均为自绘**示意**，画报已标注。
- 结果条形图与 E1 条形图为据表 V / 表 III 数字重绘；Cutting 与 Stacking 的 min–max 区间小于 0.4 mm，未画须线，仅以文字给出。
- 可编辑源 `poster.html` 被仓库 `.gitignore:193`（`reel/*/poster.html`）忽略，保留在本地；正式发布时再精确处理该路径。
