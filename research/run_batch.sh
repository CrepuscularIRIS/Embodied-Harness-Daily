#!/bin/bash
# One dual-seat panel batch: two blind seats in parallel → merge → arbitrate (if needed) → final check.
# Leaves committing to the caller. Usage: bash research/run_batch.sh <B>
B=$1
cd "$(dirname "$0")/.." || exit 1
P="research/judgments/passes"; mkdir -p "$P"
PYTHONPATH=research python3 research/judge.py --batch "$B" --seat sol > "/tmp/$B.sol.log" 2>&1 &
SOL=$!
PYTHONPATH=research python3 research/judge.py --batch "$B" --seat son55 > "/tmp/$B.son55.log" 2>&1 &
SON=$!
wait $SOL; SOL=$?
wait $SON; SON=$?
echo "seats: sol=$SOL son55=$SON (0 ok; 1 = some papers failed, see /tmp/$B.*.log)"
PYTHONPATH=research python3 research/merge_judgments.py "$B" || { echo "BATCH $B: merge failed"; exit 1; }
if python3 -c "import json,sys; sys.exit(0 if json.load(open('$P/$B.conflicts.json'))['conflicts'] else 1)"; then
  PYTHONPATH=research python3 research/judge.py --batch "$B" --arb || { echo "BATCH $B: arbiter failed"; exit 1; }
  PYTHONPATH=research python3 research/merge_judgments.py "$B" --apply-arb || { echo "BATCH $B: apply-arb failed"; exit 1; }
fi
PYTHONPATH=research python3 research/score.py check "research/judgments/$B.jsonl" "research/judgments/ids_$B.txt" \
  && echo "BATCH $B DONE" || echo "BATCH $B: final check FAILED"
