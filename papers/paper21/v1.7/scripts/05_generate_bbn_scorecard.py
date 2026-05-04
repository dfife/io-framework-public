#!/usr/bin/env python3
"""Paper 21 v1.7 reproducibility script 05.

Purpose:
    Recompute the published Paper 21 corrected BBN pulls and chi^2 from frozen
    PRyMordial output values and IO Framework Conventions v2.0 denominators.

Manuscript role:
    Supports the Paper 21 v1.5/v1.6 corrected scorecard:
    Y_p +0.70 sigma, D/H -0.55 sigma, Li-7 +12.20 sigma, and
    chi^2(D/H + Y_p) = 0.80.

Inputs:
    data/imported_constants.json.

Outputs:
    results/bbn_scorecard_results.json

External dependencies:
    Python standard library only. Frozen PRyMordial output values are imported
    from the private-lab correction audit; PRyMordial is not redistributed.

Claim boundary:
    Verified scorecard arithmetic and convention alignment. This script does
    not derive the Paper 22 rate-dressing bridge and does not solve lithium.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "bbn_scorecard_results.json"


def pull(value: float, obs: dict[str, float]) -> float:
    return (value - obs["value"]) / obs["sigma"]


def main() -> int:
    constants = json.loads(DATA.read_text())
    obs = constants["observational_conventions"]
    score = constants["paper21_corrected_scorecard"]
    y_sigma = pull(score["Y_p"], obs["Y_p"])
    d_sigma = pull(score["D_over_H"], obs["D_over_H"])
    li_sigma = pull(score["Li7_over_H"], obs["Li7_over_H"])
    chi2_dh_yp = d_sigma**2 + y_sigma**2
    payload = {
        "claim": "Paper 21 v1.7 corrected BBN scorecard",
        "status": "verified / scorecard arithmetic / YPCMB wrapper convention",
        "inputs": {
            "frozen_PRyMordial_outputs": score,
            "observational_denominators": obs
        },
        "scorecard": {
            "Y_p": score["Y_p"],
            "Y_p_sigma": y_sigma,
            "D_over_H": score["D_over_H"],
            "D_over_H_sigma": d_sigma,
            "Li7_over_H": score["Li7_over_H"],
            "Li7_over_H_sigma": li_sigma,
            "chi2_DH_plus_Yp": chi2_dh_yp
        },
        "rounded_manuscript_values": {
            "Y_p_sigma": 0.70,
            "D_over_H_sigma": -0.55,
            "Li7_over_H_sigma": 12.20,
            "chi2_DH_plus_Yp": 0.80
        },
        "claim_boundary": "Cross-paper consistency scorecard only; active lithium result belongs to Paper 24."
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "output": str(OUT), "chi2_DH_plus_Yp": chi2_dh_yp}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
