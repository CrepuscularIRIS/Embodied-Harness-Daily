# QA · 2510.20328 MemER

状态：**ready**（原文核对通过 + 实际视觉 QA 完成）

## 渲染路径

- 可编辑源：`poster.html`（单文件 HTML/CSS + 内联 SVG，无外部依赖，字体 Noto Sans CJK SC 本机已装）。
- PNG：`google-chrome --headless=new --hide-scrollbars --window-size=1200,1720 --screenshot=poster.png file://.../poster.html`（1200×1720）。
- PDF：`google-chrome --headless=new --no-pdf-header-footer --print-to-pdf=poster.pdf`，`@page 1200px×1720px`，单页 900×1290 pt。
- 版式：**条件对比矩阵**（四行对照 + 参考行 + 结论行），与本期 2610.15572（阶梯）、2506.17811（流水线）结构不同。

## 视觉检查（Read 工具实际打开 poster.png；PDF 经 pdftoppm 栅格化后打开）

- 第 1 版问题：机制图右侧"时间（2 Hz 帧）"被裁切；"记忆：每簇取中位帧"文字溢出绿色底框；曲线箭头穿过说明文字；"参考：人给子任务"折行。均已修改并重渲染。
- 终版：中文字形正常无方块；无裁切；表格数字 19–23px，缩到约 40% 宽仍可辨读；结论条与限制框完整；页脚未贴边。PDF 与 PNG 版式一致、单页。
- 剩余观感问题：表格"能看到的历史"列有 2–3 行折行，可接受。

## 内容核查

- 标题"该记什么，而不是记更多"对应表 1：32 帧窗口只部分改善且推理约 1 s，关键帧记忆最好；没有超出原文（原文 §5 "decide what to remember"）。
- 表格 35 个数字（5 行 × 7 项）逐一对照表 1；表 3 数字逐一对照。
- 已显式标注：作者结果非复现；同 15 件物体/9 件子集非未见物体迁移；3 任务单平台；关键帧只增不删；选择与训练耦合；API 模型只做离线比较。
- 示意图已标"示意"。

## 提交注意

- `poster.html` 被历史 `.gitignore:193`（`reel/*/poster.html`）忽略，仅保留本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
