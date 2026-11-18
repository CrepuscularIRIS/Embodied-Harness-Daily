# QA — 2611.21099

**状态：PASS（重做 1 次，用于修复 02 区三卡横向溢出后一次通过）**

## 渲染
- 工具链：google-chrome 156 headless。PNG：`--force-device-scale-factor=2 --window-size=1200,1700 --screenshot --hide-scrollbars`（2400×3400，1.30MB）；PDF：`--print-to-pdf --no-pdf-header-footer --virtual-time-budget=4000`（965KB，单页）。
- 终版文件：reel/2611.21099/poster.png、poster.pdf（HTML 留本地不入库，.gitignore 规则）。
- 注：本张首跑时几何脚本未触发（title 未更新），改用双保险触发（load 事件＋固定 4s 定时器）后正常取到结果；不影响渲染产物本身。

## 视觉检查
- 首检 BADCOUNT=3——02 区三层外骨骼卡横排三列导致 .col/.sec/.pr 三层横向文本溢出（sw 667/cw 557 等）。
- 唯一一次重做：.pr 由三列改单列纵向堆叠（三卡各占全宽），字号 11.9→12.3px、padding 8/10。复查 BADCOUNT=0，maxBottom 1537/1700（fill 90.4%），像素复测内容末行 3059/3400（正常页脚留白）。
- 目检（read_image 整图＋放大：02 三卡区、04 ForceBench SVG 条形）：无溢出、无裁切、无重叠；暖米色横线记录纸风与 19198（白底交接单）、19912（深色控制室）明显区分。

## 内容复核
- 所有数字来自表 3/4/5/6 与 §III，与 SOURCE.md 映射表一致；ForceBench 条形标注“示意”；标题中“力觉外骨骼”为本文机制的比喻表述（冻结模型＋外置三层结构），正文已说明不微调模型。
- 版式：实验室记录纸风（暖米色底＋衬线标题＋双线卡头＋红色批注），与现有 51 张 ready 及本期前两张不重复。

## 提交注意
- git add：poster.pdf、poster.png、SOURCE.md、QA.md（poster.html 被 .gitignore:193 忽略，留本地）。
