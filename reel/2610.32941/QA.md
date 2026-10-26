# QA · 2610.32941

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG；字体 Noto Sans CJK SC）
- PNG：headless Google Chrome（`--headless=new --force-device-scale-factor=2 --window-size=1200,1700 --screenshot`）→ 2400×3400
- PDF：同一 Chrome `--print-to-pdf --no-pdf-header-footer`，`@page 1200×1700px` → 1 页；`pdftoppm` 栅格化后查看

## 视觉检查（Read 工具实际打开 poster.png 与 PDF 栅格图）

- 第 1 次渲染：不通过。内容高 1696px，PDF 溢出为 2 页、页脚被截；机制图左侧“失败概率”被裁、报警头说明文字压在曲线上；阈值森林图的组名与 t 值上下错位、跨行重叠。
- 重做一次：机制图标签移到曲线上方空白处、整体下移收紧；阈值森林图改为单行标签“固定 50 步 · t=0.90 / t=0.95…”，行高压缩；内容高 1627px。
- 终版：单页；中文完整；两张森林图的方块、区间端点、0 线、数值列对齐可读；−1.92 一行以红色单独标出；套件格负值为红底；限制框 3 条完整。

## 内容复核

- 标题限定“仅仿真 · LIBERO / MetaWorld · 3 个 VLA”。
- 负结果与边界在场：adaptive t=0.90 显著有害；短套件三处负值；π0.5 留出种子仅 +0.70；无随机/定时回走对照；物体不复位；特权复位不可真机执行。
- 版式：机制时间带＋两张森林图＋恒等式与套件热格＋检测事实卡，与前 18 张及本期另两张不同。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 被仓库 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略：已保留在本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
