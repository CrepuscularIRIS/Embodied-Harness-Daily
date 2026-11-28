# QA — 2611.31894（取芯剖面风 / 钻探取芯记录）

## 版式

- 版式：钻探取芯记录。石灰 #f1efe9 底 + 顶部深板岩 #22303c 题头带（赭橙底线、右侧三枚大数）；五段工序做成由深到浅的地层条（Rebuild 板岩 → Examine 青灰 → Self-improve 青 → Execute 浅青 → Transfer 赭橙）；主结果左条形图（青 = RESET）+ 右"仿真 vs 真机"四机器人格；缺陷注入表用"取芯格"（实心赭 = 被打破、斜纹青 = Examine 标出）；两张赭橙警示卡 + 一张青卡；板岩虚线边界栏。与本期 34778（活页实验记录夹）、019–021 期 9 张及在库其余 56 张均不同源。
- 结构（上→下）：题头+三数 → §1 五段工序 → §2 主结果（条形 + 跨本体格）+ 拷贝对照三卡 → §3 错的世界取芯表 + 三警示卡 → §4 边界 → 页脚。

## 渲染

- google-chrome 156.0.8078.79 headless：`--window-size=1200,1700 --force-device-scale-factor=2` → poster.png 2400×3400；`--print-to-pdf --no-pdf-header-footer` → poster.pdf（HTML 加 `@page{size:1200px 1700px;margin:0}`，单页 900×1275 pt）。
- 字体：本机 Noto Serif CJK SC / Noto Sans CJK SC（不联网加载）。

## 检查方法（程序化实检；本期执行模型 glm-5.4[1m] 无图像输入，未目检）

- qa-geo / qa-extra 逻辑合并注入 poster.html 副本、`--dump-dom` 取回；另加 overflowAny；qa-blank.py 扫 poster.png（本篇无全高色脊，全图扫描即可）。

## 生产期迭代（判 fail 前的产出调整，不计重做；与 021 期口径一致）

1. 渲 1：内容偏短——bound–foot 间 317px@2x 空带；题头底距（22+8）与章头间距合成 104px@2x 纯色带；h1 与三枚大数字行高过紧（overflowAny 4 处，overflow visible 不裁切）。
2. 渲 2：增"拷过去的是世界和判据，不是代码"三卡条、字号微调、行高 1.32 / 1.3 → overflowAny=0、底部空带消失；仍余 72px@2x 纯色带（题头底距 + 底线 + 章头间距）。
3. 渲 3：题头底距 12→4、首个章头间距 14→10 → 纯色带消失。
4. 渲 4：取芯表补回原文 Table 2 的"物体缩小 ×0.8–×0.9"行（打破 1/12、标出 11/12），使打破 / 标出计数之和与正文 16 / 13 对齐；行内边距收紧后总高不变。

## 视觉检查（首检 = 渲 3，终版读数）

- qa-geo：bodySW/SH=1200/1700，docSW/SH=1200/1700，overW=0、overH=0，wide=[]；12 个 [data-qa] 块边界全部在画布内（mast 0–257 / stages 308–511 / row2 562–891 / transfer 903–1032 / core 1083–1348 / warns 1381–1503 / bound 1554–1641 / foot 1650–1676）。
- qa-extra：clipped=[]、overlaps=[]、fonts Noto Serif/Sans CJK 均加载、overflowAny=0。
- qa-blank（全图与去脊裁切同）：content_bottom=3349/3400（98.5%，页脚下 24px@1x 内边距），无 ≥60px@2x 空带。
- PDF 单页。

## 终版

- BAD=0：无溢出 / 无裁切 / 无重叠 / 无空白带 / 字体加载 / 单页 PDF；首检即过，零重做。
- 判定：程序化实检通过；**pending_visual_qa**（未实开渲染图目检字体、中文断行、取芯格与图例）。计入本期发布（022-2）。
