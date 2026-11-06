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
