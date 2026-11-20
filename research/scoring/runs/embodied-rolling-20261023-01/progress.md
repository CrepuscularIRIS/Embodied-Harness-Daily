# embodied-rolling-20261023-01 进度

## 2026-10-23 巡检班（首班）

- 新增：1 篇（2610.26659，inbox/2026-10-22-0600 → ingest.py → queue/2026-10-23-2252.txt；corpus 1376→1377）。
- L1：inc-l1-01 1/1 完成。assessed 1 / needs_material 0 / out_of_scope 0。档位 P3×1（pending_method，F0，q1=measured_own，q2=new_bottleneck）。
- L2：预算 1（=max(1, 20%×1)），inc-l2-01 1/1 完成。2610.26659 维持 P3，evidence_status → pending_material，q4_fit=partial，priority=high，next_action=to_l2（等附录材料，不转 park）。
- 漏检抽查：本轮预算 1×10% 取整为 0，无抽查名额；累计至后续班次补做。
- L2 结论要点：子卡适用 9 项——3 成立、3 部分、2 失败、1 未知（另 2 项 NA）；缓存正文缺 Appendix A/B，场景/目标数与一处结果均值存在内部冲突，缺目标可观测性核对 → 暂不能确认遗漏完全来自智能体能力。
- 待办：补 2610.26659 附录材料后重核（needs_material 排队，不隐性淘汰）。

## 2026-10-24 巡检班（第二班）

- 新增：9 篇（inbox/2026-10-23-0005 + 0600 → ingest.py → queue/2026-10-24-0452.txt；corpus 1377→1386）。
- L1：inc-l1-02 9/9 完成，全部 assessed（P3×6 / P2×3；high×6 / medium×3）。
- L2：预算 2（=max(1, 20%×累计 10 篇取整)），inc-l2-02 2/2 完成：**2610.25376 P3/confirmed/to_l3**（本 run 首个 L3 候选）；2610.30197 P3/pending_experiment/to_l2（oracle 绕过 F4 通道、无法隔离模型与接口，等实验对照材料）。
- 漏检抽查：2×10%=0.2→0，无名额，累计待后续班次。
- L2 缺口（已写入记录）：两篇缓存均裁剪（core）；25376 缺训练方差/完整成本；30197 缺共同序列化/故障暴露对照。
- 待办：补材料队列 +2610.30197（pending_experiment）；to_l2 未入本轮预算 7 篇（P3-high 4 + P2-medium 3），下班次预算按累计 L1=19 重算。

## 2026-10-24 08:43 每日 Opus 判断

- 新增 confirmed P3：1 篇（2610.25376）< 3 篇门槛 → 本轮跳过 Reel，候选留池。下轮累计或新确认达标后再选题。

## 2026-10-25 08:43 每日 Opus 判断

- 新增 confirmed P3 仍 1 篇（25376）<3 → 跳过（连续第二轮）。L2 积压 7 篇 to_l2 待预算。

## 2026-10-26 08:43 每日 Opus 判断

- 新增 confirmed P3 仍 1 篇（25376）<3 → 跳过（连续第三轮）。

## 2026-10-27 补跑班（fetch 盲区修复后）

- 盲区说明：10-24/25/26 巡检未先 git fetch，漏掉 Grok 直推远端收集；本班补齐（cron 已改 fetch-first）。
- 新增：8 篇（inbox/2026-10-26-0004 → queue/2026-10-26-1232，corpus 1386→1394）。
- L1：inc-l1-03 8/8 完成（P3×5 / P2×3，全 assessed）。
- 预算修订：run.md 2026-10-27 增量轮声明（每班 to_l2 全部 + 遗留 high ≤5）。
- L2：inc-l2-03 13/13 完成（本班 8 + 遗留 5）。**4 篇 P3/confirmed/to_l3**（31841/32348/32941/30587）；32208/32633 P3/pending_material（缺附录章节）；30478/31427/31613/32554/32776 pending_experiment（含 31613 Table IV 0.72 vs 0.78 数字冲突）；32559/30606 P2/park。子卡 69 项：holds 18 / partial 40 / fails 4 / unknown 4 / NA 3。
- 漏检抽查：欠账未清（13×10%=1.3→1，本批未含抽查名额，下班补抽）。
- 下一步：池内 confirmed P3 = 25376 + 本班 4 = 5 篇 ≥3 → 明早每日 Opus 班首次选题。

## 2026-10-27 08:43 每日 Opus 判断（第三期选题 + C003-1 落档）

- 新增 confirmed P3：5 篇 ≥3 → 首次选题。终选 3 篇（25376 TILDE / 31841 FORCA / 32941 Backtrack），3 张画报首轮渲染均不过、一轮修复后全过；30587 同题去重落选、32348 列下期第一备选。见 selections/selection-003.md。
- Correction C003-1（30587 云请求比例 50% vs Table I 24.4% 不相容）已退回 Sol 修订：inc-l2-03-rev1-30587.jsonl → P3/pending_material/to_l2（q4=partial）；接受并给出 §IV-A/Algorithm 1/§IV-D 定位。原记录保留。
- to_l3 池：32348（第一备选）。

## 2026-10-27 12:17 巡检班

- 新增：12 篇（inbox/2026-10-27-0000 → queue/2026-10-27-0517，corpus 1394→1406，材料 12/12 abstract_intro）。
- L1：inc-l1-04 12/12 完成（assessed 11 / oos 1；P3×9 / P2×2 / null×1）。
- L2：inc-l2-04 12/12（本班 to_l2 11 + 漏检抽查 33044，seed=46）。**8 篇 P3/confirmed/to_l3**（34370/34108/33487/33446/35817/34649/33718/34151）；35051/34527 P3/pending_experiment（34527 缺 §6 主要结果且 sim/real 预算不匹配）；35687 P2/park。抽查 33044 维持排除（无环境动作闭环，不属收录范围），改判 0/1。子卡 89 项：holds 37 / partial 42 / unknown 8 / fails 1 / NA 1。
- 漏检抽查：欠账 1 已补抽（0/1 无改判）；本班新增欠账 1.2 → 累计 ~1.2 待后续班次。
- to_l3 池：上期备选 32348 + 本班 8 = 9 篇 ≥3 → 明早 Opus 班选题（第四期）。

## 2026-10-28 08:43 每日 Opus 判断（第四期选题 + C004-1 落档）

- 新增 confirmed P3：9 篇 ≥3 → 第四期选题。终选 3 篇（35817 ZAP 仿真→真机单因子对照 / 34370 ThinkLocoManip 首张腿足移动操作 / 32348 LogLook 上期备选转正），3 张全过 QA（2 张经授权加修一轮，历史在 QA.md）；ReSight 列下期第一备选。见 selections/selection-004.md。累计 24 张。
- Correction C004-1（34151：Q2 应为 vertical_port——迁移 Xu[10] 日志攻击诊断）已退回 Sol 修订：inc-l2-04-rev1-34151.jsonl → **P1/confirmed/park**（q2=vertical_port；接受，§1/§5 定位）。原记录保留。
- to_l3 池：33487 ReSight（第一备选）。

## 2026-10-28 06:17 巡检班

- 新增：8 篇（inbox/2026-10-28-0600 → queue/2026-10-28-1051，corpus 1406→1414；收集 +12 中 4 篇已收录）。
- L1：inc-l1-05 8/8 完成（assessed 7 / oos 1；P3×6 / P2×1）。
- L2：inc-l2-05 8/8（本班 to_l2 7 + 欠账抽查 37547，seed=47）。**6 篇 P3/confirmed/to_l3**（36533/36143/37196/36852/37533/37378）；36013 P3/pending_material（缓存缺 §4.3–4.4 与附录）。抽查 37547 维持排除（冻结 ACT 人类引导后训练，无 LLM/VLM harness），改判 0/1。子卡 32 项：holds 9 / partial 15 / unknown 3 / fails 1 / NA 4。
- 漏检抽查：欠账 1 已补抽（0/1）；本班新增 0.8 → 累计 ~0.8。
- to_l3 池：33487（第一备选）+ 本班 6 = 7 篇 ≥3 → 今晨 Opus 班第五期选题。

## 2026-10-29 08:43 每日 Opus 判断（第五期选题 + C005-1 落档）

- 新增 confirmed P3：7 篇 ≥3 → 第五期选题。终选 3 篇（36533 RoboAuto / 37196 Best-of-N 上界=运气测量 / 37533 双手时序归因），3 张各重做一次后全过 QA；37378 列下期第一备选；ReSight 上期顾虑仍成立（真机段运动禁用）。见 selections/selection-005.md。累计 27 张。
- Correction C005-1（36852 收录范围）已退回 Sol 修订：inc-l2-05-rev1-36852.jsonl → **out_of_scope/exclude**（接受：冻结 URMA 步行策略 + Fourier/岭回归诊断，无 LLM/VLM，不满足 EVIDENCE.md B 类；与 37547 判定对齐）。原记录保留。
- to_l3 池：37378（第一备选）。待补材料：36013（§4.3–4.4 与附录 9–10）。

## 2026-10-29 08:43 每日 Opus 判断

- selection-005 后新增 confirmed P3：1 篇（37378 备选）<3 → 跳过。36013 待补材料（§4.3–4.4 与附录）。

## 2026-10-31 12:17 巡检班

- 新增：12 篇（inbox/2026-10-30-0815 13 ready 中 1 重复，ingest.py 入库→queue/2026-10-31-1054，材料 12/12）。
- L1：inc-l1-06 12/12（assessed 9 / needs_material 3：38388/39180/38405 缓存仅摘要；to_l2 12 = high 7 / medium 5）。
- L2：inc-l2-06 13/13（本班 to_l2 12 + 抽查 31013；遗留 high 0）。改判 2 篇 P2→P3（39446、39319）。**5 篇 P3/confirmed/to_l3**（39319/38744/40016/39775/38318）；6 篇 pending_material 留队 to_l2（38388/39180/38405 仅摘要，39446/40248 关键段截断，38266 待核被引原文）；38027、31013 pending_experiment。子卡 61 项。抽查 31013 维持 P2，漏检改判 0。
- 漏检抽查：seed=20261031，名额 1（预算 12×10%），池 2（31518/31013），抽中 31013；欠账 0.8+0.2→~1.0 继续滚存。
- to_l3 池：1（37378）+ 本班 5 = 6 篇 ≥3 → 明晨 Opus 班可做 selection。

## 2026-10-31 08:43 每日 Opus 判断（第六期选题）

- selection-005 后新增 confirmed P3：6 篇 ≥3 → 第六期选题。终选 3 篇（40016 LOGIV / 39775 Teaching a Tree to Recover / 37378 VLA-Stem 上期备选），各重做一次后过视觉 QA；39319、38744 与 LOGIV 同题去重，38318 主卡已饱和。无 correction。见 selections/selection-006.md。累计 30 张。

## 2026-11-01 08:43 每日 Opus 判断

- selection-006 后新增 confirmed P3：0 篇 <3 → 跳过（6 篇 pending_material 留队待补）。周末 arXiv 停更无新增。

## 2026-11-02 08:43 每日 Opus 判断

- selection-006 后新增 confirmed P3：0 篇 <3 → 跳过。隔夜收集 +12 待 12:17 巡检班入库评分；6 篇 pending_material 仍留队。

## 2026-11-02 12:17 巡检班

- 新增：12 篇（inbox/2026-11-02-0815，ingest.py 入库→queue/2026-11-02-1750，材料 12/12）。
- L1：inc-l1-07 12/12（assessed 11，out_of_scope 1：41275 纯 VLA；to_l2 11 = high 9 / medium 2）。
- L2：inc-l2-07 12/12（本班 to_l2 11 + 补抽 31518；遗留 high 0）。改判 2 篇 P2→P3（41868、31518）。**6 篇 P3/confirmed/to_l3**（40799/41216/41844/42053/41044/41857）；4 篇 pending_material 留队（41320/41383/41688/42141——BioAgent 缺 LLM/VLM 闭环证据、LEXP/RoboArchitect 缺经验流协议）；41868 P3/pending_experiment。**补抽 31518 改判 P2→P3/pending_experiment（漏检 1，待材料）**。
- 漏检抽查：seed=20261102，名额 1（预算 11×10%）+欠账 1.0 补抽，池 1 抽中 31518；改判 1。余欠账 ~0。
- to_l3 池：0 + 本班 6 = 6 篇 ≥3 → 明晨 Opus 班可做 selection。

## 2026-11-03 08:43 每日 Opus 判断（第七期选题，补跑）

- selection-006 后新增 confirmed P3：6 篇 ≥3 → 第七期选题。终选 3 篇（41857 SimuGuard / 41844 SketchMate / 41216 TinyAstral），各重做一次后过视觉 QA；40799（与 ZAP 同题）、42053（监控类已 5 张）去重落选，41044 列下期第一备选。无 correction（41857 无 LLM/VLM 在环，按 B 类评测方法收录，理由见其 SOURCE.md）。见 selections/selection-007.md。累计 33 张。

## 2026-11-04 08:43 每日 Opus 判断

- selection-007 后新增 confirmed P3：0 篇 <3 → 跳过（41044 为下期第一备选）。收集端自 11-02 晨无新产出；4 篇 pending_material 仍留队。

## 2026-11-06 08:17 巡检班（收集端恢复）

- 新增：12 篇（inbox/2026-11-04-0819，ingest.py 入库→queue/2026-11-04-1752，材料 12/12）。
- L1：inc-l1-08 12/12（全 assessed，to_l2 12 = high 10 / medium 2）。
- L2：inc-l2-08 12/12（to_l2 全部；遗留 high 0）。改判 1 篇 P2→P3（2611.05058），Q1 修正 2 篇。**7 篇 P3/confirmed/to_l3**（01560/04255/04226/04080/02391/05058/03850）；4 篇 pending_material 留队（01112/05320/00180/02497——缺 gateway 方法/准入验收/门控主实验/RQ3-5 统计）；01560 首版时间核实 2026-11-01。
- 漏检抽查：名额 1（预算 12×10%）但池 0 → 欠账 ~1.0+1.2→~2.2 滚存。seed=20261106。
- to_l3 池：0 + 7 = 7 篇 ≥3 → 今日 Opus 班达标。

## 2026-11-06 每日 Opus 判断（第八期选题 + C008-1/2 落档）

- selection-007 后新增 confirmed P3：7 篇 ≥3 → 第八期选题。终选 3 篇（04080 FEIJOA 指令后扫描发现 / 01560 uni-robot-agent harness 差异 / 41044 上期备选周界防御），各重做一次后过视觉 QA；05058/04226 与上期同题去重，04255 区间重叠，02391 列下期备选。见 selections/selection-008.md。累计 36 张。
- Correction C008-1（00344 SPARK critic precision 不可测、收益主要来自重看）落档：q4→partial、pending_experiment、to_l2 留队，P3/high 保留。
- Correction C008-2（04226 DiMuRe 801 例开发集挑选、恢复在偏移组有害）落档：**维持 P3/confirmed/to_l3**——全 891 例净增 15.71pp 成立，展示口径收窄为"整体净收益，不含无害性"；下期候选。
- 更正：上条巡检记录中第 7 篇 to_l3 应为 2611.00344（03850 实为 P2/park，笔误）。

## 2026-11-06 06:17 巡检班

- 新增：12 篇（inbox/2026-11-05-0919，ingest.py 入库→queue/2026-11-05-1751，材料 12/12）。
- L1：inc-l1-09 12/12（assessed 11，out_of_scope 1；to_l2 11）。
- L2：inc-l2-09 11/11（to_l2 全部）。改判 1 篇 P2→P3（06881）。**8 篇 P3/confirmed/to_l3**（06863/06768/06881/06475/06434/06653/05567/06453——逐篇以批次记录为准）；06654 pending_material（缺方法后半与 §5，LLM/VLM 链路未确认）；06184 pending_experiment；00405 P2/park。
- 漏检抽查：名额 1（预算 11×10%）但池 0 → 欠账 ~2.2+1.1→~3.3 滚存。seed=20261108。
- to_l3 池：0 + 8 = 8 篇 ≥3 → 今日 Opus 班达标。

## 2026-11-07 每日 Opus 判断（第九期选题）

- selection-008 后新增 confirmed P3：8 篇 ≥3 → 第九期选题。终选 3 篇（06863 重试反馈归因 / 06434 EviSeek 证据优先主动问答 / 06453 失败边界评测 B 类），各重做一次后过视觉 QA；无 correction（06863 附录补齐 L2 疑问：swap 测试无 fallback 例）。06768 与 RSI 仓独立得出一致落选判断；05567 列下期第一备选（04226/02391 亦为池外备选）。见 selections/selection-009.md。累计 39 张。

## 2026-11-08 每日 Opus 判断（第十期选题）

- selection-009 后无新增 confirmed，按前期备选池 3 篇执行。终选 2 篇（05567 MESA B 类评测基准，harness 仅侧栏对比 / 02391 Late Autumn 无 LLM planner 的 coding-agent 调优），各重做一次后过视觉 QA；04226 与 LOGIV 同卡且 LLM 归因不可分，维持落选（池清空）。无 correction（C008-2 修订记录核对无误）。隔夜收集 +13 待 12:17 巡检班。见 selections/selection-010.md。累计 41 张。

## 2026-11-08 12:17 巡检班

- 新增：13 篇（inbox/2026-11-06-0919，ingest.py 入库→queue/2026-11-06-1750，材料 13/13）。
- L1：inc-l1-10 13/13（全 assessed，to_l2 13）。
- L2：inc-l2-10 13/13（to_l2 全部；遗留 high 0）。Q1 改判 1 篇（07825 asserted→measured_own）。**11 篇 P3/confirmed/to_l3**；08462 P3/pending_material（缺 §III-C 后半及 III-D）；另 1 篇 park。2610.41970 首版核实 2026-10-30。
- 漏检抽查：名额 1（预算 13×10%）但池 0 → 欠账 ~3.3+1.3→~4.6 滚存。seed=20261109。
- to_l3 池：0 + 11 = 11 篇 ≥3 → 明晨 Opus 班达标。

## 2026-11-09 每日 Opus 判断（第十一期选题）

- selection-010 后新增 confirmed P3：11 篇 ≥3 → 第十一期选题。终选 2 篇（08209 RoboARCade 误报完成基准 / 08318 判据暴露——与 RSI 仓同篇独立核对制作，两仓版式与口径独立），各重做一次后过视觉 QA；第 3 席按证据标准空缺。41970/08039/02660 同卡去重，08425 列下期首选备选，其余范围/证据落选。无 correction（08318 的布局重叠疑点经附录 A.1 澄清：开发/测试为不同种子）。见 selections/selection-011.md。累计 43 张。

## 2026-11-10 08:43 每日 Opus 判断

- selection-011 后新增 confirmed P3：0 篇 <3 → 跳过（仅备选 08425 VLA-Tug 1 篇 <3；9 篇落选理由仍成立）。

## 2026-11-11 08:43 每日 Opus 判断

- selection-011 后新增 confirmed P3：0 篇 <3 → 跳过（备选 08425 仍 1 篇）。

## 2026-11-12 06:17 巡检班

- 新增：12 篇（inbox/2026-11-09-0921，ingest.py 入库→queue/2026-11-09-1750，材料 12/12）。
- L1：inc-l1-11 12/12（to_l2 10，out_of_scope 2）。
- L2：inc-l2-11 11/11（to_l2 10 + 补抽 1，欠账 4.6 清偿 4，余 ~0.6）。改判 1 篇 P2→P3（09355）。**5 篇 P3/confirmed/to_l3**（08698/08895/08914/09030/09355）；09892/09124/08946 pending_material 留队（缓存缺方法/消融段）。抽查 08917 维持排除，漏检 0。

## 2026-11-12 每日 Opus 判断（第十二期选题）

- selection-011 后新增 confirmed P3：5 篇 + 备选 08425 ≥3 → 第十二期选题。终选 3 篇（08914 HomeLoop 误干预基准 / 09030 对象系-世界系反馈受控研究——与 RSI 仓独立核对制作 / 08425 VLA-Tug 校准弃权边界，备选转正），各重做一次后过视觉 QA；08895/08698/09355 与既有画报重叠落选。无 correction（三处附录发现均在 Sol 已标缺口内，收窄记入 SOURCE.md）。见 selections/selection-012.md。累计 46 张。

## 2026-11-12 18:17 巡检班

- 新增：12 篇（inbox/2026-11-10-0914，ingest.py 入库→queue/2026-11-10-1750，材料 12/12）。
- L1：inc-l1-12 12/12（to_l2 10，out_of_scope 2）。L2：inc-l2-12 10/10。**7 篇 P3/confirmed/to_l3**；12885 pending_material（仅摘要）；10510 pending_experiment（TEST 参与模型选择）；1 篇 confirmed/park。
- 漏检抽查：名额 1（预算 10×10%）但池 0 → 欠账 ~0.6+1→~1.6 滚存。seed=20261115。
- to_l3 池：+7。

## 2026-11-13 每日 Opus 判断（第十三期选题）

- selection-012 后新增 confirmed P3：7 篇 ≥3 → 第十三期选题。终选 2 篇（12177 Embodied First Exam 特权状态差距 / 12409 可达性标注双手规划），各重做一次后过视觉 QA；第 3 席按证据标准空缺。11688 同族去重、11509 记忆槽饱和（RSI 已制）、10748 边界归 RSI 卡。无 correction（12177 同跑 28/30 计数差异、12409 Table III 校验器逐次正确率均记 SOURCE.md 收窄）。见 selections/selection-013.md。累计 48 张。

## 2026-11-13 12:17 巡检班

- 新增：7 篇（inbox/2026-11-11-0912，queue/2026-11-11-1751，材料 7/7）。
- L1：inc-l1-13 7/7（to_l2 6，out_of_scope 1）。L2：inc-l2-13 6/6。改判 1 篇 P2→P3（12983）。**3 篇 P3/confirmed/to_l3**；13161 pending_material（仅摘要）；13034、12958 pending_experiment（缺归因对照）。
- 漏检抽查：名额 1（预算 6×10%）但池 0 → 欠账 ~1.6+0.6→~2.2 滚存。seed=20261116。
- to_l3 池：+3。

## 2026-11-14 每日 Opus 判断（第十四期选题）

- selection-013 后新增 confirmed P3：3 篇 ≥3 → 第十四期选题。终选 2 篇（13039 Robo-MLT 步进指针 / 14115 LEASH 安全层），各重做一次后过视觉 QA；12983 证据不足以支撑画报（Sol 已标注大部分缺口，不改档）。无 correction（14115 的 3312/143 与表 3 计入 gate 变体后吻合；13039 恢复触发器置信区间重叠已记 SOURCE.md）。见 selections/selection-014.md。累计 50 张。

## 2026-11-15 08:43 每日 Opus 判断

- selection-014 后新增 confirmed P3：0 篇 <3 → 跳过（12983 已落选）。隔夜收集 +12 待 12:17 巡检班。

## 2026-11-15 12:17 巡检班

- 新增：12 篇（inbox/2026-11-13-0914，queue/2026-11-13-1753，材料 12/12）。
- L1：inc-l1-14 12/12（to_l2 10，out_of_scope 2）。L2：inc-l2-14 11/11（含补抽 14834，欠账 2.2 清偿 2）。改判 1 篇 null→P2（16487）。**8 篇 P3/confirmed/to_l3**（逐篇见批次）；16487、16632 pending_experiment/to_l2 留队。抽查 14834 维持排除，漏检改判 0。
- to_l3 池：+8。

## 2026-11-16 每日 Opus 判断（第十五期选题）

- selection-014 后新增 confirmed P3：8 篇 ≥3 → 第十五期选题。终选 2 篇，**1 张 ready**（16246 H2E：成功会话改写为 VLA 训练标签，3189 未见场景 35.0→44.9，严格对照取 Table 4）；**15651 内容核对通过但重做一次后视觉 QA 仍不过（页底溢出/标签压行），按规范不发布**，失败版仅存本地待用户决定是否追加修复。16009 与 01560 同判去重、16872 单次开发运行、15964 未具名基线、16671 仅符号重放、15317/15093 范围落选。无 correction（4 处收窄记 SOURCE.md）。见 selections/selection-015.md。累计 51 张。

## 2026-11-17 08:43 每日 Opus 判断

- selection-015 后新增 confirmed P3：0 篇 <3 → 跳过（15651 仍为 QA-fail 留存本地待用户决定）。

## 2026-11-18 08:43 每日 Opus 判断

- selection-015 后新增 confirmed P3：0 篇 <3 → 跳过（15651 仍 QA-fail 留存本地）。隔夜收集 +11 待 12:17 巡检班。

## 2026-11-18 12:17 巡检班

- 新增：11 篇（inbox/2026-11-16-0846，ingest.py 入库（arXiv 限流 4 分钟退避成功）→queue/2026-11-16-1758，材料 11/11）。
- L1：inc-l1-15 11/11（全 assessed，to_l2 11，needs_material 1：17598）。L2：inc-l2-15 11/11。改判 4 篇 P2→P3（17394/18026/18176/18298）。**6 篇 P3/confirmed/to_l3**（逐篇见批次）；17598 pending_material（X-Nav 高层 planner 未确认 LLM/VLM 在环）、18346 pending_material（SR>GR 与指标定义矛盾）、17549/18026/18359 pending_experiment。
- to_l3 池：+6。

## 2026-11-19 执行方式变更记录

- 用户指示：Opus 5.5 停用，日班 selection/Reel 改由 6.1 Sol 执行（2026-11-19 起）。Embodied selection-016 原派发因网关 ECONNREFUSED 失败（无部分输出），改派 model=sonnet 重跑。

## 2026-11-20 每日 Sol 判断（第十六期选题，Sol 执行）

- selection-015 后新增 confirmed P3：6 篇 ≥3 → 第十六期选题（6.1 Sol 执行，Opus 5.5 已停用）。终选 3 篇（17566/18298/18562），**三张均在唯一一次重做后视觉 QA 仍不过（图注/文字越界），按规范 0 发布**，ready 维持 51；失败稿仅存本地待用户决定。无 correction。见 selections/selection-016.md。

## 2026-11-20 00:17 巡检班

- 新增：7 篇（inbox/2026-11-17-0849，ingest.py 入库→queue/2026-11-17-1800，材料 7/7）。
- L1：inc-l1-16 7/7（全 assessed，to_l2 7）。L2：inc-l2-16 7/7。改判 2 篇 P2→P3（20676/19081）。**5 篇 P3/confirmed/to_l3**（逐篇见批次）；20676 pending_material（缺 §VI 恢复机制）、19274 pending_experiment（缺链接干预独立对照）留队。
- to_l3 池：+5。

## 2026-11-18 18:17 patrol (glm-5.3)
- Digest 74b83d0 (+8 candidates): ingest 8 → L1 inc-l1-17 (7 assessed, 0 OOS; 2611.23070 listed twice in raw but deduped by unique arxiv id)
- L1→L2: 7 to_l2 → L2 inc-l2-17 (7/7): 4 P3/confirmed/to_l3 (22138 RoboTeam 结构无差异感知瓶颈主导、22295 相似度≠效用、22761 配置层攻击、23070 PAIR 家务机器人 VLA 0% 任务成功)；22132 P2/pending_method/to_l2 材料补核；21958 P3/pending_material/to_l2 真机数据待补
- 抽查: seed 20261118 → 2611.22291 复核维持 P2/park
- 池 to_l3 +4 → 2+4 = 6（19081、19952、22138、22295、22761、23070）

## 2026-11-19 00:17 patrol (glm-5.3)
- 查新：refs/lists pins 三仓差分均 none；无新 inbox。
- 补做：2611.22584 InteractVLA L1+L2（18:17 班 prompt 传输损坏漏做）→ L1 inc-l1-18（assessed/high/to_l2，P3 pending_method）→ L2 inc-l2-18（P3/confirmed/to_l3；K107 卡 challenged_with_evidence，几何引导在语言编辑失效处生效；2 partial：骨干单一、RSI 分离协议未披露）。
- 池 to_l3 +1 → 7（19081、19952、22138、22295、22584、22761、23070）。

## 2026-11-20 12:17 patrol (glm-5.3)
- Digest f2a4319 (+12 candidates): ingest 12 → L1 inc-l1-19 (10 to_l2, 1 park ROAM P2/pending_material, 1 OOS JARVIS exclude)
- L2 inc-l2-19: 5 P3/confirmed/to_l3 (25179 SimAudit checker审计, 26196 EmbodyAgent 后训练栈, 26376 UniCraft 跨体契约, 26414 ZeroVLN 升档, 26613 AgentRoboCritic 动作级归因); 5 P2/confirmed/park
- 抽查 seed 20261120 → 2611.25005 复核维持 P2/park (audit_sample)
- 池 to_l3 (7d) = 10 - 3 已发布 + 5 = 12
