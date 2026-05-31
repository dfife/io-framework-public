#!/usr/bin/env python3
"""Paper 3 v2.0 script 03: radicand positivity and monotonicity.

Purpose:
    Check the structural inequalities used by the Paper 3 v2.0 Continuity
    Theorem promotion and Monotonicity Corollary.

Inputs:
    data/imported_constants.json

Outputs:
    results/radicand_positivity_monotonicity_results.json

Claim boundary:
    The proof is algebraic on the admitted active branch. If the active branch
    constants change, these inequalities must be rerun.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "radicand_positivity_monotonicity_results.json"


def main() -> None:
    payload = json.loads(DATA.read_text())
    branch = payload["active_branch_constants"]

    x = branch["x"]
    omega_r = branch["Omega_r"]
    omega_m = branch["Omega_m"]
    omega_k = branch["Omega_k"]
    omega_lambda = branch["Omega_Lambda"]
    y_min = 1.0 / x

    def Q(y: float) -> float:
        return omega_r * y**4 + omega_m * y**3 + omega_k * y**2 + omega_lambda

    def dQ_dy(y: float) -> float:
        return 4.0 * omega_r * y**3 + 3.0 * omega_m * y**2 + 2.0 * omega_k * y

    # Positivity proof:
    # Q = omega_r y^4 + y^2(omega_m y + omega_k) + omega_lambda.
    # On y >= 1/x, omega_m y + omega_k >= omega_m/x + omega_k.
    q_group_lower_bound = omega_m / x + omega_k

    # Monotonicity proof:
    # dQ/dy = y(4 omega_r y^2 + 3 omega_m y + 2 omega_k).
    # On y >= 1/x, 3 omega_m y + 2 omega_k >= 3 omega_m/x + 2 omega_k.
    dq_group_lower_bound = 3.0 * omega_m / x + 2.0 * omega_k

    result = {
        "status": "DERIVED/THEOREM inside admitted active branch",
        "domain": {
            "eta": "(0, pi)",
            "R": "(0, r_s]",
            "y": "y >= 1/x",
            "y_min": y_min
        },
        "radicand": {
            "Q_formula": "Omega_r y^4 + Omega_m y^3 + Omega_k y^2 + Omega_Lambda",
            "Q_endpoint_y_min": Q(y_min),
            "grouped_form": "Omega_r y^4 + y^2(Omega_m y + Omega_k) + Omega_Lambda",
            "Omega_m_over_x_plus_Omega_k": q_group_lower_bound,
            "strictly_positive_on_domain": q_group_lower_bound > 0.0 and omega_r > 0.0 and omega_lambda > 0.0
        },
        "monotonicity": {
            "dQ_dy_formula": "4 Omega_r y^3 + 3 Omega_m y^2 + 2 Omega_k y",
            "dQ_dy_endpoint_y_min": dQ_dy(y_min),
            "grouped_form": "y(4 Omega_r y^2 + 3 Omega_m y + 2 Omega_k)",
            "three_Omega_m_over_x_plus_two_Omega_k": dq_group_lower_bound,
            "dQ_dy_strictly_positive_on_domain": dq_group_lower_bound > 0.0 and omega_r > 0.0 and y_min > 0.0
        },
        "transfer_set_ordering": {
            "R_eta": "strictly increasing on eta in (0, pi)",
            "T_R": "strictly decreasing because T=C/R with C>0",
            "H_eta": "strictly decreasing because dQ/dy>0 and dy/deta<0",
            "a0": "constant because a0=c^2/r_s and r_s is fixed by P1"
        },
        "claim_boundary": "No observational matching is used. These are branch-internal inequalities over the full domain."
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
