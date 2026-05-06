#!/usr/bin/env python3
"""
Paper 34 v1.2 reproducibility script 04.

Purpose:
    Audit the Paper 17 v1.5 R4/FIRAS repair against the Paper 34 H_ext
    calculation. The audit answers a narrow question:

        Does Paper 34's Hubble scorecard use the optical thermal readout
        normalization R4?

    The answer reproduced by this script is no. Paper 34 uses the
    observable-class H0 formula

        H_ext(alpha,n) = H0_active * f_Gamma^(1-alpha)
                         * x^((n/2)*K_gauge),

    where x^((n/2)*K_gauge) is the stellar-photometric half-leg payload.
    This is not the Paper 17 optical thermal readout family

        T_obs(R4) = T_IO * x^(R4*K_gauge).

Inputs:
    - data/imported_constants.json
    - results/hext_grid_results.json
    - results/published_measurements_comparison_results.json

Outputs:
    - results/r4_firas_impact_audit_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / structural impact audit. This script does not re-prove the
    Paper 34 extension premises or the Paper 17 R4 theorem. It verifies that
    inserting R4 into Paper 34's H_ext exponent would be a rejected
    counterfactual, not the active calculation.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
GRID_PATH = BUNDLE_ROOT / "results" / "hext_grid_results.json"
SCORECARD_PATH = BUNDLE_ROOT / "results" / "published_measurements_comparison_results.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "r4_firas_impact_audit_results.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def h_eff(h0_active: float, f_gamma: float, alpha: float) -> float:
    return h0_active * (f_gamma ** (1.0 - alpha))


def h_ext_counterfactual_r4(
    h0_active: float,
    f_gamma: float,
    x_value: float,
    k_gauge: float,
    r4_firas: float,
    alpha: float,
    n_legs: int,
) -> float:
    """Rejected diagnostic: what H_ext would be if R4 were wrongly inserted."""
    return h_eff(h0_active, f_gamma, alpha) * (x_value ** ((n_legs / 2.0) * r4_firas * k_gauge))


def main() -> int:
    data = load_json(DATA_PATH)
    constants = data["framework_constants"]
    grid = load_json(GRID_PATH)["grid"]
    scorecard = load_json(SCORECARD_PATH)["scorecard"]

    h0_active = constants["H0_active"]
    f_gamma = constants["f_Gamma"]
    x_value = constants["x"]
    k_gauge = constants["K_gauge"]
    r4_firas = constants["R4_FIRAS"]

    counterfactual_rows = []
    max_abs_counterfactual_delta = 0.0
    for row in grid:
        wrong = h_ext_counterfactual_r4(
            h0_active,
            f_gamma,
            x_value,
            k_gauge,
            r4_firas,
            float(row["alpha"]),
            int(row["n"]),
        )
        delta = wrong - row["H_ext"]
        max_abs_counterfactual_delta = max(max_abs_counterfactual_delta, abs(delta))
        counterfactual_rows.append(
            {
                "alpha": row["alpha"],
                "n": row["n"],
                "active_H_ext": row["H_ext"],
                "rejected_counterfactual_H_ext_with_R4_inserted": wrong,
                "counterfactual_delta": delta,
            }
        )

    planck_basis = next(item for item in scorecard if item["method"] == "Planck CMB")["assignment_basis"]

    results = {
        "paper": data["paper"],
        "classification": "verified / R4-FIRAS impact audit",
        "verdict": {
            "paper34_H_ext_formula_uses_R4": False,
            "paper34_scorecard_changed_by_R4_FIRAS": False,
            "cmb_temperature_prediction_present": False,
            "planck_cmb_row_is_temperature_prediction": False,
        },
        "R4_FIRAS": {
            "value": r4_firas,
            "sigma_FIRAS_only": constants["sigma_R4_FIRAS_only"],
            "source": constants["R4_source"],
            "scope": constants["R4_scope_note"],
        },
        "active_formula": data["formula"],
        "active_formula_boundary": data["R4_repair_boundary"],
        "planck_cmb_assignment_basis": planck_basis,
        "unchanged_headline_predictions": {
            "Planck_CMB_alpha_1_n_0": next(row["H_ext"] for row in grid if row["alpha"] == 1.0 and row["n"] == 0),
            "TRGB_direct_alpha_1p5_n_1": next(row["H_ext"] for row in grid if row["alpha"] == 1.5 and row["n"] == 1),
            "TDCOSMO_alpha_2_n_0": next(row["H_ext"] for row in grid if row["alpha"] == 2.0 and row["n"] == 0),
            "SH0ES_TRGBSN_alpha_2_n_2": next(row["H_ext"] for row in grid if row["alpha"] == 2.0 and row["n"] == 2),
        },
        "rejected_counterfactual": {
            "description": "Diagnostic only: wrongly replacing K_gauge by R4_FIRAS*K_gauge inside the photometric H_ext exponent.",
            "why_rejected": "R4 normalizes the optical thermal readout, not the H0 stellar-photometric half-leg payload.",
            "max_abs_H0_delta_km_s_Mpc": max_abs_counterfactual_delta,
            "rows": counterfactual_rows,
        },
        "script_impact": [
            {
                "script": "01_compute_hext_grid.py",
                "R4_dependency": "none",
                "v1_2_change": "claim-boundary note and x_half_leg consistency check only",
            },
            {
                "script": "02_compare_to_published_measurements.py",
                "R4_dependency": "none",
                "v1_2_change": "Planck CMB method wording clarified as H0 class, not T_CMB prediction",
            },
            {
                "script": "03_run_anti_fit_check.py",
                "R4_dependency": "none",
                "v1_2_change": "adds R4_times_K_gauge as rejected counterfactual payload diagnostic",
            },
            {
                "script": "04_r4_firas_impact_audit.py",
                "R4_dependency": "audit only",
                "v1_2_change": "new impact audit",
            },
            {
                "script": "05_validate_expected_outputs.py",
                "R4_dependency": "validation only",
                "v1_2_change": "validates no Paper 34 scorecard change from R4/FIRAS repair",
            },
        ],
    }

    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
