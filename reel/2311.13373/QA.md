# QA · 2311.13373

状态：**ready**（已用 Read 实际查看渲染图；原文核对通过，展示结论已缩窄）

版式：阶段曲线（λ 日程带 + 学习曲线示意 + 收敛表）。同期三篇版式结构不同：2311.13373 是阶段曲线，2411.00081 是网格加条形，2602.15875 是分层栈。三篇共用字体和色板。

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS + 内联 SVG，字体 Noto Sans CJK SC，本地系统字体，无外部资源）。
- PNG：`google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=1240,1754 --screenshot=poster.png file://$PWD/poster.html`（Google Chrome 155.0.8059.84）。
- PDF：`google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf=poster.pdf file://$PWD/poster.html`；`@page` 1240×1754 px，`pdfinfo` 确认 1 页。
- PDF 另用 `pdftoppm -r 40` 栅格化，与 PNG 并排比对版面一致。

## 视觉验收记录

- 第 1 次渲染：页脚被裁出画面；λ 衰减标签压在 λ 线上；“从零 PPO”标签压在分层 RL 虚线上；教师标签与分层 RL 虚线交叉；表格单元格换行；PDF 溢出成 2 页。已逐项修正（移动标签、加宽结果栏、缩小表格字号与间距、固定页面高度）。
- 第 2–3 次渲染：用 Read 打开 poster.png 全图和曲线区域裁图复核。无裁切，无文字重叠，中文无缺字或方框，表格单行显示，PDF 1 页。
- 示意标注：曲线下方注明“曲线形状为自行绘制，不是原文 Fig.3 数据”。
- 事实复核：标题“会犯错的教师 / 少走弯路 / 反超”与原文一致；反超对象限定为 LLM 教师，限制栏写明分层 RL 收敛水平相近、SimpleDoorKey 未反超、仅仿真；正文与附录教师数值不一致处已注明。
- 小屏：整页缩到手机宽度约 400 px 时，标题、阶段名和 0.77 vs 0.52 仍可辨认；表格与注释需放大查看。底部约 120 px 留白，可接受。

## 交付文件

`poster.png`（1240×1754）、`poster.pdf`（1 页）、`poster.html`（可编辑源）、`SOURCE.md`、`QA.md`。未生成视频或音频。

注：`poster.html` 被历史 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略，目前只在本地保留。正式发布时需单独处理这个文件路径，不要全局取消忽略。
