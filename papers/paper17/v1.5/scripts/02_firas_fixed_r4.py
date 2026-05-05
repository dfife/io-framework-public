#!/usr/bin/env python3
from __future__ import annotations


"""Compute the FIRAS-fixed optical readout normalization R4.

Paper 17 v1.5 no longer treats the observed CMB temperature as an independent
IO prediction. Instead, FIRAS supplies the empirical observer-side thermal datum
inside the readout family

    T_obs(R4) = T_IO * x ** (R4 * K_gauge).

Solving T_obs(R4) = T_FIRAS gives the unique normalization

    R4_FIRAS = ln(T_FIRAS / T_IO) / (K_gauge * ln x).

Usage:
    python3 scripts/02_firas_fixed_r4.py

Output:
    results/firas_fixed_r4_results.json
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'imported_constants.json'
OUT = ROOT / 'results' / 'firas_fixed_r4_results.json'


def main() -> None:
    c = json.loads(DATA.read_text(encoding='utf-8'))['framework_constants']
    gamma = c['gamma_BI']['value']
    x = c['x']['value']
    t_io = c['T_IO_K']['value']
    t_firas = c['T_FIRAS_K']['value']
    sigma_firas = c['T_FIRAS_K']['sigma']
    k_gauge = math.log(1.0 + gamma * gamma)
    slope = k_gauge * math.log(x)
    r4 = math.log(t_firas / t_io) / slope
    sigma_r4 = sigma_firas / (t_firas * slope)
    t_unit = t_io * (x ** k_gauge)
    payload = {
        'claim_status': 'Conditional_Verified on Premise 2 plus FIRAS empirical thermal datum',
        'formula': 'R4_FIRAS = ln(T_FIRAS/T_IO)/(K_gauge ln x)',
        'inputs': {
            'T_IO_K': t_io,
            'T_FIRAS_K': t_firas,
            'sigma_FIRAS_K': sigma_firas,
            'x': x,
            'gamma_BI': gamma,
            'K_gauge': k_gauge,
            'K_gauge_ln_x': slope,
        },
        'outputs': {
            'R4_FIRAS': r4,
            'sigma_R4_FIRAS_only': sigma_r4,
            'sigma_effective': r4 * k_gauge,
            'T_obs_R4_FIRAS_K': t_io * (x ** (r4 * k_gauge)),
            'T_obs_R4_equals_1_K': t_unit,
            'R4_equals_1_FIRAS_residual_sigma': (t_unit - t_firas) / sigma_firas,
        },
        'guardrail': 'R4 is fixed once by FIRAS and is not retuned against downstream observables.',
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
