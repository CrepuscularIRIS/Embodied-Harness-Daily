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
