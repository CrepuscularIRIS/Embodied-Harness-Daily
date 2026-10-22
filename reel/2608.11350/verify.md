# 2608.11350 核对记录（Opus 5.5 核对席）

- 论文：Self-Evolving Embodied Agents via Skill-Harness Evolution（方法名 SHAPER），arXiv **2608.11350v2**（2026-08-11），https://arxiv.org/abs/2608.11350
- 材料：`research/fulltext/review-runs/embodied-v22-20261021-01/materials/2608.11350.txt`（FULLTEXT: html-full，正文 §1–5 + Appendix A.1–A.4，44 KB，已全文通读；无 `_pdf.txt`）。附录 Figure A1–A13（演化前后的技能/harness 代码与提示词）在缓存中只有图注，工件正文不可见。
- Sol 记录：`research/v3/runs/embodied-v3-20261021-01/final/index.jsonl`，paper_id=2608.11350，batch b048，screen_score 88.75，G4/M4/X4/E3，claim_support=supported_in_material，evidence_level=online
- 入选：`reel/selection-opus.md` C7（组内唯一 supported）
- 核对日期：2026-10-22；未运行论文代码（材料未提代码或工件发布）

## 结论：核对通过（pass）

Sol 的问题、动作、关键数字、caveat 与材料一致，未发现需退回的错误。"冻结一切、只演化文本技能与上下文代码"的设定在方法层面有明确证据；但"每次改进可独立复现"和"等预算对照"两项材料**不支持**，画报按"单次演化、描述性差异、无等算力对照"陈述。

## 逐项核对

| 项目 | 材料实际内容 | 定位 |
|---|---|---|
| 问题 | 拿不到权重/示范/奖励，又没有可编程机器人 API、只能走固定动作接口时，如何不训练地把冻结具身智能体适配到目标环境 | Abstract；§1 |
| 冻结范围 | 式(1)：θ（VLM 规划器）、φ（执行器）冻结，只优化 c=(s,h)；"action interface, output parser, and executor remain fixed"；同一 checkpoint 另换提示词充当优化器 | §1；§3.1；§3.3 |
| 演化对象 | s：规划器提示词中的文本技能（场景检查、分解、子目标、恢复、终止）；h：Python `build_context`，选择并格式化轨迹历史 | §3.1；Appendix A |
| 关键动作 | 回合级判官看 (o_t,y_t,a_t,o_{t+1}) → 回合摘要+非视觉元数据 → 文本梯度 Γ；两阶段：先演化 s（h=种子），再演化 h（s=选中技能）；h 进沙箱（必须定义上下文函数，禁 import/文件读写/动态执行，超时拒绝）；验证集 top-K beam | §3.2–3.3；Appendix A.3 |
| 搜索预算 | VLABench 15 训练 + 24 验证 episode；ESI 10+10 题；均与评测集不重叠；4 轮 beam，宽 3、分支 2、反馈 minibatch 4 | §4.1 |
| 模型/接口 | 评测时规划器均为 Qwen3.6-27B；VLABench 执行器为官方 π0（OpenPI，5 步 chunk），≤10 规划轮、≤400 环境步；ESI 走基准固定 API，≤30 步 | §4.1 |
| VLABench 主结果 | 4 个自定义留出 split×200 = 800 episode：Direct VLA 23.25、SFT 24.00、TTS 21.38/22.00/24.38/23.50、Seed 28.25、Skill 33.50、Harness 30.50、SHAPER 34.50 | Table 1–2；§4.2 |
| 非加性 | harness 在技能之上 +1.00（C1 +0.5、C2 +2.5、C3 0.0、C4 +1.0）；harness-only C3 40→46，但 skill/full 均 50；作者自己称"完整配置而非独立效应估计" | §4.2 Artifact ablations |
| ESI 结果 | 231 题（按官方类别比例抽样）：micro 32.5→41.1→49.8，macro 31.2→38.6→42.9；Specular Reflection 20→60（n=20）；Enumerative 33.3→27.8（n=18）；Action Sequencing 40→20（n=5）；GPT-5 PS 40.3 为全集外部参照、非配对 | Table 3；§4.3 |
| 成本 | 每次演化 API 等价约 $2.25（VLABench）/$2.83（ESI），按 Qwen3.6-27B 列表价折算；含 rollout、判官、摘要、优化；不含最终评测和仿真/GPU | §4.4；Appendix A.4 |
| 案例 | select_book/ep_024：种子技能重复检索指令，400 步上限 reward 0.5；演化技能检测无进展改用 pick-up，3 轮 297 步 reward 1.0。ESI 镜面题：种子 harness 只留最近 5 帧，30 步原地转（右 15/左 12/前 3）答"not sure"；演化 harness 保留第 1 步反射帧，答"middle"（置信 0.90）。均为单例 | §4.2 Figure 3；§4.3 Figure 4 |
| 局限（作者自述） | 跨本体迁移与真机验证留作未来工作 | §5 |

## 重点项："冻结设定"与"独立可复现/等预算"

- 冻结设定：**有证据**。式(1)、§3.1 固定接口/解析器/执行器，§3.3 优化器复用同一冻结权重；ESI harness 声明只用官方 RGB，不读位姿/深度/分割/仿真元数据（Appendix A.2，代码本体在缓存中不可见，无法独立核验）。
- 每次改进独立可复现：**不支持**。每个基准只报告一次演化运行，无重复搜索、无种子方差或置信区间；作者也称结果为 descriptive。
- 等预算对照：**部分**。SFT 用同样 15 条训练 episode，但 SHAPER 还额外用 24 条验证 episode 的 rollout 做选择；TTS（MG-Select/VOTE）的采样数与算力材料未报告，与 $2.25 演化成本无对齐。真正干净的对照是同规划器同执行器的 Seed Agent（28.25）。

## 与 Sol 记录的差异

无实质差异，不改分。补充四点边界（展示时缩窄措辞）：
1. "same data SFT" 只对齐 15 条训练 episode，SHAPER 另有 24 条验证 rollout；SFT 调的是执行器 π0，且无上层规划器，SFT vs SHAPER 的 10.5 点差混入了"有无规划器"。
2. ESI 没有 harness-only 行，+8.7 micro 是"在演化技能之上加 harness"的条件差，顺序固定为先技能后 harness，未测反序。
3. ESI 的演化 harness 不只是"挑选历史"：还计算确定性 RGB 裁剪、条带/切块、几何辅助并要求结构化字段（VIEW/TARGETS/EVIDENCE/READY/GAP），实质含感知预处理代码；作者称只用官方像素。
4. Seed Agent 在 C3 为 40.0，低于 Direct VLA 的 45.0——加规划器本身在该 split 有负效应。

## 关键证据定位
- 冻结范围与优化对象：§3.1 式(1)、§3.3 式(4)–(6)
- 搜索/评测切分与预算：§4.1、Table 1
- 主结果与消融：Table 2、§4.2
- ESI：Table 3、§4.3
- 成本：§4.4、Appendix A.4
