# QA · 2610.37196

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG；字体 Noto Sans CJK SC）
- PNG：headless Google Chrome（`--headless=new --force-device-scale-factor=2 --window-size=1200,1700 --screenshot`）→ 2400×3400
- PDF：同一 Chrome `--print-to-pdf --no-pdf-header-footer`，`@page 1200×1700px` → 1 页
- 渲染前用注入脚本的临时副本（/tmp）测元素溢出与内容底边，仅作排版辅助，不计为视觉验收。

## 视觉检查（Read 工具实际打开 poster.png 全图与斜率图局部）

- 第 1 次渲染：不通过。标题限定语过长，“Cosmos Policy 上验证）”单独掉到第二行；“两种神谕”示意图底注与斜率图 CI 底注各一行过长、右端被裁。
- 重做一次：标题限定语缩为“（仅仿真）”，“选择器仅在 Cosmos Policy 上验证”移入 kicker 行；两处底注各拆两行并加高 SVG。
- 终版：单页；标题一行完整；网格示意 ✓ 与两个神谕说明框清楚；份额区间条三行数字可读；结构化余量点线（Streaming 红色空心点标“未通过”）可读；斜率图四条线标签不重叠、CI 两行完整；预登记 24 格颜色与编号清楚。页底留白约 130 px（排版松，不影响阅读，记为剩余问题）。

## 内容复核

- 标题限定“仅仿真”，kicker 限定“选择器仅在 Cosmos Policy 上验证”。
- 负面与边界在场：8 项预登记不支持（逐项列出主要几项）；物体布局扰动 −1.3；未见任务仅一种扰动类别；Streaming-WAM 结构余量首轮未通过；排序器是否需要想象信号未单独证实；无实际耗时；部分检验事后登记。
- 版式：分支网格示意＋份额区间条＋点线＋斜率图＋预登记记分牌，与前 24 张及本期另两张不同。
- 剩余问题：页底留白约 130 px。

## 提交注意

- `poster.html` 被 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略，保留本地；正式发布时由总控按精确路径处理。
