#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from classy import Class
from scipy.interpolate import interp1d


ROOT = Path("/opt/cosmology-lab")
OUT = ROOT / "results" / "paper31"

X = 1.5189873277742727
RS = 6.685e26
C = 2.998e8
MPC = 3.0856775814913673e22
YEAR = 365.25 * 24.0 * 3600.0

ACTIVE = {
    "H0": 68.91,
    "Omega_k": -0.005613722564239,
    "omega_b": 0.02108,
    "omega_cdm": 0.13302837882723044,
    "N_ur": 3.044,
    "N_ncdm": 0,
    "T_cmb": 2.7253,
    "YHe": 0.2477,
    "A_s": 2.0072459972737347e-9,
    "n_s": 0.9639,
    "tau_reio": 0.02743640887145733,
    "reio_parametrization": "reio_camb",
}


def tau_os_gyr(z: float) -> float:
    u = 1.0 / (X * (1.0 + z))
    return (RS / (2.0 * C)) * (
        math.acos(1.0 - 2.0 * u) - 2.0 * math.sqrt(u * (1.0 - u))
    ) / (YEAR * 1.0e9)


def dtau_os_dz_mpc(z: float) -> float:
    # Exact OS-clock derivative converted to Mpc so the ratio to dt_proj/dz is dimensionless.
    return (RS / (C * X * (1.0 + z) ** 2 * math.sqrt(X * (1.0 + z) - 1.0))) * (C / MPC)


def peak_summary(z: np.ndarray, g: np.ndarray, *, zmin: float = 700.0, zmax: float = 1600.0) -> dict[str, float]:
    mask = (z > zmin) & (z < zmax)
    zz = z[mask]
    gg = g[mask]
    peak = int(np.argmax(gg))
    half = 0.5 * gg[peak]
    support = np.where(gg >= half)[0]
    return {
        "z_peak": float(zz[peak]),
        "g_peak": float(gg[peak]),
        "fwhm_z": float(zz[support[-1]] - zz[support[0]]),
    }


def main() -> None:
    params = {
        "output": "tCl,pCl,lCl",
        "lensing": "yes",
        "l_max_scalars": 50,
        **ACTIVE,
    }

    cosmo = Class()
    cosmo.set(params)
    cosmo.compute()

    thermo = cosmo.get_thermodynamics()
    background = cosmo.get_background()

    z = np.array(thermo["z"])
    xe = np.array(thermo["x_e"])
    dkappa = np.array(thermo["kappa' [Mpc^-1]"])
    g = np.array(thermo["g [Mpc^-1]"])

    bz = np.array(background["z"])
    tproj = np.array(background["proper time [Gyr]"])
    H = np.array(background["H [1/Mpc]"])
    order = np.argsort(bz)
    bz = bz[order]
    tproj = tproj[order]
    H = H[order]

    t_of_z = interp1d(bz, tproj, kind="linear", fill_value="extrapolate")
    H_of_z = interp1d(bz, H, kind="linear", fill_value="extrapolate")

    thermo_t = np.array(t_of_z(z))
    order_t = np.argsort(thermo_t)
    xe_of_t = interp1d(
        thermo_t[order_t],
        xe[order_t],
        kind="linear",
        bounds_error=False,
        fill_value=(float(xe[order_t][0]), float(xe[order_t][-1])),
    )

    xe_transport = np.array([float(xe_of_t(tau_os_gyr(float(zz)))) for zz in z])
    ratio = np.divide(xe_transport, xe, out=np.ones_like(xe_transport), where=xe > 0.0)
    dkappa_transport = dkappa * ratio

    Hz = np.array(H_of_z(z))
    integrand_transport = dkappa_transport / Hz / (1.0 + z)
    kappa_transport = np.zeros_like(z)
    for i in range(1, len(z)):
        dz = z[i] - z[i - 1]
        kappa_transport[i] = kappa_transport[i - 1] + 0.5 * dz * (
            integrand_transport[i] + integrand_transport[i - 1]
        )
    g_transport = dkappa_transport * np.exp(-kappa_transport)

    z_samples = [800.0, 900.0, 1000.0, 1080.0, 1100.0, 1200.0, 1400.0]
    transport_rows = []
    for zz in z_samples:
        dt_proj_dz_mpc = 1.0 / ((1.0 + zz) * float(H_of_z(zz)))
        ratio_rec = dtau_os_dz_mpc(zz) / dt_proj_dz_mpc
        transport_rows.append(
            {
                "z": zz,
                "R_rec": ratio_rec,
                "required_net_drive_fraction": 1.0 / ratio_rec,
            }
        )

    z1100_index = int(np.argmin(np.abs(z - 1100.0)))
    results = {
        "constants": {
            "x": X,
            "r_s_m": RS,
            "c_m_per_s": C,
            "active_branch": ACTIVE,
        },
        "transport_rows": transport_rows,
        "baseline_recombination_window": peak_summary(z, g),
        "transported_pullback_window": peak_summary(z, g_transport),
        "point_check_z1100": {
            "x_e_baseline": float(xe[z1100_index]),
            "x_e_transport": float(xe_transport[z1100_index]),
            "x_e_ratio": float(xe_transport[z1100_index] / xe[z1100_index]),
            "dkappa_ratio": float(dkappa_transport[z1100_index] / dkappa[z1100_index]),
        },
    }

    lines = [
        "Paper 31 Recombination Clock Transport Check",
        "============================================",
        "",
        "Exact Stage-2 OS-clock transport factor:",
        "R_rec(z) := |d tau_OS / dz| / |d t_proj / dz|",
        "",
    ]
    for row in transport_rows:
        lines.append(
            f"z = {row['z']:>6.1f}: R_rec = {row['R_rec']:.9f}, required net-drive fraction = {row['required_net_drive_fraction']:.9f}"
        )
    lines.extend(
        [
            "",
            "Baseline projected-history recombination window:",
            (
                f"z_peak = {results['baseline_recombination_window']['z_peak']:.6f}, "
                f"FWHM_z = {results['baseline_recombination_window']['fwhm_z']:.6f}, "
                f"g_peak = {results['baseline_recombination_window']['g_peak']:.9f}"
            ),
            "Naive OS-time pullback benchmark (age-match the same local history to tau_OS):",
            (
                f"z_peak = {results['transported_pullback_window']['z_peak']:.6f}, "
                f"FWHM_z = {results['transported_pullback_window']['fwhm_z']:.6f}, "
                f"g_peak = {results['transported_pullback_window']['g_peak']:.9f}"
            ),
            "",
            "Point check at z = 1100:",
            (
                f"x_e baseline = {results['point_check_z1100']['x_e_baseline']:.12f}, "
                f"x_e transport = {results['point_check_z1100']['x_e_transport']:.12f}, "
                f"ratio = {results['point_check_z1100']['x_e_ratio']:.12f}"
            ),
            (
                f"dkappa ratio at z = 1100 = {results['point_check_z1100']['dkappa_ratio']:.12f}"
            ),
        ]
    )

    (OUT / "paper31_recombination_clock_transport_check_results.json").write_text(
        json.dumps(results, indent=2) + "\n"
    )
    (OUT / "paper31_recombination_clock_transport_check_report.txt").write_text(
        "\n".join(lines) + "\n"
    )

    cosmo.struct_cleanup()
    cosmo.empty()


if __name__ == "__main__":
    main()
