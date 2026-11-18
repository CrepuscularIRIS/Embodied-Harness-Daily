# QA — 2611.19198

**状态：PASS（重做 1 次，用于修复 h1 行高溢出后一次通过）**

## 渲染
- 工具链：google-chrome 156 headless。PNG：`--force-device-scale-factor=2 --window-size=1200,1700 --screenshot --hide-scrollbars`（2400×3400，1.48MB）；PDF：`--print-to-pdf --no-pdf-header-footer --virtual-time-budget=4000`（664KB，单页）。
- 终版文件：reel/2611.19198/poster.png、poster.pdf（HTML 留本地不入库，.gitignore 规则）。

## 视觉检查
- 首渲几何检查（注入脚本测 scrollSize/viewport-overflow/content-overflow）：BADCOUNT=1——h1 两行实际高度 92px 超 clientHeight 84px（overflow:hidden 会裁标题下缘）。
- 唯一一次重做：h1 字号 32→31、行高 1.32→1.30、加 padding-bottom 9px。复查 BADCOUNT=0（scrollSize 1200×1700，无越界、无文本溢出）。
- 目检（read_image 整图 2400×3400 + 三处放大：01 诊断 SVG、05 消融 SVG、底部边界栏+页脚）：无溢出、无裁切、无重叠；SVG 条形与 p 值标注、表格行、两列边界栏排版正常。

## 内容复核
- 所有数字来自表 I/II/III 与 §V-C/§VIII，与 SOURCE.md 映射表一致；示意条形均标注"示意"。
- 版式：货运交接单风（白底＋navy 左粗边卡＋gold 点缀），与现有 51 张 ready 及近三期（16246 俯视地图色带、14115 深色题带三闸链、13039 化验单）无重复。

## 提交注意
- git add：poster.pdf、poster.png、SOURCE.md、QA.md（poster.html 被 .gitignore:193 忽略，留本地）。
