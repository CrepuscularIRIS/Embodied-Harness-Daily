# QA · 2411.04549（GVL）

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG；字体 Noto Sans CJK SC）
- PNG：headless Google Chrome 155.0.8059.84，`--force-device-scale-factor=2 --window-size=1200,1700 --screenshot` → 2400×3400
- PDF：同一 Chrome `--print-to-pdf --no-pdf-header-footer`，`@page 1200×1700px` → 1 页；`pdftoppm` 栅格化后查看

## 视觉检查（Read 工具实际打开 poster.png 与 PDF 栅格图）

- 第 1 次渲染：内容超出 1700px，页脚被截、PDF 为 2 页。已缩小标题字号、节间距，固定直方图与点图高度。
- 终版：单页；中文完整；直方图图例、坐标（VOC −1/0/1）、“示意”声明可见；真机点图 7 行无重叠，两个负结果行用红底标出；表格对齐。最小字号约 11px（首帧方块内“=0%”），2× PNG 中可辨认，属装饰性标注。
- 左下“关键动作”框与左中仿真卡下方有少量留白，不影响阅读。

## 内容复核

- 标题“按顺序看视频只会说越来越好；打乱帧才看得出失败”对应 §3–§4.4 的消融结论，限定为该 VLM 设置下的现象，未宣称普遍价值函数。
- 负结果（open-drawer 6→4、remove-gears 7→4.67）完整呈现并给出作者解释为“未单独验证”。
- 布局：上方机制条＋中部“去掉打乱 vs 打乱”消融对照＋下方两项下游结果（与另两篇结构不同）。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 被仓库 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略：已保留在本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
