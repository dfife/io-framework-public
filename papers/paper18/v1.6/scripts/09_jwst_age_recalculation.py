"""Recompute the Paper 18 conditional JWST-age branch with FIRAS-fixed T0.

Paper 18's JWST-age calculation is explicitly conditional on the now-withdrawn
`N_eff = Delta` Friedmann-radiation identification. This script is retained as
a branch diagnostic, not as an active IO prediction.

The v1.6 repair changes only the observer-side CMB-temperature input used in
the radiation-density term: v1.5's implicit `R4 = 1` shorthand `2.7253 K` is
replaced by the Paper 17 v1.5 FIRAS-fixed readout, `R4_FIRAS = 1.0031014644`,
which evaluates to `T_FIRAS = 2.7255 K`.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp


mp.mp.dps = 80

GAMMA_BI = mp.mpf("0.2375")
X_R4_SOURCE = mp.mpf("1.519")
K_GAUGE = mp.log(1 + GAMMA_BI**2)
R4_FIRAS = mp.mpf("1.0031014644")
T_IO_BULK = mp.mpf("2.6635")
T_FIRAS = mp.mpf("2.7255")
T_OBS_R4 = T_IO_BULK * (X_R4_SOURCE ** (R4_FIRAS * K_GAUGE))


def radiation_density(T0: mp.mpf, Neff: mp.mpf, h: mp.mpf) -> mp.mpf:
    omega_gamma_h2 = mp.mpf("2.4728e-5") * (T0 / mp.mpf("2.7255")) ** 4
    omega_r_h2 = omega_gamma_h2 * (1 + mp.mpf("0.22710731766") * Neff)
    return omega_r_h2 / h**2


def age_at_z(H0: mp.mpf, Or: mp.mpf, Om: mp.mpf, Ok: mp.mpf, Ol: mp.mpf, z: mp.mpf) -> mp.mpf:
    h = H0 / 100
    hubble_time_gyr = mp.mpf("9.778130") / h
    a = 1 / (1 + z)
    integrand = lambda a_: 1 / (a_ * mp.sqrt(Or / a_**4 + Om / a_**3 + Ok / a_**2 + Ol))
    return hubble_time_gyr * mp.quad(integrand, [0, a])


def model(H0: str, Om: str, Ok: str, T0: str, Neff: str) -> dict[str, object]:
    H0_m = mp.mpf(H0)
    Om_m = mp.mpf(Om)
    Ok_m = mp.mpf(Ok)
    T0_m = mp.mpf(T0)
    Neff_m = mp.mpf(Neff)
    h = H0_m / 100
    Or = radiation_density(T0_m, Neff_m, h)
    Ol = 1 - Om_m - Ok_m - Or
    ages = {}
    for z in [6, 10, 14, 20]:
        ages[str(z)] = age_at_z(H0_m, Or, Om_m, Ok_m, Ol, mp.mpf(z))
    return {
        "H0": str(H0_m),
        "Omega_m": str(Om_m),
        "Omega_k": str(Ok_m),
        "T0": str(T0_m),
        "N_eff": str(Neff_m),
        "Omega_r": str(Or),
        "Omega_Lambda": str(Ol),
        "age_today_Gyr": str(age_at_z(H0_m, Or, Om_m, Ok_m, Ol, mp.mpf("0"))),
        "ages_Gyr": {k: str(v) for k, v in ages.items()},
    }


def main() -> None:
    io = model("68.91", "0.335", "-0.006", str(T_OBS_R4), "5.62421685262410640625")
    lcdm = model("67.36", "0.3153", "0.0", "2.7255", "3.046")

    comparison = {}
    for z in ["6", "10", "14", "20"]:
        t_io = mp.mpf(io["ages_Gyr"][z])
        t_l = mp.mpf(lcdm["ages_Gyr"][z])
        comparison[z] = {
            "IO_age_Myr": str(t_io * 1000),
            "LCDM_age_Myr": str(t_l * 1000),
            "difference_Myr": str((t_io - t_l) * 1000),
            "percent_difference": str((t_io - t_l) / t_l * 100),
        }

    out = {
        "thermal_repair": {
            "R4_FIRAS": str(R4_FIRAS),
            "T_IO_bulk_K": str(T_IO_BULK),
            "T_FIRAS_K": str(T_FIRAS),
            "T_obs_R4_K": str(T_OBS_R4),
            "T_obs_R4_minus_FIRAS_K": str(T_OBS_R4 - T_FIRAS),
            "status": "FIRAS-fixed observer readout; not an independent CMB-temperature prediction.",
        },
        "IO_model": io,
        "LCDM_model": lcdm,
        "comparison": comparison,
        "sign_summary": "IO gives less time than LCDM at z = 6, 10, 14, 20",
    }

    out_path = Path(__file__).resolve().parents[1] / "results" / "paper18_jwst_age_recalculation_checks.json"
    out_path.write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
