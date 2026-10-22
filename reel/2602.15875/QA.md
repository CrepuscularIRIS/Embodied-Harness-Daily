# QA · 2602.15875

状态：**ready**（已用 Read 实际查看渲染图；原文核对通过，展示结论已缩窄）

版式：分层栈（锁定层灰色“固定”徽标，唯一高亮的接口层内嵌 SR / 错误锁定双指标阶梯）。同期三篇版式结构不同：2311.13373 是阶段曲线，2411.00081 是网格加条形，2602.15875 是分层栈。三篇共用字体和色板。

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS + 内联 SVG，字体 Noto Sans CJK SC，本地系统字体，无外部资源）。
- PNG：`google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=1240,1754 --screenshot=poster.png file://$PWD/poster.html`（Google Chrome 155.0.8059.84）。
- PDF：`google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf=poster.pdf file://$PWD/poster.html`；`@page` 1240×1754 px，`pdfinfo` 确认 1 页。
- PDF 另用 `pdftoppm -r 40` 栅格化，与 PNG 并排比对版面一致。

## 视觉验收记录

- 第 1 次渲染：用 Read 打开全图检查，版面无裁切、无重叠。措辞问题：接口层写“从左到右”，实际是自上而下，已改；指令示例需注明出处。
- 第 2 次渲染：指令示例文字超出方框，已缩短。
- 第 3 次渲染：用 Read 复核全图和顶部裁图。框内文字完整，中文正常，PDF 1 页。
- 示意标注：图下注明“分层栈为自行绘制”，条形按 Table V 等比例绘制、从 0 起、表中未给区间。
- 事实复核：标题问题与原文 Table X“暂不可见目标”结果对应；限制栏写明同栈增益 +8.3、对 SPF 的 +23.7 混有栈差异、显著性检验不覆盖 Table V、错误物体可能被稳定锁定、依赖云端。顶部标签注明本篇代表无人机/导航簇，并由漏检抽查从 P2 上移到 P3。
- 小屏：标题、三张真机数字卡和 70.4 / 0.05 在缩略尺寸下可读；接口层内副标签约 13 px，需放大查看。

## 交付文件

`poster.png`（1240×1754）、`poster.pdf`（1 页）、`poster.html`（可编辑源）、`SOURCE.md`、`QA.md`。未生成视频或音频。

注：`poster.html` 被历史 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略，目前只在本地保留。正式发布时需单独处理这个文件路径，不要全局取消忽略。
