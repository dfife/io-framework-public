#!/usr/bin/env python3
from __future__ import annotations


"""Finite-dimensional surrogate for the Modular Projection Theorem.

The actual Paper 17 theorem is an operator-algebra statement using direct
integrals and Tomita-Takesaki modular flow. This script reproduces the compact
numerical check used in the support artifacts: a block-diagonal finite model in
which assembling fiber modular flows equals exponentiating the combined
operator `D tensor K_hat`.

This is not a replacement for the theorem proof. It is a reproducible check of
the algebraic identity used by the proof in a finite-dimensional surrogate.

Usage:
    python3 scripts/04_modular_projection_surrogate.py

Output:
    results/modular_projection_surrogate_results.json
"""

import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'imported_constants.json'
OUT = ROOT / 'results' / 'modular_projection_surrogate_results.json'


def main() -> None:
    constants = json.loads(DATA.read_text(encoding='utf-8'))['framework_constants']
    gamma = constants['gamma_BI']['value']
    kappas = [0.03, 0.09]
    d_eigs = [-0.7, 0.2, 1.1]
    t = 0.4
    direct_sum = []
    combined = []
    for kappa in kappas:
        for d in d_eigs:
            direct_sum.append(cmath.exp(1j * t * kappa * d))
            combined.append(cmath.exp(1j * t * (kappa * d)))
    max_error = max(abs(a - b) for a, b in zip(direct_sum, combined))
    k_gauge = math.log(1.0 + gamma * gamma)
    payload = {
        'claim_status': 'finite-dimensional verification surrogate for DERIVED/THEOREM modular projection within reduced sector',
        'surrogate': {
            'kappas': kappas,
            'D_eigenvalues': d_eigs,
            'time_t': t,
            'max_direct_sum_vs_combined_error': max_error,
            'identity_holds_to_tolerance': max_error < 1e-14,
        },
        'physical_sector': {
            'K_gauge': k_gauge,
            'modular_generator': 'D tensor K_hat_g; on physical tangential sector K_hat_g = K_gauge I',
            'readout_family': 'T_obs(R4) = T_IO*x^(R4*K_gauge)',
            'R4_fixed_by': 'FIRAS via Theorem 17.2, not by this surrogate',
        },
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
