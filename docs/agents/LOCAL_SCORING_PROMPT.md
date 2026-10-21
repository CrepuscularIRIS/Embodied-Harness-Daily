# Claude Code：Embodied Harness 阅读、gap、模式与评分

先读 AGENTS.md、docs/MAINTAINING.md、docs/EVIDENCE.md、docs/DESIGN_BASIS.md、research/SCORE_SPEC.md 和 research/REVIEW_WORKSHEET.md。
目标是判断每篇改了什么、怎么选择并保留、证据是否支持其中心主张与留存收益；再按领域方法给分。
已有逆向卡片保留，不续跑旧批次，不读取旧分数/旧 Reel 帮助判定。

## 先整理领域依据并校准

1. 盘点既有语料、卡片、签名、期望与材料覆盖。先复用现有卡；为缺失来源/条件列补读任务，不能直接重建全部。
2. 如果安装了 Open Scientist，按其 SKILL 的 study / forge next 流程工作，用它诊断当前缺口、定向阅读和独立审阅。
   不跳过工具控制步骤手改研究状态；不强迫每篇都进入完整 idea-generation。未安装可按这里的同一方法完成阅读记录，报告工具缺口。
3. 把适用的 reviewer expectations 映射到评分轴。没有 reviews 时使用 paper_practice / paper_limitation，并记录来源强度。
4. 按 SCORE_SPEC 预登记开发/留出集；先补齐真实 0/2/4 锚点，冻结候选，独立审阅后才形成 rubric 版本。

## 对每篇按以下顺序工作

1. 固定 ID/title/version，取完整正文、附录与材料 hash；历史 fulltext 可能截断。缺材料不评分。
2. **提取事实**：操作签名（object/information/operation/output）、反馈/候选/接受拒绝/留存/回用，作者效果与失败边界。此阶段不打分。
3. **gap identify**：核祖先与最近邻、前沿残余、瓶颈代价；分别写作者 gap、核对后的 gap、本文改变与未解决部分。材料不足就定向检索。
4. **方法与模式**：解释方法如何回应 gap，匹配少量相关 Harness 卡的操作/信息/条件；无匹配则 outside_taxonomy。
   不按标签相似度打分，不把用了某模式等同于把模式做好。记录卡片更新建议，但不自行改冻结卡来抬分。
5. **审稿期望**：根据 applies_when 逐条判定；不能把 generic checklist 套给所有论文。没有真实审稿仍做此步。
6. **证据**：主张-证据矩阵；选择数据与测试数据分开，核预算、分母、反证、信息泄漏与作用范围。
   留存收益必须有后续使用和相应结果，不由“有 memory/optimizer”推断。静态 GUI/具身论文按各自主张，不硬套 RSI。
7. **评价**：G/M/X/E 各项引用、理由与反证；claim_support 和 evidence_level 单列。unknown 不出总分，不拿代码链接/名气加分。
8. **独立审阅**：隔离首次结论，先看材料独立判，再处理分歧；固定 judgment hash。模型一致不等于人工 gold。

## 冻结后的批次与交接

先实现并验证 schema/确定性算分器：版本/hash、适用类型、未知项、总权重、总分、重复版本与审核失效都必须检查。
完成小批重评后，按 docs/REEL_SELECTION.md 在同一可比池中用 quality_floor 和 max_items 选题；默认最多 9 篇。
阈值尚未确定时报告分布并等待维护者设定，不自造“80 分优秀”标准。阈值已给定后可以直接执行，不反复确认。
只有 selection 中的论文交给 Reel，未入选论文留在内部阅读/评分记录。

每阶段报告实际材料、结果、未解问题和下一步。不要自行调用付费 API、训练、运行收录代码或推送 GitHub；遵守用户已给出的具体授权。
