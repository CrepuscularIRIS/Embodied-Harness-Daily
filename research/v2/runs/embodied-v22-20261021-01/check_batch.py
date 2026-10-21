#!/usr/bin/env python3
"""总控机械校验：双席 record 结构/覆盖/算分核对 + 逐字段差异 conflicts.json。
用法: check_batch.py <batch_id> <attempt:默认a1>  (在仓库根运行)
输出: batches/<batch_id>/conflicts.json 与终端报告。只做结构与算术，不做语义判断。
"""
import json, sys, os, hashlib

RUN = "embodied-v22-20261021-01"
WEIGHTS = {"G":15,"M":20,"X":20,"E.measurement":15,"E.causality":10,"E.holdout":10,"E.statistics":5,"E.cost":5}
assert sum(WEIGHTS.values()) == 100

def load(path):
    with open(path, encoding="utf-8") as f: return json.load(f)

def ratings_of(rec):
    r = rec.get("ratings", {})
    out = {}
    for k in ("G","M","X"):
        out[k] = (r.get(k) or {}).get("rating") if isinstance(r.get(k), dict) else None
    E = r.get("E", {}) if isinstance(r.get("E"), dict) else {}
    for sub in ("measurement","causality","holdout","statistics","cost"):
        v = E.get(sub)
        if v is None:  # 兼容扁平 "E.<sub>" 键（son55 席格式）
            v = r.get(f"E.{sub}")
        out[f"E.{sub}"] = v.get("rating") if isinstance(v, dict) else None
    return out

def recompute(rec):
    rt = ratings_of(rec)
    vals = [v for v in rt.values()]
    known = {k:v for k,v in rt.items() if isinstance(v,int)}
    def calc(vals):  # dict of int ratings -> weighted sum /4
        return sum(WEIGHTS[k]*v for k,v in vals.items())/4
    if len(known) < 8:
        lower = calc({k:(v if isinstance(v,int) else 0) for k,v in rt.items()})
        upper = calc({k:(v if isinstance(v,int) else 4) for k,v in rt.items()})
        cov = sum(WEIGHTS[k] for k in known)/100
        return None, None, round(lower,4), round(upper,4), round(cov,4)
    raw = calc(known)
    return round(raw,4), round(raw,1), round(raw,4), round(raw,4), 1.0

def seat_file(d, paper): return os.path.join(d, f"{paper}.json")

def main(batch, att="a1"):
    base = f"research/v2/runs/{RUN}/batches/{batch}"
    man = load(f"{base}/inputs_manifest.json")
    papers = [p["paper_key"] for p in man["papers"]]
    seats = {}
    for seat in ("sol","son55"):
        d = f"{base}/seats/{seat}/attempts/{att}"
        recs = {}
        missing = []
        for p in papers:
            fp = seat_file(d,p)
            if os.path.exists(fp): recs[p] = load(fp)
            else: missing.append(p)
        # 材料核对
        mat_bad = []
        for p,rec in recs.items():
            mh = (rec.get("materials") or [{}])[0].get("sha256")
            want = next(x["material_sha256"] for x in man["papers"] if x["paper_key"]==p)
            if mh != want: mat_bad.append(p)
        seats[seat] = {"recs":recs,"missing":missing,"mat_bad":mat_bad,"dir":d}
        print(f"[{seat}] reviewed={len(recs)}/{len(papers)} missing={missing} material_hash_mismatch={mat_bad}")

    # 算分核对
    for seat in ("sol","son55"):
        for p,rec in seats[seat]["recs"].items():
            raw,disp,lo,up,cov = recompute(rec)
            sc = rec.get("score",{})
            if sc.get("raw") is not None and raw is not None and abs(sc.get("raw",-1)-raw) > 0.01:
                print(f"[{seat}:{p}] SCORE MISMATCH record={sc.get('raw')} recomputed={raw}")
            if sc.get("raw") is None and raw is not None:
                print(f"[{seat}:{p}] record raw=null but all 8 ratings known -> recomputed={raw}")

    # 逐字段差异
    conflicts = []
    common = set(seats["sol"]["recs"]) & set(seats["son55"]["recs"])
    for p in sorted(common):
        a, b = seats["sol"]["recs"][p], seats["son55"]["recs"][p]
        diffs = []
        def cmp(path, va, vb):
            if va != vb: diffs.append({"field":path,"sol":va,"son55":vb})
        cmp("claim_type", a.get("paper",{}).get("claim_type"), b.get("paper",{}).get("claim_type"))
        cmp("evidence_level", a.get("assessment",{}).get("evidence_level"), b.get("assessment",{}).get("evidence_level"))
        cmp("claim_support", a.get("assessment",{}).get("claim_support"), b.get("assessment",{}).get("claim_support"))
        cmp("status", a.get("status"), b.get("status"))
        rap, rbp = a.get("rs_pattern",{}), b.get("rs_pattern",{})
        cmp("rs_pattern.primary", rap.get("primary"), rbp.get("primary"))
        cmp("rs_pattern.outside_taxonomy", rap.get("outside_taxonomy"), rbp.get("outside_taxonomy"))
        subs_a = [m.get("sub_id") for m in rap.get("matches",[])]
        subs_b = [m.get("sub_id") for m in rbp.get("matches",[])]
        cmp("rs_pattern.sub_ids", subs_a, subs_b)
        ra, rb = ratings_of(a), ratings_of(b)
        for k in WEIGHTS:
            va, vb = ra[k], rb[k]
            if va != vb: diffs.append({"field":f"rating.{k}","sol":va,"son55":vb})
        if a.get("score",{}).get("raw") is not None and b.get("score",{}).get("raw") is not None:
            d = round(abs(a["score"]["raw"]-b["score"]["raw"]),2)
            if d > 0: diffs.append({"field":"score.raw_diff","sol":a["score"]["raw"],"son55":b["score"]["raw"],"abs_diff":d})
        conflicts.append({"paper_key":p,"n_diffs":len(diffs),"diffs":diffs})
    with open(f"{base}/conflicts.json","w",encoding="utf-8") as f:
        json.dump({"batch_id":batch,"attempt":att,"generated":"controller",
                   "papers":conflicts}, f, ensure_ascii=False, indent=1)
    n = sum(c["n_diffs"] for c in conflicts)
    rated = [(p, c) for c in conflicts for p in [c["paper_key"]]]
    print(f"conflicts: {n} field-diffs across {len(conflicts)} papers -> conflicts.json")
    for c in conflicts:
        if c["n_diffs"]:
            top = ", ".join(d["field"] for d in c["diffs"][:6])
            print(f"  {c['paper_key']}: {c['n_diffs']} diffs [{top}{' ...' if c['n_diffs']>6 else ''}]")
    # JSON 可解析性兜底
    bad_json = []
    for seat in ("sol","son55"):
        for p in papers:
            fp = seat_file(seats[seat]["dir"],p)
            if os.path.exists(fp):
                try: load(fp)
                except Exception as e: bad_json.append((seat,p,str(e)[:60]))
    if bad_json: print("UNPARSEABLE:", bad_json)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "a1"))
