#!/usr/bin/env python3
from __future__ import annotations


"""Produce a compact machine summary of the Paper 17 kappa audit.

Usage:
    python3 scripts/08_kappa_audit_summary.py

Output:
    results/kappa_audit_summary_results.json
"""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'reports' / 'paper17_kappa_audit_results.json'
OUT = ROOT / 'results' / 'kappa_audit_summary_results.json'


def main() -> None:
    audit = json.loads(AUDIT.read_text(encoding='utf-8'))
    verdicts = Counter(t['verdict'] for t in audit['targets'])
    payload = {
        'paper': audit['paper'],
        'executive_verdict': audit['executive_verdict'],
        'hidden_parameter_found': audit['hidden_parameter_found'],
        'load_bearing_visible_field': audit['load_bearing_visible_field'],
        'retired_claim': audit['retired_claim'],
        'active_claim': audit['active_claim'],
        'target_count': len(audit['targets']),
        'verdict_counts': dict(verdicts),
        'open_items': audit['open_items'],
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
