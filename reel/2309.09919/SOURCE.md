# SOURCE · 2309.09919

- 论文：Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents，arXiv **2309.09919v3**（PDF 页眉 2023-11-28）
- 阅读原文：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2309.09919_pdf.txt`（PDF 抽取，正文 + 附录 A–F）；对照 `2309.09919.txt`（html-full，无表格）。完整原文不提交。
- 初筛记录：`research/scoring/runs/embodied-full-v11-20261022/l2-merged.json`（L2，P3 / confirmed / to_l3）；入选：`selections/selection-002.md` #2（形式约束门控）。规则 problem-core-v1.1。

## 核对结论（Opus 5.5，2026-10-22）

通过。L2 的 facts 与 subcard_checks 与原文一致：Lang2LTL 式翻译 + 专家验证；GPT-4（gpt-4-0613）；FourRoom / MobileManip 安全率 Base 38/30、NL 56/56、未验证 chip 84/94、专家 chip 100/100（成功率 98/98）；Spot 两任务、最多 10 条约束、每设置跑两次、chip 安全率 100%；假设无翻译错与无机械失败，所有方法获对象状态与预定义技能。

核对说明：
- PDF 抽取的 Table I 列顺序被打乱。按“Four Room | Success, Safety | Mobile Manipulation | Success, Safety”还原：成功率列（90/100/100/76/98；94/100/96/88/98）与安全率列（38/56/54/84/100；30/56/62/94/100）的归属，由“专家 chip 安全率 100%”“未验证 chip 成功率因误译下降”“Base 成功率低于有约束的两种智能体”三处正文陈述交叉确认，与 L2 一致。未见原 PDF 版面图，此还原为我们依正文的判断。
- L2 未提 NL Constraints*（专家改写的精确自然语言约束：54 / 62%），画报补充展示，显示改写文字几乎不提高安全率。
- 原文未列 Table I 每格分母（两环境共 20 任务、约束 1→5 条递增；各值均为偶数百分比）。画报不写分母。
- html 版 §IV-D 写作“As Table II and Figure 4 show”，PDF v3 为“Table I”；按 PDF。

## 数字与断言映射

| 画报内容 | 原文位置 |
|---|---|
| 问题：LLM 智能体难以持续遵守“不许做”，约束越多越难 | Abstract；§I（三项障碍） |
| 英文约束 → LTL → 专家验证 → 合并为自动机；人类设计者需懂 LTL | §III-A–C；附录 B |
| 自动机推进命题级轨迹、屏蔽违规动作；可检测矛盾约束而中止 | §III-D；§V-B |
| 重提示：屏蔽 + 查询系统用 LLM 解释违规原因，回填为错误信息；“go to toilet”例 | §III-E–F；附录 F |
| 前提“假设完美真值函数与转移模型” | §III-E |
| Base Model 起初不知约束，被告知留意错误信息并重新生成 | §IV-B |
| VirtualHome：20 个任务、每任务 5 条可满足约束、1→5 递增；约束属 avoidance/trigger 模式；示例为真值动作序列；任务保证可完成；从模拟器读位置与状态 | §IV-A、§IV-C |
| 安全率 / 成功率定义 | §IV-C |
| NL Constraints* 为专家依据已验证 LTL 改写的精确 NL | §IV-C |
| Table I 全部 20 个数值 | Table I（按上文还原） |
| “专家验证 chip 安全 100%；未验证仍有较大优势但成功率受误译影响；NL 基线即使用专家 NL 仍难遵守” | §IV-D |
| Spot：23 个物体与地标、2 个任务、每任务 10 条约束、6 种模式、逐步增加；假设无误译与无机械失败；预定义技能、对象状态、规划器；每任务跑两次、temperature 0 | §V-A |
| Table II：CaP 53/55、NL 98/34、chip 98/100 | Table II |
| 约束 >5：NL 0%、CaP 40%；<5：NL 75%、CaP 70% | §V-B |
| 3 次自相矛盾中止测试 | §V-B |
| “把书送到书架”10 条约束拦截—重提示链 | 附录 A |
| 违规解释由命题真值变化生成 | 附录 F |

## 我们的读法

- “专家验证后的 100% 是符号模型内的保证”：安全率由同一套自动机/命题定义判定，且真值来自模拟器或预设状态，因此 100% 更接近构造性保证；真正被检验的是翻译质量与成功率是否保住。画报已标“我们的读法”。

## 自绘与示意

- “两种接法”双车道图（据 §III 与 Fig. 1–2 的文字描述）为本画报自绘示意，不是论文原图；红绿圆点仅示意违规/合法动作，不表示比例。
- 横向条形为 Table I 数值重绘；附录 A 对话链为节选意译。未运行论文代码，未复现实验。
