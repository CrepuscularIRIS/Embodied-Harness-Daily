# v3.1 领域 pattern 批量评分进度

- 总量：500 篇 = 54 个材料批次（494 篇）+ b999 无材料 6 篇（needs_material，已完成）
- 并发：6.1 Sol 内置 Subagent 滚动补位（4 起，稳定后升 6）
- 每批完成后总控跑 check.py，通过才算完成

| 批次 | 状态 | scored | needs_material | out_of_scope | 备注 |
|---|---|---|---|---|---|
| b999 | done | 0 | 6 | 0 | 无任何材料，总控机械记录 |
