# QA · 2306.15724

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG，无外部依赖；Noto Sans CJK SC 本机字体）
- PNG：`google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,1700 --screenshot=poster.png file://…/poster.html` → 2400×3400
- PDF：`google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=poster.pdf file://…/poster.html`（`@page 1200×1700px`）→ 1 页，900×1275 pt；用 `pdftoppm` 栅格化后查看

## 视觉检查（Read 工具实际打开 poster.png、局部裁切图与 PDF 栅格图）

- 第 1 次：页脚被裁出画布、PDF 2 页；时间轴“回溯”说明文字压在虚线弧上；双柱图图注被截断（“· Ta”）；机制图两个分析框末行贴边；Table 1 方法名带中文注释导致换行、行高过大。已修：方法名改为单行英文、释义移到表下注；时间轴弧线与文字分离；图注缩短；分析框加高。
- 第 2 次：PNG 完整，但 PDF 仍 2 页（总高约超 12px）。收紧区块间距与页边后 PDF 为 1 页。
- 终版：中文无缺字；无裁切、无重叠；页脚完整；最小字号 12.5px（SVG 注释），2× PNG 中可读。

## 内容复核

- 标题“纠正之前，先说清楚为什么失败”对应原文“explanation guides correction”主张，未超出。
- 模拟真值感知、人工注入失败、真实场景无纠正分母、单一 GPT-4、作者自述局限均在“边界”框显式标注；我们的差值计算与读法已标注。
- 布局：时间轴 + 流程图/双柱对照 + 双表，与本期另两篇（横向双车道拦截图、阶梯图）及 s001 九类不同。
- 剩余问题：无。

## 提交注意

- `poster.html` 被 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略，保留本地；发布时由总控按精确路径处理。
