# 2611.22761 配置层攻击 — SOURCE

论文：配置层安全审计（arXiv 2611.22761v1，2026-11-18）。全部数字/断言映射到原文。

## 报头

| 海报断言 | 原文出处 |
|---|---|
| 11 条提示注入 0 成功、5 类（假冒身份/抽取系统提示/越权工具/安全绕过/记忆腐蚀） | 表 5 + §4 |
| save+apply 两请求 <2s 替换 instructions.txt、重启持久化 | §4.1 |
| Gradio 0.0.0.0:7860 无鉴权、FastAPI 8000 仅 loopback | §3.1 |
| V1 本地/V2 同 /24 远程复现、法语/西班牙语人格改变 | §4.1 |
| CVSS 6.5 MEDIUM | §4.3 |
| 已负责任披露（私有 GHSA 先于论文） | §5.2 |

## 01 攻击链（§4.1，示意重绘）

- POST /api/v1/personalities/save + apply（persist:true）：§4.1。
- apply 断开重连 HuggingFace 会话、即时生效：§3.1。
- save 响应回显全部已装 personality 清单（次要泄露）：§4.1。
- 同仓库 FastAPI 仅 loopback 证明是孤立配置疏忽：§3.1。

## 02 四层对照（表 5）

- LLM 推理层 11→0（作者自注 scoped manual control 非鲁棒性主张）：表 5。
- 本地配置 1/1、网络配置 1/1、memory sink 4/4：表 5。

## 03 CVSS 与跨源（§4.3）

- CWE-306+CWE-1327，AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N=6.5：§4.3。
- save 用 Starlette Request.json() 不查 Content-Type、text/plain 免预检、auto-submit 表单跨源写入（CWE-352 AV:N/UI:R 另计 6.5）：§4.3。
- apply 需 application/json 触发预检被浏览器挡（422）：§4.3。

## 04 记忆升级（§4.4）

- remember 工具"不存敏感数据"仅为自然语言描述：§4.4。
- 绕过 LLM 直调 add_memory_fact()：WiFi 密码/住址/健康诊断/部分卡号全部写入 memory.v1.json 且 list_memory_facts() 可检索：§4.4。

## 05 生态调查（表 6 + §5.2）

- Gradio/FastAPI 默认 loopback、一行配置暴露；Streamlit 默认全接口：表 6。
- 59 公开仓库、11 个部署真应用 10 个可源码验证缺鉴权（含框架默认 11/11）：§5.2。
- "采样内复现，非商业产品流行率"：§5.2。

## 06 危害模型（§6）

- 摄像头麦克风监控、护理场景社工、对话层无异常表象：§6 讨论危害模型。
- 修复方向（loopback+鉴权/配置审计/完整性校验）：§6 建议。

## 边界区（论文自述）

- 11 条为手工定向非穷尽红队：表 5 注。
- 单目标深挖+抽样生态调查非流行率：§5.2。
- 攻击面为本地/同 /24：§4。
- CVSS 6.5 以 AV:A 计、跨源变体另评未合并：§4.3。
