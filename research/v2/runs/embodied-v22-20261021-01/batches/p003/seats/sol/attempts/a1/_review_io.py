"""Attempt-local record assembly and strict source/arithmetic checks; no paper code runs."""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path('/home/lingxufeng/embodied-harness-radar')
RUN = ROOT / 'research/v2/runs/embodied-v22-20261021-01'
OUT = RUN / 'batches/p003/seats/sol/attempts/a1'
INPUT = json.loads((RUN / 'batches/p003/inputs_manifest.json').read_text())
META = json.loads((RUN / 'manifest.json').read_text())
WEIGHTS = {'G': 15, 'M': 20, 'X': 20, 'measurement': 15, 'causality': 10,
           'holdout': 10, 'statistics': 5, 'cost': 5}
RS = ROOT / 'research/reference/researchstudio-15-31'
PARENTS = dict(line.split('\t') for line in (RS / 'PARENTS.tsv').read_text().splitlines()[1:] if line)
TAX = json.loads((ROOT / 'research/patterns/taxonomy.json').read_text())


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def asset_map(paths: list[str]) -> dict[str, str]:
    return {p: sha((ROOT / p).read_bytes()) for p in sorted(set(paths))}


def bundle_hash(mapping: dict[str, str]) -> str:
    return sha(json.dumps(mapping, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode())


def atomic(path: Path, record: dict[str, Any]) -> None:
    if path.exists():
        raise FileExistsError(f'Refusing to overwrite completed output: {path}')
    temp = path.with_suffix('.json.tmp')
    with temp.open('x', encoding='utf-8') as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    json.loads(temp.read_text())
    os.replace(temp, path)


def write_review(c: dict[str, Any]) -> dict[str, Any]:
    p = next(x for x in INPUT['papers'] if x['paper_key'] == c['id'])
    source = ROOT / p['material_path']
    text = source.read_text()
    assert sha(source.read_bytes()) == p['material_sha256']
    ev = []
    for index, (quote, section, explanation) in enumerate(c['evidence'], 1):
        position = text.find(quote)
        assert position >= 0, (p['paper_key'], quote)
        line = text[:position].count('\n') + 1
        ev.append({'evidence_id': f'E{index:03}', 'material_id': 'M1',
                   'material_hash': p['material_sha256'], 'sha256': p['material_sha256'],
                   'locator': f'{p["version"]}; {section}; extracted-text L{line}; character {position}',
                   'quote': quote, 'support_explanation': explanation, 'kind': 'author_report'})
    cardpaths = ['research/patterns/taxonomy.json', 'research/patterns/conditions.json']
    for domain in c['domain']:
        cardpaths.append(f'patterns/main/{domain["main"]}.md')
        if domain['sub']:
            cardpaths.append(f'patterns/sub/{domain["sub"]}.md')
    exp_paths = c['expectation_sources']
    cards = asset_map(cardpaths)
    exps = asset_map(exp_paths)
    originals = asset_map(['research/reference/researchstudio-15-31/PARENTS.tsv',
                          'research/reference/researchstudio-15-31/MANIFEST.tsv'] +
                         [f'research/reference/researchstudio-15-31/ideation-patterns/{m["main_id"]}.md' for m in c['rs']] +
                         [f'research/reference/researchstudio-15-31/ideation-sub-patterns/{m["sub_id"][3:]}.md' for m in c['rs'] if m['sub_id']])
    for domain in c['domain']:
        if domain['sub']:
            assert TAX['sub'][domain['sub']]['main'] == domain['main']
        domain.update(namespace='embodied', version='embodied-agent-harness/v1 + board-induced 2026-10-21')
    for match in c['rs']:
        if match['sub_id']:
            assert match['sub_id'].startswith('rs:')
            assert PARENTS[match['sub_id'][3:]] == match['main_id']
    ratings = {'E': {}}
    for key, value, reason, refs, counter in c['ratings']:
        row = {'status': 'not_reported' if value == 0 else 'resolved', 'rating': value,
               'reason': reason, 'evidence_ids': refs, 'counterevidence_ids': counter,
               'search_scope': [p['version'] + ': full main text, experiments, limitations, all supplied appendices; cost/call/token/latency/budget reporting'] if value == 0 else []}
        if key in ('G', 'M', 'X'):
            ratings[key] = row
        else:
            ratings['E'][key] = row
    raw = sum(WEIGHTS[key] * value for key, value, *_ in c['ratings']) / 4
    record = {
        'schema_version': 'radar-review-v2.2', 'run_id': INPUT['run_id'], 'batch_id': 'p003',
        'attempt_id': 'a1', 'seat': 'sol',
        'paper': {k: p[k] for k in ('paper_key', 'paper_id', 'title', 'version')},
        'provenance': {
            'input_hash': INPUT['input_hash'], 'rubric_version': META['rubric_version'],
            'rubric_hash': META['hashes']['score_spec'], 'rs_manifest_hash': META['hashes']['rs_manifest'],
            'domain_cards_hash': bundle_hash(cards), 'expectations_hash': bundle_hash(exps),
            'asset_hash_scheme': 'SHA256(canonical JSON relative-path -> SHA256(file bytes), sort_keys UTF8 ensure_ascii=false compact)',
            'domain_card_assets': cards, 'expectation_assets': exps, 'rs_assets': originals,
            'expectations_note': 'Expectations are embedded in fixed main cards; no standalone expectations asset. Historical reviewer expectations are source-derived checks, not evidence of this paper\'s review outcome.',
            'model_type': 'sonnet', 'model_type_description': 'sonnet type overlay gpt-6.1-sol (6.1 Sol)',
            'actual_model': 'gpt-6.1-sol', 'actual_model_basis': 'Assigned runtime identity; no model probing or reconfiguration.',
            'session_id': None, 'receipt_ref': None,
            'session_receipt_unavailable_reason': 'No independently available subagent session ID/receipt in assigned runtime; not fabricated or probed.',
            'timestamp': datetime.now(timezone.utc).isoformat(), 'phase': 'production',
            'anchors_version': 'v2', 'anchors_sha256': '3ececdd11cc3d14469939731c6290ee42c423e8bf840ba8a8295c1cb58aedb73',
            'score_regime': 'production-under-anchors-v2', 'formally_frozen': False,
            'downstream_restriction': 'Not for formal ranking/Reel before further user confirmation.',
            'blindness': 'Only assigned manifest/materials, fixed rules/cards and designated anchors read; no other-seat, aggregate, old scores or outcome labels read.'},
        'materials': [{'material_id': 'M1', 'url': f'https://arxiv.org/html/{p["version"]}',
                       'version': p['version'], 'path': p['material_path'], 'sha256': p['material_sha256'],
                       'sections_read': c['sections'], 'complete': True, 'missing_sections': [],
                       'extraction_limits': c.get('extraction_limits', 'Full supplied text including appendices read. No external videos, code, or linked pages retrieved.'),
                       'completeness_basis': 'Methods, experimental protocol/results, limitations and end of supplied appendices inspected; completeness is text-material completeness, not independent verification of figures or software.'}],
        'evidence': ev, 'signatures': c['signatures'], 'gap': c['gap'],
        'rs_pattern': {'primary': c['rs'][0]['main_id'] if c['rs'] else None,
                       'supporting': [m['main_id'] for m in c['rs'][1:]], 'matches': c['rs'],
                       'outside_taxonomy': not bool(c['rs']), 'reason': c['rs_reason'],
                       'executes_pattern': True, 'resolves_problem': False},
        'domain_pattern': {'namespace': 'embodied', 'matches': c['domain'],
                           'unassigned': c.get('unassigned', []), 'revision_proposals': c.get('revision_proposals', [])},
        'pattern_mapping': c['mapping'], 'expectations': c['expectations'], 'claims': c['claims'],
        'assessment': c['assessment'], 'ratings': ratings,
        'score': {'raw': raw, 'display': round(raw, 1), 'lower': raw, 'upper': raw,
                  'coverage': 1.0, 'rubric_hash': META['hashes']['score_spec']},
        'status': 'reviewed', 'reason': c['reason'], 'scope': c['scope'],
        'audit_status': 'pending', 'audit_note': 'Independent initial seat review; source-quote/identity/hash/parent/arithmetic checks passed, not aggregate acceptance or reproduction.'}
    record['paper'].update(claim_type='system_method', central_claim=c['claim'])
    validate(record)
    atomic(OUT / (c['id'] + '.json'), record)
    return record


def validate(r: dict[str, Any]) -> None:
    expected = next(x for x in INPUT['papers'] if x['paper_key'] == r['paper']['paper_key'])
    assert all(r['paper'][k] == expected[k] for k in ('paper_id', 'version', 'title'))
    text = (ROOT / expected['material_path']).read_text()
    assert r['materials'][0]['sha256'] == sha((ROOT / expected['material_path']).read_bytes())
    assert sha((ROOT / 'research/SCORE_SPEC.md').read_bytes()) == r['score']['rubric_hash']
    assert sha((RS / 'MANIFEST.tsv').read_bytes()) == r['provenance']['rs_manifest_hash']
    assert sha((RUN / 'calibration/anchors.md').read_bytes()) == r['provenance']['anchors_sha256']
    assert len(r['domain_pattern']['matches']) <= 3
    ids = {e['evidence_id'] for e in r['evidence']}
    assert len(ids) == len(r['evidence'])
    for evidence in r['evidence']:
        assert evidence['quote'] and evidence['quote'] in text
        assert evidence['material_hash'] == expected['material_sha256']
    def walk(obj: Any) -> None:
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key in ('evidence_ids', 'counterevidence_ids'):
                    assert set(value) <= ids, (key, value)
                walk(value)
        elif isinstance(obj, list):
            for value in obj:
                walk(value)
    walk(r)
    total = 0
    for key, weight in WEIGHTS.items():
        row = r['ratings'][key] if key in ('G', 'M', 'X') else r['ratings']['E'][key]
        assert type(row['rating']) is int and 0 <= row['rating'] <= 4
        assert row['reason'] and (row['evidence_ids'] or row['search_scope'])
        assert row['status'] != 'not_reported' or (row['rating'] == 0 and row['search_scope'])
        total += weight * row['rating'] / 4
    assert r['score']['raw'] == total == r['score']['lower'] == r['score']['upper']
    assert r['score']['display'] == round(total, 1) and r['score']['coverage'] == 1
    for mapping in r['rs_pattern']['matches']:
        if mapping['sub_id']:
            assert PARENTS[mapping['sub_id'][3:]] == mapping['main_id']
    required = {'schema_version', 'run_id', 'batch_id', 'attempt_id', 'seat', 'paper', 'provenance',
                'materials', 'evidence', 'signatures', 'gap', 'rs_pattern', 'domain_pattern',
                'pattern_mapping', 'expectations', 'claims', 'assessment', 'ratings', 'score', 'status', 'reason'}
    assert required <= r.keys()


def rs_match(main: str, sub: str | None, role: str, fit: str, steps: list[str], checks: list[dict[str, Any]], refs: list[str], reason: str) -> dict[str, Any]:
    return {'main_id': main, 'sub_id': sub, 'role': role, 'fit': fit,
            'tactic_steps_checked': steps, 'success_failure_checks': checks,
            'evidence_ids': refs, 'reason': reason}


def check(identifier: str, status: str, reason: str, refs: list[str]) -> dict[str, Any]:
    return {'id': identifier, 'status': status, 'reason': reason, 'evidence_ids': refs}


def expectation(identifier: str, source: str, requirement: str, when: str, status: str,
                reason: str, score: list[str], refs: list[str], applicable: bool = True) -> dict[str, Any]:
    return {'id': identifier, 'version': 'fixed cards 2026-10-21', 'source_strength': 'common_practice',
            'source_refs': [source + '#Reviewer expectations'], 'requirement': requirement,
            'applies_when': when, 'applicable': applicable, 'status': status,
            'reason': reason, 'evidence_ids': refs, 'score_item': score}
