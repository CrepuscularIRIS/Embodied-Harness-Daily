#!/usr/bin/env python3
"""从 queue 取下一批 material_ready 且未处理的论文，建生产批次目录。
用法: make_batch.py [batch_size]  -> 打印 batch_id
优先 screen A 类、字典序；跳过已有任何 batch 记录的 paper。
"""
import json, sys, os, hashlib

RUN = "embodied-v22-20261021-01"
BASE = f"research/v2/runs/{RUN}"

def sha(p):
    h = hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1<<16),b''): h.update(c)
    return h.hexdigest()

def main(n=5):
    queue = [json.loads(l) for l in open(f"{BASE}/queue.jsonl")]
    # 已在任何生产批次中的 paper
    done = set()
    for b in os.listdir(f"{BASE}/batches"):
        mp = f"{BASE}/batches/{b}/inputs_manifest.json"
        if os.path.exists(mp):
            m = json.load(open(mp))
            if m.get("phase","production").startswith("production"):
                done |= {p["paper_key"] for p in m["papers"]}
    # 已进入 final index 的（聚合完成）也跳过
    ip = f"{BASE}/final/index.jsonl"
    if os.path.exists(ip):
        done |= {json.loads(l)["paper_key"] for l in open(ip)}
    cand = [q for q in queue if q["status"]=="material_ready" and q["paper_key"] not in done]
    cand.sort(key=lambda q:(q["screen_tier"]!="A", q["paper_key"]))
    if not cand:
        print("NO-CANDIDATES"); return 1
    papers = cand[:n]
    # batch id: p001, p002 ...
    nums = [int(b[1:]) for b in os.listdir(f"{BASE}/batches") if b.startswith("p") and b[1:].isdigit()]
    bid = f"p{max(nums, default=0)+1:03d}"
    d = f"{BASE}/batches/{bid}"
    for s in ("sol","son55"): os.makedirs(f"{d}/seats/{s}/attempts/a1", exist_ok=True)
    os.makedirs(f"{d}/aggregate/attempts/a1", exist_ok=True)
    m = {"batch_id": bid, "run_id": RUN, "phase": "production",
         "papers": [{"paper_key":q["paper_key"],"paper_id":q["paper_id"],"version":q["version"],
                     "title":q["title"],"material_path":f"research/fulltext/{q['paper_key']}.txt",
                     "material_sha256":q["material_hash"]} for q in papers]}
    m["input_hash"] = hashlib.sha256(json.dumps(m,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    with open(f"{d}/inputs_manifest.json","w") as f: json.dump(m,f,ensure_ascii=False,indent=1)
    print(bid, [p["paper_key"] for p in papers])
    return 0

if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv)>1 else 5))
