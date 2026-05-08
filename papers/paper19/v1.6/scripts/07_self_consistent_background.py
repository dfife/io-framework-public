from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import mpmath as mp

"""
Reproduce the Paper 19 self-consistent background diagnostic branches.

This heavy optional rerun imports script 06 for BOSS, BAO, CLASS, and distance
helpers. It propagates the Paper 17 v1.5 FIRAS-fixed observer-side temperature
and writes the age-closed and Schur-branch diagnostics. The age-closed
``N_mode`` value is an open-premise diagnostic branch unless theorem-fixed
elsewhere; it is not a zero-fitted-parameter prediction.

Output:
    ../results/self_consistent_background_results.json
"""

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT
OUT = BUNDLE_ROOT / "results" / "self_consistent_background_results.json"


def load_scorecard_module():
    spec = importlib.util.spec_from_file_location(
        "paper19_scorecard", BUNDLE_ROOT / "scripts" / "06_corrected_scorecard.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


score = load_scorecard_module()


GAMMA = 0.2375
X = 1.51899
DELTA = X**4 * (1 + GAMMA**2)
SQRT_DELTA = math.sqrt(DELTA)
K_GAUGE = math.log(1 + GAMMA**2)

T_IO = 2.6635
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255
# Paper 17 v1.5 replaced the old implicit R4=1 temperature readout with a
# FIRAS-fixed normalization. This script propagates the frozen observer-side
# thermal datum; it does not claim an independent CMB-temperature prediction.
T0_OBS = T_FIRAS
N_EFF_SM = 3.044

H0_GEOM = 58.42
OMEGA_M_GEOM = 0.197
OMEGA_K_GEOM = -0.130

H0_PAPER18_SCHUR = 68.91
NORM_PAPER18_SCHUR = (H0_PAPER18_SCHUR / H0_GEOM) ** 2
PK_PAPER10 = DELTA ** (-1.0 / (X**2))
PK_SCHUR_DELTA = math.exp(-DELTA / 2.0)
OMEGA_LAMBDA_BARE = (
    NORM_PAPER18_SCHUR - OMEGA_M_GEOM * SQRT_DELTA - OMEGA_K_GEOM * PK_SCHUR_DELTA
) / SQRT_DELTA

H_GEOM = H0_GEOM / 100.0
OMEGA_B_ALPHA1 = OMEGA_M_GEOM * (H_GEOM**2) * (2.0 * GAMMA / X)
OMEGA_B_CLUST = OMEGA_B_ALPHA1 * (X ** (-0.5))
R_D_FIXED = 143.3

TARGET_AGE_GYR = 13.8


def omega_r(t0: float, n_eff: float, h: float) -> float:
    omega_gamma_h2 = 2.4728e-5 * (t0 / 2.7255) ** 4
    omega_r_h2 = omega_gamma_h2 * (1.0 + 0.22710731766 * n_eff)
    return omega_r_h2 / (h * h)


def age_today_gyr(*, h0: float, omega_m: float, omega_k: float, t0: float, n_eff: float) -> float:
    mp.mp.dps = 80
    H0_m = mp.mpf(str(h0))
    Om_m = mp.mpf(str(omega_m))
    Ok_m = mp.mpf(str(omega_k))
    T0_m = mp.mpf(str(t0))
    Neff_m = mp.mpf(str(n_eff))
    h = H0_m / 100
    omega_gamma = mp.mpf("2.4728e-5") * (T0_m / mp.mpf("2.7255")) ** 4
    omega_r_val = omega_gamma * (1 + mp.mpf("0.22710731766") * Neff_m) / (h**2)
    omega_lambda = 1 - Om_m - Ok_m - omega_r_val
    integrand = lambda a_: 1 / (a_ * mp.sqrt(omega_r_val / a_**4 + Om_m / a_**3 + Ok_m / a_**2 + omega_lambda))
    return float((mp.mpf("9.778130") / h) * mp.quad(integrand, [0, 1]))


def background_from_pk(pk_value: float) -> dict[str, float]:
    norm = OMEGA_M_GEOM * SQRT_DELTA + OMEGA_K_GEOM * pk_value + OMEGA_LAMBDA_BARE * SQRT_DELTA
    h0 = H0_GEOM * math.sqrt(norm)
    omega_m = OMEGA_M_GEOM * SQRT_DELTA / norm
    omega_k = OMEGA_K_GEOM * pk_value / norm
    omega_lambda = OMEGA_LAMBDA_BARE * SQRT_DELTA / norm
    age = age_today_gyr(h0=h0, omega_m=omega_m, omega_k=omega_k, t0=T0_OBS, n_eff=N_EFF_SM)
    return {
        "P_k": pk_value,
        "N_norm": norm,
        "H0": h0,
        "Omega_m": omega_m,
        "Omega_k": omega_k,
        "Omega_lambda": omega_lambda,
        "age_Gyr": age,
    }


def background_from_schur_mode(n_mode: float) -> dict[str, float]:
    result = background_from_pk(math.exp(-n_mode / 2.0))
    result["N_mode"] = n_mode
    return result


def solve_age_closed_n_mode() -> float:
    lo = mp.mpf("0.0")
    hi = mp.mpf("1.0")
    target = mp.mpf(str(TARGET_AGE_GYR))
    while mp.mpf(str(background_from_schur_mode(float(hi))["age_Gyr"])) > target:
        hi *= 2
    for _ in range(120):
        mid = (lo + hi) / 2
        age_mid = mp.mpf(str(background_from_schur_mode(float(mid))["age_Gyr"]))
        if age_mid > target:
            lo = mid
        else:
            hi = mid
    return float((lo + hi) / 2)


def z_eq(background: dict[str, float]) -> float:
    h = background["H0"] / 100.0
    omega_r_val = omega_r(T0_OBS, N_EFF_SM, h)
    return background["Omega_m"] / omega_r_val - 1.0


def branch_metrics(name: str, background: dict[str, float]) -> dict[str, object]:
    clust_model = score.run_class_model(
        h0=background["H0"],
        omega_m=background["Omega_m"],
        omega_k=background["Omega_k"],
        t0=T0_OBS,
        n_eff=N_EFF_SM,
        omega_b=OMEGA_B_CLUST,
    )
    alpha1_model = score.run_class_model(
        h0=background["H0"],
        omega_m=background["Omega_m"],
        omega_k=background["Omega_k"],
        t0=T0_OBS,
        n_eff=N_EFF_SM,
        omega_b=OMEGA_B_ALPHA1,
    )
    jwst = score.jwst_ages(
        h0=background["H0"],
        omega_m=background["Omega_m"],
        omega_k=background["Omega_k"],
        t0=T0_OBS,
        n_eff=N_EFF_SM,
    )
    bao_fixed_chi2, bao_fixed_pte = score.bao_chi2(
        h0=background["H0"],
        omega_m=background["Omega_m"],
        omega_k=background["Omega_k"],
        t0=T0_OBS,
        n_eff=N_EFF_SM,
        r_d=R_D_FIXED,
    )
    bao_std_clust_chi2, bao_std_clust_pte = score.bao_chi2(
        h0=background["H0"],
        omega_m=background["Omega_m"],
        omega_k=background["Omega_k"],
        t0=T0_OBS,
        n_eff=N_EFF_SM,
        r_d=clust_model["rs_drag_Mpc"],
    )
    bao_std_alpha1_chi2, bao_std_alpha1_pte = score.bao_chi2(
        h0=background["H0"],
        omega_m=background["Omega_m"],
        omega_k=background["Omega_k"],
        t0=T0_OBS,
        n_eff=N_EFF_SM,
        r_d=alpha1_model["rs_drag_Mpc"],
    )
    boss_chi2 = score.boss_fullshape_chi2(
        h0=background["H0"],
        omega_m=background["Omega_m"],
        omega_k=background["Omega_k"],
        t0=T0_OBS,
        n_eff=N_EFF_SM,
        omega_b=OMEGA_B_CLUST,
    )
    return {
        "name": name,
        "background": background,
        "z_eq": z_eq(background),
        "T_CMB_obs_K": T0_OBS,
        "omega_b_alpha1": OMEGA_B_ALPHA1,
        "omega_b_clust_alpha_3_over_2": OMEGA_B_CLUST,
        "clustering_sector": {
            "omega_b": OMEGA_B_CLUST,
            "sigma8": clust_model["sigma8"],
            "S8": clust_model["S8"],
            "rs_drag_Mpc_if_forced": clust_model["rs_drag_Mpc"],
            "boss_fullshape_chi2": boss_chi2,
            "bao_standard_ruler_chi2_if_forced": bao_std_clust_chi2,
            "bao_standard_ruler_pte_if_forced": bao_std_clust_pte,
        },
        "bao_sector": {
            "fixed_ruler_r_d_Mpc": R_D_FIXED,
            "fixed_ruler_chi2": bao_fixed_chi2,
            "fixed_ruler_pte": bao_fixed_pte,
            "alpha1_omega_b": OMEGA_B_ALPHA1,
            "alpha1_rs_drag_Mpc": alpha1_model["rs_drag_Mpc"],
            "alpha1_standard_ruler_chi2": bao_std_alpha1_chi2,
            "alpha1_standard_ruler_pte": bao_std_alpha1_pte,
        },
        "jwst_ages_Myr": {
            "z6": float(jwst["6"]),
            "z10": float(jwst["10"]),
            "z14": float(jwst["14"]),
            "z20": float(jwst["20"]),
            "today_Gyr": float(jwst["today_Gyr"]),
        },
    }


def scan_n_mode() -> dict[str, object]:
    rows = []
    best_bao = None
    best_boss = None
    best_joint = None
    for i in range(0, 25):
        n_mode = i * 0.25
        background = background_from_schur_mode(n_mode)
        clust_model = score.run_class_model(
            h0=background["H0"],
            omega_m=background["Omega_m"],
            omega_k=background["Omega_k"],
            t0=T0_OBS,
            n_eff=N_EFF_SM,
            omega_b=OMEGA_B_CLUST,
        )
        alpha1_model = score.run_class_model(
            h0=background["H0"],
            omega_m=background["Omega_m"],
            omega_k=background["Omega_k"],
            t0=T0_OBS,
            n_eff=N_EFF_SM,
            omega_b=OMEGA_B_ALPHA1,
        )
        bao_chi2, _ = score.bao_chi2(
            h0=background["H0"],
            omega_m=background["Omega_m"],
            omega_k=background["Omega_k"],
            t0=T0_OBS,
            n_eff=N_EFF_SM,
            r_d=alpha1_model["rs_drag_Mpc"],
        )
        boss_chi2 = score.boss_fullshape_chi2(
            h0=background["H0"],
            omega_m=background["Omega_m"],
            omega_k=background["Omega_k"],
            t0=T0_OBS,
            n_eff=N_EFF_SM,
            omega_b=OMEGA_B_CLUST,
        )
        row = {
            "N_mode": n_mode,
            "P_k": background["P_k"],
            "H0": background["H0"],
            "Omega_m": background["Omega_m"],
            "Omega_k": background["Omega_k"],
            "age_Gyr": background["age_Gyr"],
            "bao_alpha1_standard_chi2": bao_chi2,
            "boss_clust_chi2": boss_chi2,
            "S8_clust": clust_model["S8"],
            "joint_chi2": bao_chi2 + boss_chi2,
        }
        rows.append(row)
        if best_bao is None or row["bao_alpha1_standard_chi2"] < best_bao["bao_alpha1_standard_chi2"]:
            best_bao = row
        if best_boss is None or row["boss_clust_chi2"] < best_boss["boss_clust_chi2"]:
            best_boss = row
        if best_joint is None or row["joint_chi2"] < best_joint["joint_chi2"]:
            best_joint = row
    return {
        "rows": rows,
        "best_bao_alpha1_standard": best_bao,
        "best_boss_clustering": best_boss,
        "best_joint": best_joint,
    }


def main() -> None:
    age_closed_n_mode = solve_age_closed_n_mode()
    schur_age = branch_metrics("schur_age_closed", background_from_schur_mode(age_closed_n_mode))
    schur_topological = branch_metrics("schur_topological_N_equals_4", background_from_schur_mode(4.0))
    schur_candidate = branch_metrics("schur_candidate_N_equals_Delta", background_from_schur_mode(DELTA))
    paper10_fallback = branch_metrics("paper10_fallback", background_from_pk(PK_PAPER10))

    payload = {
        "inputs": {
            "gamma": GAMMA,
            "x": X,
            "Delta": DELTA,
            "sqrt_Delta": SQRT_DELTA,
            "K_gauge": K_GAUGE,
            "T_IO": T_IO,
            "R4_FIRAS": R4_FIRAS,
            "T_FIRAS_K": T_FIRAS,
            "T_obs_R4_formula": "T_obs(R4) = T_IO * x^(R4*K_gauge); FIRAS fixes R4 in Paper 17 v1.5",
            "temperature_status": "IMPORTED/EMPIRICAL FIRAS-fixed observer-side thermal datum; not an independent CMB prediction",
            "T_CMB_obs": T0_OBS,
            "N_eff_SM_imported": N_EFF_SM,
            "H0_geom": H0_GEOM,
            "Omega_m_geom": OMEGA_M_GEOM,
            "Omega_k_geom": OMEGA_K_GEOM,
            "Omega_lambda_bare": OMEGA_LAMBDA_BARE,
            "omega_b_alpha1": OMEGA_B_ALPHA1,
            "omega_b_clust_alpha_3_over_2": OMEGA_B_CLUST,
            "target_age_Gyr": TARGET_AGE_GYR,
        },
        "branches": {
            "schur_age_closed": schur_age,
            "schur_topological_N_equals_4": schur_topological,
            "schur_candidate_N_equals_Delta": schur_candidate,
            "paper10_fallback": paper10_fallback,
        },
        "scan_n_mode": scan_n_mode(),
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
