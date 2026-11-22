# SOURCE — 2611.26196 EmbodyAgent：后训练全栈（poster 021-2）

- 论文：EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and Reinforcement Learning（arXiv 2611.26196v1，2026-11-19）
- 全文：research/fulltext/2611.26196.txt（全文 24 行长行；下表行号即该文件行号）
- L2 记录：batches/inc-l2-17.jsonl（cards: offline_harness_distillation + harness_native_rl + teacher_seeded_sparse_rl；轴 F0/F1；capability/new_bottleneck；已逐条核对一致）

## 画报断言 → 原文位置

| # | 画报断言 | 原文位置 | 原文关键语 |
|---|---|---|---|
| 1 | 头条：0/100 → 84/100（held-out 100 测试态） | L6（Abstract） | 'held-out success on 100 test states rises from 0/100 (base 9B VLM) to 14/100 (after SFT) and 84/100 (after RL)' |
| 2 | 接口契约：env.observation() 主相机+双腕+本体；env.action(a) a∈[-1,1]^7 无动作解码器；think-then-code 全程不变 | L9（§1）、L12（§3） | 接口描述与 'no change to the think-then-code interface'（L15 §4 开头复述） |
| 3 | S1 黑盒教师：Astra Medium，1,620 试次 → 100 验证 episodes / 1,475 目标，32% 接受率，1,887 s/ep 一次性成本 | L12（§3） | '1,620'、'1,475'、'32%'、'1,887' 均在该行 |
| 4 | S2 SFT：0→14/100；底座全格式无效；失败 85/86 耗尽预算 | L6（Abstract）、L9（§1） | '0/100 \to 14/100'；底座格式无效与预算耗尽叙述 |
| 5 | S3 GRPO：14→84/100；DAPO 非对称裁剪 (0.2, 0.28)；G=8；无 KL；lr 2e-6；sixteen PPU 加速器 | L15（§4.1） | '(\varepsilon_lo, \varepsilon_hi)=(0.2, 0.28)'、'G=8'、'no KL penalty'、'2\times 10^{-6}'、'sixteen PPU' |
| 6 | 病理：traceback 进历史 h_t 获正组优势自增强；轮 11–20 错误 <5/100；轮 21 激增并平台于 63–69（轮 24–32）；成功 40→34；聚合成功滞后指标（连升六轮） | L18（§5.2）、L21（§6） | 'runtime errors surge and plateau at 63–69 per 100 across rounds 24–32, pulling held-out success…'；'Aggregate success rate is a lagging indicator…continued rising for six rounds' |
| 7 | 整改单：成功格每错误 −0.05·k_i（保序：任何成功 ≥0.8 > 任何失败 ≤0）；不可解析重采 ≤2；4 个错误格截断；>1M token episode ≤3 次重 roll；仅训练期生效；错误 69→14、成功 mid-30s→84 | L15（§4.1 奖赏 + §4.2 保障）、L18（§5.2） | 奖赏三段式定义；'per-error'；'one million'；训练期 'strictly during training sampling'；轮 64 后 69→14 |
| 8 | 曲线图：红=每百 episode 运行时错误、绿=held-out 成功 %；标注点（<5、63–69、40→34、→14、→84）为原文数值，连线为示意 | L18（§5.2）、L6（Abstract） | 同 #6；图为示意连线（已标注） |
| 9 | 验收协议：10 个 LIBERO Spatial 任务，30 训练/10 验证/10 测试严格不相交初始态；greedy（温度 0）；预算 2,000 仿真步 / 150 次模型调用 / 600s 代码块超时；单 run 二项 SE ±3.7pt | L18（§5.1）、L21（§6） | '2,000 simulator steps, 150 model calls, 600-second code-block timeout'；'\pm 3.7 points' |
| 10 | 副指标：train rollout 成功 8.4%→87.7%；median 模型调用 36→11；成功 episode 136s | L6（Abstract）、L18（§5.3） | 'median model calls per episode drop from 36 to 11'；'136' 在 L18 |
| 11 | 边界：单 suite（LIBERO-Spatial）单 run；task 4 仅 0/10→4/10；整改三件套联合生效未拆消融；1,887 s/ep 教师成本未折进对比账 | L18（§5.1/5.2）、L21（§6 Limitations） | 'task 4 rises from 0/10 to 4/10'；限制自述 |

## 展示缩窄（相对原文的取舍）

- 三阶段各只保留一条主数字链（0→14→84），训练超参只列 DAPO 裁剪、G、KL、lr、硬件五项，其余（vLLM、ZeRO-3、flash-linear-attention、温度 1 采样、32 组信息组过滤、基础设施错误重采排除）从略。
- 病理→整改只画「错误曲线 + 聚合成功滞后」一条主叙事；§4.2 的快败地板 −0.2（50 步内失败）未单独上画，仅保留于奖赏保序说明。
- 副指标三卡是原文摘要/实验的直引；「无轮数惩罚」指奖赏中不含调用次数项（据 §4.1 奖赏定义），调用下降 36→11 非惩罚所致——此因果表述为本文归纳，原文未用该措辞。
- 12 基准对照、与 GO-3 等外部基线的横向比较原文未做（单 suite），画报不引入外部基准数字。

## 事实修正记录（生产期，未计重做）

- 600s 初稿写作「回合时限」，核对 L18 后改为「代码块超时」（600-second code-block timeout）。