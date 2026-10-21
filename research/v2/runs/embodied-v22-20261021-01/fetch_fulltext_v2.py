#!/usr/bin/env python3
"""为评分运行抓未裁剪 arXiv 全文（含 related work 与附录）。

与 research/fetch_fulltext.py 的区别：不 DROP 任何章节、不设 40KB cap；仅去掉参考文献
列表与脚注，math 保留 TeX alttext。输出 research/fulltext/review-runs/<run>/materials/。
404 时尝试 ar5iv；仍无则写 FULLTEXT: none 行。限速复用 research/net.py。

用法: python3 fetch_fulltext_v2.py <ids...>   (仓库根运行；已存在且完整的文件跳过)
"""
import json, re, sys, hashlib
from pathlib import Path
sys.path.insert(0, str(Path("research").resolve()))
from net import RateLimited, get  # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402
import urllib.error  # noqa: E402

RUN = "embodied-v22-20261021-01"
OUT = Path(f"research/fulltext/review-runs/{RUN}/materials")
OUT.mkdir(parents=True, exist_ok=True)
META = {r["arxiv"]: r for r in map(json.loads, Path("research/corpus.jsonl").read_text().splitlines())}
ARXIV = "https://arxiv.org/html/{v}"
AR5IV = "https://ar5iv.labs.arxiv.org/html/{id}"

def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for sel in (".ltx_bibliography", ".ltx_note", "script", "style", ".ltx_bibblock"):
        for t in soup.select(sel):
            t.decompose()
    for t in soup.select("math"):
        t.replace_with(f" {t.get('alttext','')} ")
    parts = []
    for sec in soup.select("section.ltx_section, section.ltx_appendix"):
        h = sec.find(["h1","h2","h3"])
        title = " ".join(h.get_text(" ").split()) if h else ""
        body = " ".join(sec.get_text(" ").split())
        if title: body = body[len(title):].strip() if body.startswith(title) else body
        parts.append(f"## {title}\n{body}" if title else body)
    if not parts:  # 无 ltx_section 结构的页面：整页去标签
        text = " ".join(soup.get_text(" ").split())
        parts = [text] if text else []
    return "\n\n".join(parts)

def fetch_one(aid: str) -> str | None:
    m = META.get(aid, {})
    ver = m.get("latest_version") or aid
    for url in (ARXIV.format(v=ver), AR5IV.format(id=aid)):
        try:
            html = get(url).decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            if e.code == 404: continue
            print(f"{aid}: {e!r} via {url[:40]}"); return None
        except RateLimited as e:
            raise
        except Exception as e:
            print(f"{aid}: {e!r} via {url[:40]}"); continue
        body = html_to_text(html)
        if len(body) > 3000:
            head = f"# {m.get('title', aid)}\narXiv {ver} | {m.get('published','')}\n\n## Abstract\n{m.get('abstract','')}\n\n"
            return f"FULLTEXT: html-full\n{head}{body}\n"
    return None

def main(ids: list[str]) -> int:
    done, misses = [], []
    for aid in ids:
        out = OUT / f"{aid}.txt"
        if out.exists() and out.read_text(encoding="utf-8", errors="ignore").startswith("FULLTEXT: html-full"):
            done.append(aid); continue
        try:
            txt = fetch_one(aid)
        except RateLimited as e:
            print(f"rate-limited at {aid}: {e}; rerun later"); return 75
        if txt is None:
            # 保留旧 abstract 行避免重复抓
            if not out.exists():
                out.write_text(f"FULLTEXT: none (no html rendering)\n# {META.get(aid,{}).get('title',aid)}\n", encoding="utf-8")
            misses.append(aid); continue
        out.write_text(txt, encoding="utf-8")
        done.append(aid)
        print(f"{aid}: {out.stat().st_size}B", flush=True)
    print(f"fetched={len(done)} no_html={len(misses)} {misses}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
