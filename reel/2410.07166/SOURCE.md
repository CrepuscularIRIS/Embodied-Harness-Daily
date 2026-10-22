# SOURCE — 2410.07166

- 论文：Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making，arXiv **2410.07166v3**（材料标 2024-10-09），https://arxiv.org/abs/2410.07166
- 本刊材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2410.07166.txt`（html-full；私有缓存，不提交）。图只有图注，无图像。
- 初筛记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl` paper_id=2410.07166（batch b012，screen 88.75，G4/M4/X4/E3，evaluation_resource，controlled_diagnostic_design，supported_in_material，online）。核对与缩窄见 `verify.md`。
- 图形：全部本刊自绘。机制图（总线 + 四模块 + 分诊树）为示意，按原文定义重画，非原图 4/19；树右列计数与结果哑铃图为原表 6、表 16 数字重绘。

## 数字与断言 → 原文定位

| 画报内容 | 原文定位 |
|---|---|
| VirtualHome 338 条指令、BEHAVIOR 100 个任务 | §3 表 2（#task instruction 338 / 100） |
| 18 个 LLM，四模块 × 两模拟器 | §4 首段；表 3；附录 O.3 表 30 |
| 问题：输入输出各异、只报最终成功率、无法定位缺失能力 | 摘要；§1 |
| 状态 s=⟨U,F⟩、对象间布尔关系，例 is-open(cabinet1)、ontop(rag0, window3) | §2.1；表 1 |
| LTL 片段：∧ ∨ ¬ ⇒ ∀ ∃ ∃⁼ⁿ，时序只实现 then（未实现 globally/until） | §2.2；附录 C.3 |
| 子目标例 browse Internet（ontop … then holds_rh … ∧ holds_lh … then facing …） | §2.2 末段 |
| “LLM 只占这一格、其余用真值/工具” | §2.2 图 4 图注（isolate this single module） |
| G：s₀ + l_g → LTL 目标 ĝ，限“动作 then 命题合取”；与真值落地目标集合求 F1 取最大 | §2.3；表 1 |
| BEHAVIOR 平均每任务 6.7 个落地目标、4,164.4 种目标选项（画报写约 4,164） | §3 Annotations |
| Φ：s₀ + g → 子目标 LTL 序列；BFS 落地；取多条落地序列最高分；指标同 Q | §2.4；附录 D.3 |
| Q：s₀ + g + M → ā；模拟器执行、首个不可执行动作停止；执行成功/任务成功/部分满足 | §2.5；附录 D.2 Goal Satisfaction |
| T：s₀ + g + 算子 o → PDDL pre/eff；逻辑 F1 + PDDL 规划器，只看状态目标 | §2.6；附录 D.4 |
| 逻辑 F1 用递归二分图匹配 | 附录 D.4 Logic Form Accuracy |
| 敏感性：每次只把一个真值动作换成 LLM 预测 | 附录 F.1–F.2 |
| 错误类型：解析 / 幻觉（动作名、对象名）/ 谓词-参数个数；可供性、多余步、缺步、顺序错；判定顺序 1→4；open(shelf) 例 | 附录 D.2、图 19 图注与伪代码 |
| 目标未满足按状态/关系/动作目标统计；G 按三类算 P/R/F1 | 附录 D.1、D.2；表 4、表 5 |
| 树右列 GPT-4o · BEHAVIOR · 动作序列：执行成功 53、任务成功 47；解析 0、幻觉 1、参数个数 0、顺序错 9、缺步 36、可供性 1、多余步 0（合计 47）；“6”= 53−47 | 表 6 GPT-4o 行 B 列（本刊相减） |
| 结果哑铃图 6 个模型 M→P：Opus 51→46 / 59→54；Sonnet 44→41 / 57→53；GPT-4o 47→42 / 53→55；Gemini 1.5 Pro 42→37 / 54→55；Mistral Large 33→31 / 50→38；Llama 3 70B 34→26 / 42→40 | 附录 G 表 16 “Goal Interpretation + Action Sequencing”，BEHAVIOR |
| 15/15 模型任务成功下降，幅度 1–12；10/15 执行成功差 ≤5；Mistral Large −12、GPT-3.5 +12；表中无 o1 | 表 16 全部 15 行，本刊逐行相减统计 |
| M/P 定义（真值目标 vs 同一 LLM 先 G 后 Q） | 附录 G.1–G.2 |
| “可组合但有误差累积”为作者结论 | 附录 G.3 Takeaways；§4.1 末段 |
| temperature 0、单次运行 | 附录 O.1–O.2 |
| 限制：关系图抽象、无感知与低层控制 | §6；附录 S.2 |
| BEHAVIOR 转移层为作者自写符号层（EvalGibson，30 个动作） | §3 Implementation on simulators；附录 N.1 |
| 规划器能解出的计划在真实环境中可能不可行 | §4.1 Transition Modeling 段末 |

## 未采用

- 附录 H 表 17 重规划 65.2%→77.4%（Sol evidence[2]）：只测 GPT-4o、模拟器未写明，基线与主表 GPT-4o 不一致，未上画报（见 verify.md 差异 2）。
- 表 3 模型总排名：单次运行无方差，不作排名展示。
