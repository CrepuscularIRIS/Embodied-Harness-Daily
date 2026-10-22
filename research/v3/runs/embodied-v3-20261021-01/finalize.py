#!/usr/bin/env python3
"""v3 收尾：合并批次 → final/index.jsonl，统计分布，按 SELECTION 产出前 15 候选。"""
import glob
import json
import os

RUN = os.path.dirname(os.path.abspath(__file__))

def main() -> None:
    rows = {}
    for f in sorted(glob.glob(os.path.join(RUN, "batches", "b*.jsonl"))):
        for line in open(f):
            r = json.loads(line)
            pid = r["paper_id"]
            assert pid not in rows, f"重复 {pid}"
            r["_batch"] = os.path.basename(f).replace(".jsonl", "")
            rows[pid] = r
    os.makedirs(os.path.join(RUN, "final"), exist_ok=True)
    with open(os.path.join(RUN, "final", "index.jsonl"), "w") as f:
        for pid in sorted(rows):
            f.write(json.dumps(rows[pid], ensure_ascii=False) + "\n")

    scored = [r for r in rows.values() if r["status"] == "scored"]
    nm = [r for r in rows.values() if r["status"] == "needs_material"]
    oos = [r for r in rows.values() if r["status"] == "out_of_scope"]
    print(f"总计 {len(rows)} = scored {len(scored)} + needs_material {len(nm)} + out_of_scope {len(oos)}")
    ss = sorted((r["screen_score"] for r in scored), reverse=True)
    import statistics
    print(f"分数: max {ss[0]}  p90 {ss[int(len(ss)*0.1)]:.2f}  中位 {statistics.median(ss):.2f}  min {ss[-1]}")

    # SELECTION：分数降序，同分按 E、M 降序再 paper_id；contradicted/unresolved 进问题清单
    ok = [r for r in scored if r["claim_support"] in ("supported_in_material", "scoped")]
    flagged = [r for r in scored if r["claim_support"] in ("contradicted", "unresolved")]
    ok.sort(key=lambda r: (-r["screen_score"], -(r["ratings"]["E"] or 0), -(r["ratings"]["M"] or 0), r["paper_id"]))
    with open(os.path.join(RUN, "final", "selection.md"), "w") as f:
        f.write(f"# v3 选读候选（run embodied-v3-20261021-01）\n\n规则：screen_score 降序（同分按 E、M），claim_support=contradicted/unresolved 不入候选。quality_floor=null（用户未指定）。取前 15 进入 Opus 原文核对。\n\n## 候选 15\n\n| # | paper_id | score | G/M/X/E | claim_type | claim_support | 一句话 move |\n|---|---|---|---|---|---|---|\n")
        for i, r in enumerate(ok[:15], 1):
            g = r["ratings"]
            f.write(f"| {i} | {r['paper_id']} | {r['screen_score']:.1f} | {g['G']}/{g['M']}/{g['X']}/{g['E']} | {r['claim_type']} | {r['claim_support']} | {(r['move'] or '')[:60]} |\n")
        f.write(f"\n## 问题清单（claim_support 异常，先纠正/补证）\n\n")
        for r in flagged:
            f.write(f"- {r['paper_id']} score={r['screen_score']:.1f} {r['claim_support']}\n")
        f.write(f"\n## 待补材料（needs_material {len(nm)} 篇，不混排）\n\n")
        for r in nm:
            f.write(f"- {r['paper_id']} needs={r.get('needs')}\n")
    print(f"候选前 15 已写 final/selection.md；问题清单 {len(flagged)} 篇")

if __name__ == "__main__":
    main()
