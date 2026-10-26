# QA · 2610.31841

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG；字体 Noto Sans CJK SC）
- PNG：headless Google Chrome（`--headless=new --force-device-scale-factor=2 --window-size=1200,1700 --screenshot`）→ 2400×3400
- PDF：同一 Chrome `--print-to-pdf --no-pdf-header-footer`，`@page 1200×1700px` → 1 页；`pdftoppm` 栅格化后查看

## 视觉检查（Read 工具实际打开 poster.png 与 PDF 栅格图）

- 第 1 次渲染：不通过。内容高 1766px 超出页面（PDF 2 页）；kicker 折行；顶部流程格中 `<b>` 被设为块级，导致“执行中 / 不调用 / 基础模型”断成三行。
- 重做一次：时间线行高与泳道间距压缩、kicker 缩短、流程格标题改用独立类名；内容高 1655px。
- 终版：单页；中文完整；两条泳道 20 个迭代点、装置故障框、▲修订标记与下方说明对应；结果表 5 行数值与子指标可读；限制框 3 条完整。

## 内容复核

- 标题限定“UR5e 真机 · 5 任务 · 每项 10 次”；未写成通用控制学习或无人工。
- 明确只有一条开发链、力与诊断同时改变、人负责场景；敲方块单列为无对照、仅报迭代数。
- 版式：双泳道迭代日志（开发过程本身作为机制图）＋结果对照表＋成本格，与前 18 张及本期另两张不同。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 被仓库 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略：已保留在本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
