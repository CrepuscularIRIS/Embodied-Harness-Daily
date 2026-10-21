# inbox — candidate papers waiting to be processed

The collector (Grok bot) writes one file per run: `inbox/YYYY-MM-DD.jsonl` (append if the file exists). One JSON object per line:

```json
{"arxiv": "2610.12345", "url": "https://arxiv.org/abs/2610.12345", "title": "…", "source": "arxiv-listing|hf-daily|hf-trending|github|x|openreview|blog",
 "github": "https://github.com/owner/repo or null", "why": "≤25 words: which embodiment (manipulation / navigation / aerial / humanoid / …), what the model calls through the harness, and which part the paper changes",
 "found": "2026-10-21"}
```

- `arxiv` is required when the work is on arXiv; otherwise give `url` (technical report, blog, repo) and leave `arxiv` null.
- Recall over precision: the scorer (Dots) screens. But do not add papers that are clearly out of scope: end-to-end VLA / visuomotor policies with no harness, agent loop or teacher-harness distillation; GUI / browser / computer-use agents with no embodiment; non-embodied harness self-improvement; wire, cable or test harnesses; general VLM benchmarks without closed-loop interaction.
- Do not judge quality, do not score, do not edit any other file.
- After `research/ingest.py` has run on it, the collector moves the file to `inbox/processed/`; new ids go to `research/queue/` for the scorer (Dots).
