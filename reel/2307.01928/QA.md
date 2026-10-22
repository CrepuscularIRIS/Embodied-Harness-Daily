# QA · 2307.01928

状态：**ready**（已用 Read 实际打开 poster.png 与 PDF 栅格图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG，无外部依赖；字体 Noto Sans CJK SC）
- PNG：`google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,1700 --screenshot=poster.png file://…/poster.html` → 2400×3400
- PDF：`google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=poster.pdf file://…/poster.html`（`@page 1200×1700px`）→ 1 页，900×1275 pt；`pdftoppm -r 50` 栅格化后查看

## 视觉检查

- 第 1 次渲染发现：流程图底部“示意”说明第二行贴着 SVG 下边缘被截；页眉写了“CoRL 2023 版”，缓存原文未标会议，属我们添加；边界中“被问烦”为原文没有的说法。已修：SVG 视框加高；页眉改为 v2 日期；边界改为原文 §5/§6 的表述。
- 终版：单页 PDF 与 PNG 一致；中文无豆腐块；无裁切、无重叠；阈值虚线正好落在 0.08 与 0.41 之间，与“集合 2 项”一致；配色（KnowNo 蓝、Simple Set 灰、不求助土黄）在条形与表格中一致；最小字号 12px，2× PNG 中可读。
- 小瑕疵：右侧“保证链”卡片下方与左侧流程图底部有少量留白，不影响阅读。

## 内容复核

- 标题“只在拿不准时开口 / 按用户要的成功率校准”对应原文 uncertainty alignment 的两条要求（calibrated confidence、minimal help）；保证对象在画报中明确限定为“规划正确率”，不写成任务成功或安全保证。
- 主对照在规划成功率对齐（0.87）的条件下比较求助率 0.67 vs 0.81，并同时展示任务成功、集合大小与不求助基线。
- 布局：左侧自上而下的决策流（阈值条＋菱形分支）＋右侧校准与保证链，下方整宽对照块。与 s001 九种版式及本组另两篇不同。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 若被仓库 `.gitignore` 的 `reel/*/poster.html` 规则忽略，则保留在本地；正式发布时由总控按精确路径处理，不全局取消忽略。
