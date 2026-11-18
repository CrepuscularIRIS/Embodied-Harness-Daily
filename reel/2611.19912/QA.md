# QA — 2611.19912

**状态：PASS（重做 1 次，用于修复底部大面积空白后一次通过）**

## 渲染
- 工具链：google-chrome 156 headless。PNG：`--force-device-scale-factor=2 --window-size=1200,1700 --screenshot --hide-scrollbars`（2400×3400，1.25MB）；PDF：`--print-to-pdf --no-pdf-header-footer --virtual-time-budget=4000`（637KB，单页）。
- 终版文件：reel/2611.19912/poster.png、poster.pdf（HTML 留本地不入库，.gitignore 规则）。

## 视觉检查
- 首渲几何检查 BADCOUNT=0（无溢出），但像素级填充测量发现内容只到 2515/3400（fill 74%），底部空白 442 CSS px——海报下半大片空背景，视觉不平衡，判不通过。
- 唯一一次重做：全局放大（h1 34px、正文 14–15px、区块 padding 15–17px、lim 13.8px 等 22 处替换）。复查 BADCOUNT=0，maxBottom 1551/1700（fill 91.3%），像素复测内容末行 3083/3400（底部余 158 CSS px，正常页脚留白）。
- 目检（read_image 整图＋放大：01 授权时间线 SVG、04 消融表）：无溢出、无裁切、无重叠；深色控制室风与浅色 19198 明显区分。

## 内容复核
- 所有数字来自表 I/II 与 §VI/§VI-B，与 SOURCE.md 映射表一致；授权生命周期条标注为机制示意。
- 版式：调度控制室风（深色面板＋amber/cyan 双色编号＋等宽时间戳元素），与现有 51 张 ready、19198（货运交接单风）、近三期均不重复。

## 提交注意
- git add：poster.pdf、poster.png、SOURCE.md、QA.md（poster.html 被 .gitignore:193 忽略，留本地）。
