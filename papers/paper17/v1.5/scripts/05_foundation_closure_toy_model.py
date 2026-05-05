#!/usr/bin/env python3
from __future__ import annotations


"""Toy KMS/GNS check for the Paper 17 A-vacuum foundation package.

Paper 17 constructs the A-vacuum as a direct integral of fiberwise KMS states.
This public script gives a deterministic 2x2 finite-dimensional check of the
KMS identity for a Gibbs state and records positivity/faithfulness diagnostics.

The script is support tooling, not a proof of the full operator-algebra theorem.
It is included so reviewers can rerun the numerical sanity check without the
private lab environment.

Usage:
    python3 scripts/05_foundation_closure_toy_model.py

Output:
    results/foundation_closure_toy_model_results.json
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results' / 'foundation_closure_toy_model_results.json'


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def main() -> None:
    h0, h1 = 0.0, 1.0
    z = math.exp(-h0) + math.exp(-h1)
    rho = [[math.exp(-h0) / z, 0.0], [0.0, math.exp(-h1) / z]]
    exp_minus_h = [[math.exp(-h0), 0.0], [0.0, math.exp(-h1)]]
    exp_plus_h = [[math.exp(h0), 0.0], [0.0, math.exp(h1)]]
    a = [[0.2, 0.7], [-0.4, 0.3]]
    b = [[0.1, -0.5], [0.8, -0.2]]
    alpha_i_b = matmul(matmul(exp_minus_h, b), exp_plus_h)
    lhs = trace(matmul(matmul(rho, a), alpha_i_b))
    rhs = trace(matmul(matmul(rho, b), a))
    residual = abs(lhs - rhs)
    payload = {
        'claim_status': 'finite-dimensional KMS/GNS support check for constructed A-vacuum package',
        'rho': rho,
        'rho_min_eigenvalue': min(rho[0][0], rho[1][1]),
        'rho_positive': rho[0][0] > 0 and rho[1][1] > 0,
        'rho_normalized': abs(trace(rho) - 1.0) < 1e-15,
        'kms_residual_beta_1': residual,
        'kms_holds_to_tolerance': residual < 1e-14,
        'scope_boundary': 'toy finite-dimensional check only; full theorem relies on standard GNS/KMS/direct-integral operator algebra',
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
