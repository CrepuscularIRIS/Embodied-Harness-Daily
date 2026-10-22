# QA · 2506.17811 RoboMonkey

状态：**ready**（原文核对通过 + 实际视觉 QA 完成）

## 渲染路径

- 可编辑源：`poster.html`（单文件 HTML/CSS + 内联 SVG，字体 Noto Sans CJK SC）。
- PNG：`google-chrome --headless=new --hide-scrollbars --window-size=1200,1540 --screenshot=poster.png`（1200×1540）。
- PDF：`google-chrome --headless=new --no-pdf-header-footer --print-to-pdf=poster.pdf`，`@page 1200px×1540px`，单页 900×1155 pt。
- 版式：**横向流水线**（离线训练泳道 + 部署四段流程 + 时间成本条），与 2510.20328（矩阵）、2610.15572（阶梯）不同。

## 视觉检查（Read 工具实际打开 poster.png；PDF 经 pdftoppm 栅格化后打开）

- 第 1 版问题：③ 验证框内示意柱压住"给每个 (图像, 指令, 动作) 打分"一行；时间轴刻度位置与比例不符；页面底部约 200px 空白。已下移示意柱、按 1120 px/s 重排刻度、页高改为 1540。
- 终版：中文正常无方块；无裁切与重叠；35/30/60% 数字 20–22px，40% 缩放下仍可读；"部署时不用 oracle 验证器"卖点条显著。剩余：时间条内白字 13px 偏小，但对比度足够。

## 内容核查

- 标题"多采几个动作，再让学来的验证器挑一个"描述方法，不含效果夸大。
- "不用 oracle"限定为**部署时**；同时写明训练标签来自示范动作 RMSE（oracle 式距离代理），没有掩盖这一来源。
- 已注明：每方法 40 次真机；V-GPS 预算不同；仿真按任务取最佳配置；闭环无"不验证"组；验证器偏好示范模态；约 1.5 Hz 与 28 GB 显存；两种机械臂。
- 时间条两段来自不同测量，已在页脚注明仅作量级参考。

## 提交注意

- `poster.html` 被历史 `.gitignore:193`（`reel/*/poster.html`）忽略，仅保留本地；正式发布时由总控精确处理该成品路径，不全局取消忽略。
