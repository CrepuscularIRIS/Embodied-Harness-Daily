# 2611.22295 RICL — SOURCE

论文：*Similar Is Not Useful: In-Context Selection by Closed-Loop Utility*（arXiv 2611.22295v1，2026-11-17）。全部数字/断言映射到原文。

## 报头

| 海报断言 | 原文出处 |
|---|---|
| 冻结 π0-FAST 2.9B、LIBERO 第三方 port | §3 实验设置 |
| 19 任务 760 paired episodes、40 paired ep/格/任务 | §3、表 1 |
| top-5 效用池 66.4% vs dino 相似度 55.7% vs 随机 55.5% vs bottom 43.8% | 表 1 |
| top−dino +10.8pp，p=3.2e-6（exact McNemar） | 表 1 |
| dino−random +0.1pp（统计上即随机） | 表 1 |

## 机制图（§3 方法）

- 60 个固定大小 |S|=5 池、dino 随机分配：§3.1。
- pool-swap 控制消息（换出 1 条换入 1 条）：§3.2。
- 岭回归 λ=1 估计每条示范效用 φ̂，拟合 init 0-9、评测 init 10-49（不相交）：§3.3。
- 模型全程冻结，只动上下文池：§3。

## 为何相似度失效（§5）

- 任务内 pool 相似度与成功 Spearman 均值 0.10：§5.2。
- goal:9 的最近邻 57.5% 属于其它任务：§5.2。
- 共享场景不共享目标、两 goal 任务共享场景时池重叠 2.50/2.40 of 5（随机水平）：§5.2。

## 边界条件（§4.2 / 表 4）

- 池大小 3→+12.9pp、5→+11.8pp、10→+0.7pp（消失）：§4.2。
- vs shipped 20 池：top5 +7.0pp（p=0.006，560 paired）、rerank +4.5pp（p=0.055）：§4.2。
- 按相似度精选（curation）反而 −6.8pp：§4.2。

## 反直觉账（表 2）

- split-half Spearman 0.14（逐条排序不可靠，只有聚合排序可靠）：§4.3。
- top-minus-worst（删最差）无检出效果：§4.2。
- 六条中途被推翻的假设列表：表 2。
- 增益 2/3 来自选对最好（best-of-ten 直接搜索 100 rollouts）：§4.1。

## 边界区（论文自述限制 + 本席核对）

- 单一 checkpoint、单一第三方 port；另 3 个 checkpoint 未过 context-necessity 前置检查：§6 限制。
- 真机未测：§6。
- 7 任务研究 170 GPU-h（φ̂ 回归的评测预算成本）：§4.3。
- 机制解释限于观测相关（未做干预实验）：本席按 §5 表述注明。

## 页脚

- 「相似度检索回答哪个任务，闭环效用回答哪条示范」：本文概括 §5.3 结论，原文表述为 retrievers should be paired with outcome signals。
