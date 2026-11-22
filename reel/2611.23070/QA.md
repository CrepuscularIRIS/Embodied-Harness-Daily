# QA — 2611.23070（复古家电手册风）

## 版式

- 版式：复古家电使用与检定手册。暖米黄 #f7efdc 底 + 双层描边（实线/虚线）+ 锈橙 #bf5b2a 与湖蓝 #33708c 双色；型号铭牌、圆形检定戳、§1–§7 章节编号、条纹警示边。与 020 三张及本期 26613（米白对局谱）、26196（深炭工序卡）均不同源。
- 结构（上→下）：铭牌+手册头（含 0.0% 检定戳）→ §1 出厂规格六格 → §2 用户习性三卡 → §3 主检定 0.0% 警示框 → §4 加装模块三卡 → §5 双瓶颈对照（条图+刻度 / 规划器排行）→ §6 通道选择三卡 → §7 保修范围（边界）→ 页脚。

## 渲染

- google-chrome headless，window-size 1200×1700、force-device-scale-factor=2 → poster.png 2400×3400；--print-to-pdf --no-pdf-header-footer → poster.pdf。

## 视觉检查（首检）

- 程序化三件套（qa-geo / qa-extra / qa-blank；本期执行模型 glm-5.3 无图像输入，方法说明见 selection-021.md）：
  - qa-geo：overW=0、overH=0，wide=[]；16 个 [data-qa] 块边界全部在画布内。
  - qa-extra：clipped=[]、overlaps=[]、fonts Noto Serif/Sans CJK 加载。
  - qa-blank：content_bottom=3379/3400（99.4%），全程无 ≥60px@2x 空带。

## 生产期迭代（判 fail 前的产出调整，不计重做）

1. 首渲即通过全部程序检查；随后修一处图例瑕疵：对照条图例写「灰条=无 API」但未渲染灰条，改为「虚线刻度=无 API 读数」。
2. 刻度元素初版上下超出条高 3px，被条形容器 overflow:hidden 裁切（程序检查报 clipped=2）；改为条内满高后复检 clipped=0。

## 终版

- BAD=0：无溢出 / 无裁切 / 无重叠 / 无页面级空白带 / 字体加载 / content_bottom 99.4%（foot 钉在页底）。
- 判定：通过。计入本期发布（021-3）。