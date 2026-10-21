#!/usr/bin/env python3
"""总控状态推进：校验聚合产出 -> 更新 queue.jsonl 状态 -> 写轮次 checkpoint -> 更新 final/index.jsonl。
用法: update_state.py <batch_id> [aggregate_attempt]
机械核对 final record：status 集合、resolutions 覆盖、final_record_hash 复算、score 重算。
"""
import json, sys, os, hashlib, glob
from datetime import datetime

RUN = "embodied-v22-20261021-01"
BASE = f"research/v2/runs/{RUN}"
WEIGHTS = {"G":15,"M":20,"X":20,"E.measurement":15,"E.causality":10,"E.holdout":10,"E.statistics":5,"E.cost":5}

def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

def final_hash_ok(rec):
    h = rec.get("final_record_hash")
    if not h: return False, "missing final_record_hash"
    r2 = {k:v for k,v in rec.items() if k != "final_record_hash"}
    calc = hashlib.sha256(json.dumps(r2, sort_keys=True, ensure_ascii=False, separators=(",",":")).encode("utf-8")).hexdigest()
    return calc == h, f"record={h[:12]} calc={calc[:12]}"

def recompute_score(rec):
    r = rec.get("ratings", {})
    def get(node, k): return node.get(k, {}).get("rating") if isinstance(node.get(k), dict) else None
    vals = {"G":get(r,"G"),"M":get(r,"M"),"X":get(r,"X")}
    E = r.get("E", {})
    for sub in ("measurement","causality","holdout","statistics","cost"):
        vals[f"E.{sub}"] = get(E, sub)
    known = {k:v for k,v in vals.items() if isinstance(v,int)}
    if len(known) < 8: return None
    return round(sum(WEIGHTS[k]*v for k,v in known.items())/4, 4)

def main(batch, att=None):
    agg_dir = f"{BASE}/batches/{batch}/aggregate/attempts"
    att = att or sorted(os.listdir(agg_dir))[-1]
    ad = f"{agg_dir}/{att}"
    man = load(f"{BASE}/batches/{batch}/inputs_manifest.json")
    papers = [p["paper_key"] for p in man["papers"]]
    results = {}
    problems = []
    for p in papers:
        fp = f"{ad}/{p}.json"
        if not os.path.exists(fp):
            problems.append(f"{p}: missing aggregate record"); continue
        rec = load(fp)
        ok, msg = final_hash_ok(rec)
        if not ok: problems.append(f"{p}: final_record_hash mismatch ({msg})")
        raw = recompute_score(rec)
        sc = rec.get("score", {}).get("raw")
        if raw is not None and sc is not None and abs(raw-sc) > 0.01:
            problems.append(f"{p}: score mismatch record={sc} recompute={raw}")
        st = rec.get("aggregate_status")
        nres = len(rec.get("resolutions", []))
        unres = sum(1 for r in rec.get("resolutions", []) if r.get("decision") == "unresolved")
        results[p] = {"status": st, "raw": sc, "display": rec.get("score",{}).get("display"),
                      "resolutions": nres, "unresolved": unres,
                      "seat_hashes": bool(rec.get("input_seat_hashes"))}
        if st == "accepted_final" and unres:
            problems.append(f"{p}: accepted_final with unresolved={unres}")
        if st == "accepted_final" and not rec.get("input_seat_hashes"):
            problems.append(f"{p}: accepted_final without input_seat_hashes")
    # checkpoint
    n_ok = sum(1 for r in results.values() if r["status"]=="accepted_final")
    round_id = f"{batch}-finalize-{att}"
    ckpt = {"round_id": round_id, "batch_id": batch, "aggregate_attempt": att,
            "ts": datetime.now().isoformat(timespec="seconds"),
            "papers": results, "problems": problems}
    with open(f"{BASE}/rounds/{round_id}.json","w",encoding="utf-8") as f:
        json.dump(ckpt, f, ensure_ascii=False, indent=1)
    # queue + final index
    queue = [json.loads(l) for l in open(f"{BASE}/queue.jsonl")]
    idx = []
    idx_path = f"{BASE}/final/index.jsonl"
    if os.path.exists(idx_path):
        idx = [json.loads(l) for l in open(idx_path)]
    idx_by_key = {r["paper_key"]: r for r in idx}
    for p, r in results.items():
        rec_status = None
        fp = f"{ad}/{p}.json"
        if os.path.exists(fp):
            rec_status = load(fp).get("status")
        for q in queue:
            if q["paper_key"] == p:
                q["status"] = rec_status if rec_status in ("out_of_scope","needs_fulltext","needs_evidence") else ("aggregated" if r["status"]=="accepted_final" else (r["status"] or "aggregated"))
                q["last_batch"], q["aggregate_attempt"] = batch, att
        if r["status"] == "accepted_final":
            fp = f"{ad}/{p}.json"
            rec = load(fp)
            row = {"paper_key": p, "version": next((x["version"] for x in man["papers"] if x["paper_key"]==p), None),
                   "batch": batch, "aggregate_attempt": att, "status": r["status"],
                   "claim_type": rec.get("paper",{}).get("claim_type"),
                   "evidence_level": rec.get("assessment",{}).get("evidence_level"),
                   "claim_support": rec.get("assessment",{}).get("claim_support"),
                   "score_raw": r["raw"], "score_display": r["display"],
                   "record_path": f"batches/{batch}/aggregate/attempts/{att}/{p}.json",
                   "final_record_hash": rec.get("final_record_hash")}
            idx_by_key[p] = row
    with open(f"{BASE}/queue.jsonl","w",encoding="utf-8") as f:
        for q in queue: f.write(json.dumps(q,ensure_ascii=False)+"\n")
    with open(idx_path,"w",encoding="utf-8") as f:
        for r in idx_by_key.values(): f.write(json.dumps(r,ensure_ascii=False)+"\n")
    print(f"batch={batch} att={att}: accepted_final={n_ok}/{len(papers)} problems={len(problems)}")
    for p in problems: print("  !", p)
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None))
