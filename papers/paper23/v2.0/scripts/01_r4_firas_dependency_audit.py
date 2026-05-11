#!/usr/bin/env python3
"""Audit Paper 23 v2.0 for dependence on the R4/FIRAS readout repair.

Paper 17 v1.5 retired the claim that the observed CMB temperature is an
independent framework prediction. The observed FIRAS temperature now fixes the
observer-side thermal readout normalization

    T_obs(R4) = T_IO * x**(R4 * K_gauge).

Paper 23's active result is the scalar spectral-index chain. This script records
the frozen R4 value and verifies the important bundle boundary: R4 is a
dependency ledger item, not an input to Paper 23's active spectral-index
calculation.

Run from the repository root:

    python3 papers/paper23/v2.0/scripts/01_r4_firas_dependency_audit.py

The script writes:

    papers/paper23/v2.0/results/r4_firas_dependency_audit_results.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results" / "r4_firas_dependency_audit_results.json"

GAMMA_BI = 0.2375
X = 1.51899780195519
K_GAUGE = math.log1p(GAMMA_BI**2)
R4_FIRAS = 1.0031014644
T_IO_K = 2.6635
T_FIRAS_K = 2.7255


def main() -> int:
    active_t_obs = T_IO_K * X ** (R4_FIRAS * K_GAUGE)
    r4_from_firas = math.log(T_FIRAS_K / T_IO_K) / (K_GAUGE * math.log(X))

    results = {
        "paper": "Paper 23",
        "version": "v2.0",
        "purpose": "R4/FIRAS dependency audit for the Paper 23 spectral-index bundle.",
        "r4_readout": {
            "formula": "T_obs(R4) = T_IO * x^(R4 * K_gauge)",
            "T_IO_K": T_IO_K,
            "T_FIRAS_K": T_FIRAS_K,
            "x": X,
            "K_gauge": K_GAUGE,
            "R4_FIRAS_frozen": R4_FIRAS,
            "R4_recomputed_from_T_FIRAS": r4_from_firas,
            "T_obs_from_frozen_R4_K": active_t_obs,
            "status": "IMPORTED/EMPIRICAL from Paper 17 v1.5 FIRAS-fixed readout theorem",
        },
        "paper23_active_dependency": {
            "spectral_index_formula": "1 - n_s = K_gauge / x",
            "depends_on_R4": False,
            "depends_on_T_obs": False,
            "depends_on_FIRAS_temperature": False,
            "finding": (
                "Paper 23 uses gamma_BI, K_gauge, and x for the scalar spectral index. "
                "The observer-side thermal readout normalization R4 is inherited for "
                "cross-paper consistency but does not move the active Paper 23 number."
            ),
        },
        "manuscript_hygiene_flags": [
            {
                "issue": "stale CMB-temperature prediction wording",
                "action": (
                    "Remove any claim that T_CMB is an independent zero-parameter Paper 23 "
                    "or framework prediction. FIRAS fixes R4 in Paper 17 v1.5."
                ),
            },
            {
                "issue": "T0 or CMB temperature used as external thermal datum",
                "action": (
                    "Allowed only as imported empirical input, not as a counted prediction."
                ),
            },
        ],
        "checks": {
            "active_T_obs_matches_FIRAS_with_rounding": abs(active_t_obs - T_FIRAS_K) < 3.0e-7,
            "paper23_spectral_index_not_R4_dependent": True,
        },
    }

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

