# QA · 2501.11858

状态：**ready**（已用 Read 实际打开 poster.png 与 PDF 栅格图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG，无外部依赖；字体 Noto Sans CJK SC）
- PNG：`google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,1700 --screenshot=poster.png file://…/poster.html` → 2400×3400
- PDF：`google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=poster.pdf file://…/poster.html`（`@page 1200×1700px`）→ 1 页，900×1275 pt；`pdftoppm -r 50` 栅格化后查看

## 视觉检查

- 第 1 次渲染发现：标题 50px 时“25.00%”单独折到第二行；整体超高，页脚被画布底边裁掉；点图中“随机 5.49”标签压住横轴“0”。已修：标题改 44px 单行；压缩区块间距；随机标签移到轴下方左侧并加箭头说明。
- 第 2 次复核：一处措辞“模型为 2024 年版本快照”属我们推断，改为“结果对应论文评测时的模型版本”。
- 终版：单页 PDF 与 PNG 一致；中文无豆腐块；无裁切、无重叠；配对条形中白色数字在绿色条内可读、红色数字在条外；点图左端模型点有重叠（6–13% 区间密集），这正是要表达的聚集，已在图注给出范围与开源最好值；最小字号 12px，2× PNG 中可读。
- 小瑕疵：上方条形面板底部、右下蓝色注记面板底部各有少量留白，不影响阅读。

## 内容复核

- 标题数字 97.26% / 25.00% 与 Table 2 一致，限定“同一套眼睛和按钮”（同观测同动作空间），未超出原文。
- 反例注记只画方向、标示意，并写明只测 Gemini-Flash、不能推到所有 MLLM。
- 布局：左侧接口竖流程＋右侧配对条形（鸿沟）为主，中部 19 模型点图，下方交互表与反例注记并列。与 s001 九种版式及本组另两篇不同。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 若被仓库 `.gitignore` 的 `reel/*/poster.html` 规则忽略，则保留在本地；正式发布时由总控按精确路径处理，不全局取消忽略。
