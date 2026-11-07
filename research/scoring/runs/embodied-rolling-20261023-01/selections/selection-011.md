# selection-011 · embodied-rolling-20261023-01

- 规则版本：`problem-core-v1.1`；选择席：Opus 5.5 L3 选题与 Reel 席（claude-kimi fable 槽，单席串行）；日期 2026-11-07
- 本仓第十一期。前十期 41 篇（run embodied-full-v11-20261022 selection-001/002 共 18 篇；本 run selection-003–009 各 3 篇、selection-010 2 篇）不再重复入选，只用作同题/同卡对照。
- 候选池：11 篇，均出自 inc-l2-10，按 batches 最新记录均为 P3 / confirmed / to_l3（标题查 `research/corpus.jsonl`）。无 P2 confirmed 编辑候选（同批 07825 为 P2/park，不入池）。
- 结果：入选 **2 篇**，2 张均 ready（每张首轮渲染不过、重做一次后通过）；与前期已选同卡重复 3，范围与代表性让位 4，证据不足以展示 2。本期 **correction 0**。不为凑满 3 篇制作第三张。
- 档位为问题评价，不是审稿结论；入选不代表方法或结果已被验证。未运行论文代码，未复现。

## 候选（11 篇）

| paper_id | 标题（简） | tier | q3 | 族 | 主卡 | 处理 |
|---|---|---|---|---|---|---|
| 2611.08209 | RoboARCade: Benchmarking Agentic Robot Control | P3 | judgment | F1,F2 | harness_effect_evaluation / observe_act_interface | **入选 #1**（B 类评测基准，被测对象即 LLM 代理 harness） |
| 2611.08318 | Learning the Task or Learning the Verifier? Criteria Exposure | P3 | judgment | F2,F4 | harness_self_optimization / privileged_teacher_supervision | **入选 #2** |
| 2610.41970 | When Does Test-Time Search Help World Action Models? | P3 | judgment | F2,F5 | sample_verify_select / harness_effect_evaluation | 与前期已选同卡重复 → 2610.37196（s005） |
| 2611.08039 | HITCH: VLM Operating a Humanoid through a Whole-Body Harness | P3 | capability | F3,F4 | observe_act_interface / privileged_teacher_supervision | 与前期已选同卡重复 → 2610.34370（s004）、2610.35817（s004） |
| 2611.02660 | HeLM: Hierarchical Explicit Language Memory | P3 | capability | F5,F3 | harness_memory_skill_reuse / trained_vlm_vla_hierarchy | 与前期已选同卡重复（记忆槽：2510.20328 MemER、2610.32348 LogLook） |
| 2611.08425 | VLA-Tug: Calibrated Latent Probing for VLA Failure Prediction | P3 | capability | F2,F3 | external_verification_control | 范围与代表性让位（下期备选） |
| 2611.08449 | VFlash: Flash Primitive Decoding for Visual Planning | P3 | capability | F0,F2 | observe_act_interface / trained_vlm_vla_hierarchy | 范围与代表性让位 |
| 2611.07964 | Time-Indexed Skill Success Models | P3 | judgment | F2,F4 | external_verification_control / observe_act_interface | 范围与代表性让位 |
| 2611.08144 | Silent Faults at the Environment-Trainer Boundary in RL | P3 | judgment | F2,F1 | observe_act_interface / harness_effect_evaluation | 范围与代表性让位 |
| 2611.07417 | MessyNav: Zero-Shot Navigation via Manipulation | P3 | capability | F3,F1 | observe_act_interface / external_verification_control | 证据不足以展示 |
| 2611.07517 | Embodied RAG++ / E2W-Bench | P3 | capability | F4,F2 | llm_symbolic_solver_planning / harness_memory_skill_reuse | 证据不足以展示 |

## 入选

| # | paper_id | 类型 | 入选理由 |
|---|---|---|---|
| 1 | 2611.08209 | 评测基准：前沿代理直接控制机器人时，分开数“会不会做”与“知不知道做完” | 被测对象本身就是 LLM 代理 harness（Claude Code / Codex 经 MCP 界面看像素、下末端指令，无学习型策略），判分谓词在沙箱外、代理看不到，因此“误报完成”可以干净计数：附录表 5 中代理以为整个任务做完而结束、实际未解决的决定占 33–63%，按尝试子任务计 24–39%。同一基准还给出两条对 harness 设计有用的判断：更丰富的 VIA 界面只多 1.5–6.8 点、花费 1.7–2.3 倍（表 1）；自我改进（ICL、自写并按评分修改的文本提示）把完全成功从 19/50 提到 32/50，主要是消掉卡死超时，误报完成始终 12–15 次（附录表 8）。与前期评测画报问题不同：s010 05567 MESA 测 VLA 的“选错目标”、s008 01560 测开放模型换 harness 的落差、s001/002 EmbodiedEval 测人机同接口鸿沟；本篇的核心是代理的完成自检。 |
| 2 | 2611.08318 | harness 自我优化的反馈协议：学习者能否读基准判分代码 | 受控设计扎实：同一回路（冻结 GPT-6 Astra 执行者＋Claude Code 学习者改技能库）只改学习者读什么；任务分组在看结果前固定；同一批 320 个测试回合用两套判据重判，行为完全相同，差别只来自判据——原判据下 51.6 vs 27.8，忠于指令的判据下 45.0 vs 47.2（差距缩小 25.9 点，按任务自助 95% 区间 4.7–54.4）；反向让学习者读新判据，分数又跟着读过的判据走（65.0 → 13.5）；领先不随库迁到新任务（80 vs 71 of 200）。它改变的是一个常用做法的解读：把判分代码交给自我改进学习者所得的增益，部分是验证器拟合。与前期同卡画报（s003 FORCA、s005 RoboAuto、s007 TinyAstral、s010 Late Autumn：编码代理改机器人程序的收益与归因）问题不同，本篇问的是反馈信息本身是否可部署。RSI 仓 selection-011 已独立制作本篇；三仓不共享画报，本仓按 Embodied 卡口径独立核对与设计。 |

### 画报侧重（已制作）

- **2611.08209**：深色题带；三框流程＋虚线“沙箱外判分谓词”框（示意）；表 5 双层横条＋核验准确率列；表 1 花费—成功散点（同模型虚线箭头）；三格大数＋代理引语框（我们翻译）；表 8 四组 50 格结局方阵（完成 / 耗尽预算 / 误报完成）。限制栏写明子任务评分、无区间、模型与运行时捆绑、自改进任务经挑选且 T2 读评分结果、种子分隔未写明。
- **2611.08318**：报刊式双线题头＋衬线标题；窄左栏：42 格审读格、指令/判据对照、竖向回路（示意）、经验写法、迁移表；宽右栏：表 1 分组条、同批回合两把尺子的斜率图、2×2 判据矩阵（对角黄格）、作者与给基准的建议。限制栏写明 C_faith 为作者自写、只改 RoboDojo、仿真反馈、单测试种子、只测两档、任务挑选（我们的读法）、读判据方多拿得分与阶段。

## 排列、去重与取舍（编辑理由，均有原文或记录依据）

1. 11 篇均为 P3 / confirmed；q3：judgment 5（41970、07964、08144、08209、08318）、capability 6，不分先后，不按数值排序。
2. **与前期已选同卡重复（3）：**
   - 41970 → 2610.37196（s005）：同为世界动作模型测试时 Best-of-N 的候选可选信号（学习型选择器不如随机、后验神谕区间跨零），s005 已做“上界多半是续跑运气”；本篇新增的计时与渲染损坏审计有价值，但被测对象仍是无 LLM/VLM 在环的冻结策略，属 B 类审计，不足以另占一张。
   - 08039 HITCH → 2610.34370 ThinkLocoManip（人形全身控制 harness 把机身姿态做成工具）与 2610.35817 ZAP（在仿真 harness 轨迹上微调 VLM 学“怎么动”）：同卡同问题。L2 亦自述缓存在教师数据生成处截断、K505 两项 partial；负迁移（加 SIMPLE 示范后 HumanoidArena 42.5→28.8）值得记，但不改变同卡判断。
   - 02660 HeLM：记忆槽已有 MemER、LogLook，且 s005（33487）、s006（38318）、s009（06475）均以记忆槽饱和落选；本篇真机非 Markov 任务扎实，但跨回合 89.2 vs 16.6 为子任务分、无强持久记忆基线（L2 已记）。
3. **范围与代表性让位（4）：**
   - 08425 VLA-Tug：冻结 VLA 隐层探针，无 LLM/VLM harness 在环，按 B 类失败检测器收录成立；但它对 harness 交还的价值（steering）作者明说只是概念验证、未定量，未见任务上的双风险认证只在 40–86% / 57–90% 的运行中经验成立。监控/门控槽已有 KnowNo、REFLECT、37378、39775、40016、32941。**列下期首选备选**：若下期池中缺 F2 监控类候选，兑现条件为画报以“提前告警＋可弃权的双风险校准”为主体，steering 只作边界。
   - 08449 VFlash：主体是训练型 VLM 视觉计划的并行解码加速；闭环 70.2 vs 62.6 的基线同时换了编码器，AR 计划 61.0 行才是同接口对照（L2 已记），25× 为单次 rollout，附录训练预算与种子未在缓存给齐。harness 相关性弱于本期两篇。
   - 07964：无 LLM 在环，主体为解析控制器上的技能选择与等待时机方法；其 B 类价值（冻结时钟评测最多高估 22.8 点、真机静态模型预测 99% 实得 63%）真实，但真机为单技能 35 次，且对 LLM harness 只是可接入的评分工具。
   - 08144：通用 RL 环境—训练器边界故障审计（Pendulum、HalfCheetah、Hopper、Pusher），无 LLM/VLM，π0.5 只有一步训练；Sol 按 B 类工具收录不算错误，但与具身 harness 主题的代表性弱。
4. **证据不足以展示（2）：** 07417 MessyNav 真机每方法 15 场景各 1 次（10/15 vs 6/15），离线 825 次假定低层完美执行、夜间 29.2 低于基线 44.2；07517 Embodied RAG++ 为 20 个手写静态快照的离线配对准确率，无闭环执行。两篇 L2 判断本身成立，只是不足以支撑一张画报的核心结果。
5. 入选两篇主卡不同（harness_effect_evaluation vs harness_self_optimization），对象分别为前沿代理零样本控制与编码代理自我改进的反馈协议，不算同题；覆盖 F1、F2、F4。两篇都触及“完成判定”（前者代理自判，后者基准判据），画报各取其主问题，不合并。
6. later_work：11 篇均无 later_work 记录。

## 原文核对状态

钉定依据：`research/fulltext/<pid>.txt` 文件头所标版本。入选两篇缓存头均为 `FULLTEXT: html`、v1、core 裁剪版（08209 缺 §2 与全部附录；08318 缺 §2–§3 与全部附录）；arXiv 两篇均只有 v1（export API 2026-11-07）。两篇另取同版本 arXiv HTML（2026-11-07，转换稿仅在 /tmp，不提交）读全文与全部附录。

| paper_id | 版本 | 读到范围 | 结论 |
|---|---|---|---|
| 2611.08209 | v1 | HTML §1–5＋附录 A.1–A.8（提示词、表 3–8、图 4） | 通过，无 correction。展示取舍：主图用附录表 5 决定级误报并与正文子任务级 24–39% 分列；自改进用表 8 完全成功次数并注明与表 2 平均评分不同；T2 读评分结果、测试种子分隔未写明入限制栏。 |
| 2611.08318 | v1 | HTML §1–6＋附录 A–C（表 3–5、改写规则与逐项变更） | 通过，无 correction。L2 K401 疑“开发/测试布局重叠未交代”：附录 A.1、表 3 写明开发为种子 1 布局 0–4、测试为种子 0 布局 0–19 且学习者未见，缓存缺附录所致，不改字段。25 任务中 20 个按零样本 <50% 挑选，作为挑选效应（我们的读法）入限制栏。 |
| 其余 9 篇 | 缓存版本 | 仅 core 缓存＋L2 记录 | 未入选，落选理由为同卡、范围与证据展示层面的编辑判断，不涉及 L2 字段；未作全文核对，不据此判断其 L2 正误。 |

## Correction

本期无。

## 待补与漏检抽查

- 待补：同批 2611.08462（VLS 语义纠正 steering）P3 / pending_material / to_l2——缺 §III-C 后半及 III-D（门控/代价生成、反例验证、候选选择细则），补齐后可确认 Q4；不在本期池内，由 Sol 单篇 L2。前期待补项（06654、06184、00344 等）见 progress.md，本期未变动。
- 漏检抽查：本期无新增抽查改判；inc-l2-10 抽查名额池为 0，欠账按 progress.md 滚存。
- 下期备选：2611.08425 VLA-Tug（兑现条件见上）。

## 成品路径

| paper_id | 状态 | 文件 |
|---|---|---|
| 2611.08209 | **ready**（第 1 次 PDF 2 页、散点标签互压、15/24 舍入为 62% → 重做一次后通过） | `reel/2611.08209/`：poster.html · poster.png（2400×3400）· poster.pdf（1 页）· SOURCE.md · QA.md |
| 2611.08318 | **ready**（第 1 次 PDF 2 页、斜率图标签压字与刻度被遮、迁移图右列被裁、两栏失衡 → 重做一次后通过） | `reel/2611.08318/`：同上 |

- `poster.html` 被 `.gitignore:193`（`reel/*/poster.html`）忽略，保留本地；正式发布时由总控按精确路径处理。
- 索引已更新：`reel/README.md`（张数 41→43、增量 run 23→25 张、新增 2 行、“选择与制作”新增本期条目）；`README.md` 第 9 行本季漏斗统计行（追加 “11 P3-confirmed → +2 posters”，41 → **43 posters**），其余段落未动。progress.md 未动（由总控写共享进度）。
