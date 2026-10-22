# QA · 2411.00081

状态：**ready**（已用 Read 实际查看渲染图；原文核对通过，展示结论已缩窄）

版式：网格 + 条形（反直觉步数条形为主图，2×2 受控维度格）。同期三篇版式结构不同：2311.13373 是阶段曲线，2411.00081 是网格加条形，2602.15875 是分层栈。三篇共用字体和色板。

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS + 内联 SVG，字体 Noto Sans CJK SC，本地系统字体，无外部资源）。
- PNG：`google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=1240,1754 --screenshot=poster.png file://$PWD/poster.html`（Google Chrome 155.0.8059.84）。
- PDF：`google-chrome --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf=poster.pdf file://$PWD/poster.html`；`@page` 1240×1754 px，`pdfinfo` 确认 1 页。
- PDF 另用 `pdftoppm -r 40` 栅格化，与 PNG 并排比对版面一致。

## 视觉验收记录

- 第 1 次渲染：底部大块留白；条形图字号偏小；“测试集 2668”标签压在单人基准虚线上；“ConceptGraph”标签紧贴格边。已放大条形图和字号，文字加白描边，加宽感知列。
- 第 2 次渲染：“测试集 4080”被裁出右边界。已扩大 viewBox 宽度。
- 第 3 次渲染：用 Read 打开全图和两处裁图复核。无裁切、无重叠，ConceptGraph 完整显示，中文正常，图例完整，PDF 1 页。
- 事实复核：条形 0 起点按真实比例绘制；标题“反而更慢”有限定：条形图注和限制栏写明测试集中微调 8B 反而更快、ReAct 仅慢约 4%，并写明真人在仿真中操作、成功率含重试、正文与附录数字不一致处用表值。
- 小屏：标题与四根主条形数值在缩略尺寸下可读；格内配置标签需放大查看。底部约 150 px 留白。

## 交付文件

`poster.png`（1240×1754）、`poster.pdf`（1 页）、`poster.html`（可编辑源）、`SOURCE.md`、`QA.md`。未生成视频或音频。

注：`poster.html` 被历史 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略，目前只在本地保留。正式发布时需单独处理这个文件路径，不要全局取消忽略。
