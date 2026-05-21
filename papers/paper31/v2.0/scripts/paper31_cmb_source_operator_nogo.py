#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from classy import Class


ROOT = Path("/opt/cosmology-lab")
OUT = ROOT / "results" / "paper31"
TMP = ROOT / "tmp" / "planck-lite-py"
if str(TMP) not in sys.path:
    sys.path.insert(0, str(TMP))

from planck_lite_py import PlanckLitePy  # type: ignore  # noqa: E402


L_MAX = 2508
X = 1.5189873277742727
OMEGA_B_GEOM = 0.02108
OMEGA_B_EFF = 0.02910
OMEGA_B_CONTROL = 0.02710
F_GEOM = OMEGA_B_GEOM / OMEGA_B_CONTROL
F_EFF = OMEGA_B_EFF / OMEGA_B_CONTROL

BASE = {
    "output": "tCl,pCl,lCl",
    "lensing": "yes",
    "l_max_scalars": L_MAX,
    "lcmb_rescale": X ** (-0.5),
    "lcmb_tilt": 0.0,
    "lcmb_pivot": 0.05,
    "lcmb_curved_shift": -3.0,
    "lcmb_curved_order": -0.25,
    "H0": 67.58,
    "T_cmb": 2.7253,
    "Omega_k": -0.006,
    "N_ur": 3.044,
    "N_ncdm": 0,
    "YHe": 0.2477,
    "n_s": 0.9639,
    "alpha_s": 5.0e-5,
    "reio_parametrization": "reio_camb",
    "A_s": 2.0240459972737345e-9,
    "tau_reio": 0.0093,
}


def evaluate(extra: dict) -> dict:
    params = dict(BASE)
    params.update(extra)
    plik = PlanckLitePy(data_directory=str(TMP / "data"), year=2018, spectra="TTTEEE", use_low_ell_bins=True)
    cosmo = Class()
    try:
        cosmo.set(params)
        cosmo.compute()
        cls = cosmo.lensed_cl(L_MAX)
        ell = cls["ell"][2:]
        temp_scale = (params["T_cmb"] * 1.0e6) ** 2
        pref = ell * (ell + 1.0) / (2.0 * math.pi) * temp_scale
        chi2 = -2.0 * float(plik.loglike(pref * cls["tt"][2:], pref * cls["te"][2:], pref * cls["ee"][2:], ellmin=2))
        derived = cosmo.get_current_derived_parameters(["100*theta_s", "z_rec", "rs_rec"])
        return {
            "chi2_TTTEEE_lowTT": chi2,
            "A_eff": float(params["A_s"] * math.exp(-2.0 * params["tau_reio"])),
            "100theta_s": float(derived["100*theta_s"]),
            "z_rec": float(derived["z_rec"]),
            "rs_rec": float(derived["rs_rec"]),
        }
    finally:
        cosmo.struct_cleanup()
        cosmo.empty()


def main() -> None:
    cases = {
        "onefluid_control": {
            "omega_b": OMEGA_B_CONTROL,
            "omega_cdm": 0.13229026836,
        },
        "native_zero_borrow": {
            "omega_b": OMEGA_B_EFF,
            "omega_cdm": 0.13029026836,
        },
        "typed_geom_eff_eff_opacity_geom": {
            "omega_cdm": 0.13029026836,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_clustering": OMEGA_B_EFF,
            "io_baryon_opacity_source": "geom",
        },
        "typed_geom_eff_eff_opacity_eff": {
            "omega_cdm": 0.13029026836,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_clustering": OMEGA_B_EFF,
            "io_baryon_opacity_source": "eff",
        },
        "typed_geom_eff_eff_opacity_geom_uniform_local": {
            "omega_cdm": 0.13029026836,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_clustering": OMEGA_B_EFF,
            "io_baryon_opacity_source": "geom",
            "io_apply_baryon_boundary_projection": "yes",
        },
        "typed_geom_eff_eff_opacity_eff_uniform_local": {
            "omega_cdm": 0.13029026836,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_clustering": OMEGA_B_EFF,
            "io_baryon_opacity_source": "eff",
            "io_apply_baryon_boundary_projection": "yes",
        },
        "onefluid_control_sw_geom_dop_eff_pol_eff": {
            "omega_b": OMEGA_B_CONTROL,
            "omega_cdm": 0.13229026836,
            "io_source_sw_factor": F_GEOM,
            "io_source_dop_factor": F_EFF,
            "io_source_pol_factor": F_EFF,
        },
        "onefluid_control_sw_geom_dop_eff_pol_one": {
            "omega_b": OMEGA_B_CONTROL,
            "omega_cdm": 0.13229026836,
            "io_source_sw_factor": F_GEOM,
            "io_source_dop_factor": F_EFF,
            "io_source_pol_factor": 1.0,
        },
        "onefluid_control_sw_geom_only": {
            "omega_b": OMEGA_B_CONTROL,
            "omega_cdm": 0.13229026836,
            "io_source_sw_factor": F_GEOM,
        },
    }

    results = {
        "constants": {
            "x": X,
            "lcmb_rescale": X ** (-0.5),
            "lcmb_curved_shift": -3.0,
            "lcmb_curved_order": -0.25,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_control": OMEGA_B_CONTROL,
            "uniform_J_b": OMEGA_B_EFF / OMEGA_B_GEOM,
            "F_geom_over_control": F_GEOM,
            "F_eff_over_control": F_EFF,
            "base_A_s": BASE["A_s"],
            "base_tau": BASE["tau_reio"],
        },
        "cases": {},
    }

    for name, extra in cases.items():
        results["cases"][name] = {"params": extra, "result": evaluate(extra)}

    report = [
        "Paper 31 CMB Source Operator No-Go Audit",
        "=========================================",
        "",
        f"x = {X}",
        f"exact Weyl kernel = x^(-1/2) * ((k^2 - 3K)/(k_p^2 - 3K))^(-1/4)",
        f"uniform local factor J_b = omega_b_eff / omega_b_geom = {OMEGA_B_EFF / OMEGA_B_GEOM:.15f}",
        f"geom/control = {F_GEOM:.15f}",
        f"eff/control = {F_EFF:.15f}",
        "",
        "All cases evaluated at the same exact-kernel one-fluid control best-fit point:",
        f"A_s = {BASE['A_s']:.16e}",
        f"tau = {BASE['tau_reio']:.12f}",
        "",
    ]

    for name, payload in results["cases"].items():
        row = payload["result"]
        report.extend(
            [
                name,
                "-" * len(name),
                f"chi2_TTTEEE_lowTT = {row['chi2_TTTEEE_lowTT']:.6f}",
                f"A_eff = {row['A_eff']:.16e}",
                f"100theta_s = {row['100theta_s']:.9f}",
                f"z_rec = {row['z_rec']:.9f}",
                f"rs_rec = {row['rs_rec']:.9f}",
                "",
            ]
        )

    (OUT / "paper31_cmb_source_operator_nogo_results.json").write_text(json.dumps(results, indent=2) + "\n")
    (OUT / "paper31_cmb_source_operator_nogo_report.txt").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
