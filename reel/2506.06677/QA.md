# QA · 2506.06677 RoboCerebra

状态：**ready**（原文核对通过 + 实际视觉 QA 完成）

## 渲染路径

- 可编辑源：`poster.html`（单文件 HTML/CSS＋内联 SVG，无外部依赖；字体 Noto Sans CJK SC）。
- PNG：`google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,1700 --screenshot=poster.png file://…/poster.html` → 2400×3400。
- PDF：`google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=poster.pdf …`（`@page 1200×1700px`）→ 1 页，900×1275 pt。
- Google Chrome 155.0.8059.84；PDF 经 `pdftoppm -r 50` 栅格化后查看。
- 版式：**分层瓶颈漏斗**（100 → GT-plan → GPT-4o → Blind → 无规划器，每层右侧注明丢失量与原因），与 s001 及本期其他篇不同。

## 视觉检查（Read 实际打开 poster.png 与 PDF 栅格图）

- 第 1 次渲染：漏斗“去掉画面”注释行末 “(11.87 vs 11.19)” 被右缘裁切；“−10.53” 与虚线引线重叠。已缩短注释文字、把 −10.53 移到漏斗左侧、引线起点右移。
- 终版：单页；中文无豆腐块、无裁切；漏斗四层数字 30px，缩小到 50% 仍清楚；表格高亮 SFT 行可辨；底部约 80px 留白，不影响阅读。

## 内容复核

- 标题“直接给它正确的计划，成功率也只有 25%”对应 Table 4 GT-plan 25.16；SR 为部分得分已在设置条与边界中写明。
- “低层是主约束”写为“先卡住了上限”，并在边界注明 GT-plan 非完全隔离、anchor 不测自主停止、无方差、仅仿真。
- 剩余问题：无。

## 提交注意

- `poster.html` 被仓库 `.gitignore`（`reel/*/poster.html`）忽略：已保留本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
- 未更新 `reel/README.md` 与 selection-002 核对状态（与并行组共享，交总控）。
