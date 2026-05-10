#!/usr/bin/env python3
"""Audit Paper 22 v2.0 for the Paper 17 R4/FIRAS thermal-readout repair.

Paper 17 v1.5 retired the older claim that the Interior Observer framework
independently predicts the observed cosmic microwave background temperature.
The current convention is narrower and safer: FIRAS supplies the empirical
observer-side thermal datum, and the optical readout family

    T_obs(R4) = T_IO * x ** (R4 * K_gauge)

fixes a unique normalization R4.  Paper 22 does not use R4 to compute its
active rate-dressing Big Bang nucleosynthesis scorecard, but its appendix and
cross-paper references inherit the corrected thermal-readout convention.

Run from the bundle root:

    python3 scripts/01_r4_firas_dependency_audit.py

Output:

    results/r4_firas_dependency_audit_results.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
CONSTANTS_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT_PATH = BUNDLE_ROOT / "results" / "r4_firas_dependency_audit_results.json"


def main() -> None:
    constants = json.loads(CONSTANTS_PATH.read_text(encoding="utf-8"))
    fw = constants["framework_constants"]
    readout = constants["thermal_readout_r4_repair"]

    t_io = fw["T_IO_K"]
    x = fw["x"]
    k_gauge = fw["K_gauge"]
    r4_frozen = readout["R4_FIRAS"]
    t_firas = readout["T_FIRAS_K"]

    r4_from_firas = math.log(t_firas / t_io) / (k_gauge * math.log(x))
    active_t_obs = t_io * x ** (r4_frozen * k_gauge)
    retired_r4_equals_one = t_io * x**k_gauge
    retired_half_gauge = t_io * math.exp(k_gauge / 2.0)

    result = {
        "script": Path(__file__).name,
        "claim_support": [
            "Paper 17 v1.5 Theorem 17.2 FIRAS-fixed unique readout normalization",
            "Paper 22 v2.0 R4/CMB damage audit",
        ],
        "status": "VERIFIED audit field; Paper 22 active BBN scorecard is not R4-dependent",
        "active_readout": {
            "formula": readout["active_formula"],
            "T_IO_K": t_io,
            "x": x,
            "K_gauge": k_gauge,
            "R4_FIRAS_frozen": r4_frozen,
            "R4_from_FIRAS_formula": "ln(T_FIRAS/T_IO) / (K_gauge * ln(x))",
            "R4_from_FIRAS_using_rounded_inputs": r4_from_firas,
            "T_obs_from_frozen_R4_K": active_t_obs,
            "T_FIRAS_K": t_firas,
            "absolute_temperature_difference_K": abs(active_t_obs - t_firas),
        },
        "retired_readouts": {
            "R4_equals_one": {
                "formula": readout["retired_R4_equals_one_formula"],
                "T_obs_K": retired_r4_equals_one,
                "reason_retired": "R4=1 is not forced by the modular-projection stack; Paper 17 v1.5 uses FIRAS to fix R4 once.",
            },
            "half_gauge": {
                "formula": readout["retired_half_gauge_formula"],
                "T_obs_K": retired_half_gauge,
                "reason_retired": "exp(K_gauge/2) is not the active GTTP optical-readout law and evaluates to 2.7376 K, not 2.7255 K.",
            },
        },
        "paper22_dependency": {
            "active_scorecard_depends_on_R4": readout["paper22_active_scorecard_depends_on_R4"],
            "independent_CMB_temperature_prediction_retired": readout["independent_CMB_temperature_prediction_retired"],
            "dependency_note": readout["paper22_dependency_note"],
        },
        "checks": {
            "frozen_R4_matches_paper17_value": abs(r4_frozen - 1.0031014644) < 1.0e-12,
            "active_T_obs_matches_firas_with_rounding": abs(active_t_obs - t_firas) < 1.0e-5,
            "retired_R4_equals_one_differs_from_active": abs(retired_r4_equals_one - active_t_obs) > 1.0e-4,
            "retired_half_gauge_differs_from_active": abs(retired_half_gauge - active_t_obs) > 1.0e-2,
            "paper22_scorecard_not_R4_dependent": readout["paper22_active_scorecard_depends_on_R4"] is False,
        },
    }
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
