#!/usr/bin/env python3
"""Recompute active-branch Paper 5 expansion-rate ratios."""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]


def load_constants() -> dict:
    return json.loads((BUNDLE_ROOT / "data" / "imported_constants.json").read_text())


def e2(z: float, params: dict) -> float:
    u = 1.0 / (1.0 + z)
    return (
        params["Omega_r"] / u**4
        + params["Omega_m"] / u**3
        + params["Omega_k"] / u**2
        + params["Omega_Lambda"]
    )


def hubble(z: float, params: dict) -> float:
    return params["H0_km_s_Mpc"] * math.sqrt(e2(z, params))


def main() -> None:
    constants = load_constants()
    active = constants["active_branch_papers_10_29"]
    lcdm = constants["flat_lcdm_comparator"]
    redshifts = [1.0e9, 1100.0, 0.0]
    rows = []
    for z in redshifts:
        h_io = hubble(z, active)
        h_lcdm = hubble(z, lcdm)
        ratio = h_io / h_lcdm
        rows.append(
            {
                "z": z,
                "u": 1.0 / (1.0 + z),
                "H_IO_km_s_Mpc": h_io,
                "H_LCDM_km_s_Mpc": h_lcdm,
                "ratio_H_IO_over_H_LCDM": ratio,
                "percent_offset": 100.0 * (ratio - 1.0),
                "E2_IO": e2(z, active),
                "E2_LCDM": e2(z, lcdm),
            }
        )

    radiation_ratio = (
        active["H0_km_s_Mpc"]
        * math.sqrt(active["Omega_r"])
        / (lcdm["H0_km_s_Mpc"] * math.sqrt(lcdm["Omega_r"]))
    )
    payload = {
        "status": "DERIVED",
        "formula": "H^2 = H0^2*(Omega_r/u^4 + Omega_m/u^3 + Omega_k/u^2 + Omega_Lambda)",
        "redshift_rows": rows,
        "radiation_era_asymptotic_ratio": radiation_ratio,
        "bbn_reconciliation": (
            "At z=1e9 the active branch is only 0.0896 percent faster than the "
            "flat-LCDM comparator. Paper 22/24 light-element improvements should "
            "therefore be read as cross-section rate dressing on top of a near-standard "
            "background expansion, not as a modified-H(z) solution."
        ),
        "rounded_omega_note": (
            "The z=0 row uses the rounded active Omegas supplied to Paper 5, whose "
            "sum is 1.000091575. If exact E(0)=1 normalization is imposed, the z=0 "
            "ratio is H0_IO/H0_LCDM = 67.58/67.4."
        ),
    }
    out = BUNDLE_ROOT / "results" / "mixed_friedmann_bbn_results.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(out)


if __name__ == "__main__":
    main()
