# QA · 2603.26666

状态：**ready**（已用 Read 实际打开 poster.png 与 PDF 栅格图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG，无外部依赖；字体 Noto Sans CJK SC，本机 `/usr/share/fonts/opentype/noto/`）
- PNG：`google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=2 --window-size=1200,1700 --screenshot=poster.png file://…/poster.html` → 2400×3400
- PDF：`google-chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=poster.pdf file://…/poster.html`（`@page 1200×1700px`）→ 1 页，900×1275 pt；`pdftoppm -r 50` 栅格化后查看

## 视觉检查

- 第 1 次渲染发现：(a) 图“性能谷”标注文字压在前向 KL 曲线上，“共同起点”与曲线重叠；两张哑铃图“平均”行的数值标签压住圆点和教师刻度；底部留白约 120px。已修：标注移到谷右侧空白并加引线，起点标签移到坐标轴附近，删除行内数值改由图例给出（RoboTwin 补图例），加大区块间距与边界框字号。
- 终版：单页 PDF，与 PNG 一致；中文字形完整、无豆腐块；无裁切、无文字重叠；三色（反向 KL 蓝、前向 KL 橙、硬 CE 绿虚线）在曲线和右侧目标卡中一致；最小字号 12px（坐标刻度/示意标注），2× PNG 中可读。
- 小瑕疵（不影响阅读）：LIBERO 各行“＋GRPO”紫点与教师刻度几乎重合，教师刻度部分被遮挡；数值已在图例和 SOURCE 中给出。

## 内容复核

- 标题“用哪种目标才不会训崩？”对应原文 §3.4/§4.4 的目标比较，未超出；“反向 KL 最优”在边界框限定为单任务曲线上的结论。
- “示意”标签：曲线图标题处和页脚均标注；“下降超过 50%”保留原文措辞。
- 布局：上方三阶段横条＋中部“双联曲线分岔＋三张目标卡”＋下方双哑铃图。与 s001 九种版式及本组另两篇不同（本组：曲线分岔 / 能力鸿沟条形 / 求助决策流）。
- 剩余问题：无。

## 提交注意

- 可编辑源 `poster.html` 若被仓库 `.gitignore` 的 `reel/*/poster.html` 规则忽略，则保留在本地；正式发布时由总控按精确路径处理，不全局取消忽略。
