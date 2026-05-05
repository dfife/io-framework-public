#!/usr/bin/env python3
from __future__ import annotations


"""Verify the uniqueness condition in Paper 17 Theorem 17.2.

The theorem is algebraic. Since

    ln T_obs(R4) = ln T_IO + R4 * K_gauge * ln x,

and `K_gauge * ln x` is nonzero, the map from R4 to log-temperature is affine
with nonzero slope. Therefore exactly one R4 maps the readout family to FIRAS.

Usage:
    python3 scripts/03_readout_uniqueness_check.py

Output:
    results/readout_uniqueness_results.json
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'imported_constants.json'
OUT = ROOT / 'results' / 'readout_uniqueness_results.json'


def main() -> None:
    c = json.loads(DATA.read_text(encoding='utf-8'))['framework_constants']
    gamma = c['gamma_BI']['value']
    x = c['x']['value']
    t_io = c['T_IO_K']['value']
    t_firas = c['T_FIRAS_K']['value']
    k_gauge = math.log(1.0 + gamma * gamma)
    slope = k_gauge * math.log(x)
    r4 = math.log(t_firas / t_io) / slope
    samples = []
    for candidate in [0.5, 1.0, r4, 1.5]:
        samples.append({'R4': candidate, 'T_obs_K': t_io * (x ** (candidate * k_gauge))})
    payload = {
        'theorem': 'Uniqueness of the empirical readout normalization',
        'conditions': {
            'T_IO_positive': t_io > 0,
            'T_FIRAS_positive': t_firas > 0,
            'x_positive': x > 0,
            'x_not_one': x != 1.0,
            'K_gauge_not_zero': k_gauge != 0.0,
            'slope_nonzero': slope != 0.0,
        },
        'slope_K_gauge_ln_x': slope,
        'strictly_monotone': slope > 0,
        'unique_R4_solution': r4,
        'sample_values': samples,
        'status': 'DERIVED uniqueness given the FIRAS empirical datum',
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
