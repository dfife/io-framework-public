#!/usr/bin/env python3
"""Recompute Paper 26 v2.0's effective source-covariance damping parameter.

The old broad C3 premise is replaced in v2.0 by Theorem 26.C3. On the reduced
centered Gaussian source-covariance class, inverse-kernel propagation gives one
factor exp(-K_gauge) on the covariance. Standard TT notation writes the
observed combination as A_eff = A_s exp(-2 tau), so this corresponds to
tau_eff = K_gauge / 2.

This is not the same claim as deriving the astrophysical reionization optical
depth or the low-l EE bump.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "tau_eff_and_damping_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    k_gauge = data["framework_constants"]["K_gauge"]
    a_s = data["scalar_amplitude"]["A_s"]
    tau_eff = k_gauge / 2.0
    damping = math.exp(-k_gauge)
    a_eff = a_s * damping
    lcdm_ref = data["tau_eff"]["LCDM_TT_extraction_reference"]

    result = {
        "paper": "Paper 26 v2.0",
        "K_gauge": k_gauge,
        "tau_eff_IO": tau_eff,
        "damping_factor_exp_minus_K_gauge": damping,
        "A_s": a_s,
        "A_eff": a_eff,
        "LCDM_TT_extraction_reference": lcdm_ref,
        "fractional_delta_vs_LCDM_TT": (a_eff - lcdm_ref) / lcdm_ref,
        "status": "DERIVED/CONDITIONAL_VERIFIED on Theorem 26.C3 and Definition 26.C3.3",
        "scope": data["tau_eff"]["scope"],
        "low_ell_EE_closed": False
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
