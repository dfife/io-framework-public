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
X = 1.519
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

START = {
    "A_s": 2.0072459972737347e-9,
    "tau_reio": 0.02743640887145733,
    "lcmb_tilt": -0.4,
}


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
    cache = {}

    def get(a_s: float, tau: float, tilt: float) -> dict:
        key = (round(a_s, 15), round(tau, 12), round(tilt, 6))
        if key not in cache:
            params = dict(BASE_PARAMS)
            params["A_s"] = a_s
            params["tau_reio"] = tau
            params["lcmb_tilt"] = tilt
            cache[key] = {"A_s": a_s, "tau": tau, "lcmb_tilt": tilt, **evaluate(params, plik)}
        return cache[key]

    best = dict(START)
    span_a = 0.18e-9
    span_tau = 0.03
    span_tilt = 0.5
    history = []

    for level, n in enumerate((5, 5, 5), start=1):
        a_vals = [best["A_s"] - span_a + 2 * span_a * i / (n - 1) for i in range(n)]
        t_vals = [max(0.0021, best["tau_reio"] - span_tau + 2 * span_tau * j / (n - 1)) for j in range(n)]
        l_vals = [best["lcmb_tilt"] - span_tilt + 2 * span_tilt * k / (n - 1) for k in range(n)]
        level_best = None
        for a_s in a_vals:
            for tau in t_vals:
                for tilt in l_vals:
                    row = get(a_s, tau, tilt)
                    if row["valid"] and (level_best is None or row["chi2"] < level_best["chi2"]):
                        level_best = row
        assert level_best is not None
        history.append(
            {
                "level": level,
                "span_A_s": span_a,
                "span_tau": span_tau,
                "span_lcmb_tilt": span_tilt,
                "best": level_best,
            }
        )
        best = {"A_s": level_best["A_s"], "tau_reio": level_best["tau"], "lcmb_tilt": level_best["lcmb_tilt"]}
        span_a *= 0.35
        span_tau *= 0.35
        span_tilt *= 0.5

    results = {
        "constants": {"x": X, "lcmb_rescale": LCMB_RESCALE},
        "start": START,
        "evaluation_count": len(cache),
        "best_fit": history[-1]["best"],
        "history": history,
    }

    report = [
        "Paper 31 Planck Weyl Tilt Refit",
        "================================",
        "",
        f"x = {X}",
        f"lcmb_rescale = x^(-1/2) = {LCMB_RESCALE:.15f}",
        "Branch: one-fluid IO control",
        f"start A_s = {START['A_s']:.16e}",
        f"start tau = {START['tau_reio']:.12f}",
        f"start lcmb_tilt = {START['lcmb_tilt']:+.3f}",
        f"evaluations = {len(cache)}",
        "",
    ]
    best_fit = history[-1]["best"]
    report.extend(
        [
            f"best-fit A_s = {best_fit['A_s']:.16e}",
            f"best-fit tau = {best_fit['tau']:.12f}",
            f"best-fit lcmb_tilt = {best_fit['lcmb_tilt']:+.6f}",
            f"best-fit A_eff = {best_fit['A_eff']:.16e}",
            f"best-fit chi2 = {best_fit['chi2']:.6f}",
            f"best-fit 100theta_s = {best_fit['100theta_s']:.9f}",
        ]
    )

    (OUT / "paper31_planck_weyl_tilt_refit_results.json").write_text(json.dumps(results, indent=2) + "\n")
    (OUT / "paper31_planck_weyl_tilt_refit_report.txt").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
