# QA — 2611.30550（配对流转双岸风 / 船闸式流转图）

## 版式

- 版式：配对流转双岸。暖纸 #f7f4ec 底 + 靛蓝 #1e2a4a 左粗边题头与右侧深靛"恒等式卡"；四步流程卡（递话 → 看进展 → 改写 → 接管→交还，末卡赭红底）；核心为按配对计数绘制的左右双岸流转图（深靛 = 保留、赭红 = 弄丢、苔绿 = 救回、浅灰 = 两边都败）＋右侧"无 VLM 对照"卡；五策略哑铃卡；迁移对照条（中线为 0，绿正红负）与收益构成三格；靛蓝虚线边界栏。与本期 34778（活页实验记录夹）、31894（取芯剖面）及 019–021 期 9 张、在库其余 56 张均不同源（在库深色天平双轨 26414 为深底双轨对照，本篇为浅底流转图）。
- 结构（上→下）：题头+恒等式卡 → §1 四步流程 → §2 配对流转图 + 无 VLM 对照 → §3 五策略 → §4 迁移对照 + 收益构成 → §5 边界 → 页脚。

## 渲染

- google-chrome 156.0.8078.79 headless：`--window-size=1200,1700 --force-device-scale-factor=2` → poster.png 2400×3400；`--print-to-pdf --no-pdf-header-footer` → poster.pdf（HTML 加 `@page{size:1200px 1700px;margin:0}`，单页 900×1275 pt）。
- 字体：本机 Noto Serif CJK SC / Noto Sans CJK SC（不联网加载；SVG 文本同样指定本机字体）。

## 检查方法（程序化实检；本期执行模型 glm-5.4[1m] 无图像输入，未目检）

- qa-geo / qa-extra 逻辑合并注入 poster.html 副本、`--dump-dom` 取回；另加 overflowAny；qa-blank.py 扫 poster.png（无全高色脊，全图扫描即可）。

## 生产期迭代（判 fail 前的产出调整，不计重做）

1. 渲 1：内容超页 22px（overH=22，.inner scrollHeight 1722）；流转 SVG 640×460 使 §2 达 561px；一处 SVG 标签与"113/200"大数字行高过紧（overflowAny 3 处）。
2. 渲 2：流转图等比缩至 640×396、标签缩短、行高 1.2→1.3 → overH=0、overflowAny=0。

## 视觉检查（首检 = 渲 2，终版读数）

- qa-geo：bodySW/SH=1200/1700，docSW/SH=1200/1700，overW=0、overH=0，wide=[]；13 个 [data-qa] 块边界全部在画布内（mast 28–264 / flow 317–464 / pair 517–1015 / pol 1068–1186 / mig 1239–1477 / bound 1530–1616 / foot 1634–1676）。
- qa-extra：clipped=[]、overlaps=[["mast","eq",340,236]]（父子包含，设计如此）、fonts Noto Serif/Sans CJK 均加载、overflowAny=0。
- qa-blank（全图与去脊裁切同）：content_bottom=3349/3400（98.5%，页脚下 24px@1x 内边距），无 ≥60px@2x 空带。
- PDF 单页。

## 终版

- BAD=0：无溢出 / 无裁切 / 无非父子重叠 / 无空白带 / 字体加载 / 单页 PDF；首检即过，零重做。
- 判定：程序化实检通过；**pending_visual_qa**（未实开渲染图目检字体、中文断行、流转图色带与标签）。计入本期发布（022-3）。
