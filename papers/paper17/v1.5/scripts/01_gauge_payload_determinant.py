#!/usr/bin/env python3
from __future__ import annotations


"""Reproduce the Paper 17 v1.5 gauge-payload determinant arithmetic.

This script is intentionally small and explicit. It verifies the gauge-side
objects used by Paper 17's Modular Projection Theorem:

    Q = 1 + gamma_BI^2
    a = dim(S2) / 2 = 1
    K_gauge = ln(Q)

The `a` here is the Gaussian determinant exponent internal to the gauge-side
construction of `K_gauge`. It is not the optical readout normalization `R4`.
That distinction is load-bearing in Paper 17 v1.5.

Usage:
    python3 scripts/01_gauge_payload_determinant.py

Output:
    results/gauge_payload_determinant_results.json
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'imported_constants.json'
OUT = ROOT / 'results' / 'gauge_payload_determinant_results.json'


def main() -> None:
    constants = json.loads(DATA.read_text(encoding='utf-8'))['framework_constants']
    gamma = constants['gamma_BI']['value']
    dim_s2 = constants['dim_S2']['value']
    x = constants['x']['value']
    q = 1.0 + gamma * gamma
    a = dim_s2 / 2.0
    k_gauge = math.log(q)
    transfer_unit = x ** k_gauge
    payload = {
        'claim_status': 'DERIVED for gauge payload within Paper 17 G1-G6; a is internal gauge determinant exponent, not R4',
        'gamma_BI': gamma,
        'Q': q,
        'dim_S2': dim_s2,
        'a_dim_S2_over_2': a,
        'a_is_R4': False,
        'K_gauge': k_gauge,
        'x_to_K_gauge': transfer_unit,
        'checks': {
            'a_equals_one': abs(a - 1.0) < 1e-15,
            'K_gauge_matches_manuscript': abs(k_gauge - 0.05487281774291466) < 1e-15,
        },
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
