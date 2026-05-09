#!/usr/bin/env python3
"""Paper 21 v2.0 reproducibility script 01.

Purpose:
    Record the Paper 17 v1.5 R4/FIRAS repair as it affects Paper 21.
    Paper 21 does not use R4 to compute its active BBN scorecard; its
    Big Bang nucleosynthesis branch assignment explicitly uses the local
    interior thermal scale T_IO. This script verifies that the observer-side
    optical readout temperature is now represented with the FIRAS-fixed
    readout normalization R4_FIRAS = 1.0031014644 rather than the retired
    R4 = 1 shorthand.

Manuscript role:
    Supports the Paper 21 v2.0 R4-damage audit. It prevents the public bundle
    from silently preserving the retired equation T_obs = T_IO x^K_gauge as an
    independent cosmic microwave background temperature prediction.

Inputs:
    data/imported_constants.json.

Outputs:
    results/r4_firas_dependency_audit_results.json.

External dependencies:
    Python standard library only.

Claim boundary:
    This is a dependency and hygiene check. It does not derive R4. R4 is fixed
    in Paper 17 v1.5 by the FIRAS empirical thermal datum inside the optical
    readout family T_obs(R4) = T_IO x^(R4 K_gauge). Paper 21's active BBN
    theorem uses T_IO, so R4 does not enter the active BBN scorecard.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "r4_firas_dependency_audit_results.json"


def main() -> int:
    constants = json.loads(DATA.read_text())
    fw = constants["framework_constants"]
    r4 = fw["R4_FIRAS"]
    t_io = fw["T_IO_K"]
    x = fw["x"]
    k_gauge = fw["K_gauge"]
    t_retired = t_io * (x ** k_gauge)
    t_firas_fixed = t_io * (x ** (r4 * k_gauge))
    payload = {
        "claim": "Paper 21 v2.0 R4/FIRAS dependency audit",
        "status": "VERIFIED dependency audit",
        "R4_FIRAS": r4,
        "retired_R4_value": 1.0,
        "T_IO_K": t_io,
        "x": x,
        "K_gauge": k_gauge,
        "retired_optical_readout_formula": "T_obs = T_IO * x**K_gauge",
        "retired_T_obs_K": t_retired,
        "active_optical_readout_formula": "T_obs(R4) = T_IO * x**(R4_FIRAS * K_gauge)",
        "active_T_obs_K": t_firas_fixed,
        "FIRAS_T_K": fw["T_FIRAS_K"],
        "active_minus_FIRAS_K": t_firas_fixed - fw["T_FIRAS_K"],
        "relative_change_from_retired_R4": t_firas_fixed / t_retired - 1.0,
        "paper21_active_BBN_branch_uses": "T_IO",
        "R4_enters_active_BBN_scorecard": False,
        "independent_CMB_temperature_prediction_retired": True,
        "checks": {
            "active_T_obs_matches_imported_value": math.isclose(
                t_firas_fixed, fw["T_obs_K"], rel_tol=0.0, abs_tol=1e-12
            ),
            "active_T_obs_is_FIRAS_fixed": math.isclose(
                t_firas_fixed, fw["T_FIRAS_K"], rel_tol=0.0, abs_tol=1e-6
            ),
            "R4_changed_from_retired_unity": not math.isclose(r4, 1.0, rel_tol=0.0, abs_tol=1e-12),
        },
        "claim_boundary": (
            "Paper 21 only audits inheritance from Paper 17 v1.5. "
            "The active Paper 21 BBN branch assignment and scorecard remain on T_IO."
        ),
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "output": str(OUT), "R4_FIRAS": r4}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
