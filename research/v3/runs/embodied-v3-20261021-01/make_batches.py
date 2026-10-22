#!/usr/bin/env python3
"""v3 批次构建：按材料体量打包（预算制），输出 batches/<id>-inputs.tsv。"""
import json
import os
import sys

RUN = os.path.dirname(os.path.abspath(__file__))
QUEUE = os.path.join(RUN, "../../../v2/runs/embodied-v22-20261021-01/queue.jsonl")
BATCH_DIR = os.path.join(RUN, "batches")
SIZE_BUDGET = 550 * 1024  # 每批材料总字节预算
MAX_PAPERS = 16

def main() -> None:
    repo = os.path.abspath(os.path.join(RUN, "../../../.."))
    papers = []
    for line in open(QUEUE):
        q = json.loads(line)
        mp = os.path.join(repo, q["material_path"]) if q.get("material_path") else None
        if not mp or not os.path.exists(mp):
            continue
        q["material_abs"] = mp
        papers.append(q)
    # 按体量降序，贪心装箱：大批先放，小批填缝
    papers.sort(key=lambda q: os.path.getsize(q["material_abs"]), reverse=True)
    batches = []
    for q in papers:
        sz = os.path.getsize(q["material_abs"])
        placed = False
        for b in batches:
            if b["bytes"] + sz <= SIZE_BUDGET and len(b["papers"]) < MAX_PAPERS:
                b["papers"].append(q); b["bytes"] += sz; placed = True; break
        if not placed:
            batches.append({"papers": [q], "bytes": sz})
    batches.sort(key=lambda b: b["papers"][0]["paper_id"])
    os.makedirs(BATCH_DIR, exist_ok=True)
    for i, b in enumerate(batches, 1):
        bid = f"b{i:03d}"
        with open(os.path.join(BATCH_DIR, f"{bid}-inputs.tsv"), "w") as f:
            f.write("paper_id\tversion\tsource_url\ttitle\tmaterial_path\tpdf_supplement\tbytes\n")
            for q in sorted(b["papers"], key=lambda q: q["paper_id"]):
                pid = q["paper_id"]
                supp = os.path.join(repo, "research/fulltext/review-runs/embodied-v22-20261021-01/materials", f"{pid}_pdf.txt")
                supp = supp if os.path.exists(supp) else ""
                url = f"https://arxiv.org/abs/{pid}"
                title = q["title"].replace("\t", " ")
                f.write(f"{pid}\t{q['version']}\t{url}\t{title}\t{q['material_abs']}\t{supp}\t{os.path.getsize(q['material_abs'])}\n")
    total = sum(len(b["papers"]) for b in batches)
    print(f"batches={len(batches)} papers={total} max_batch_bytes={max(b['bytes'] for b in batches)//1024}KB")

if __name__ == "__main__":
    sys.exit(main())
