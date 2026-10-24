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
