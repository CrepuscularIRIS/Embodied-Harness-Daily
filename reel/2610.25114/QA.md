# QA · 2610.25114

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG；字体 Noto Sans CJK SC）
- PNG：headless Google Chrome 155.0.8059.84，`--force-device-scale-factor=2 --window-size=1200,1700 --screenshot` → 2400×3400
- PDF：同一 Chrome `--print-to-pdf --no-pdf-header-footer`，`@page 1200×1700px` → 1 页；`pdftoppm` 栅格化后查看

## 视觉检查（Read 工具实际打开 poster.png 与 PDF 栅格图）

- 第 1 次渲染发现：流程条下说明文字在右缘被截断；“148/150”贴住卡片右缘；“DeepSeek-flash”标签折成 4 行；页面底部约 250px 空白。已修：说明拆成两行、加宽执行者列、加入“编译阶段”四格事实条填补空白。
- 第 2 次渲染后补：标题加范围限定“（仿真 · 单任务 · 3 个 campaign）”，write-once 差值方向改写清楚，“128 布局”改为“其中 3 次扩到 128 个”。
- 终版：单页；中文完整；瀑布图坐标、柱值、campaign 点、p=0.125 标注均可读，无重叠；复用条与表格对齐；限制 1（p=0.125）与限制 2（仅仿真）以独立标签显式标出。

## 内容复核

- 标题限定范围后未超出 §7.4 / §8 原文结论（“most of the gap comes from inheriting… feedback adds a little more at the margin”）。
- “尝试选择”单独说明为共享规则，没有伪造成第三个数值成分。
- 148/150 与 147/150 并列，Wilson 区间与逐技能计数均给出；成本未与直接控制做盈亏比较。
- 布局：顶部流程条＋左侧收益瀑布拆解＋右侧复用/成本＋编译事实条＋双限制标签（与另两篇结构不同）。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 被仓库 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略：已保留在本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
