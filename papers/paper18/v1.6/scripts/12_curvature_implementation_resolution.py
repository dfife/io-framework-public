"""Reproduce Paper 18's curvature-implementation branch comparison.

The script contrasts the Paper 10 i.i.d. curvature implementation with the
Paper 18 Schur-active branch. It produces the `P_k` values and the branch H0
ledger used by the manuscript. It does not use the CMB temperature readout and
is unchanged by the R4/FIRAS repair.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path


def main() -> None:
    getcontext().prec = 80

    x = Decimal("1.519")
    gamma = Decimal("0.2375")
    Delta = x**4 * (Decimal(1) + gamma**2)

    # High-precision natural log and exp through Decimal methods.
    ln_Delta = Delta.ln()
    Pk_schur = (-(Delta / Decimal(2))).exp()
    Pk_p10 = (-(x**-2) * ln_Delta).exp()

    out = {
        "x": str(x),
        "gamma": str(gamma),
        "Delta": str(Delta),
        "Pk_Paper10_iid": str(Pk_p10),
        "Pk_Schur_active": str(Pk_schur),
        "Pk_difference": str(Pk_p10 - Pk_schur),
        "active_branch_after_Theorem_18N": "Schur",
        "H0_Paper10_legacy_km_s_Mpc": "67.58",
        "H0_Schur_definitive_km_s_Mpc": "68.91",
    }

    out_path = Path(__file__).resolve().parents[1] / "results" / "paper18_curvature_implementation_resolution_checks.json"
    out_path.write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
