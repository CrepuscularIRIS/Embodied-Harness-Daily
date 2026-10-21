# v2 证据记录边界

旧 yes/no 九项 schema 已归档。现行提案见 [SCORE_SPEC](SCORE_SPEC.md) 的“证据与记录”。
状态：draft_uncalibrated；尚未实现新机器 schema/validator。旧 check_evidence.py 已停用，不能用它验证 v2。

要求：逐篇、固定版本、固定材料 hash、可定位引用、推理与反证并列；unknown 与 not_reported 分开。
不自动迁移旧 judgment，不把旧 VERIFIED.json 视为新语义验证。
