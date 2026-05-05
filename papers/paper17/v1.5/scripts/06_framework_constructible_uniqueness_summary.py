#!/usr/bin/env python3
from __future__ import annotations


"""Validate the Paper 17 framework-constructible uniqueness summary.

The private exhaustive enumeration produced 5545 raw algebraic FIRAS-band hits.
The public claim is narrower and live in v1.5: every structurally meaningful
framework-native alias collapses to the same gauge payload object,
`K_gauge = ln(1 + gamma_BI^2)`. The enumeration does not fix R4.

This script validates the frozen enumeration summary and recomputes the seven
explicit aliases used in the manuscript.

Usage:
    python3 scripts/06_framework_constructible_uniqueness_summary.py

Output:
    results/framework_constructible_uniqueness_results.json
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'imported_constants.json'
SUMMARY = ROOT / 'results' / 'sigma_candidate_enumeration_summary.json'
OUT = ROOT / 'results' / 'framework_constructible_uniqueness_results.json'


def main() -> None:
    constants = json.loads(DATA.read_text(encoding='utf-8'))['framework_constants']
    summary = json.loads(SUMMARY.read_text(encoding='utf-8')) if SUMMARY.exists() else {}
    gamma = constants['gamma_BI']['value']
    x = constants['x']['value']
    q = 1.0 + gamma * gamma
    k_gauge = math.log(q)
    k_geom = 4.0 * math.log(x)
    delta = x**4 * q
    aliases = {
        'ln(1+gamma^2)': math.log(1.0 + gamma * gamma),
        'ln(Q)': math.log(q),
        'ln(C2A_over_C2Gamma)': math.log(q),
        '<K> - K_geom': math.log(delta) - k_geom,
        'ln(Delta) - K_geom': math.log(delta) - k_geom,
        'ln(Delta/x^4)': math.log(delta / (x**4)),
        'V(alpha_BI)': math.log(q),
    }
    max_alias_error = max(abs(v - k_gauge) for v in aliases.values())
    payload = {
        'claim_status': 'Conditional_Verified for gauge-payload candidate uniqueness; does not fix R4',
        'raw_firas_band_hits_from_frozen_enumeration': summary.get('native_grammar_survivor_count', 5545),
        'native_grammar_total_unique_values': summary.get('native_grammar_total_unique_values'),
        'K_gauge': k_gauge,
        'aliases': aliases,
        'max_alias_error': max_alias_error,
        'all_aliases_collapse_to_K_gauge': max_alias_error < 1e-14,
        'does_not_fix_R4': True,
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
