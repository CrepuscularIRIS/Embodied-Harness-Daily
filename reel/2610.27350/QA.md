# QA · 2610.27350

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG，无外部依赖；字体 Noto Sans CJK SC，本机 `/usr/share/fonts/opentype/noto/`）
- PNG：`google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,1700 --screenshot=poster.png file://…/poster.html` → 2400×3400
- PDF：`google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=poster.pdf file://…/poster.html`（`@page 1200×1700px`）→ 1 页，900×1275 pt
- Google Chrome 155.0.8059.84；PDF 用 `pdftoppm` 栅格化后查看

## 视觉检查（Read 工具实际打开 poster.png 与 PDF 栅格图）

- 第 1 次渲染发现：右栏卡片被画布右缘裁切（SVG 固定宽度撑破 grid 列）；“15/15”大号数字的斜线压到下方 Wilson 区间文字；PDF 溢出为 2 页。已修：列改 `minmax(0,1fr)`、SVG 自适应宽度、调整行高与边距。
- 第 2 次渲染发现：左栏“示意”说明文字贴住“才进入动作循环”框。已移到左侧空白处。
- 终版：单页 PDF；中文字形完整、无豆腐块；无裁切；两栏左右对称，STOP/循环示意清楚；数字字号在 1200px 宽缩小查看时仍可读；最小字号 12px（SVG 内示意标注），在 2× PNG 中可读。

## 内容复核

- 标题“问它时拒绝，让它做时照做”对应原文标题与 §4 结论，未超出。
- 15 次、单台 SO-101、单模型单 harness、离线首帧问询（反事实）、未比较安全提醒 prompt，均在“边界”框显式标注。
- 布局：左右双栏对照（本期三篇中唯一的对称双栏结构）。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 被仓库 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略：已保留在本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
