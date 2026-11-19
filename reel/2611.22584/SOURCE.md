# 2611.22584 InteractVLA — SOURCE

论文：*InteractVLA*（arXiv 2611.22584v1，2026-11-18）。全部数字/断言映射到原文。

## 报头

| 海报断言 | 原文出处 |
|---|---|
| 不改权重不重训、测试时几何接口 | 摘要/§1（test-time framework） |
| 目标位姿→单次去噪轨迹内输入梯度 | 摘要 forward direction + §2.1 |
| 软时间对齐把到达时刻当潜变量 | 摘要 + §2.2 |
| 反向：动作块+标定重投影交智能体诊断 | 摘要 reverse + §2.3 |
| "语言换说法推出分布、重试近乎无效" | §1（rephrasing degrades success, retries futile） |
| 骨干 MR-0；LIBERO-Plus/RoboDojo/RoboCasa365/真机 Dexmal | §3 Setup、§3.3 |

## 01 机制图（§2，示意重绘）

- 可微 command-to-pose、E_h 聚合位置/姿态/夹爪误差、式(2)(3)：§2.1。
- 梯度限幅 B_t、内部活动窗、端点保留原生流场：§2.1。
- C_t=exp[-max(r_t/r_0, d_t/d_0)]，C_t<e⁻¹ 早停还给智能体：§2.1 式(4)。
- 软时间对齐 log-sum-exp、q_h(t) softmax 分配、tτ 调幅：§2.2 式(5)(6)。
- 反向：完整 chunk+已执行前缀+重投影；区分目标偏/执行滑/过早抓取；改 G 重调或局部修动作段：§2.3。
- 消融：固定步 39.1%、硬最小 44.2%、软对齐 48.6%（RoboDojo）：§3.4 表 8。

## 02 LIBERO-Plus（表 1）

- MR-0 88.5、+GT 91.3、+离线 Sol 目标 94.5；Sol+MR-0 93.1 → Sol+InteractVLA 98.3：表 1。
- 布局 89.5→98.4、相机 87.6→98.4：表 1 + §3.1。

## 03 RoboDojo（表 2）

- 泛化 8.2/21.6/26.0、记忆 8.9/16.5/22.2、开放 2.4/31.2/39.6、Overall 9.2（GT 12.17）/18.0/26.0：表 2。
- GT 目标伤精度与长程；静态约束不够需在线闭环：§3.1。

## 04 真机 Dexmal（表 6）

- Water Pouring 41.6/38.5/79.2（时间 27.4/97.0/71.2）；Move Cube 51.5/86.7/97.6、时间 -59% 165.2→67.5、API -67% 14.4→4.7；Upright Bottle 16.9/37.9/74.6；Tabletop Tidying 31.2/65.5/92.5、API 23.5→9.9：表 6 + §3.3。
- 4 任务×30 试、50 示范/任务：§3.3。

## 05 RSI（表 3-5）

- LIBERO-Plus 99.4（RV-ICL 95.8、HarnessVLA 86.7、π0-FAST 61.6）：表 3。
- RoboDojo 48.62（HexaShell-Preview 46.85、GPT-6 Astra 22.48）：表 4。
- RoboCasa365 89.4（HexaShell 1.5 85.6、组合未见 84.8）：表 5。
- RSI 机制（练习滚动诊断→沉淀策略→迁移未见评测）：§3.2。

## 边界区

- 依赖流式 action expert 可微性：§2.1（对 flow velocity field 求梯度）。
- 真机仅 4 任务 30 试、50 示范重训骨干：§3.3。
- Astra/Sol 混合、成本未统一报告：§3 Setup。
- RoboDojo 精度维 4.0 vs 基线 7.8（引导非全维无代价）：表 2。
