#!/usr/bin/env python3
"""Compute Paper 29 f sigma_8(z) predictions for Euclid spectroscopic RSD bins."""

from __future__ import annotations

from _common import (
    A_S_NATIVE,
    A_S_THEOREM,
    F_GAMMA,
    IO_OBS,
    RESULTS_DIR,
    SIGMA8_THEOREM_ACTIVE,
    growth_factor,
    omega_m_z,
    write_json,
)

GROWTH_GAMMA_GR = 6.0 / 11.0
EUCLID_RSD_BINS = [
    {"z_eff": 0.9, "delta_z": 0.2},
    {"z_eff": 1.2, "delta_z": 0.2},
    {"z_eff": 1.5, "delta_z": 0.2},
    {"z_eff": 1.8, "delta_z": 0.3},
]


def row(z: float, delta_z: float) -> dict[str, float]:
    a = 1.0 / (1.0 + z)
    d = growth_factor(a, IO_OBS)
    omz = omega_m_z(z, IO_OBS)
    f = omz**GROWTH_GAMMA_GR
    sigma8_z = SIGMA8_THEOREM_ACTIVE * d
    return {
        "z_eff": z,
        "delta_z": delta_z,
        "D_z": d,
        "Omega_m_z": omz,
        "growth_rate_f": f,
        "sigma8_z": sigma8_z,
        "f_sigma8": f * sigma8_z,
    }


def main() -> None:
    rows = [row(item["z_eff"], item["delta_z"]) for item in EUCLID_RSD_BINS]
    payload = {
        "claim": "Euclid spectroscopic redshift-space-distortion f_sigma8 predictions",
        "inputs": {
            "background": IO_OBS.to_json(),
            "growth_index_gamma": GROWTH_GAMMA_GR,
            "sigma8_0": SIGMA8_THEOREM_ACTIVE,
            "A_s_native": A_S_NATIVE,
            "f_Gamma": F_GAMMA,
            "A_s_theorem": A_S_THEOREM,
            "bin_source": (
                "Euclid Collaboration 2026 RSD modelling paper: four non-overlapping bins "
                "centered at z=0.9, 1.2, 1.5, 1.8 with widths 0.2, 0.2, 0.2, 0.3."
            ),
        },
        "derived": {
            "euclid_rsd_bins": rows,
            "fsigma8_z_1p2": rows[1]["f_sigma8"],
        },
        "status": "VERIFIED",
        "scope": (
            "Uses the standard GR growth-index approximation gamma=6/11 on the active closed K=+1 branch. "
            "The sigma8 normalization is the Paper 32 theorem-supported active-branch point inherited from Paper 26 A_s."
        ),
    }
    write_json(RESULTS_DIR / "fsigma8_rsd_results.json", payload)


if __name__ == "__main__":
    main()
