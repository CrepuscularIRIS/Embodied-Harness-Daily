# v3 批量评分进度

- 总量：500 篇 = 54 个材料批次（494 篇）+ b999 无材料 6 篇（needs_material，已完成）
- 并发：6.1 Sol Subagent 滚动补位；b006 后由 4 升至 6（连续 5 批稳定后）
- 每批完成后由总控跑 check.py 机械校验，通过才算完成

| 批次 | 状态 | scored | needs_material | out_of_scope | 备注 |
|---|---|---|---|---|---|
| b999 | done | 0 | 6 | 0 | 无任何材料，总控机械记录 |
| b001 | done | 8 | 0 | 0 | check.py 通过 |
| b002 | done | 6 | 0 | 0 | check.py 通过 |
| b003 | done | 8 | 0 | 0 | check.py 通过；Gen-CoT 分数机制内部冲突、2610.12957 真机仅案例已注明 |
| b004 | done | 12 | 0 | 0 | check.py 通过 |
| b005 | done | 15 | 0 | 0 | check.py 通过；Uni-Skill 表III数值不一致已注明 |
| b006 | done | 12 | 0 | 0 | check.py 通过 |
| b007 | done | 9 | 1 | 0 | check.py 通过；2505.23266 材料缺方法/主实验正文 → needs_material |
| b008 | done | 11 | 0 | 0 | check.py 通过 |
| b009 | done | 16 | 0 | 0 | check.py 通过；GAgent/BUMBLE 截断、EmbodiedRSI 缺所引附录 → 按 core 评分 |
| b018 | done | 16 | 0 | 0 | check.py 通过；公式/计数/百分比冲突已注明 |
| b025 | done | 3 | 0 | 0 | check.py 通过；综述按分析主张评分 evidence_level=unknown |
| b030 | done | 5 | 2 | 1 | check.py 通过；BEDI/RoboValue 材料仅摘要→needs_material，FSAR → out_of_scope |
| b034 | done | 9 | 0 | 0 | check.py 通过 |
| b038 | done | 10 | 0 | 0 | check.py 通过；Show-Harness 缺 Table 2 数值按 core |
| b043 | done | 9 | 0 | 0 | check.py 通过 |
| b048 | done | 13 | 0 | 0 | check.py 通过 |
| b054 | running | | | | | 最后一个材料批次 |
| b010 | done | 15 | 0 | 0 | check.py 通过 |
| b011 | done | 6 | 0 | 0 | check.py 通过 |
| b012 | done | 3 | 0 | 0 | check.py 通过（大材料批，仅 3 篇） |
| b013 | done | 4 | 0 | 0 | check.py 通过（大材料批）；MEMORA 静态指标未视为闭环迁移 |
| b019 | done | 5 | 0 | 0 | check.py 通过 |
| b024 | done | 16 | 0 | 0 | check.py 通过 |
| b032 | done | 16 | 0 | 0 | check.py 通过；ChunkAct 分母矛盾与算术错误已注明 |
| b039 | done | 14 | 1 | 0 | check.py 通过；2610.19913 实验表为占位符 → needs_material |
| b045 | done | 13 | 0 | 0 | check.py 通过 |
| b050 | done | 8 | 0 | 0 | check.py 通过 |
| b014 | done | 11 | 0 | 0 | check.py 通过 |
| b022 | done | 4 | 0 | 0 | check.py 通过；ERA/MaCoPlanner 数值不一致、EmbodiedSWE 选点边界已注明 |
| b027 | done | 16 | 0 | 0 | check.py 通过 |
| b033 | done | 7 | 0 | 0 | check.py 通过；首篇总分算术修正 58.75 |
| b037 | done | 7 | 0 | 0 | check.py 通过 |
| b042 | done | 7 | 0 | 0 | check.py 通过 |
| b046 | done | 9 | 0 | 0 | check.py 通过 |
| b051 | done | 4 | 0 | 0 | check.py 通过 |
| b015 | done | 5 | 0 | 0 | check.py 通过 |
| b021 | done | 14 | 0 | 0 | check.py 通过 |
| b028 | done | 10 | 0 | 0 | check.py 通过 |
| b016 | done | 11 | 0 | 0 | check.py 通过 |
| b023 | done | 16 | 0 | 0 | check.py 通过；MFNP 表题不一致、HIMM 摘要增幅与表格算术不符已注明 |
| b029 | done | 6 | 0 | 0 | check.py 通过 |
| b035 | done | 5 | 0 | 0 | check.py 通过；AgentSpec 数值冲突/列重复已注明 |
| b040 | done | 5 | 0 | 0 | check.py 通过 |
| b044 | done | 6 | 0 | 0 | check.py 通过 |
| b049 | done | 7 | 0 | 0 | check.py 通过 |
| b053 | done | 5 | 0 | 0 | check.py 通过 |
| b017 | done | 4 | 0 | 0 | check.py 通过 |
| b020 | done | 10 | 0 | 0 | check.py 通过；RegenHarness 递归改进仅协议无收益证据已限定 |
| b026 | done | 7 | 1 | 0 | check.py 通过；2201.07207 总分机械修正 73.75（四轴未变） |
| b031 | done | 6 | 0 | 0 | check.py 通过；F4R 参数描述不一致已注明 |
| b036 | done | 5 | 0 | 0 | check.py 通过；PhysMem 删节提示记 core |
| b041 | done | 8 | 0 | 0 | check.py 通过 |
| b047 | done | 8 | 0 | 0 | check.py 通过；2505.22050 末尾截断按 core |
| b052 | done | 8 | 0 | 1 | check.py 通过；Continual Harness 纯游戏环境 → out_of_scope |
