#!/usr/bin/env python3
"""v3.1 批次机械校验：ID 一一对应、字段齐全、档位范围、算术、patterns/card_checks 结构。"""
import json
import os
import sys

RUN = os.path.dirname(os.path.abspath(__file__))
FIELDS = ["paper_id", "version", "source_url", "material_level", "status", "claim_type",
          "move", "gap", "patterns", "card_checks", "ratings", "screen_score", "reasons",
          "evidence", "claim_support", "evidence_level", "caveat", "needs"]
W = {"G": 15, "M": 20, "X": 20, "E": 45}
VERDICTS = {"met", "partial", "unmet", "unknown", "challenged_with_evidence"}

def check_batch(bid: str) -> list[str]:
    errs = []
    inp = os.path.join(RUN, "batches", f"{bid}-inputs.tsv")
    out = os.path.join(RUN, "batches", f"{bid}.jsonl")
    if not os.path.exists(out):
        return [f"{bid}: 输出文件不存在"]
    rows = [l.rstrip("\n") for l in open(inp) if not l.startswith("paper_id")]
    want = {r.split("\t")[0] for r in rows}
    got = {}
    for i, line in enumerate(open(out), 1):
        try:
            r = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"{bid}:{i}: 非法 JSON ({e})"); continue
        pid = r.get("paper_id")
        if pid in got:
            errs.append(f"{bid}:{pid}: 重复行")
        got[pid] = r
        for k in FIELDS:
            if k not in r:
                errs.append(f"{bid}:{pid}: 缺字段 {k}")
        p = r.get("patterns") or {}
        for k in ("primary", "subcards", "supporting", "status", "reason"):
            if k not in p:
                errs.append(f"{bid}:{pid}: patterns 缺 {k}")
        if p.get("status") == "matched" and not str(p.get("primary") or "").startswith("embodied:"):
            errs.append(f"{bid}:{pid}: matched 但 primary 非 embodied:<id>")
        for cc in r.get("card_checks") or []:
            if cc.get("verdict") not in VERDICTS:
                errs.append(f"{bid}:{pid}: card_checks verdict={cc.get('verdict')} 非法")
            for k in ("card", "criterion_ref", "criterion", "paper_evidence", "axes"):
                if not cc.get(k):
                    errs.append(f"{bid}:{pid}: card_checks 项缺 {k}")
        rt = r.get("ratings") or {}
        vals = {k: rt.get(k) for k in "GMXE"}
        for k, v in vals.items():
            if v is not None and not (isinstance(v, int) and 0 <= v <= 4):
                errs.append(f"{bid}:{pid}: {k}={v} 越界")
        if any(v is None for v in vals.values()):
            if r.get("screen_score") is not None:
                errs.append(f"{bid}:{pid}: 有 null 轴但 screen_score 非 null")
            if r.get("status") not in ("needs_material", "out_of_scope"):
                errs.append(f"{bid}:{pid}: 有 null 轴但 status={r.get('status')}")
        elif r.get("status") == "scored":
            exp = sum(W[k] * vals[k] for k in "GMXE") / 4
            if r.get("screen_score") is None or abs(r["screen_score"] - exp) > 1e-6:
                errs.append(f"{bid}:{pid}: screen_score={r.get('screen_score')} 应为 {exp}")
            if not r.get("evidence"):
                errs.append(f"{bid}:{pid}: scored 但 evidence 为空")
    for pid in want:
        if pid not in got:
            errs.append(f"{bid}:{pid}: 缺输出行")
    for pid in got:
        if pid not in want:
            errs.append(f"{bid}:{pid}: 输出不在输入清单")
    return errs

def main() -> int:
    bids = sys.argv[1:]
    if not bids:
        for f in os.listdir(os.path.join(RUN, "batches")):
            if f.endswith("-inputs.tsv"):
                bids.append(f[:-len("-inputs.tsv")])
        bids.sort()
    errs = []
    for bid in bids:
        errs += check_batch(bid)
    for e in errs:
        print(e)
    print(f"OK: {len(bids)} 批, {len(errs)} 个问题" if not errs else f"FAILED: {len(errs)} 个问题")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main())
