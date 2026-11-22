# 2611.26613 AgentRoboCritic QA 记录

## 版式
对局复盘谱风（米白谱纸+双线框+圆形朱砂章"复盘谱·局 021"+棋盘格谱面带落子①–⑤+五手谱注+意图有无左右对照（墨底 vs 纸底）+失败七式 4×2 词表+恢复不对称四格+墨底开源卡+朱砂虚线边界栏）。与本期 26196（工序流转卡）、23070（复古家电手册）及近三期（017 记录纸/控制室/交接单、018 报纸/蓝图/审计报告、019 实验台/作业纸/终端演化、020 复式账簿/契约文书/深色天平）和在库 62 张均不重复。

## 渲染
- google-chrome headless：`--window-size=1200,1700 --force-device-scale-factor=2` → poster.png 2400×3400；`--print-to-pdf --no-pdf-header-footer` → poster.pdf。
- 生产期迭代（均在 QA 判定前）：初版内容止于 1266/1700 偏短 → 增"失败七式"词表、放大字号、page 改 flex 列钉住页脚、块间距 20→26px；核对原文修正两处口径（Cost 列为 400 动作测试集整体花费，非"每千动作"；">90%"为复检计入后与人工一致率，非接受率）。以上为代码与事实修正，不计入重做。

## 视觉检查（2026-11-22，glm-5.3）
- 本执行模型无图像输入，目检以程序化视觉检查替代并实际运行于渲染结果：
  - qa-geo.js（DOM 几何）：bodySW/SH=1200/1700，overW=0、overH=0，wide=[]（无元素越界）。
  - qa-extra.js（本次新增）：clipped=[]（所有 overflow≠visible 元素 scrollW/H≤clientW/H+2，无文字裁切）；[data-qa] 块间唯一重叠为 board⊇moves 父子包含（设计如此）；document.fonts.check 确认 Noto Serif CJK SC / Noto Sans CJK SC 均已加载（中文正常渲染）。
  - qa-blank.py（PNG 空带）：2400×3400，content_bottom=3367（99.0%），无 ≥60px 空带。
- 版面节奏：mast 34–192 → 谱面 243–615 → 意图对照 641–833 → 七式词表 859–1076 → 恢复 1102–1334 → 开源/边界 1360–1553 → 页脚 1644–1670。

## 终版
- 首检即过（BAD=0，零重做）。poster.html 留本地（.gitignore:193），其余 4 件提交。
