#!/usr/bin/env python3
"""Paper 18 v1.6 script 17: validate expected outputs.

Purpose:
    Referee entry point. Rerun the core non-external numbered scripts and
    validate every live frozen output against explicit tolerances.

External-data discipline:
    Scripts 08 and 10 require DESI/CLASS and BOSS/CAMB external assets. The
    validator checks their frozen audited JSON outputs but does not refetch
    or redistribute external datasets by default. Run those scripts manually
    after following `data/external_data_sources.md` if a full external rerun is
    desired.

Run from repository root:

    python3 papers/paper18/v1.6/scripts/17_validate_expected_outputs.py

or from this bundle root:

    python3 scripts/17_validate_expected_outputs.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"

CORE_SCRIPTS = [
    "01_cmp_theorem.py",
    "02_bdp_theorem.py",
    "03_bdp_gap_closure.py",
    "04_v_alpha_uniqueness.py",
    "05_neff_entropy_rank.py",
    "06_bogoliubov_coefficients.py",
    "07_modular_bogoliubov_upgrade.py",
    "09_jwst_age_recalculation.py",
    "11_zeq_kruskal_audit.py",
    "12_curvature_implementation_resolution.py",
    "13_bdp_epoch_independence_audit.py",
    "14_structural_attacks_audit.py",
    "15_r4_impact_audit.py",
    "16_kappa_audit_summary.py",
]


def load_json(name: str) -> Any:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def at(obj: Any, path: tuple[Any, ...]) -> Any:
    cur = obj
    for key in path:
        cur = cur[key]
    return cur


def close(actual: float, expected: float, tol: float) -> bool:
    return abs(actual - expected) <= tol


def record(checks: list[tuple[str, bool, str]], name: str, passed: bool, detail: str = "") -> None:
    checks.append((name, passed, detail))
    status = "PASS" if passed else "FAIL"
    print(f"{status} {name}{(' ' + detail) if detail else ''}")


def main() -> int:
    for script in CORE_SCRIPTS:
        subprocess.run([sys.executable, str(BUNDLE_ROOT / "scripts" / script)], check=True)

    checks: list[tuple[str, bool, str]] = []

    cmp = load_json("paper18_cmp_theorem_checks.json")
    bdp = load_json("paper18_bdp_theorem_checks.json")
    bdpgap = load_json("paper18_bdp_gap_closure_checks.json")
    valpha = load_json("paper18_v_alpha_theorem_checks.json")
    neff = load_json("paper18_neff_delta_theorem_checks.json")
    bog = load_json("paper18_bogoliubov_coefficients_checks.json")
    mod = load_json("paper18_modular_bogoliubov_upgrade_checks.json")
    legacy = load_json("paper18_legacy_observables_recalculation_checks.json")
    jwst = load_json("paper18_jwst_age_recalculation_checks.json")
    matter = load_json("paper18_matter_power_shape_test_checks.json")
    zeq = load_json("paper18_zeq_kruskal_audit_checks.json")
    curvature = load_json("paper18_curvature_implementation_resolution_checks.json")
    epoch = load_json("paper18_bdp_epoch_independence_audit_checks.json")
    attacks = load_json("paper18_structural_attacks_audit_checks.json")
    impact = load_json("paper18_v16_r4_impact_audit_results.json")
    audit = load_json("paper18_v16_r4_kappa_audit_results.json")
    summary = load_json("kappa_audit_summary_results.json")

    record(checks, "CMP Delta", cmp["Delta = x^4 (1 + gamma^2)"] == "5.62421685262410640625")
    record(checks, "CMP additive closure", cmp["additive_error = K_geom + K_gauge - ln Delta"] == "0E-99")
    record(checks, "BDP f_b", bdp["f_b = V_prime / x = 2 gamma / x"].startswith("0.31270572745227123107"))
    record(checks, "BDP identity", bdp["identity_error = f_b*F - <K>/4"] == "0E-100")
    record(checks, "BDP gap identity", bdpgap["identity_f_b_F_minus_<K>/4"] == "0E-100")
    record(checks, "V(alpha) ODE", valpha["symbolic"]["ODE_residual_V_double_prime_minus_2expV"] == "0")
    record(checks, "V(alpha) V_prime", valpha["numeric_gamma_0.2375"]["V_prime = 2 gamma"] == "0.4750")
    record(checks, "entropy-rank Delta", neff["N_eff_numeric"] == "5.62421685262410640625")
    record(checks, "entropy-rank P_k", neff["P_k_numeric"].startswith("0.06007818832778484010"))

    record(checks, "R4_FIRAS in Bogoliubov", close(bog["inputs"]["R4_FIRAS"], 1.0031014644, 1e-13))
    record(checks, "T_obs equals FIRAS", close(bog["inputs"]["T_obs_K"], 2.7255, 1e-12))
    record(checks, "Bogoliubov CCR residual", bog["wavepacket_matrix_checks"]["max_ccr_residual"] < 1e-14)
    record(checks, "Bogoliubov obs peak frequency", close(bog["peak_examples"]["obs_peak_frequency_GHz"], 160.23012152462556, 1e-9))
    record(checks, "modular pushforward residual", close(mod["uniqueness_checks"]["modular_transport_residual"], 0.0, 1e-15))

    record(checks, "legacy BAO chi2", close(legacy["bao"]["IO_chi2"], 19.80166516162162, 1e-10))
    record(checks, "legacy S8", close(legacy["sigma8"]["IO_geometric_baryons"]["S8"], 0.8021928657913614, 1e-12))
    record(checks, "legacy w0 apparent", close(legacy["w"]["w0_apparent_flat_CPL_misread"], -1.0060161104282384, 1e-12))
    record(checks, "JWST z10 IO age", close(float(jwst["comparison"]["10"]["IO_age_Myr"]), 445.6912681580386, 1e-9))
    record(checks, "JWST z14 IO age", close(float(jwst["comparison"]["14"]["IO_age_Myr"]), 279.3744527598197, 1e-9))
    record(checks, "P(k) amp_const chi2", close(matter["totals"]["amp_const"]["IO"], 1056.553249244046, 1e-9))
    record(checks, "P(k) amp_const_k2 chi2", close(matter["totals"]["amp_const_k2"]["IO"], 842.1065323642468, 1e-9))
    record(checks, "z_eq active", close(zeq["equality_redshift"]["z_eq_active"], 2823.8794250543247, 1e-9))
    record(checks, "curvature Schur branch", curvature["active_branch_after_Theorem_18N"] == "Schur")
    record(checks, "epoch present fb", close(epoch["present_epoch"]["fb_eta_s"], 0.31270778609476385, 1e-15))
    record(checks, "structural attack 1 valid", attacks["attack1_commutative_modular_fact"]["status"] == "valid_terminology_attack")

    record(checks, "impact map count", len(impact["r4_usage_map"]) == 6)
    record(checks, "impact hidden parameter false", impact["kappa_audit_verdict"]["hidden_continuous_fitted_parameter_found"] is False)
    record(checks, "audit hidden parameter false", audit["hidden_continuous_fitted_parameter_found"] is False)
    record(checks, "audit stale overclaim true", audit["stale_overclaim_found"] is True)
    record(checks, "summary retires CMB prediction", summary["checks"]["independent_CMB_temperature_prediction_retired"] is True)

    pass_count = sum(1 for _, passed, _ in checks if passed)
    fail_count = len(checks) - pass_count
    print(f"SUMMARY total_checks={len(checks)} pass_count={pass_count} fail_count={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
