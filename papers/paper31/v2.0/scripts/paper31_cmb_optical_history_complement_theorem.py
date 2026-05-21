#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from functools import lru_cache
from pathlib import Path

from classy import Class
from scipy.optimize import minimize


ROOT = Path("/opt/cosmology-lab")
OUT = ROOT / "results" / "paper31"
TMP = ROOT / "tmp" / "planck-lite-py"
if str(TMP) not in sys.path:
    sys.path.insert(0, str(TMP))

from planck_lite_py import PlanckLitePy  # type: ignore  # noqa: E402


L_MAX = 2508
X = 1.5189873277742727
GAMMA = 0.2375
J_PHI = X ** (-0.5)
F_GAMMA = 1.0 / (1.0 + GAMMA**2)
F_GAMMA_SQUARED = F_GAMMA**2

OMEGA_B_GEOM = 0.02108
OMEGA_B_CONTROL = 0.02710
SQRT_GEOM_OVER_CONTROL = math.sqrt(OMEGA_B_GEOM / OMEGA_B_CONTROL)

BASE = {
    "output": "tCl,pCl,lCl",
    "lensing": "yes",
    "l_max_scalars": L_MAX,
    "lcmb_rescale": J_PHI,
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
    "omega_b": OMEGA_B_CONTROL,
    "omega_cdm": 0.13229026836,
    "A_s": 2.0240459972737345e-9,
    "tau_reio": 0.0093,
}


def make_plik() -> PlanckLitePy:
    return PlanckLitePy(
        data_directory=str(TMP / "data"),
        year=2018,
        spectra="TTTEEE",
        use_low_ell_bins=True,
    )


@lru_cache(maxsize=None)
def evaluate(c_vis: float, d_drag: float, h_hier: float) -> tuple[float, float, float, float]:
    params = dict(BASE)
    params["io_visibility_opacity_factor"] = float(c_vis)
    params["io_acoustic_drag_factor"] = float(d_drag)
    params["io_acoustic_hierarchy_factor"] = float(h_hier)
    plik = make_plik()
    cosmo = Class()
    try:
        cosmo.set(params)
        cosmo.compute()
        cls = cosmo.lensed_cl(L_MAX)
        ell = cls["ell"][2:]
        temp_scale = (params["T_cmb"] * 1.0e6) ** 2
        pref = ell * (ell + 1.0) / (2.0 * math.pi) * temp_scale
        chi2 = -2.0 * float(
            plik.loglike(pref * cls["tt"][2:], pref * cls["te"][2:], pref * cls["ee"][2:], ellmin=2)
        )
        derived = cosmo.get_current_derived_parameters(["100*theta_s", "z_rec", "rs_rec"])
        return (
            chi2,
            float(derived["100*theta_s"]),
            float(derived["z_rec"]),
            float(derived["rs_rec"]),
        )
    finally:
        cosmo.struct_cleanup()
        cosmo.empty()


def chi2_only(c_vis: float, d_drag: float, h_hier: float) -> float:
    return evaluate(round(float(c_vis), 9), round(float(d_drag), 9), round(float(h_hier), 9))[0]


def main() -> None:
    baseline = evaluate(1.0, 1.0, 1.0)

    named_points = {
        "baseline": (1.0, 1.0, 1.0),
        "theorem_candidate_common_fGamma2": (F_GAMMA_SQUARED, 1.0, F_GAMMA_SQUARED),
        "theorem_candidate_hierarchy_only_fGamma2": (1.0, 1.0, F_GAMMA_SQUARED),
        "theorem_candidate_visibility_only_fGamma2": (F_GAMMA_SQUARED, 1.0, 1.0),
        "exploratory_fGamma2_visibility_fGamma3_hierarchy": (F_GAMMA_SQUARED, 1.0, F_GAMMA**3),
        "one_leg_common_fGamma": (F_GAMMA, 1.0, F_GAMMA),
        "one_leg_hierarchy_only_fGamma": (1.0, 1.0, F_GAMMA),
        "common_sqrt_geom_over_control": (SQRT_GEOM_OVER_CONTROL, 1.0, SQRT_GEOM_OVER_CONTROL),
    }

    results: dict[str, object] = {
        "constants": {
            "x": X,
            "gamma": GAMMA,
            "j_phi": J_PHI,
            "f_gamma": F_GAMMA,
            "f_gamma_squared": F_GAMMA_SQUARED,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_control": OMEGA_B_CONTROL,
            "sqrt_geom_over_control": SQRT_GEOM_OVER_CONTROL,
        },
        "baseline": {
            "c_visibility": 1.0,
            "d_drag": 1.0,
            "h_hierarchy": 1.0,
            "chi2": baseline[0],
            "100theta_s": baseline[1],
            "z_rec": baseline[2],
            "rs_rec": baseline[3],
        },
        "named_points": {},
    }

    report = [
        "Paper 31 CMB Optical-History Complement Theorem Scan",
        "====================================================",
        "",
        "Exact curved IO Weyl kernel fixed throughout.",
        "",
        "Constants",
        "---------",
        f"gamma = {GAMMA:.15f}",
        f"f_Gamma = 1 / (1 + gamma^2) = {F_GAMMA:.15f}",
        f"f_Gamma^2 = {F_GAMMA_SQUARED:.15f}",
        f"sqrt(omega_b_geom / omega_b_control) = {SQRT_GEOM_OVER_CONTROL:.15f}",
        "",
        "Control branch baseline",
        "-----------------------",
        f"chi2 = {baseline[0]:.6f}",
        f"100theta_s = {baseline[1]:.9f}",
        f"z_rec = {baseline[2]:.9f}",
        f"rs_rec = {baseline[3]:.9f}",
        "",
        "Named points",
        "------------",
    ]

    for name, (c_vis, d_drag, h_hier) in named_points.items():
        value = evaluate(c_vis, d_drag, h_hier)
        results["named_points"][name] = {
            "c_visibility": c_vis,
            "d_drag": d_drag,
            "h_hierarchy": h_hier,
            "chi2": value[0],
            "100theta_s": value[1],
            "z_rec": value[2],
            "rs_rec": value[3],
            "delta_chi2_vs_baseline": value[0] - baseline[0],
        }
        report.append(
            f"{name}: c = {c_vis:.9f}, d = {d_drag:.9f}, h = {h_hier:.9f}, chi2 = {value[0]:.6f}, delta = {value[0] - baseline[0]:+.6f}"
        )

    opt_common = minimize(
        lambda x: chi2_only(x[0], 1.0, x[0]),
        x0=[0.89],
        method="Nelder-Mead",
        options={"xatol": 1.0e-4, "fatol": 0.2, "maxiter": 60},
    )
    best_common = evaluate(float(opt_common.x[0]), 1.0, float(opt_common.x[0]))
    results["common_optimum"] = {
        "a_best": float(opt_common.x[0]),
        "chi2_best": best_common[0],
        "100theta_s": best_common[1],
        "z_rec": best_common[2],
        "rs_rec": best_common[3],
        "delta_chi2_vs_baseline": best_common[0] - baseline[0],
    }
    report.extend(
        [
            "",
            "One-parameter common optical-history family",
            "------------------------------------------",
            f"a_best = {float(opt_common.x[0]):.9f}",
            f"chi2_best = {best_common[0]:.6f}",
            f"delta = {best_common[0] - baseline[0]:+.6f}",
        ]
    )

    opt_ch = minimize(
        lambda x: chi2_only(x[0], 1.0, x[1]),
        x0=[0.90, 0.89],
        method="Nelder-Mead",
        options={"xatol": 1.0e-4, "fatol": 0.2, "maxiter": 90},
    )
    best_ch = evaluate(float(opt_ch.x[0]), 1.0, float(opt_ch.x[1]))
    results["visibility_hierarchy_optimum"] = {
        "c_best": float(opt_ch.x[0]),
        "h_best": float(opt_ch.x[1]),
        "chi2_best": best_ch[0],
        "100theta_s": best_ch[1],
        "z_rec": best_ch[2],
        "rs_rec": best_ch[3],
        "delta_chi2_vs_baseline": best_ch[0] - baseline[0],
    }
    report.extend(
        [
            "",
            "Two-parameter optical-history family with drag fixed",
            "---------------------------------------------------",
            f"c_best = {float(opt_ch.x[0]):.9f}",
            f"h_best = {float(opt_ch.x[1]):.9f}",
            f"chi2_best = {best_ch[0]:.6f}",
            f"delta = {best_ch[0] - baseline[0]:+.6f}",
        ]
    )

    opt_cdh = minimize(
        lambda x: chi2_only(x[0], x[1], x[2]),
        x0=[0.90, 0.98, 0.86],
        method="Nelder-Mead",
        options={"xatol": 1.0e-4, "fatol": 0.2, "maxiter": 120},
    )
    best_cdh = evaluate(float(opt_cdh.x[0]), float(opt_cdh.x[1]), float(opt_cdh.x[2]))
    results["visibility_drag_hierarchy_optimum"] = {
        "c_best": float(opt_cdh.x[0]),
        "d_best": float(opt_cdh.x[1]),
        "h_best": float(opt_cdh.x[2]),
        "chi2_best": best_cdh[0],
        "100theta_s": best_cdh[1],
        "z_rec": best_cdh[2],
        "rs_rec": best_cdh[3],
        "delta_chi2_vs_baseline": best_cdh[0] - baseline[0],
    }
    report.extend(
        [
            "",
            "Three-parameter visibility+drag+hierarchy family",
            "-----------------------------------------------",
            f"c_best = {float(opt_cdh.x[0]):.9f}",
            f"d_best = {float(opt_cdh.x[1]):.9f}",
            f"h_best = {float(opt_cdh.x[2]):.9f}",
            f"chi2_best = {best_cdh[0]:.6f}",
            f"delta = {best_cdh[0] - baseline[0]:+.6f}",
        ]
    )

    (OUT / "paper31_cmb_optical_history_complement_theorem_results.json").write_text(
        json.dumps(results, indent=2) + "\n"
    )
    (OUT / "paper31_cmb_optical_history_complement_theorem_report.txt").write_text(
        "\n".join(report) + "\n"
    )


if __name__ == "__main__":
    main()
