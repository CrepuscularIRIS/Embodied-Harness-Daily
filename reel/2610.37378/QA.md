# QA · 2610.37378

状态：**ready**（已实际查看渲染图）

## 渲染路径

- 源：`poster.html`（单文件 HTML/CSS＋内联 SVG；字体 Noto Sans CJK SC）。散点 SVG 由临时脚本按 Table I 生成后嵌入 poster.html（脚本仅在 /tmp，poster.html 为完整可编辑源）。
- PNG：headless Google Chrome（`--headless=new --force-device-scale-factor=2 --window-size=1200,1700 --screenshot`）→ 2400×3400
- PDF：同一 Chrome `--print-to-pdf --no-pdf-header-footer`，`@page 1200×1700px` → 1 页

## 视觉检查（Read 工具实际打开 poster.png 全图与机制图、散点两处局部裁切）

- 第 1 次渲染：不通过。散点 x 轴“100%”刻度被裁；机制图参考轨迹虚线穿过“障碍框”字样；消融标签“PickCube，去输入＋去奖励”折成三行，“励”单独成行。
- 重做一次：散点 viewBox 加宽；“障碍框”下移到框底；消融标签缩短、标签列加宽；局部裁切再看发现注释引线起点贴在一个 VLSA-ARM 方点旁、易误读，同一轮内把起点下移到虚线连线上。
- 终版：单页；中文完整；散点 30 点、图例与六设置平均清楚，PickCube-静态配对连线与注释指向明确；机制图场景三条路径与右侧四框清楚；消融三组条与标签单行；真机区间条与数字对齐。

## 内容复核

- 标题限定“结构化障碍 · 不改 VLA 权重”；机制图注明“不是零成本”。
- 负面与边界在场：低维框与真值/AprilTag；无速度；同一生成器；逐任务训练与 82.3M 转移；碰撞 8–34%、无形式保证；真机只有区间；去参考消融混合两因素。
- 版式：参考路线场景＋流程栈＋安全-完成散点平面＋消融成对条＋真机区间条，与前 27 张及本期另两张不同。
- 剩余问题：散点中 OS-静态的 VLSA-EE 与 VLSA-ARM 两点数值几乎相同而重叠（Table I 原值 0.2609/0.3503 与 0.2644/0.3506），属数据本身。

## 提交注意

- `poster.html` 被 `.gitignore` 第 193 行 `reel/*/poster.html` 忽略，保留本地；正式发布时由总控按精确路径处理。
