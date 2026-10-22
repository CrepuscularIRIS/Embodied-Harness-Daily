"""Local record assembly/checking only; does not execute paper code."""
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/lingxufeng/embodied-harness-radar')
OUT = ROOT / 'research/v2/runs/embodied-v22-20261021-01/batches/p005/seats/sol/attempts/a1'
MANIFEST = json.loads((ROOT / 'research/v2/runs/embodied-v22-20261021-01/batches/p005/inputs_manifest.json').read_text())
WEIGHTS = {'G': 15, 'M': 20, 'X': 20, 'measurement': 15, 'causality': 10, 'holdout': 10, 'statistics': 5, 'cost': 5}
RUBRIC_HASH = '0b0192c8fc72f53487508f053e5b9e8fd2fd20a25f3fcf636dc48f969e683d51'


def rating(value: int | None, reason: str, evidence: list[str], counter: list[str] | None = None, scope: list[str] | None = None) -> dict:
    return {'status': 'unknown' if value is None else 'resolved', 'rating': value, 'reason': reason, 'evidence_ids': evidence, 'counterevidence_ids': counter or [], 'search_scope': scope or []}


def evidence(eid: str, locator: str, quote: str, explanation: str) -> dict:
    return {'evidence_id': eid, 'material_id': 'M1', 'locator': locator, 'quote': quote, 'support_explanation': explanation, 'kind': 'author_report'}


def expectation(eid: str, ref: str, applies: str, status: str, reason: str, ids: list[str], score: list[str], applicable: bool = True) -> dict:
    return {'id': eid, 'version': 'domain-card snapshot 2026-10-21', 'source_strength': 'common_practice', 'source_refs': [ref], 'applies_when': applies, 'applicable': applicable, 'status': status, 'reason': reason, 'evidence_ids': ids, 'score_item': score}


def save(key: str, body: dict) -> None:
    paper = next(p for p in MANIFEST['papers'] if p['paper_key'] == key)
    path = ROOT / paper['material_path']
    text = path.read_text()
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == paper['material_sha256']
    ident = {k: paper[k] for k in ('paper_key', 'paper_id', 'title', 'version')}
    ident.update(body['paper'])
    prov = {
        'input_hash': MANIFEST['input_hash'],
        'rubric_version': 'SCORE_SPEC v2.2 draft_uncalibrated + anchors v2 (3ececdd11cc3d144)',
        'rubric_hash': RUBRIC_HASH,
        'rs_manifest_hash': '3fc06b621b26f2ea87aa273ee34e2a80308fd09102f1530056428662b0971e32',
        'domain_cards_hash': {
            'taxonomy': 'daf38e579a46689d2f8da6291bb3f79fb050bb1c1383dad4c704353f32ec9e0e',
            'conditions': '2ca1e76481d3468d1c0020eb81e4eb42a4bd4e814df0d0b187ee316e8825cfa1',
            'overview': '2bc4cdeb322e2c8ed96598feb5c4867b858f48b6bf9efa0eb29943735d84cdcf'
        },
        'expectations_hash': 'db5ce019a8741274e2e71a284a59f3457cf2dfc5454fcc4bf98d34b6e76b24c7',
        'model_type': 'sonnet type (overlay gpt-6.1-sol, 6.1 Sol)',
        'actual_model': 'gpt-6.1-sol', 'session_id': None, 'receipt_ref': None,
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'notes': [
            'phase=production; anchors_version=v2 (3ececdd11cc3d144); independent sol initial review, no other-seat/aggregate outputs read.',
            'Model identity from existing session context; no probing or reconfiguration. Session ID/receipt unavailable in task-local supplied metadata; null is not a missing scientific-evidence blocker.',
            'expectations_hash 由总控提供，内容未读; exact hash checked locally only. Expectation substance comes from authorized embedded domain main cards, not unread private profile.',
            'Offline fixed materials only. All empirical results below are author reports; no paper code run and no reproduction claimed.'
        ]
    }
    record = {'schema_version': 'radar-review-v2.2', 'run_id': MANIFEST['run_id'], 'batch_id': 'p005', 'attempt_id': 'a1', 'seat': 'sol', **body, 'paper': ident, 'provenance': prov}
    record['materials'] = [{**m, 'material_id': 'M1', 'url': 'https://arxiv.org/abs/' + paper['version'], 'path': paper['material_path'], 'sha256': digest} for m in body['materials']]
    record['evidence'] = [{**e, 'material_sha256': digest} for e in body['evidence']]
    rows = {**{k: record['ratings'][k] for k in ('G', 'M', 'X')}, **record['ratings']['E']}
    assert set(rows) == set(WEIGHTS)
    known = 0
    lower = 0.0
    upper = 0.0
    for name, weight in WEIGHTS.items():
        r = rows[name]
        assert set(('status', 'rating', 'reason', 'evidence_ids', 'counterevidence_ids', 'search_scope')) <= set(r)
        assert r['reason']
        if r['status'] == 'unknown':
            assert r['rating'] is None
            upper += weight
        else:
            assert r['status'] in ('resolved', 'not_reported')
            assert type(r['rating']) is int and 0 <= r['rating'] <= 4
            if r['status'] == 'not_reported':
                assert r['rating'] == 0 and r['search_scope']
            known += weight
            lower += weight * r['rating'] / 4
            upper += weight * r['rating'] / 4
    record['score'] = {'raw': lower if known == 100 else None, 'display': round(lower, 1) if known == 100 else None, 'lower': lower, 'upper': upper, 'coverage': known / 100, 'rubric_hash': RUBRIC_HASH}
    ids = {e['evidence_id'] for e in record['evidence']}
    assert len(ids) == len(record['evidence'])
    for e in record['evidence']:
        assert e['quote'] and e['quote'] in text, (key, e['evidence_id'], 'quote not continuous exact text')
    def check_refs(obj: object) -> None:
        if isinstance(obj, dict):
            for name, val in obj.items():
                if name in ('evidence_ids', 'counterevidence_ids'):
                    assert set(val) <= ids, (key, name, val)
                check_refs(val)
        elif isinstance(obj, list):
            for val in obj:
                check_refs(val)
    check_refs(record)
    assert record['domain_pattern']['namespace'] == 'embodied'
    assert len(record['domain_pattern']['matches']) <= 3
    assert len(record['rs_pattern']['supporting']) <= 2
    parents = {}
    for line in (ROOT / 'research/reference/researchstudio-15-31/PARENTS.tsv').read_text().splitlines():
        parts = line.split('\t')
        if len(parts) >= 2:
            parents['rs:' + parts[0]] = parts[1]
    for match in record['rs_pattern']['matches']:
        if match['sub_id'] is not None:
            assert parents[match['sub_id']] == match['main_id'], (match, parents)
    required = {'schema_version','run_id','batch_id','attempt_id','seat','paper','provenance','materials','evidence','signatures','gap','rs_pattern','domain_pattern','pattern_mapping','expectations','claims','assessment','ratings','score','status','reason'}
    assert required <= set(record)
    assert record['status'] in ('reviewed','needs_fulltext','needs_evidence','out_of_scope')
    target = OUT / (key + '.json')
    assert not target.exists(), 'Never overwrite a completed record'
    temp = OUT / (key + '.json.tmp')
    with temp.open('w') as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())
    assert json.loads(temp.read_text()) == record
    os.replace(temp, target)
    print(json.dumps({'paper': key, 'status': record['status'], 'score': record['score']}, ensure_ascii=False))
