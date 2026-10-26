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
