# SOURCE — 2611.23070 PAIR：智居机器人检定手册（poster 021-3）

- 论文：PAIR: Bringing Household Robots into the Smart Home（arXiv 2611.23070v1，2026-11-17）
- 全文：research/fulltext/2611.23070.txt（长行文本；下表行号为该文件行号，行内容以 § 为准）
- L2 记录：batches/inc-l2-19.jsonl（axis observe_act_interface；judgment；new_bottleneck；已逐条核对一致）

## 画报断言 → 原文位置

| # | 画报断言 | 原文位置 | 原文关键语 |
|---|---|---|---|
| 1 | 84 件资产：14 家电类 + 4 传感器类；真实感 4.63/5；物理+API 共享设备状态，单向延迟 200 ms；ambient 演化 | L9（§1）、L12（§3） | 'across 14 appliance categories and four sensor categories'；'4.63'；'200 ms' |
| 2 | 调查：108 人 1,443 条请求（筛后保留）；58.4% 状态确认/等待事件；仅 API 可完成 39.6%，其余 60.4% 需物理/感知 | L6（Abstract）、L9（§1） | 'retained 1,443 requests from 108 participants'；'58.4'；'APIs alone could complete only 39.6% of them, while the remaining 60.4%…' |
| 3 | 标注质量：多数投票三作者，micro F1=0.881、κ=0.856 | L15（§4） | '(micro F1 = 0.881, \kappa=0.856' |
| 4 | 40 任务全部需要动手、且全部可在不用 API 情况下完成；120 检定 episodes；340 条演示（每任务约 3 条层级演示） | L9（§1）、L18（§5）、L27（§8） | 任务构造叙述；'none of the 120 evaluation episodes'；演示数自述 |
| 5 | 6 种 VLA 配置（π0.5 / GR00T N1.7 × 独立 / +HL / +HL(API)）任务成功率全部 0.0%；平均 9.9 个子任务 | L6（Abstract）、L18（§5 Table 3） | 'two fine-tuned VLA policies complete none of the 120 evaluation episodes'；Table 3 全 0 行；'9.9' |
| 6 | 规划层从不选 continue/wait；81–83% 指令 ≤5 s 即被替换；独立 VLA 抓取中位 22–24 s（时间尺度错配） | L21（§6） | 'the planner never selects the continue or wait action, and 81–83% of the instructions it replaces are replaced after just 5 s'；'median of 22' |
| 7 | Place 子任务 1.2%；失败停在导航/抓取/开门 | L21（§6）、L6（Abstract） | '1.2%'；'stall at navigating, grasping, or operating a door' |
| 8 | +HL(API)：设备操作 0.4%→14.1 / 14.5%；域内子任务 24.0%→47.0%；设备类 11.5→35.9 / 10.3→38.5% | L18（§5 Table 3）、L21（§6） | 表 3 与 §6 数值 |
| 9 | oracle 规划 + 真机身：π0.5 Progress 24.2（有 API）vs 9.2（无）；GR00T 17.2 vs 10.0；>90% 失败停 nav/pick/door；给 API 后集中在导航+抓取 77–85%；160 回合仅 1 个走完全部计划 | L21（§6）、L6（Abstract） | '24.2'、'9.2'、'17.2'、'10.0'；'concentrate on navigation and picking (77–85%)'；'Only one of the 160 rollouts completes its entire plan' |
| 10 | oracle 机身 + 规划器：InternVL3.5-4B 9.8 / Qwen3-VL-8B 34.1 / Gemini 3.5 FL 46.7 / GPT-6 Luna 57.3——规划与执行互补瓶颈 | L21（§6）、L9（§1） | 各 Progress 值；'planning and execution' 互补结论 |
| 11 | 通道选择：3 距离 × 3 声明延迟（0.4/4/16 s）= 1,944 例/模型；Qwen3.5-9B 0.45 m 仅 1% 走 API、2.0–3.5 m 17%；GPT-6 Luna 带推理 5%→32–37%（Qwen3.5 带推理 19–25%→73–83%）；对面板可见性的响应比对声明延迟更一致 | L21（§6）、L9（§1） | 'three stated API round-trip delays (0.4, 4, and 16 s) yields 1,944 cases per model'；'chooses the API in only 1%…at 0.45 m but in 17% at 2.0 and 3.5 m'；'(5% vs. 32–37%…'；'in response to panel visibility more consistently than to the stated API delay' |
| 12 | 按键复杂度：Qwen3-VL-8B 单输入操作 52% 走 API、≥4 输入仅 13%；Qwen3.5-9B 稳定 11–13% | L21（§6） | '52% of single-input operations but for only 13% of those that need four or more inputs' |
| 13 | 边界：340 演示偏少自认；智居委托场景不外推；代码 upon publication 未放出；延迟为声明值非真实网络 | L27（§8）、L29（LLM Usage） | 自述限制 |

## 展示缩窄（相对原文的取舍）

- 「0.0%」为 6 配置任务成功率的合并读数（原文按配置逐行 0），画报以单一大数字呈现并注明「全部 6 种配置」。
- 表 3 的完整子任务技能分布（Pick/Place/开门/拧钮/按键/导航等逐项）未上画，仅保留 Place 1.2%、设备类三组与域内合计，以免与 §4 卡数字重复。
- 通道实验只保留「距离→可见性」「推理强度→摆动」「输入数→避让」三条主叙事；1944 例的完整四模型 × 九条件矩阵从略。
- 「延迟 0.4→16 s 变化下选择变化远小于可见性项」为原文「对面板可见性的响应比对声明延迟更一致」的归纳表述，未引具体 pp 数值。
- 头部「先别怪它不会用 App」为编辑修辞；全部断言性数字均在上表可溯源。

## 事实修正记录（生产期，未计重做）

- 对照条图例初稿写「灰色条=无 API」但并未实际渲染灰条，改为「虚线刻度=无 API 读数」；条长按有 API 值满刻度（π0.5 24.2→94%、GR00T 17.2→67%），刻度按同比例折算（9.2→36%、10.0→39%），右侧读数仍为原值。
- 刻度元素初版超出条高 3px 被 overflow:hidden 裁切（程序检查 clipped=2），改为条内满高；复检 clipped=0。