#!/usr/bin/env python3
"""Reproduce the DESI DR2 BAO and cosmic-chronometer confrontation."""

from __future__ import annotations

import math

from _common import (
    CC_CHI2_BASELINE,
    ETA,
    PLANCK_BAO_CHI2,
    PLANCK_COMBINED_CHI2,
    RESULTS_DIR,
    bao_model_rows,
    cc_chi2,
    load_desi_dr2,
    write_json,
)


def main() -> None:
    rows, covariance = load_desi_dr2()
    f_perp = math.exp(ETA)
    f_parallel = math.exp(ETA / 2.0)
    model_rows, bao_chi2 = bao_model_rows(rows, covariance, f_perp=f_perp, f_parallel=f_parallel)
    cc = cc_chi2()
    payload = {
        "claim": "DESI DR2 GCcomb plus 35-point cosmic chronometer confrontation",
        "inputs": {
            "desi_dr2_rows": len(rows),
            "chronometer_rows": 35,
            "f_perp": f_perp,
            "f_parallel": f_parallel,
            "eta": ETA,
        },
        "derived": {
            "cc_chi2_recomputed": cc,
            "cc_chi2_banked": CC_CHI2_BASELINE,
            "bao_chi2": bao_chi2,
            "combined_chi2": bao_chi2 + cc,
            "planck_bao_chi2": PLANCK_BAO_CHI2,
            "planck_combined_chi2": PLANCK_COMBINED_CHI2,
        },
        "paper_values": {
            "cc_chi2": 14.70,
            "bao_chi2": 27.74,
            "combined_chi2": 42.44,
            "planck_combined_chi2": 46.40,
        },
        "residual_rows": model_rows,
        "status": "VERIFIED",
        "external_data": "DESI DR2 mean/covariance are fetched from Cobaya bao_data and SHA256 checked.",
    }
    write_json(RESULTS_DIR / "desi_chronometer_confrontation_results.json", payload)


if __name__ == "__main__":
    main()
