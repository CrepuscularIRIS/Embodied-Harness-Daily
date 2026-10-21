#!/usr/bin/env bash
# 派发 Opus 5.5 聚合席（逐篇证据核查、分歧裁决、最终聚合）
# 用法: aggregate_worker.sh <batch_id> <attempt:默认a1> [phase: production|calibration]
set -euo pipefail
BATCH=$1; ATTEMPT=${2:-a1}; PHASE=${3:-production}
RUN=embodied-v22-20261021-01
ROOT=/home/lingxufeng/embodied-harness-radar
MODEL=claude-opus-5-5
OUT="$ROOT/research/v2/runs/$RUN/batches/$BATCH/aggregate/attempts/$ATTEMPT"
LOG_DIR="$ROOT/research/fulltext/review-runs/$RUN"
mkdir -p "$OUT" "$LOG_DIR"

PROMPT="你是 Opus 5.5 聚合席（本会话实际模型即 $MODEL，不要重新配置或探测）。仅处理 run=$RUN、batch=$BATCH、aggregate attempt=$ATTEMPT、phase=$PHASE。
工作目录固定为 $ROOT（所有相对路径以此为根）。

必读（按序）：
1. docs/agents/AGGREGATE_OPUS.md（你的职责与边界，逐篇执行）
2. research/SCORE_SPEC.md、research/BATCH_CONTRACT.md、research/PATTERN_PROTOCOL.md、research/REVIEW_WORKSHEET.md、docs/EVIDENCE.md
3. research/reference/researchstudio-15-31/ 两个 overview.md；patterns/overview.md、research/patterns/taxonomy.json
4. 本批输入清单 research/v2/runs/$RUN/batches/$BATCH/inputs_manifest.json（含每篇 material_path；需要时读原文核对）
5. 两席原件：batches/$BATCH/seats/sol/attempts/*/ 与 seats/son55/attempts/*/ 下每篇 JSON 与 batch-report
6. 总控机械差异报告：batches/$BATCH/conflicts.json

对每篇按 AGGREGATE_OPUS.md 顺序执行：先读中心主张/方法/关键结果写初步证据判断（此时不看两席总分）→ 核对两席材料/版本/识别完整性 → 逐项检查实质分歧并读原文裁决（每个分歧一条 resolution：field_path、sol_value、son55_value、decision(sol/son55/revised/unresolved/same_supported_fact)、final_value、reason、evidence_ids、score_impact）→ 检查共有错误并建 shared_error_corrections → 组装 final judgment。

final record 按 BATCH_CONTRACT「聚合 record 与分歧」节：包含原 record 全部字段、input_seat_hashes（两席各文件 sha256，用 sha256sum 计算）、resolutions[]、shared_error_corrections[]、aggregate_model=\"$MODEL\"、aggregate_status(accepted_final/needs_revision/needs_evidence/needs_fulltext)、final_record_hash（对移除 final_record_hash 字段后的完整 record：UTF-8、sort_keys=true、紧凑分隔符、ensure_ascii=False 编码取 SHA-256；用 python3 -c 生成并核验）。
分数由确定性公式计算：S=(15G+20M+20X+15Em+10Ec+10Eh+5Es+5Ek)/4；仍有计分 unknown 或关键证据未解则 score.raw=null 不进正常精选。

逐篇原子写入 $OUT/<paper_key>.json；完成后写 $OUT/batch-report.json（每篇 status、分歧数、共有错误数、未解数、score raw/display、resolution 摘要）。
最后只回复简短文本：每篇一行状态、输出目录、阻塞项。不自己挑 Reel、不改分迎合名额、不发布榜单；不操作 git、不写 $OUT 之外文件、不改两席原件。"

cd "$ROOT"
printf '%s' "$PROMPT" | claude -p --model "$MODEL" \
  --permission-mode acceptEdits \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash" \
  > "$LOG_DIR/${BATCH}-aggregate-${ATTEMPT}.log" 2>&1
echo "done: $BATCH aggregate $ATTEMPT (exit $?)"
