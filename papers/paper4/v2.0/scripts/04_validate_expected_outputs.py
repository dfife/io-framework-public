#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_generators() -> None:
    for script in (
        "01_horizon_connections.py",
        "02_projected_age_and_curvature.py",
        "03_inherited_claims.py",
    ):
        subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True, cwd=ROOT)


def get(obj, path):
    cur = obj
    for key in path:
        cur = cur[key]
    return cur


def check(name: str, actual, expected, tol: float = 0.0) -> bool:
    if isinstance(expected, str):
        ok = actual == expected
    else:
        ok = math.isclose(float(actual), float(expected), rel_tol=0.0, abs_tol=tol)
    print(f"{'PASS' if ok else 'FAIL'} {name}: actual={actual!r} expected={expected!r} tol={tol}")
    return ok


def main() -> None:
    run_generators()
    h = json.loads((ROOT / "results" / "horizon_connections_results.json").read_text())
    a = json.loads((ROOT / "results" / "projected_age_and_curvature_results.json").read_text())
    i = json.loads((ROOT / "results" / "inherited_claims_results.json").read_text())

    tests = [
        ("r_s", h["derived"]["r_s_m"], 6.6835442422068e26, 1e15),
        ("T_IO", h["derived"]["T_IO_at_R_U_K"], 2.6631785086103616, 1e-12),
        ("thermal_invariant", h["derived"]["thermal_invariant_K_m"], 1.1717964823462745e27, 1e15),
        ("a0", h["derived"]["a0_m_s2"], 1.344728404820229e-10, 1e-22),
        ("rho_torsion_eff", h["derived"]["rho_Lambda_torsion_eff_kg_m3"], 5.81759252416424e-27, 1e-39),
        ("rho_torsion_percent", h["derived"]["rho_Lambda_torsion_eff_percent_offset_vs_observed"], -2.38938717845234, 1e-12),
        ("rho_active", h["derived"]["rho_Lambda_active_observer_kg_m3"], 5.9792089957916785e-27, 1e-39),
        ("rho_active_percent", h["derived"]["rho_Lambda_active_percent_offset_vs_observed"], 0.32229858710870474, 1e-12),
        ("gamma_bridge", h["derived"]["gamma_BI_recovered_paper2_v20"], 0.240, 1e-15),
        ("gamma_bridge_percent", h["derived"]["gamma_BI_recovered_percent_offset_vs_0p2375"], 1.0526315789473717, 1e-12),
        ("age_z6", a["projected_optical_age_rows"][0]["t_IO_projected_Gyr"], 0.8834558231309765, 1e-12),
        ("age_z20", a["projected_optical_age_rows"][3]["t_IO_projected_Gyr"], 0.16870704032521391, 1e-12),
        ("age_z20_ratio", a["projected_optical_age_rows"][3]["ratio_IO_over_LCDM"], 0.9500503897904048, 1e-12),
        ("old_w0_diagnostic", a["old_curvature_diagnostic"]["w0_apparent"], -1.0471070148489503, 1e-15),
        ("paper35_w0", a["paper35_flat_cpl_reinterpretation"]["w0"], -1.030263043675755, 1e-15),
        ("jwst_z14", i["jwst_formation_clock"]["rows"][2]["t_form_gyr"], 0.43886595571758996, 1e-15),
        ("S8", i["s8_growth"]["S8"], 0.8113047125049078, 1e-15),
        ("sigma8", i["s8_growth"]["sigma8"], 0.9274824965120387, 1e-15),
        ("S8_pull", i["s8_growth"]["pull_sigma_vs_weak_lensing"], 1.0652356252453865, 1e-15),
        ("D_H", i["bbn_scorecard"]["D_H"], 2.5072097840055007e-05, 1e-18),
        ("D_H_sigma", i["bbn_scorecard"]["D_H_sigma"], -0.659673866483311, 1e-15),
        ("Y_p", i["bbn_scorecard"]["Y_p"], 0.24770877182909237, 1e-15),
        ("Y_p_sigma", i["bbn_scorecard"]["Y_p_sigma"], 0.6771929572730941, 1e-15),
        ("Li7_H", i["bbn_scorecard"]["Li7_H"], 1.7414708079857392e-10, 1e-22),
        ("Li7_sigma", i["bbn_scorecard"]["Li7_sigma"], 0.520873574147546, 1e-15),
        ("theta_star", i["acoustic_scale"]["theta_star_pred_deg_current_rounded_row"], 0.598873398398795, 1e-15),
        ("theta_star_sigma", i["acoustic_scale"]["theta_star_sigma_offset_current_rounded_row"], 9.205378456904015, 1e-15)
    ]
    passes = sum(1 for t in tests if check(*t))
    total = len(tests)
    failures = total - passes
    print(f"SUMMARY total_checks={total} pass_count={passes} fail_count={failures}")
    raise SystemExit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
