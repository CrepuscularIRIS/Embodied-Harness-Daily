# QA — 2611.34778（受控试验矩阵风 / 活页实验记录夹）

## 版式

- 版式：活页实验记录夹。冷灰 #e6ebec 底 + 左侧深青 #0f4c5c 活页脊（打孔、竖排英文）＋ 题头右侧深青统计卡；七行"替代方案 → 本文选择｜效应"矩阵（T1–T4 深青=从 VLM 出发、T5–T7 赭橙=从 VLA 出发）；下方左"能力匹配路由"2×2 格（示意）＋右 X-Harness 结果双条（灰=VLA 单独、青=Offline、斜纹=Semi-online）；赭橙虚线边界栏。与 019–021 期 9 张（深色数据实验台 / 横纹作业纸 / 深蓝绿终端 / 复式账簿 / 契约文书 / 深色天平双轨 / 对局复盘谱 / 工序流转卡 / 复古家电手册）及在库其余 56 张均不同源。
- 结构（上→下）：题头+统计卡 → §1 七次受控试验矩阵 → §2 能力匹配路由（左）/ X-Harness 组合结果（右）→ §3 边界 → 页脚。

## 渲染

- google-chrome 156.0.8078.79 headless：`--window-size=1200,1700 --force-device-scale-factor=2` → poster.png 2400×3400；`--print-to-pdf --no-pdf-header-footer` → poster.pdf（本篇 HTML 加 `@page{size:1200px 1700px;margin:0}`，单页 900×1275 pt，与 PNG 同比例；在库旧 PDF 为 Letter 两页）。
- 字体：本机 Noto Serif CJK SC / Noto Sans CJK SC（不联网加载）。

## 检查方法（程序化实检；本期执行模型 glm-5.4[1m] 无图像输入，未目检）

- 注入方式：把 reel/qa-geo.js 与 reel/qa-extra.js 的逻辑合并为一段脚本追加到 poster.html 副本末尾，结果写入 DOM 后用 `--dump-dom` 取回；另加 overflowAny（所有元素 scrollW/H vs clientW/H，不限 overflow 值）。qa-blank.py 直接扫 poster.png，并加一次去左脊裁切扫描（全高色脊使行标准差对页内空带不敏感，裁切后才能看见内容区空档）。

## 生产期迭代（判 fail 前的产出调整，不计重做；与 021 期 26196/26613 同一口径）

1. 渲 1：矩阵行内联元素在 flex 列容器里被拆成多行，.mx 容器被 overflow:hidden 裁切（clipped=1，scrollHeight 1327 vs clientHeight 523）——改块级排版。
2. 渲 2：子块改为不收缩后暴露自然高度，内容超页 417px（overH=417）——压缩七行文案与题头、字号回落。
3. 渲 3：overW/H=0、clipped=[]、wide=[]、overlaps 仅父子包含；但 bound 与页脚间留 111px@1x 空档（全图 qa-blank 因左脊未报，去脊裁切后可见）。

## 视觉检查（首检 = 渲 3）

- qa-geo：overW=0、overH=0，wide=[]；9 个 [data-qa] 块边界在画布内。
- qa-extra：clipped=[]、overlaps=[["mast","hstats"]]（父子包含）、字体加载。
- qa-blank（去脊裁切）：bound–foot 间 111px@1x 空档 → **判 fail**（页面级空白带）。

## 重做 1 次（计入）

- 整体字号上调 3–5%（h1 35→36、矩阵 12.1/11.9→12.5/12.4、路由格 11.9→12.3、边界 12.2→12.7 等）、章头间距 16→18；同一轮内 .hs .v 行高 1.1→1.3（overflowAny 4→0）。未改结构与文案。
- 复查（终版读数）：
  - qa-geo：bodySW/SH=1200/1700，docSW/SH=1200/1700，overW=0、overH=0，wide=[]；块边界 mast 28–302 / mx 341–901 / lower 970–1437 / bound 1491–1621 / foot 1634–1676。
  - qa-extra：clipped=[]、overlaps=[["mast","hstats",318,274]]（父子包含，设计如此）、fonts Noto Serif/Sans CJK 均加载、overflowAny=0。
  - qa-blank（全图）：content_bottom=3399/3400（100.0%），无 ≥60px@2x 空带；（去脊裁切）：content_bottom=3349/3400（98.5%，页脚下 24px@1x 内边距），无 ≥60px@2x 空带；bound–foot 空档收至 28px@1x。
  - PDF 单页。

## 终版

- BAD=0：无溢出 / 无裁切 / 无非父子重叠 / 无页面级空白带 / 字体加载 / 单页 PDF。
- 判定：程序化实检通过（重做 1 次后）；**pending_visual_qa**（未实开渲染图目检字体、中文断行与图例）。计入本期发布（022-1）。
