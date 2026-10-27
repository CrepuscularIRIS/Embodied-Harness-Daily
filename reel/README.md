# 精选 Reel

所有 Reel 仅来自 problem-core 评分入选、经 Opus 5.5 原文核对并完成实际视觉 QA 的论文。每次选择默认最多 9 篇，不为凑数制作。2026-10-22 之前的旧版成品已随 v3 重置归档。当前 24 张：18 张来自 run embodied-full-v11-20261022，6 张来自增量 run embodied-rolling-20261023-01（均为 problem-core-v1.1），按 paper_id 前缀分组、新者在前。

## Posters — recent 3 months（2608–2610）

| paper | 画报主题 | 版式 | 成品 |
|---|---|---|---|
| 2610.35817 | ZAP 只在仿真学“怎么动”：模型 × harness 两因素 | 训练流程带＋两因素格＋逐任务热格 | ✅ ready（QA passed） |
| 2610.34370 | ThinkLocoManip 把机身姿态做成 LLM 工具 | 工具域格＋双循环示意＋逐次试验方块 | ✅ ready（QA passed） |
| 2610.32348 | LogLook 系统记账、模型挑看：执行器会遮蔽记忆差异 | 记忆分工三栏＋分歧回合原因账本＋成本条 | ✅ ready（QA passed） |
| 2610.32941 | Backtrack 冻结 VLA 先倒回手臂再重试 | 机制时间带＋森林图＋恒等式热格 | ✅ ready（QA passed） |
| 2610.31841 | FORCA 编码智能体读腕部力迹改程序 | 双泳道迭代日志＋结果表 | ✅ ready（QA passed） |
| 2610.25376 | TILDE 教师接手后的状态也要蒸馏 | 状态分布示意＋区间点图＋错误状态方阵 | ✅ ready（QA passed） |
| 2610.27350 | 动作时不再拒绝——安全诊断 | 双栏对照 | ✅ ready（QA passed） |
| 2610.25114 | 自我改进收益拆解 | 收益成分拆解 | ✅ ready（QA passed） |
| 2610.15572 | AIDA 教师导航行为阶梯 | 递进阶梯 | ✅ ready（QA passed） |
| 2609.35318 | DexAgent 人视频→示范 | 视频→示范管线＋热力图 | ✅ ready（QA passed） |

## Posters — earlier（≤2607）

| paper | 画报主题 | 版式 | 成品 |
|---|---|---|---|
| 2603.26666 | VLA-OPD 用哪种蒸馏目标不训崩 | 曲线分岔＋目标卡 | ✅ ready（QA passed） |
| 2602.15875 | Fly0 只换目标接口 | 分层栈 | ✅ ready（QA passed） |
| 2512.02002 | 文本模拟替代动态仿真修码 | 双路径汇合 | ✅ ready（QA passed） |
| 2510.20328 | MemER 该记什么 | 条件矩阵 | ✅ ready（QA passed） |
| 2506.17811 | RoboMonkey 采样-验证-选择 | 流水线 | ✅ ready（QA passed） |
| 2506.06677 | RoboCerebra 分层瓶颈 | 分层瓶颈漏斗 | ✅ ready（QA passed） |
| 2501.11858 | EmbodiedEval 人与模型同接口鸿沟 | 接口流程＋配对鸿沟条 | ✅ ready（QA passed） |
| 2411.04549 | GVL 验证信号——进度分数在测什么 | 消融对比 | ✅ ready（QA passed） |
| 2411.00081 | PARTNR 人机合作反直觉 | 网格+数据条 | ✅ ready（QA passed） |
| 2409.01652 | ReKep 自动约束 vs 人工参照 | 三方对照台阶图 | ✅ ready（QA passed） |
| 2311.13373 | 会犯错的 LLM 教师 | 阶段曲线 | ✅ ready（QA passed） |
| 2309.09919 | Safety Chip 提示禁令 vs LTL 动作拦截 | 横向双车道拦截门 | ✅ ready（QA passed） |
| 2307.01928 | KnowNo 何时求助 | 不确定性决策流 | ✅ ready（QA passed） |
| 2306.15724 | REFLECT 先解释失败再纠正 | 时间轴＋解释/纠正双柱 | ✅ ready（QA passed） |

## 选择与制作

- L2 第一波后：91 篇 P3-confirmed 候选 → 同题去重 22 + 多样性截断 60 → 9 篇（2610.27350、2411.04549、2610.25114、2510.20328、2610.15572、2506.17811、2311.13373、2411.00081、2602.15875；记录见 run selections/selection-001.md）
- L2 第二波后：327 篇候选（to_l3 共 336，扣第一波已选 9）→ 同题去重 33 + 多样性截断 285 → 9 篇（其余 9 张；记录见 run selections/selection-002.md）
- 第二波所选 9 篇中 8 篇来自 L2 第二波 P2→P3 上移篇；唯一非上移篇 2307.01928（KnowNo）是第一波选择时留给求助槽的后备首选，第二波兑现
- 增量 run embodied-rolling-20261023-01 首次选题：5 篇 P3-confirmed 候选 → 同题去重 1（2610.30587 归入 2610.32941）＋多样性截断 1（2610.32348）→ 3 篇（2610.25376、2610.31841、2610.32941；记录见该 run selections/selection-003.md）；入选 3 篇原文核对无 L2 判断错误；另对未入选的 2610.30587 记 1 条 correction 退回 Sol 单篇修订（CRR 计数口径与 Algorithm 1 不一致）
- 增量 run 第四期选题：9 篇 P3-confirmed 候选 → 同题/同卡去重 3（33446→34370、33487→32348、33718）＋与前期已选重复 1（34108→2610.32941）＋暂停 1（34151，correction C004-1 退回 Sol：Q2 疑为 vertical_port）＋多样性截断 1（34649）→ 3 篇（2610.35817、2610.34370、2610.32348；记录见该 run selections/selection-004.md）；入选 3 篇原文核对无 L2 判断错误。视觉 QA：35817 重做一次后通过；34370（文字溢出 1 处）与 32348（标题限定语断行）重做一次后仍未过、先记 fail，经总控授权的唯一一轮额外单行修复后均通过（各篇 QA.md 记录全过程）
- 版式：18 张两两不重复（第三期 3 张亦与之前及彼此不重复）（各篇 QA.md 记录版式并与先前版式比对）
- 制作与核对：Opus 5.5 逐篇原文核对（第一波 3 处展示缩窄，均无判断错误退回；展示缩窄与措辞小注记于各篇 SOURCE.md），视觉 QA 实开渲染图
- `poster.html` 可编辑源被 .gitignore:193 忽略，保留本地；正式发布时按精确路径放行
- 数字与断言映射：各篇 SOURCE.md（节/表定位）
