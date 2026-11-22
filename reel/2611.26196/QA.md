# QA — 2611.26196（工序流转卡风）

## 版式

- 版式：工厂工序流转卡。深炭底 #24221e + 上下琥珀黑斜纹警示条 + 左上工序标签框（NO. 021-2）；与 020 三张（复式账簿 / 契约文书 / 深色天平）及本期 26613（米白对局复盘谱）不同源。
- 结构（上→下）：警示头条 → 工序标签 + 标题 → 接口契约三格 → S1/S2/S3 三道工序卡 → 轮次曲线（SVG 双线）→ 验收协议四格 → 病理警报 + 整改单 → 副指标三卡 | 边界 → 页脚。

## 渲染

- google-chrome headless，window-size 1200×1700、force-device-scale-factor=2 → poster.png 2400×3400；--print-to-pdf --no-pdf-header-footer → poster.pdf。

## 视觉检查（首检）

- 本期执行模型 glm-5.3 无图像输入，视觉 QA 采用程序化三件套（reel/qa-geo.js + reel/qa-extra.js + reel/qa-blank.py）替代目检，方法已在 selection-021.md 说明：
  - qa-geo：bodySW/SH=1200/1700，docSW/SH=1200/1700，overW=0、overH=0（无滚动溢出），wide=[]（无超宽元素）；9 个 [data-qa] 块边界全部在画布内。
  - qa-extra：clipped=[]（无文字裁切）、overlaps=[]（无非父子包含的重叠块）、fonts Noto Serif/Sans CJK 均加载。
  - qa-blank（2400×3400 PNG）：content_bottom=3399（100.0%）；仅两条带 rows 1212–1280（69px@2x）、rows 2071–2143（73px@2x），均位于图表卡内部深底（图例与曲线之间、轴标签与卡底边之间，约 35px@1x），为设计间距，非空洞；无 ≥60px@2x 的页面级空白带。

## 生产期迭代（判 fail 前的产出调整，不计重做）

1. 首渲内容偏短：底部 348px@1x 空 → 增「接口契约」三格条。
2. 二渲仍余 165px@1x → 增「验收协议」四格条；图表 SVG 由 360 加高至 440，消除图内空带。
3. 事实修正一处：600s 由「回合时限」改为「代码块超时」（见 SOURCE.md 修正记录），文字改动后重渲。

## 终版

- BAD=0：无溢出 / 无裁切 / 无重叠 / 无页面级空白带 / 字体加载 / content_bottom 100%。
- 判定：通过。计入本期发布（021-2）。