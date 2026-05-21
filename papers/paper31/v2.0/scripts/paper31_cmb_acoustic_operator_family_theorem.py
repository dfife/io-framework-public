#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from functools import lru_cache
from pathlib import Path

from classy import Class
from scipy.optimize import minimize, minimize_scalar


ROOT = Path("/opt/cosmology-lab")
OUT = ROOT / "results" / "paper31"
TMP = ROOT / "tmp" / "planck-lite-py"
if str(TMP) not in sys.path:
    sys.path.insert(0, str(TMP))

from planck_lite_py import PlanckLitePy  # type: ignore  # noqa: E402


L_MAX = 2508
X = 1.5189873277742727
J_PHI = X ** (-0.5)

OMEGA_B_GEOM = 0.02108
OMEGA_B_EFF = 0.02910
OMEGA_B_CLUSTER = 0.017053042566349
OMEGA_B_CONTROL = 0.02710

R_GEOM_OVER_CONTROL = OMEGA_B_GEOM / OMEGA_B_CONTROL
R_EFF_OVER_CONTROL = OMEGA_B_EFF / OMEGA_B_CONTROL
R_CLUSTER_OVER_CONTROL = OMEGA_B_CLUSTER / OMEGA_B_CONTROL
R_GEOM_OVER_EFF = OMEGA_B_GEOM / OMEGA_B_EFF
R_CLUSTER_OVER_EFF = OMEGA_B_CLUSTER / OMEGA_B_EFF

BASE_COMMON = {
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
}

BRANCHES = {
    "control": {
        **BASE_COMMON,
        "omega_b": OMEGA_B_CONTROL,
        "omega_cdm": 0.13229026836,
        "A_s": 2.0240459972737345e-9,
        "tau_reio": 0.0093,
    },
    "native": {
        **BASE_COMMON,
        "omega_b": OMEGA_B_EFF,
        "omega_cdm": 0.13029026836,
        "A_s": 2.0780459972737345e-9,
        "tau_reio": 0.022636408871457327,
    },
}


def make_plik() -> PlanckLitePy:
    return PlanckLitePy(
        data_directory=str(TMP / "data"),
        year=2018,
        spectra="TTTEEE",
        use_low_ell_bins=True,
    )


@lru_cache(maxsize=None)
def evaluate(branch: str, r_fac: float, m_fac: float, s_fac: float) -> tuple[float, float, float, float]:
    plik = make_plik()
    params = dict(BRANCHES[branch])
    params["io_acoustic_r_factor"] = float(r_fac)
    params["io_acoustic_metric_factor"] = float(m_fac)
    params["io_acoustic_scattering_factor"] = float(s_fac)

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


def chi2_only(branch: str, r_fac: float, m_fac: float, s_fac: float) -> float:
    return evaluate(branch, round(float(r_fac), 9), round(float(m_fac), 9), round(float(s_fac), 9))[0]


def main() -> None:
    results: dict[str, object] = {
        "constants": {
            "x": X,
            "j_phi": J_PHI,
            "ratios": {
                "geom_over_control": R_GEOM_OVER_CONTROL,
                "eff_over_control": R_EFF_OVER_CONTROL,
                "cluster_over_control": R_CLUSTER_OVER_CONTROL,
                "geom_over_eff": R_GEOM_OVER_EFF,
                "cluster_over_eff": R_CLUSTER_OVER_EFF,
            },
        },
        "branches": {},
    }

    report = [
        "Paper 31 CMB Acoustic Operator Family Theorem",
        "=============================================",
        "",
        "ODE-level operator family on a fixed exact-kernel branch:",
        "1. acoustic inertia leg: R -> r R inside photon-baryon evolution only",
        "2. acoustic metric-driving leg: metric_euler -> m metric_euler inside photon-baryon evolution only",
        "3. acoustic Thomson leg: dkappa -> s dkappa inside photon-baryon evolution/TCA only",
        "",
        "All scans are forward-only and keep the exact curved IO Weyl kernel fixed.",
        "",
    ]

    physical_candidates = {
        "control": {
            "r_geom": (R_GEOM_OVER_CONTROL, 1.0, 1.0),
            "r_eff": (R_EFF_OVER_CONTROL, 1.0, 1.0),
            "r_cluster": (R_CLUSTER_OVER_CONTROL, 1.0, 1.0),
            "metric_weyl": (1.0, J_PHI, 1.0),
            "scatter_geom": (1.0, 1.0, R_GEOM_OVER_CONTROL),
            "scatter_eff": (1.0, 1.0, R_EFF_OVER_CONTROL),
        },
        "native": {
            "r_geom": (R_GEOM_OVER_EFF, 1.0, 1.0),
            "r_cluster": (R_CLUSTER_OVER_EFF, 1.0, 1.0),
            "metric_weyl": (1.0, J_PHI, 1.0),
            "scatter_geom": (1.0, 1.0, R_GEOM_OVER_EFF),
        },
    }

    for branch in ("control", "native"):
        baseline = evaluate(branch, 1.0, 1.0, 1.0)
        branch_results: dict[str, object] = {
            "baseline": {
                "r": 1.0,
                "m": 1.0,
                "s": 1.0,
                "chi2": baseline[0],
                "100theta_s": baseline[1],
                "z_rec": baseline[2],
                "rs_rec": baseline[3],
            },
            "physical_points": {},
        }

        report.extend(
            [
                branch,
                "-" * len(branch),
                f"baseline: r = 1, m = 1, s = 1, chi2 = {baseline[0]:.6f}",
            ]
        )

        for label, (r_fac, m_fac, s_fac) in physical_candidates[branch].items():
            point = evaluate(branch, r_fac, m_fac, s_fac)
            branch_results["physical_points"][label] = {
                "r": r_fac,
                "m": m_fac,
                "s": s_fac,
                "chi2": point[0],
                "100theta_s": point[1],
                "z_rec": point[2],
                "rs_rec": point[3],
                "delta_chi2_vs_baseline": point[0] - baseline[0],
            }
            report.append(
                f"{label}: r = {r_fac:.9f}, m = {m_fac:.9f}, s = {s_fac:.9f}, chi2 = {point[0]:.6f}, delta = {point[0] - baseline[0]:+.6f}"
            )

        r_opt = minimize_scalar(
            lambda r: chi2_only(branch, r, 1.0, 1.0),
            bounds=(0.55, 1.15),
            method="bounded",
            options={"xatol": 5.0e-3},
        )
        m_opt = minimize_scalar(
            lambda m: chi2_only(branch, 1.0, m, 1.0),
            bounds=(0.7, 1.2),
            method="bounded",
            options={"xatol": 5.0e-3},
        )
        s_opt = minimize_scalar(
            lambda s: chi2_only(branch, 1.0, 1.0, s),
            bounds=(0.7, 1.15),
            method="bounded",
            options={"xatol": 5.0e-3},
        )

        r_best = evaluate(branch, float(r_opt.x), 1.0, 1.0)
        m_best = evaluate(branch, 1.0, float(m_opt.x), 1.0)
        s_best = evaluate(branch, 1.0, 1.0, float(s_opt.x))

        branch_results["r_leg_optimum"] = {
            "r_best": float(r_opt.x),
            "chi2_best": r_best[0],
            "delta_chi2_vs_baseline": r_best[0] - baseline[0],
            "100theta_s": r_best[1],
            "z_rec": r_best[2],
            "rs_rec": r_best[3],
        }
        branch_results["metric_leg_optimum"] = {
            "m_best": float(m_opt.x),
            "chi2_best": m_best[0],
            "delta_chi2_vs_baseline": m_best[0] - baseline[0],
            "100theta_s": m_best[1],
            "z_rec": m_best[2],
            "rs_rec": m_best[3],
        }
        branch_results["scatter_leg_optimum"] = {
            "s_best": float(s_opt.x),
            "chi2_best": s_best[0],
            "delta_chi2_vs_baseline": s_best[0] - baseline[0],
            "100theta_s": s_best[1],
            "z_rec": s_best[2],
            "rs_rec": s_best[3],
        }

        report.extend(
            [
                f"R-leg optimum: r_best = {float(r_opt.x):.9f}, chi2 = {r_best[0]:.6f}, delta = {r_best[0] - baseline[0]:+.6f}",
                f"metric-leg optimum: m_best = {float(m_opt.x):.9f}, chi2 = {m_best[0]:.6f}, delta = {m_best[0] - baseline[0]:+.6f}",
                f"scatter-leg optimum: s_best = {float(s_opt.x):.9f}, chi2 = {s_best[0]:.6f}, delta = {s_best[0] - baseline[0]:+.6f}",
            ]
        )

        if branch == "control":
            rm_opt = minimize(
                lambda x: chi2_only(branch, x[0], x[1], 1.0),
                x0=[1.0, 1.0],
                method="Powell",
                bounds=[(0.55, 1.15), (0.7, 1.2)],
                options={"xtol": 5.0e-3, "ftol": 1.0e-2, "maxiter": 40, "maxfev": 80},
            )
            rs_opt = minimize(
                lambda x: chi2_only(branch, x[0], 1.0, x[1]),
                x0=[1.0, 1.0],
                method="Powell",
                bounds=[(0.55, 1.15), (0.7, 1.15)],
                options={"xtol": 5.0e-3, "ftol": 1.0e-2, "maxiter": 40, "maxfev": 80},
            )
            full_opt = minimize(
                lambda x: chi2_only(branch, x[0], x[1], x[2]),
                x0=[1.0, 1.0, 1.0],
                method="Powell",
                bounds=[(0.55, 1.15), (0.7, 1.2), (0.7, 1.15)],
                options={"xtol": 5.0e-3, "ftol": 1.0e-2, "maxiter": 60, "maxfev": 140},
            )
            rm_best = evaluate(branch, float(rm_opt.x[0]), float(rm_opt.x[1]), 1.0)
            rs_best = evaluate(branch, float(rs_opt.x[0]), 1.0, float(rs_opt.x[1]))
            full_best = evaluate(branch, float(full_opt.x[0]), float(full_opt.x[1]), float(full_opt.x[2]))
            branch_results["rm_family_optimum"] = {
                "r_best": float(rm_opt.x[0]),
                "m_best": float(rm_opt.x[1]),
                "chi2_best": rm_best[0],
                "delta_chi2_vs_baseline": rm_best[0] - baseline[0],
                "success": bool(rm_opt.success),
                "message": str(rm_opt.message),
                "nfev": int(rm_opt.nfev),
            }
            branch_results["rs_family_optimum"] = {
                "r_best": float(rs_opt.x[0]),
                "s_best": float(rs_opt.x[1]),
                "chi2_best": rs_best[0],
                "delta_chi2_vs_baseline": rs_best[0] - baseline[0],
                "success": bool(rs_opt.success),
                "message": str(rs_opt.message),
                "nfev": int(rs_opt.nfev),
            }
            branch_results["full_family_optimum"] = {
                "r_best": float(full_opt.x[0]),
                "m_best": float(full_opt.x[1]),
                "s_best": float(full_opt.x[2]),
                "chi2_best": full_best[0],
                "delta_chi2_vs_baseline": full_best[0] - baseline[0],
                "success": bool(full_opt.success),
                "message": str(full_opt.message),
                "nfev": int(full_opt.nfev),
            }
            report.extend(
                [
                    f"R+metric optimum: r_best = {float(rm_opt.x[0]):.9f}, m_best = {float(rm_opt.x[1]):.9f}, chi2 = {rm_best[0]:.6f}, delta = {rm_best[0] - baseline[0]:+.6f}",
                    f"R+scatter optimum: r_best = {float(rs_opt.x[0]):.9f}, s_best = {float(rs_opt.x[1]):.9f}, chi2 = {rs_best[0]:.6f}, delta = {rs_best[0] - baseline[0]:+.6f}",
                    f"full three-leg optimum: r_best = {float(full_opt.x[0]):.9f}, m_best = {float(full_opt.x[1]):.9f}, s_best = {float(full_opt.x[2]):.9f}, chi2 = {full_best[0]:.6f}, delta = {full_best[0] - baseline[0]:+.6f}",
                ]
            )

        report.append("")
        results["branches"][branch] = branch_results

    (OUT / "paper31_cmb_acoustic_operator_family_theorem_results.json").write_text(
        json.dumps(results, indent=2) + "\n"
    )
    (OUT / "paper31_cmb_acoustic_operator_family_theorem_report.txt").write_text(
        "\n".join(report) + "\n"
    )


if __name__ == "__main__":
    main()
