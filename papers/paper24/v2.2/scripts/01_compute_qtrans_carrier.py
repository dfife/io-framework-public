#!/usr/bin/env python3
"""
Paper 24 v2.2 reproducibility script 01.

Purpose:
    Recompute the final-state quadrupole carrier audit used in Paper 24's
    mass-7 TT dressing chain. This is the non-PRyMordial part of the support
    bundle: it checks how the old required effective quadrupole scale maps to
    the manuscript carrier scale Q_trans ~= 0.040 b.

Inputs:
    All numeric inputs are recorded directly in this script and duplicated in
    data/imported_constants.json. No private lab files are read.

Outputs:
    results/qtrans_carrier_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    - verified: arithmetic and JSON reproduction of the carrier audit.
    - conditional: the final-state measured-Q(7Li) carrier rule.
    - reconstruction: minimal alpha+t cluster estimate.

Run:
    python3 scripts/01_compute_qtrans_carrier.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = BUNDLE_ROOT / "results" / "qtrans_carrier_results.json"


def compute() -> dict:
    """Return the Paper 24 v2.2 Q_trans carrier audit payload."""

    # IO and BBN constants used by the Paper 24 v2.2 carrier calculation.
    x = 1.519
    gamma = 0.2375
    q_d_barn = 0.0028578
    epsilon_n = 0.023843043660342757
    q_7li_barn = 0.04
    q_7be_theory_barn = 0.068
    q_req_old_barn = 0.026352749999399957
    li_obs = 1.58e-10
    li_sigma = 3.1e-11
    li0 = 5.391179180337131e-10
    nu34 = 5.796722954744

    def li_prediction(q_trans_barn: float) -> dict:
        """Evaluate the simplified lithium response for one Q_trans choice."""

        # In the corrected bridge convention the x^{-1} projection acts on the
        # effective branch amplitude, so Q_eff = Q_trans / x.
        q_eff = q_trans_barn / x

        # Simplified mass-7 suppression model used in the carrier audit:
        # Li7/H = Li0 * exp[-epsilon_n * 0.963 * (Q_eff/Q_d) * nu34].
        li = li0 * math.exp(-epsilon_n * 0.963 * (q_eff / q_d_barn) * nu34)
        return {
            "Q_trans_barn": q_trans_barn,
            "Q_eff_barn": q_eff,
            "Li7_H": li,
            "Li_sigma": (li - li_obs) / li_sigma,
        }

    # Minimal alpha+t cluster estimate. The goal is not to prove the carrier
    # rule, but to show the static mass-7 quadrupole scale is physically
    # plausible from measured charge radii.
    rc_7li = 2.4440
    rc_alpha = 1.6810
    rc_t = 1.7590
    z_alpha = 2.0
    z_t = 1.0
    m_alpha = 4.0
    m_t = 3.0
    m = m_alpha + m_t
    z = z_alpha + z_t
    intrinsic = (z_alpha / z) * rc_alpha**2 + (z_t / z) * rc_t**2
    radius_coef = (z_alpha / z) * (m_t / m) ** 2 + (z_t / z) * (m_alpha / m) ** 2
    rel_r2 = (rc_7li**2 - intrinsic) / radius_coef

    # Effective E2 charge for a two-cluster alpha+t decomposition.
    e2_eff = z_alpha * (m_t / m) ** 2 + z_t * (m_alpha / m) ** 2
    q_cluster_fm2 = -(2.0 / 5.0) * e2_eff * rel_r2
    q_cluster_barn = q_cluster_fm2 / 100.0

    # Historical target translation: the older effective target was Q_eff.
    # Paper 24 v2.2 reports the carrier scale before the x^{-1} projection.
    q_trans_required_exact = x * q_req_old_barn
    return {
        "claim_discipline": {
            "Qtrans_from_measured_low_energy_E2_Sfactor": "derived / no",
            "Qtrans_from_published_ab_initio_E2_capture_amplitudes": "derived / no",
            "Qtrans_from_final_state_measured_Q7Li": "conditional",
            "Qtrans_from_minimal_cluster_model": "reconstruction with measured nuclear data",
            "sqrt_minus_g_linear_TT_route_derives_Qtrans": "derived / no",
        },
        "inputs": {
            "x": x,
            "gamma": gamma,
            "K_gauge": math.log(1.0 + gamma * gamma),
            "Delta": x**4 * (1.0 + gamma * gamma),
            "K_total": math.log(x**4 * (1.0 + gamma * gamma)),
            "L2": 0.13805247907094412,
            "epsilon_n_paper22": epsilon_n,
            "li_obs": {"value": li_obs, "sigma": li_sigma},
            "q_d_barn": q_d_barn,
            "q_7li_barn": q_7li_barn,
            "q_7be_theory_barn": q_7be_theory_barn,
            "q_req_old_barn": q_req_old_barn,
        },
        "cluster_route": {
            "radii_fm": {
                "r_c_7Li": rc_7li,
                "r_c_alpha": rc_alpha,
                "r_c_triton": rc_t,
            },
            "effective_charge_factor_E2": e2_eff,
            "relative_separation_r2_fm2": rel_r2,
            "relative_separation_r_fm": math.sqrt(rel_r2),
            "Q_cluster_fm2": q_cluster_fm2,
            "Q_cluster_barn": q_cluster_barn,
        },
        "framework_geometry": {
            "metric_expansion": {
                "formula_line_element": (
                    "dl_phys = a sqrt[(gamma_ij + h_ij^TT) dx^i dx^j] "
                    "= a dl [1 + 1/2 h_ij^TT n^i n^j + O(h^2)]"
                ),
                "formula_det": (
                    "sqrt(det(gamma+h^TT)) = sqrt(gamma) [1 + 1/2 tr(h^TT) + O(h^2)] "
                    "= sqrt(gamma)[1+O(h^2)]"
                ),
                "derived_fact": "TT perturbations are traceless, so local sqrt(g) has no linear correction.",
                "coulomb_variation": "delta V_C / V_C = -1/2 h_ij^TT n^i n^j + O(h^2)",
            },
            "corrected_dressing_law": {
                "formula": "deltaGamma_r/Gamma_r = (epsilon_bdy/x) * (Q_trans,r/Q_d) * nu_r",
                "statement": "The x^{-1} projection belongs on the bridge amplitude epsilon_bdy, not on Q_trans.",
            },
            "target_translation": {
                "Q_old_required_barn": q_req_old_barn,
                "Q_trans_required_exact_barn": q_trans_required_exact,
                "Q_trans_user_prediction_barn": q_7li_barn,
                "relative_difference_exact_vs_0p040": (q_trans_required_exact - q_7li_barn) / q_7li_barn,
            },
        },
        "final_state_carrier_rules": {
            "measured_final_state_rule": {
                "formula": "Q_trans(7Be) = |Q(7Li)|",
                "Q_trans_barn": q_7li_barn,
                "relative_error_vs_target": 0.0,
            },
            "cluster_final_state_rule": {
                "formula": "Q_trans(7Be) approx |Q_cluster(7Li)| from alpha+t geometry",
                "Q_trans_barn": abs(q_cluster_barn),
                "relative_error_vs_target": (abs(q_cluster_barn) - q_7li_barn) / q_7li_barn,
            },
            "initial_state_theory_rule": {
                "formula": "Q_trans(7Be) = |Q_theory(7Be)|",
                "Q_trans_barn": q_7be_theory_barn,
                "relative_error_vs_target": (q_7be_theory_barn - q_7li_barn) / q_7li_barn,
            },
        },
        "li_predictions": {
            "from_measured_Q7Li": li_prediction(q_7li_barn),
            "from_cluster_Q7Li": li_prediction(abs(q_cluster_barn)),
            "from_theory_Q7Be": li_prediction(q_7be_theory_barn),
        },
    }


def main() -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    payload = compute()
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["framework_geometry"]["target_translation"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
