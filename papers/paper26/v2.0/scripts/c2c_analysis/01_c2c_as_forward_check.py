#!/usr/bin/env python3
"""Forward-only check for the Paper 26 C2c Hawking-state analysis.

This script does not fit or infer any parameter from A_s.  It starts from the
candidate C2c Hawking/KMS boundary covariance on the S2 ell=1 coexact carrier,

    G_H(ell=1) = [exp(4*pi*sqrt(2)) - 1]^-1 I,

then propagates the Paper 26 body formula

    A_s = (25/9) * [gamma_BI^2/(1+gamma_BI^2)]
          * [1/sqrt(2)] * [exp(4*pi*sqrt(2)) - 1]^-1.

The status of the thermal occupation factor depends on the C2c state-selection
question.  The arithmetic here only verifies the forward numerical consequence
of the selected state class.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[2]
RESULTS_PATH = BUNDLE_ROOT / "results" / "c2c_analysis" / "c2c_as_forward_check_results.json"

GAMMA_BI = 0.2375
PLANCK_A_S = 2.100e-9
PLANCK_SIGMA = 0.030e-9


def compute() -> dict[str, object]:
    q = 1.0 + GAMMA_BI**2
    beta_omega = 4.0 * math.pi * math.sqrt(2.0)
    hawking_occupation = 1.0 / (math.exp(beta_omega) - 1.0)
    canonical_source = hawking_occupation / math.sqrt(2.0)
    extrinsic_fraction = GAMMA_BI**2 / q
    dust_factor = 25.0 / 9.0
    a_s = dust_factor * extrinsic_fraction * canonical_source

    # Appendix Step 387 in one extracted v2.0 text uses a squared occupation
    # expression.  This diagnostic records that the squared expression is not
    # the body formula and does not reproduce the quoted value.
    squared_candidate = dust_factor * extrinsic_fraction * (2.0 * hawking_occupation) ** 2

    return {
        "paper": "Paper 26 v2.0 C2c analysis",
        "claim_boundary": (
            "Forward arithmetic only. C2c full state selection is not proved by "
            "this script."
        ),
        "inputs": {
            "gamma_BI": GAMMA_BI,
            "Q": q,
            "Planck_A_s_reference": PLANCK_A_S,
            "Planck_A_s_sigma": PLANCK_SIGMA,
        },
        "c2c_fixed_carrier_terms": {
            "beta_hbar_omega_l1": beta_omega,
            "hawking_occupation_l1": hawking_occupation,
            "canonical_source_covariance": canonical_source,
        },
        "paper26_body_formula_terms": {
            "dust_conversion_factor": dust_factor,
            "extrinsic_fraction_gamma2_over_Q": extrinsic_fraction,
            "A_s": a_s,
            "fractional_delta_vs_Planck": (a_s - PLANCK_A_S) / PLANCK_A_S,
            "sigma_delta_vs_Planck": (a_s - PLANCK_A_S) / PLANCK_SIGMA,
        },
        "appendix_formula_guard": {
            "squared_occupation_candidate": squared_candidate,
            "matches_body_A_s": math.isclose(squared_candidate, a_s, rel_tol=1e-12, abs_tol=0.0),
            "note": (
                "If the manuscript still contains an A_s formula proportional "
                "to [2/(exp(4*pi*sqrt(2))-1)]^2, that formula is not the active "
                "body formula and is numerically inconsistent with 2.007e-9."
            ),
        },
    }


def main() -> None:
    payload = compute()
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
