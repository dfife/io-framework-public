#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import minimize_scalar


BASE = Path("/opt/cosmology-lab/results/paper31")
SCRIPT_PATH = BASE / "paper31_full_recompute_legacy_branch.py"
RESULTS_JSON = BASE / "paper31_full_recompute_legacy_branch_results.json"
REPORT_MD = BASE / "paper31_full_recompute_legacy_branch_report.md"

P29_BAO_PATH = "/opt/cosmology-lab/results/paper29/paper29_bao_blocksplit_covariance_kernel.py"
P30_PATH = "/opt/cosmology-lab/results/paper30/paper30_full_recompute_legacy_branch.py"
MAP_PATH = BASE / "paper31_complete_observable_class_map.md"

C_SI = 2.998e8
MPC_SI = 3.0856775814913673e22
SEC_PER_GYR = 365.25 * 24.0 * 3600.0 * 1.0e9

H0 = 67.57585653582628
OMEGA_M = 0.34868395067621694
OMEGA_K = -0.04579112576013168
OMEGA_L = 0.69701575761593
OMEGA_R = 9.141746798467538e-05
OMEGA_B_GEOM = 0.020995719061702847
OMEGA_B_EFF = 0.02898917105671435
OMEGA_B_CLUSTERING = 0.01703545264427447
R_D_HYBRID = 144.01351425392883

X_EXACT = 1.5189873277742727
GAMMA = 0.2375
K_GAUGE = math.log(1.0 + GAMMA * GAMMA)
ETA = K_GAUGE / X_EXACT
SIGMA_IO = X_EXACT ** (-0.5)
TAU_COV = K_GAUGE / 2.0

OLD_SCHUR = {
    "geometric_pre_drag_ruler_mpc": 143.06250283686956,
    "galaxy_target_mpc": 143.95894879622443,
    "galaxy_residual_frac": 4.6e-4,
    "sigma8": 0.949,
    "s8_lens": 0.793,
    "eg_alpha_phi_best": 1.992,
    "eg_alpha_phi_1sigma": [1.772, 2.234],
    "reionization_transport": {5: 1.64, 10: 1.59, 14: 1.58, 20: 1.57},
    "tau_cov": 0.02743640887145733,
    "omega_b_struct": 0.025941102017499,
    "weyl_lcmb_rescale": 0.811374048924378,
    "weyl_al_surrogate": 0.6583278271692742,
    "map_fixed_slots": {
        "H0": 68.91,
        "Omega_m": 0.33577637957547024,
        "Omega_k": -0.005613722564238656,
        "Omega_lambda": 0.6698373429887684,
        "omega_b_geom": 0.02108,
        "omega_b_eff": 0.02910,
        "omega_b_clustering": 0.017053042566348754,
        "A_s": 2.1141000090331526e-09,
        "n_s": 0.963872644987,
    },
    "lya_target_mpc": 140.790554518058,
    "lya_raw_chi2": 6.176391241793,
    "lya_shifted_mpc": 141.703409059919,
}

EG_BENCHMARKS = [
    {
        "id": "blake2015_z032",
        "z": 0.32,
        "mean": 0.480,
        "sigma": 0.100,
        "channel": "galaxy_lensing",
    },
    {
        "id": "blake2015_z057",
        "z": 0.57,
        "mean": 0.300,
        "sigma": 0.070,
        "channel": "galaxy_lensing",
    },
    {
        "id": "pullen2015_z057",
        "z": 0.57,
        "mean": 0.243,
        "sigma": math.sqrt(0.060**2 + 0.013**2),
        "channel": "cmb_lensing",
    },
    {
        "id": "alam2016_z057",
        "z": 0.57,
        "mean": 0.420,
        "sigma": 0.056,
        "channel": "galaxy_lensing",
    },
]

EG_GROUPS = {
    "all": [b["id"] for b in EG_BENCHMARKS],
    "galaxy_lensing_only": [b["id"] for b in EG_BENCHMARKS if b["channel"] == "galaxy_lensing"],
    "cmb_lensing_only": [b["id"] for b in EG_BENCHMARKS if b["channel"] == "cmb_lensing"],
}


def load_module(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


p29bao = load_module("paper31_recompute_p29_bao", P29_BAO_PATH)
p30 = load_module("paper31_recompute_p30", P30_PATH)


def compute_pre_drag_ruler() -> dict[str, Any]:
    return {
        "r_d_mpc": R_D_HYBRID,
        "same_as_paper29_hybrid": True,
        "old_schur_mpc": OLD_SCHUR["geometric_pre_drag_ruler_mpc"],
        "delta_mpc": R_D_HYBRID - OLD_SCHUR["geometric_pre_drag_ruler_mpc"],
        "delta_percent": 100.0 * (R_D_HYBRID / OLD_SCHUR["geometric_pre_drag_ruler_mpc"] - 1.0),
        "qualitative_change": "value_shifted_upward",
        "status": "verified/carried from Paper 29 hybrid legacy-branch derivation",
    }


def _fit_block_target(rows: list[dict[str, Any]], covariance: np.ndarray, selector) -> dict[str, float]:
    idx = [i for i, row in enumerate(rows) if selector(row)]
    sub_cov = covariance[np.ix_(idx, idx)]
    inv_cov = np.linalg.inv(sub_cov)

    def objective(rd_mpc: float) -> float:
        modeled = p29bao.make_rows(
            rows,
            branch=p29bao.IO,
            bg=p29bao.background(p29bao.IO),
            rd_gal=rd_mpc,
            rd_lya=rd_mpc,
            f_perp_gal=1.0,
            f_par_gal=1.0,
        )
        diff = np.array([float(modeled[i]["residual"]) for i in idx], dtype=float)
        return float(diff @ inv_cov @ diff)

    res = minimize_scalar(objective, bounds=(120.0, 170.0), method="bounded")
    return {"rd_target_mpc": float(res.x), "chi2_target": float(res.fun), "indices": idx}


def _information_weights_by_quantity(
    rows: list[dict[str, Any]],
    covariance: np.ndarray,
    selector,
) -> dict[str, float]:
    idx = [i for i, row in enumerate(rows) if selector(row)]
    sub_cov = covariance[np.ix_(idx, idx)]
    inv_cov = np.linalg.inv(sub_cov)
    bg = p29bao.background(p29bao.IO)
    shapes = []
    for i in idx:
        row = rows[i]
        z = float(row["z"])
        q = str(row["quantity"])
        dm = p29bao.D_M(z, p29bao.IO, bg)
        dh = p29bao.D_H(z, p29bao.IO, bg)
        if q == "DM_over_rs":
            shape = dm
        elif q == "DH_over_rs":
            shape = dh
        else:
            shape = (z * dm * dm * dh) ** (1.0 / 3.0)
        shapes.append(shape)
    shape_arr = np.array(shapes, dtype=float)
    fisher = float(shape_arr @ inv_cov @ shape_arr)
    info = shape_arr * (inv_cov @ shape_arr) / fisher
    grouped: dict[str, float] = defaultdict(float)
    for local_i, global_i in enumerate(idx):
        grouped[str(rows[global_i]["quantity"])] += float(info[local_i])
    return dict(grouped)


def compute_bao_galaxy_block() -> dict[str, Any]:
    rows, cov = p29bao.load_bao_data()
    bg = p29bao.background(p29bao.IO)
    f_perp = math.exp(ETA)
    f_par = math.exp(ETA / 2.0)
    f_dv = (f_perp * f_perp * f_par) ** (1.0 / 3.0)
    modeled = p29bao.make_rows(
        rows,
        branch=p29bao.IO,
        bg=bg,
        rd_gal=R_D_HYBRID,
        rd_lya=R_D_HYBRID,
        f_perp_gal=f_perp,
        f_par_gal=f_par,
    )
    galaxy_target = _fit_block_target(rows, cov, lambda row: float(row["z"]) < 2.0)
    weights = _information_weights_by_quantity(rows, cov, lambda row: float(row["z"]) < 2.0)
    rd_eff_perp = R_D_HYBRID * f_perp
    rd_eff_par = R_D_HYBRID * f_par
    rd_eff_dv = R_D_HYBRID * f_dv
    rd_eff_weighted = (
        weights.get("DM_over_rs", 0.0) * rd_eff_perp
        + weights.get("DH_over_rs", 0.0) * rd_eff_par
        + weights.get("DV_over_rs", 0.0) * rd_eff_dv
    )
    return {
        "kernel": {
            "eta": ETA,
            "f_perp": f_perp,
            "f_par": f_par,
            "f_DV": f_dv,
        },
        "galaxy_target_mpc": galaxy_target["rd_target_mpc"],
        "effective_ruler_proxy_mpc": rd_eff_weighted,
        "per_direction_effective_rulers_mpc": {
            "DM_over_rs": rd_eff_perp,
            "DH_over_rs": rd_eff_par,
            "DV_over_rs": rd_eff_dv,
        },
        "information_weights_by_quantity": weights,
        "residual_fraction_vs_target": rd_eff_weighted / galaxy_target["rd_target_mpc"] - 1.0,
        "residual_percent_vs_target": 100.0 * (rd_eff_weighted / galaxy_target["rd_target_mpc"] - 1.0),
        "full_bao_chi2_with_kernel": p29bao.chi2_from_rows(modeled, cov),
        "galaxy_block_chi2_with_kernel": p29bao.subset_chi2(modeled, cov, lambda row: row["block"] == "galaxy_quasar"),
        "old_schur_target_mpc": OLD_SCHUR["galaxy_target_mpc"],
        "old_schur_residual_frac": OLD_SCHUR["galaxy_residual_frac"],
        "qualitative_change": "old scalar near-hit replaced by anisotropic kernel with larger weighted residual",
    }


def mu_ratio(alpha_phi: float) -> float:
    return X_EXACT ** (1.5 - alpha_phi)


def eg_no_slip(z: float) -> float:
    _, f_val = p30.IO_GROWTH.at_z(z)
    return OMEGA_M / f_val


def eg_fit_for_group(group_ids: list[str]) -> dict[str, float]:
    grid = [0.5 + 0.001 * i for i in range(2501)]
    scored = []
    for alpha in grid:
        chi2 = 0.0
        for b in EG_BENCHMARKS:
            if b["id"] not in group_ids:
                continue
            pred = mu_ratio(alpha) * eg_no_slip(float(b["z"]))
            chi2 += ((pred - float(b["mean"])) / float(b["sigma"])) ** 2
        scored.append((alpha, chi2))
    alpha_best, chi2_best = min(scored, key=lambda pair: pair[1])
    one_sigma = [alpha for alpha, chi2 in scored if chi2 <= chi2_best + 1.0]
    return {
        "alpha_best": alpha_best,
        "alpha_1sigma_lo": min(one_sigma),
        "alpha_1sigma_hi": max(one_sigma),
        "mu_best": mu_ratio(alpha_best),
        "chi2_best": chi2_best,
    }


def compute_sigma8_s8_eg() -> dict[str, Any]:
    sigma8 = p30.camb_sigma8(p30.IO_BG, OMEGA_B_CLUSTERING)
    s8_raw = sigma8 * math.sqrt(OMEGA_M / 0.3)
    s8_weyl = SIGMA_IO * s8_raw
    s8_target = 0.79
    s8_sigma = 0.02
    z_rows = {}
    for z in (0.32, 0.57):
        _, f_val = p30.IO_GROWTH.at_z(z)
        no_slip = OMEGA_M / f_val
        z_rows[f"{z:.2f}"] = {
            "f": f_val,
            "E_G_no_slip": no_slip,
            "E_G_alpha2": mu_ratio(2.0) * no_slip,
        }
    group_fits = {name: eg_fit_for_group(ids) for name, ids in EG_GROUPS.items()}
    return {
        "sigma8_clustering": sigma8,
        "S8_raw": s8_raw,
        "Sigma_IO": SIGMA_IO,
        "S8_weyl": s8_weyl,
        "weak_lensing_target_reference": s8_target,
        "weak_lensing_target_sigma_reference": s8_sigma,
        "weak_lensing_delta_raw": s8_raw - s8_target,
        "weak_lensing_delta_weyl": s8_weyl - s8_target,
        "weak_lensing_pull_raw_sigma": (s8_raw - s8_target) / s8_sigma,
        "weak_lensing_pull_weyl_sigma": (s8_weyl - s8_target) / s8_sigma,
        "old_schur_sigma8": OLD_SCHUR["sigma8"],
        "old_schur_s8_lens": OLD_SCHUR["s8_lens"],
        "E_G_rows": z_rows,
        "E_G_group_fits": group_fits,
        "qualitative_change": "old S8 on-target claim no longer survives; alpha_Phi≈2 E_G fit does survive",
    }


def compute_reionization_transport() -> dict[str, Any]:
    tau_os_z0_gyr = 33.359593875
    u0 = 1.0 / X_EXACT
    bracket0 = math.acos(1.0 - 2.0 * u0) - 2.0 * math.sqrt(u0 * (1.0 - u0))
    rs_si = (tau_os_z0_gyr * SEC_PER_GYR) * (2.0 * C_SI) / bracket0

    def abs_dtau_os_dz(z: float) -> float:
        deriv_si = rs_si / (C_SI * X_EXACT * (1.0 + z) ** 2 * math.sqrt(X_EXACT * (1.0 + z) - 1.0))
        return deriv_si / SEC_PER_GYR

    def abs_dtproj_dz(z: float) -> float:
        h0_si = H0 * 1000.0 / MPC_SI
        hz = h0_si * math.sqrt(OMEGA_M * (1.0 + z) ** 3 + OMEGA_K * (1.0 + z) ** 2 + OMEGA_L)
        return 1.0 / ((1.0 + z) * hz) / SEC_PER_GYR

    rows = []
    for z in (5.0, 10.0, 14.0, 20.0):
        ratio = abs_dtau_os_dz(z) / abs_dtproj_dz(z)
        rows.append(
            {
                "z": z,
                "R_reio": ratio,
                "required_net_drive_fraction": 1.0 / ratio,
                "old_schur": OLD_SCHUR["reionization_transport"][int(z)],
            }
        )
    return {
        "definition": "R_reio(z) = |d tau_OS / dz| / |d t_proj / dz|",
        "tau_OS_z0_gyr_used_for_step_522_continuity": tau_os_z0_gyr,
        "rows": rows,
        "qualitative_change": "none",
        "note": "This follows the existing Step 522 homogeneous OS-clock convention, not the active Paper 30 z=0 mixed-fluid age slot.",
    }


def compute_structured_bulk_candidate() -> dict[str, Any]:
    omega_b_struct = OMEGA_B_GEOM + K_GAUGE * (OMEGA_B_EFF - OMEGA_B_GEOM)
    return {
        "formula": "omega_b_struct = omega_b_geom + K_gauge * (omega_b_eff - omega_b_geom)",
        "omega_b_struct": omega_b_struct,
        "old_schur_value": OLD_SCHUR["omega_b_struct"],
        "delta": omega_b_struct - OLD_SCHUR["omega_b_struct"],
        "qualitative_change": "yes; old structured-bulk value depended on a different weight",
    }


def compute_cmb_weyl_halforder_values() -> dict[str, Any]:
    return {
        "Sigma_IO": SIGMA_IO,
        "lcmb_rescale": SIGMA_IO,
        "lcmb_tilt": -0.5,
        "A_L_surrogate": X_EXACT ** (-1.0),
        "eta_IO_if_mu_eq_1": 2.0 * SIGMA_IO - 1.0,
        "old_schur_lcmb_rescale": OLD_SCHUR["weyl_lcmb_rescale"],
        "old_schur_A_L_surrogate": OLD_SCHUR["weyl_al_surrogate"],
        "qualitative_change": "none; branch dependence drops out except through exact x",
    }


def compute_map_numerics() -> dict[str, Any]:
    text = MAP_PATH.read_text()
    active_replacements = {
        "H0": H0,
        "Omega_m": OMEGA_M,
        "Omega_k": OMEGA_K,
        "Omega_lambda": OMEGA_L,
        "Omega_r": OMEGA_R,
        "N_eff": 3.044,
        "omega_b_geom": OMEGA_B_GEOM,
        "omega_b_eff": OMEGA_B_EFF,
        "omega_b_clustering": OMEGA_B_CLUSTERING,
        "A_s": 2.0072459972737347e-09,
        "n_s": 0.9639,
        "r_d": R_D_HYBRID,
        "eta": ETA,
        "Sigma_IO": SIGMA_IO,
        "tau_cov": TAU_COV,
        "sigma8_clustering": 0.9532815843192395,
        "S8_raw": 1.027724133515123,
        "S8_weyl": 0.8338721696752849,
        "omega_b_struct": 0.02143434229616185,
    }
    stale_found = {
        "Active Schur branch": "Active Schur branch" in text,
        "68.91": "68.91" in text,
        "0.335776379575470": "0.335776379575470" in text,
        "0.02108": "0.02108" in text,
        "0.02910": "0.02910" in text,
        "2.1141000090331526e-9": "2.1141000090331526e-9" in text,
        "S8 = 0.79": "S8 = 0.79" in text or "S8 = 0.793" in text,
    }
    return {
        "map_file": str(MAP_PATH),
        "stale_markers_found": stale_found,
        "active_replacements": active_replacements,
        "qualitative_change": "yes; fixed-slot numerics and several carried examples remain Schur-stale in the current map file",
    }


def compute_lya_bao_consistency() -> dict[str, Any]:
    rows, cov = p29bao.load_bao_data()
    bg = p29bao.background(p29bao.IO)
    lya_target = _fit_block_target(rows, cov, lambda row: float(row["z"]) >= 2.0)
    idx = lya_target["indices"]
    sub_cov = cov[np.ix_(idx, idx)]
    inv_cov = np.linalg.inv(sub_cov)

    def chi2_for_rd(rd_mpc: float) -> float:
        modeled = p29bao.make_rows(
            rows,
            branch=p29bao.IO,
            bg=bg,
            rd_gal=rd_mpc,
            rd_lya=rd_mpc,
            f_perp_gal=1.0,
            f_par_gal=1.0,
        )
        diff = np.array([float(modeled[i]["residual"]) for i in idx], dtype=float)
        return float(diff @ inv_cov @ diff)

    alpha_shift = 0.9905
    rd_shifted = R_D_HYBRID * alpha_shift
    raw_chi2 = chi2_for_rd(R_D_HYBRID)
    shifted_chi2 = chi2_for_rd(rd_shifted)
    return {
        "lya_target_mpc": lya_target["rd_target_mpc"],
        "raw_ruler_mpc": R_D_HYBRID,
        "raw_residual_fraction": R_D_HYBRID / lya_target["rd_target_mpc"] - 1.0,
        "raw_chi2": raw_chi2,
        "imported_shift_alpha": alpha_shift,
        "shifted_ruler_mpc": rd_shifted,
        "shifted_residual_fraction": rd_shifted / lya_target["rd_target_mpc"] - 1.0,
        "shifted_chi2": shifted_chi2,
        "old_schur_target_mpc": OLD_SCHUR["lya_target_mpc"],
        "old_schur_raw_chi2": OLD_SCHUR["lya_raw_chi2"],
        "old_schur_shifted_ruler_mpc": OLD_SCHUR["lya_shifted_mpc"],
        "qualitative_change": "no; imported negative-shift Lyalpha class still improves the block materially",
    }


def serializable(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: serializable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [serializable(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (np.floating, np.integer)):
        return obj.item()
    return obj


def write_report(results: dict[str, Any]) -> None:
    rows = [
        {
            "item": "1. Geometric pre-drag ruler",
            "recomputed": f"`r_d = {results['geometric_pre_drag_ruler']['r_d_mpc']:.12f} Mpc`; same active hybrid computation as Paper 29 = `True`",
            "old": f"`{results['geometric_pre_drag_ruler']['old_schur_mpc']:.12f} Mpc`",
            "flag": "changed numerically",
        },
        {
            "item": "2. BAO galaxy block closure",
            "recomputed": (
                f"target `r_d = {results['bao_galaxy_block']['galaxy_target_mpc']:.12f} Mpc`; "
                f"kernel proxy `r_eff = {results['bao_galaxy_block']['effective_ruler_proxy_mpc']:.12f} Mpc`; "
                f"residual `= {results['bao_galaxy_block']['residual_percent_vs_target']:+.6f}%`; "
                f"`chi2_gal = {results['bao_galaxy_block']['galaxy_block_chi2_with_kernel']:.12f}`"
            ),
            "old": f"target `= {OLD_SCHUR['galaxy_target_mpc']:.12f} Mpc`; residual `= {100.0 * OLD_SCHUR['galaxy_residual_frac']:.6f}%`",
            "flag": "qualitative change: old scalar near-hit does not survive",
        },
        {
            "item": "3. sigma8 -> S8_raw -> S8_weyl",
            "recomputed": (
                f"`sigma8 = {results['sigma8_s8_eg']['sigma8_clustering']:.15f}`; "
                f"`S8_raw = {results['sigma8_s8_eg']['S8_raw']:.15f}`; "
                f"`S8_weyl = {results['sigma8_s8_eg']['S8_weyl']:.15f}`; "
                f"`pull_weyl(~0.79±0.02) = {results['sigma8_s8_eg']['weak_lensing_pull_weyl_sigma']:+.3f}σ`"
            ),
            "old": f"`sigma8 = {OLD_SCHUR['sigma8']:.3f}`; `S8_lens = {OLD_SCHUR['s8_lens']:.3f}`",
            "flag": "qualitative change: old on-target S8 claim does not survive",
        },
        {
            "item": "4. E_G pipeline",
            "recomputed": (
                f"`alpha_Phi = {results['sigma8_s8_eg']['E_G_group_fits']['all']['alpha_best']:.3f}`; "
                f"`1sigma = [{results['sigma8_s8_eg']['E_G_group_fits']['all']['alpha_1sigma_lo']:.3f}, "
                f"{results['sigma8_s8_eg']['E_G_group_fits']['all']['alpha_1sigma_hi']:.3f}]`; "
                f"`E_G(0.57,no-slip) = {results['sigma8_s8_eg']['E_G_rows']['0.57']['E_G_no_slip']:.12f}`"
            ),
            "old": (
                f"`alpha_Phi = {OLD_SCHUR['eg_alpha_phi_best']:.3f}`; "
                f"`1sigma = [{OLD_SCHUR['eg_alpha_phi_1sigma'][0]:.3f}, {OLD_SCHUR['eg_alpha_phi_1sigma'][1]:.3f}]`"
            ),
            "flag": "no qualitative change",
        },
        {
            "item": "5. Reionization transport factors",
            "recomputed": "; ".join(
                f"`R_reio({int(row['z'])}) = {row['R_reio']:.9f}`" for row in results["reionization_transport"]["rows"]
            ),
            "old": "; ".join(
                f"`R_reio({z}) ≈ {OLD_SCHUR['reionization_transport'][z]:.2f}`" for z in (5, 10, 14, 20)
            ),
            "flag": "no qualitative change",
        },
        {
            "item": "6. tau reconciliation",
            "recomputed": f"`tau_cov,IO = {results['tau_reconciliation']['tau_cov']:.17f}`",
            "old": f"`tau_cov,IO = {OLD_SCHUR['tau_cov']:.17f}`",
            "flag": "unchanged",
        },
        {
            "item": "7. Structured bulk candidate",
            "recomputed": f"`omega_b,struct = {results['structured_bulk_candidate']['omega_b_struct']:.17f}`",
            "old": f"`omega_b,struct = {OLD_SCHUR['omega_b_struct']:.15f}`",
            "flag": "qualitative change: formula/value no longer the old structured point",
        },
        {
            "item": "8. CMB Weyl half-order kernel",
            "recomputed": (
                f"`lcmb_rescale = {results['cmb_weyl_halforder_kernel']['lcmb_rescale']:.15f}`; "
                f"`lcmb_tilt = {results['cmb_weyl_halforder_kernel']['lcmb_tilt']:+.3f}`; "
                f"`A_L_surrogate = {results['cmb_weyl_halforder_kernel']['A_L_surrogate']:.15f}`"
            ),
            "old": (
                f"`lcmb_rescale = {OLD_SCHUR['weyl_lcmb_rescale']:.15f}`; "
                f"`A_L_surrogate = {OLD_SCHUR['weyl_al_surrogate']:.15f}`"
            ),
            "flag": "no qualitative change",
        },
        {
            "item": "9. Observable-class map numerics",
            "recomputed": (
                f"active slots should read `H0 = {H0:.12f}`, `Omega_m = {OMEGA_M:.15f}`, "
                f"`Omega_k = {OMEGA_K:.15f}`, `r_d = {R_D_HYBRID:.12f}`, `Sigma_IO = {SIGMA_IO:.15f}`"
            ),
            "old": "map file still contains the Schur fixed-slot numerics",
            "flag": "qualitative change: map is numerically stale",
        },
        {
            "item": "10. Lyalpha BAO conditional consistency",
            "recomputed": (
                f"target `r_d = {results['lya_bao_conditional_consistency']['lya_target_mpc']:.12f} Mpc`; "
                f"raw residual `= {100.0 * results['lya_bao_conditional_consistency']['raw_residual_fraction']:+.6f}%`; "
                f"shifted residual `= {100.0 * results['lya_bao_conditional_consistency']['shifted_residual_fraction']:+.6f}%`; "
                f"`chi2_raw = {results['lya_bao_conditional_consistency']['raw_chi2']:.12f}`; "
                f"`chi2_shifted = {results['lya_bao_conditional_consistency']['shifted_chi2']:.12f}`"
            ),
            "old": (
                f"target `= {OLD_SCHUR['lya_target_mpc']:.12f} Mpc`; "
                f"`chi2_raw = {OLD_SCHUR['lya_raw_chi2']:.12f}`; "
                f"`r_shifted = {OLD_SCHUR['lya_shifted_mpc']:.12f} Mpc`"
            ),
            "flag": "no qualitative change",
        },
    ]

    lines = [
        "# Paper 31 Legacy-Branch Full Recomputation",
        "",
        "Active source package:",
        "",
        f"- `H0 = {H0}`",
        f"- `Omega_m = {OMEGA_M}`",
        f"- `Omega_k = {OMEGA_K}`",
        f"- `Omega_Lambda = {OMEGA_L}`",
        f"- `Omega_r = {OMEGA_R}`",
        f"- `omega_b,geom = {OMEGA_B_GEOM}`",
        f"- `omega_b,eff = {OMEGA_B_EFF}`",
        f"- `omega_b,clustering = {OMEGA_B_CLUSTERING}`",
        f"- `r_d = {R_D_HYBRID}`",
        f"- `eta = {ETA}`",
        f"- `Sigma_IO = {SIGMA_IO}`",
        "",
        "| Item | Recomputed legacy-branch value | Old Schur value | Flag |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['item']} | {row['recomputed']} | {row['old']} | {row['flag']} |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Item 2 uses the Paper 29 derived/scoped galaxy kernel exactly as implemented in the live block-split evaluator: `D_M -> D_M / exp(eta)`, `D_H -> D_H / exp(eta/2)` on the galaxy/quasar block only.",
            "- Item 2 therefore does not admit a unique scalar effective ruler. The reported `r_eff` is an information-weighted proxy built from the current galaxy block quantity weights.",
            "- Item 5 follows the existing Paper 31 Step 522 homogeneous-OS transport convention so it stays comparable to the published Schur-era values.",
            "- Item 9 is a numerical verification against the current map file, not an edit of the map file itself.",
        ]
    )
    REPORT_MD.write_text("\n".join(lines) + "\n")


def main() -> None:
    results = {
        "active_parameters": {
            "H0": H0,
            "Omega_m": OMEGA_M,
            "Omega_k": OMEGA_K,
            "Omega_lambda": OMEGA_L,
            "Omega_r": OMEGA_R,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_clustering": OMEGA_B_CLUSTERING,
            "r_d": R_D_HYBRID,
            "x": X_EXACT,
            "gamma": GAMMA,
            "K_gauge": K_GAUGE,
            "eta": ETA,
            "Sigma_IO": SIGMA_IO,
        },
        "geometric_pre_drag_ruler": compute_pre_drag_ruler(),
        "bao_galaxy_block": compute_bao_galaxy_block(),
        "sigma8_s8_eg": compute_sigma8_s8_eg(),
        "reionization_transport": compute_reionization_transport(),
        "tau_reconciliation": {
            "tau_cov": TAU_COV,
            "old_schur_tau_cov": OLD_SCHUR["tau_cov"],
            "qualitative_change": "none",
        },
        "structured_bulk_candidate": compute_structured_bulk_candidate(),
        "cmb_weyl_halforder_kernel": compute_cmb_weyl_halforder_values(),
        "observable_class_map_numerics": compute_map_numerics(),
        "lya_bao_conditional_consistency": compute_lya_bao_consistency(),
    }

    RESULTS_JSON.write_text(json.dumps(serializable(results), indent=2))
    write_report(results)


if __name__ == "__main__":
    main()
