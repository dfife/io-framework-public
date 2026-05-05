#!/usr/bin/env python3
from __future__ import annotations


"""Referee-facing validator for the Paper 17 v1.5 bundle.

The validator reruns all active public scripts, then checks the generated JSON
outputs against the values quoted in Paper 17 v1.5. It exits with code 0 only
if every check passes.

Usage from repository root:
    python3 papers/paper17/v1.5/scripts/09_validate_expected_outputs.py

Usage from bundle root:
    python3 scripts/09_validate_expected_outputs.py
"""

import json
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    '01_gauge_payload_determinant.py',
    '02_firas_fixed_r4.py',
    '03_readout_uniqueness_check.py',
    '04_modular_projection_surrogate.py',
    '05_foundation_closure_toy_model.py',
    '06_framework_constructible_uniqueness_summary.py',
    '07_r4_no_go_registry.py',
    '08_kappa_audit_summary.py',
]

checks = []


def add(name: str, passed: bool, observed, expected, tolerance) -> None:
    checks.append({'name': name, 'pass': bool(passed), 'observed': observed, 'expected': expected, 'tolerance': tolerance})


def close(obs, exp, tol):
    return abs(obs - exp) <= tol


def load(name):
    return json.loads((ROOT / 'results' / name).read_text(encoding='utf-8'))


def main() -> int:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(ROOT / 'scripts' / script)], check=True, cwd=ROOT, stdout=subprocess.DEVNULL)

    det = load('gauge_payload_determinant_results.json')
    r4 = load('firas_fixed_r4_results.json')
    uniq = load('readout_uniqueness_results.json')
    mod = load('modular_projection_surrogate_results.json')
    gns = load('foundation_closure_toy_model_results.json')
    enum = load('framework_constructible_uniqueness_results.json')
    nogo = load('r4_no_go_registry_results.json')
    audit = load('kappa_audit_summary_results.json')

    add('Q = 1 + gamma_BI^2', close(det['Q'], 1.05640625, 1e-15), det['Q'], 1.05640625, 1e-15)
    add('a = dim(S2)/2 = 1', close(det['a_dim_S2_over_2'], 1.0, 1e-15), det['a_dim_S2_over_2'], 1.0, 1e-15)
    add('a is not R4', det['a_is_R4'] is False, det['a_is_R4'], False, 'exact')
    add('K_gauge', close(det['K_gauge'], 0.05487281774291466, 1e-15), det['K_gauge'], 0.05487281774291466, 1e-15)
    add('x^K_gauge', close(det['x_to_K_gauge'], 1.0232048419891602, 1e-15), det['x_to_K_gauge'], 1.0232048419891602, 1e-15)

    outs = r4['outputs']
    add('R4_FIRAS', close(outs['R4_FIRAS'], 1.0031014644105183, 1e-15), outs['R4_FIRAS'], 1.0031014644105183, 1e-15)
    add('sigma_R4_FIRAS_only', close(outs['sigma_R4_FIRAS_only'], 0.009596597151571828, 1e-15), outs['sigma_R4_FIRAS_only'], 0.009596597151571828, 1e-15)
    add('T_obs(R4_FIRAS)=FIRAS', close(outs['T_obs_R4_FIRAS_K'], 2.7255, 1e-15), outs['T_obs_R4_FIRAS_K'], 2.7255, 1e-15)
    add('T_obs(R4=1) historical diagnostic', close(outs['T_obs_R4_equals_1_K'], 2.725306096638128, 1e-15), outs['T_obs_R4_equals_1_K'], 2.725306096638128, 1e-15)

    add('Theorem 17.2 slope nonzero', uniq['conditions']['slope_nonzero'], uniq['slope_K_gauge_ln_x'], 'nonzero', 'boolean')
    add('Theorem 17.2 strictly monotone', uniq['strictly_monotone'], uniq['strictly_monotone'], True, 'boolean')
    add('Theorem 17.2 unique R4', close(uniq['unique_R4_solution'], 1.0031014644105183, 1e-15), uniq['unique_R4_solution'], 1.0031014644105183, 1e-15)

    add('modular projection surrogate identity', mod['surrogate']['identity_holds_to_tolerance'], mod['surrogate']['max_direct_sum_vs_combined_error'], '<1e-14', 'boolean')
    add('physical sector R4 fixed externally', mod['physical_sector']['R4_fixed_by'].startswith('FIRAS'), mod['physical_sector']['R4_fixed_by'], 'FIRAS via Theorem 17.2', 'string')

    add('toy GNS state positive', gns['rho_positive'], gns['rho_positive'], True, 'boolean')
    add('toy GNS state normalized', gns['rho_normalized'], gns['rho_normalized'], True, 'boolean')
    add('toy KMS residual', gns['kms_residual_beta_1'] < 1e-14, gns['kms_residual_beta_1'], '<1e-14', 'boolean')

    add('enumeration raw FIRAS-band hits', enum['raw_firas_band_hits_from_frozen_enumeration'] == 5545, enum['raw_firas_band_hits_from_frozen_enumeration'], 5545, 'exact')
    add('seven aliases collapse to K_gauge', enum['all_aliases_collapse_to_K_gauge'], enum['max_alias_error'], '<1e-14', 'boolean')
    add('enumeration does not fix R4', enum['does_not_fix_R4'], enum['does_not_fix_R4'], True, 'boolean')

    add('R4 not internally derived', nogo['r4_internally_derived'] is False, nogo['r4_internally_derived'], False, 'exact')
    add('R4 visible in v1.5', nogo['r4_visible_in_v15'] is True, nogo['r4_visible_in_v15'], True, 'exact')
    add('kappa audit no hidden parameter', audit['hidden_parameter_found'] is False, audit['hidden_parameter_found'], False, 'exact')
    add('kappa audit target count', audit['target_count'] == 12, audit['target_count'], 12, 'exact')

    fail_count = 0
    for item in checks:
        status = 'PASS' if item['pass'] else 'FAIL'
        if not item['pass']:
            fail_count += 1
        print(f"{status} {item['name']} observed={item['observed']} expected={item['expected']} tol={item['tolerance']}")

    pass_count = len(checks) - fail_count
    print(f'SUMMARY total_checks={len(checks)} pass_count={pass_count} fail_count={fail_count}')
    return 0 if fail_count == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main())
