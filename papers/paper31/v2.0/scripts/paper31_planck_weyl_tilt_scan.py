#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from classy import Class


ROOT = Path("/opt/cosmology-lab")
OUT = ROOT / "results" / "paper31"
TMP = ROOT / "tmp"
PLANCK_LITE_REPO = TMP / "planck-lite-py"
PLANCK_LITE_DATA = PLANCK_LITE_REPO / "data"

if str(PLANCK_LITE_REPO) not in sys.path:
    sys.path.insert(0, str(PLANCK_LITE_REPO))

from planck_lite_py import PlanckLitePy  # type: ignore  # noqa: E402


L_MAX = 2508
T_CMB = 2.7253
X = 1.5189873277742727
LCMB_RESCALE = X ** (-0.5)

BASE_PARAMS = {
    "output": "tCl,pCl,lCl",
    "lensing": "yes",
    "l_max_scalars": L_MAX,
    "H0": 67.58,
    "T_cmb": T_CMB,
    "omega_b": 0.02710,
    "omega_cdm": 0.13229026836,
    "Omega_k": -0.006,
    "N_ur": 3.044,
    "N_ncdm": 0,
    "YHe": 0.2477,
    "n_s": 0.9639,
    "alpha_s": 5.0e-5,
    "reio_parametrization": "reio_camb",
    "lcmb_rescale": LCMB_RESCALE,
    "lcmb_pivot": 0.05,
}

PACKAGES = {
    "old": {"A_s": 2.0072459972737347e-9, "tau_reio": 0.02743640887145733},
    "new": {"A_s": 2.1141000090331526e-9, "tau_reio": 0.05487281774291466},
}

TILTS = [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]


def likelihood() -> PlanckLitePy:
    return PlanckLitePy(
        data_directory=str(PLANCK_LITE_DATA),
        year=2018,
        spectra="TTTEEE",
        use_low_ell_bins=True,
    )


def evaluate(params: dict, plik: PlanckLitePy) -> dict:
    cosmo = Class()
    try:
        cosmo.set(params)
        cosmo.compute()
        cls = cosmo.lensed_cl(L_MAX)
        ell = cls["ell"][2:]
        temp_scale = (params["T_cmb"] * 1.0e6) ** 2
        pref = ell * (ell + 1.0) / (2.0 * math.pi) * temp_scale
        dl_tt = pref * cls["tt"][2:]
        dl_te = pref * cls["te"][2:]
        dl_ee = pref * cls["ee"][2:]
        chi2 = -2.0 * float(plik.loglike(dl_tt, dl_te, dl_ee, ellmin=2))
        derived = cosmo.get_current_derived_parameters(["100*theta_s"])
        return {
            "valid": True,
            "chi2": chi2,
            "100theta_s": float(derived["100*theta_s"]),
            "A_eff": float(params["A_s"] * math.exp(-2.0 * params["tau_reio"])),
        }
    except Exception as exc:
        return {
            "valid": False,
            "chi2": float("inf"),
            "100theta_s": float("nan"),
            "A_eff": float(params["A_s"] * math.exp(-2.0 * params["tau_reio"])),
            "error": str(exc),
        }
    finally:
        cosmo.struct_cleanup()
        cosmo.empty()


def main() -> None:
    plik = likelihood()
    results = {
        "constants": {
            "x": X,
            "lcmb_rescale": LCMB_RESCALE,
            "tilts": TILTS,
        },
        "packages": {},
    }
    report = [
        "Paper 31 Planck Weyl Tilt Scan",
        "===============================",
        "",
        f"x = {X}",
        f"lcmb_rescale = x^(-1/2) = {LCMB_RESCALE:.15f}",
        "Branch: one-fluid IO control",
        "",
    ]

    for key, pkg in PACKAGES.items():
        rows = []
        best = None
        for tilt in TILTS:
            params = dict(BASE_PARAMS)
            params.update(pkg)
            params["lcmb_tilt"] = tilt
            row = {"lcmb_tilt": tilt, **evaluate(params, plik)}
            rows.append(row)
            if row["valid"] and (best is None or row["chi2"] < best["chi2"]):
                best = row
        results["packages"][key] = {"params": pkg, "rows": rows, "best": best}
        report.append(f"Package: {key}")
        report.append(f"  A_s = {pkg['A_s']:.16e}")
        report.append(f"  tau = {pkg['tau_reio']:.12f}")
        if best is not None:
            report.append(f"  best lcmb_tilt = {best['lcmb_tilt']:+.3f}")
            report.append(f"  best chi2 = {best['chi2']:.6f}")
            report.append(f"  best 100theta_s = {best['100theta_s']:.9f}")
        for row in rows:
            if row["valid"]:
                report.append(
                    f"    tilt={row['lcmb_tilt']:+.3f} chi2={row['chi2']:.6f} "
                    f"100theta_s={row['100theta_s']:.9f}"
                )
            else:
                report.append(f"    tilt={row['lcmb_tilt']:+.3f} invalid")
        report.append("")

    (OUT / "paper31_planck_weyl_tilt_scan_results.json").write_text(json.dumps(results, indent=2) + "\n")
    (OUT / "paper31_planck_weyl_tilt_scan_report.txt").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
