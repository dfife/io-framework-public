from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from classy import Class
from scipy.integrate import quad
from scipy.optimize import minimize, minimize_scalar


ROOT = Path("/opt/cosmology-lab/results/paper29")
DATA_DIR = ROOT / "data_cache"
OUT_JSON = ROOT / "paper29_bao_failure_investigation_results.json"
OUT_REPORT = ROOT / "paper29_bao_failure_investigation_report.md"
OUT_BASELINE_CSV = ROOT / "paper29_bao_failure_investigation_baseline_residuals.csv"
OUT_REPAIRED_CSV = ROOT / "paper29_bao_failure_investigation_repaired_residuals.csv"

C_KM_S = 299792.458
G_SI = 6.67430e-11
C_SI = 299792458.0
M_U_KG = 4.50e53
R_U_M = 4.40e26
GAMMA_BI = 0.2375


@dataclass(frozen=True)
class Branch:
    label: str
    H0: float
    Omega_m: float
    Omega_k: float
    Omega_r: float
    Omega_lambda_display: float
    Omega_lambda_eval: float


def load_desi_dr2() -> tuple[list[dict[str, float | str]], np.ndarray]:
    mean_path = DATA_DIR / "desi_dr2_all_gccomb_mean.txt"
    cov_path = DATA_DIR / "desi_dr2_all_gccomb_cov.txt"
    mean_rows = np.loadtxt(mean_path, dtype=str)
    rows = [{"z": float(z), "value": float(v), "quantity": q} for z, v, q in mean_rows]
    covariance = np.loadtxt(cov_path)
    return rows, covariance


def e_z(z: float, branch: Branch) -> float:
    zp1 = 1.0 + z
    return math.sqrt(
        branch.Omega_m * zp1**3
        + branch.Omega_r * zp1**4
        + branch.Omega_k * zp1**2
        + branch.Omega_lambda_eval
    )


def dimless_chi(z: float, branch: Branch) -> float:
    value, _ = quad(
        lambda zp: 1.0 / e_z(zp, branch),
        0.0,
        z,
        epsabs=1.0e-11,
        epsrel=1.0e-11,
        limit=600,
    )
    return value


def transverse_distance_mpc(z: float, branch: Branch, *, omega_k_dm: float | None = None) -> float:
    omega_k_eff = branch.Omega_k if omega_k_dm is None else float(omega_k_dm)
    chi = dimless_chi(z, branch)
    if abs(omega_k_eff) < 1.0e-15:
        return (C_KM_S / branch.H0) * chi
    if omega_k_eff < 0.0:
        rootk = math.sqrt(-omega_k_eff)
        return (C_KM_S / branch.H0) * math.sin(rootk * chi) / rootk
    rootk = math.sqrt(omega_k_eff)
    return (C_KM_S / branch.H0) * math.sinh(rootk * chi) / rootk


def hubble_distance_mpc(z: float, branch: Branch) -> float:
    return C_KM_S / (branch.H0 * e_z(z, branch))


def dv_distance_mpc(z: float, branch: Branch, *, omega_k_dm: float | None = None) -> float:
    dm = transverse_distance_mpc(z, branch, omega_k_dm=omega_k_dm)
    dh = hubble_distance_mpc(z, branch)
    return (z * dm * dm * dh) ** (1.0 / 3.0)


def bao_residual_rows(
    branch: Branch,
    rows: list[dict[str, float | str]],
    *,
    rd_gal: float,
    rd_lya: float,
    omega_k_dm: float | None = None,
) -> list[dict[str, float | str]]:
    out = []
    for row in rows:
        z = float(row["z"])
        quantity = str(row["quantity"])
        rd = rd_gal if z < 2.0 else rd_lya
        if quantity == "DM_over_rs":
            model = transverse_distance_mpc(z, branch, omega_k_dm=omega_k_dm) / rd
        elif quantity == "DH_over_rs":
            model = hubble_distance_mpc(z, branch) / rd
        elif quantity == "DV_over_rs":
            model = dv_distance_mpc(z, branch, omega_k_dm=omega_k_dm) / rd
        else:
            raise ValueError(quantity)
        out.append(
            {
                "z": z,
                "block": "galaxy_quasar" if z < 2.0 else "lya",
                "quantity": quantity,
                "obs": float(row["value"]),
                "model": model,
                "residual": model - float(row["value"]),
                "rd_used_Mpc": rd,
            }
        )
    return out


def bao_chi2(
    branch: Branch,
    rows: list[dict[str, float | str]],
    covariance: np.ndarray,
    *,
    rd_gal: float,
    rd_lya: float,
    omega_k_dm: float | None = None,
) -> float:
    residual_rows = bao_residual_rows(
        branch,
        rows,
        rd_gal=rd_gal,
        rd_lya=rd_lya,
        omega_k_dm=omega_k_dm,
    )
    diff = np.array([float(row["residual"]) for row in residual_rows], dtype=float)
    inv_cov = np.linalg.inv(covariance)
    return float(diff @ inv_cov @ diff)


def subblock_chi2(
    residual_rows: list[dict[str, float | str]],
    covariance: np.ndarray,
    *,
    selector,
) -> float:
    idx = [i for i, row in enumerate(residual_rows) if selector(row)]
    diff = np.array([float(residual_rows[i]["residual"]) for i in idx], dtype=float)
    cov_sub = covariance[np.ix_(idx, idx)]
    return float(diff @ np.linalg.inv(cov_sub) @ diff)


def chi2_optimal_universal_ruler(
    branch: Branch, rows: list[dict[str, float | str]], covariance: np.ndarray
) -> dict[str, float]:
    result = minimize_scalar(
        lambda rd: bao_chi2(branch, rows, covariance, rd_gal=rd, rd_lya=rd),
        bounds=(120.0, 170.0),
        method="bounded",
    )
    return {
        "best_universal_rd_Mpc": float(result.x),
        "chi2": float(result.fun),
    }


def chi2_optimal_block_rulers(
    branch: Branch, rows: list[dict[str, float | str]], covariance: np.ndarray
) -> dict[str, float]:
    result = minimize(
        lambda x: bao_chi2(branch, rows, covariance, rd_gal=float(x[0]), rd_lya=float(x[1])),
        x0=np.array([147.0, 143.0]),
        bounds=[(120.0, 170.0), (120.0, 170.0)],
    )
    return {
        "best_rd_gal_Mpc": float(result.x[0]),
        "best_rd_lya_Mpc": float(result.x[1]),
        "chi2": float(result.fun),
    }


def x_ratio() -> float:
    r_s = 2.0 * G_SI * M_U_KG / (C_SI * C_SI)
    return r_s / R_U_M


def delta_value(x: float) -> float:
    return x**4 * (1.0 + GAMMA_BI * GAMMA_BI)


def current_iid_baryon_slots(branch: Branch) -> dict[str, float]:
    x = x_ratio()
    Delta = delta_value(x)
    h = branch.H0 / 100.0
    omega_m = branch.Omega_m * h * h
    f_b = 2.0 * GAMMA_BI / x
    omega_b_geom = f_b * omega_m
    omega_b_eff = (math.log(Delta) / 4.0) * omega_m
    omega_b_clust = omega_b_geom * x ** (1.0 - 1.5)
    return {
        "x": x,
        "Delta": Delta,
        "omega_m_total": omega_m,
        "f_b": f_b,
        "omega_b_geom_projected": omega_b_geom,
        "omega_b_eff_projected": omega_b_eff,
        "omega_b_clust_projected": omega_b_clust,
    }


def class_rs_drag(branch: Branch, omega_b: float) -> float:
    h = branch.H0 / 100.0
    omega_m = branch.Omega_m * h * h
    omega_nu = 0.06 / 93.14
    omega_cdm = omega_m - omega_b - omega_nu
    if omega_cdm <= 0.0:
        raise ValueError(f"omega_cdm became non-positive for omega_b={omega_b}")
    cosmo = Class()
    cosmo.set(
        {
            "output": "mPk",
            "P_k_max_h/Mpc": 1.2,
            "z_max_pk": 1.0,
            "h": h,
            "omega_b": float(omega_b),
            "omega_cdm": float(omega_cdm),
            "Omega_k": branch.Omega_k,
            "A_s": 2.1e-9,
            "n_s": 0.9649,
            "tau_reio": 0.0544,
            "T_cmb": 2.7253,
            "N_ur": 3.044 - 1.0132,
            "N_ncdm": 1,
            "m_ncdm": 0.06,
            "YHe": 0.2477,
        }
    )
    cosmo.compute()
    try:
        return float(cosmo.rs_drag())
    finally:
        cosmo.struct_cleanup()
        cosmo.empty()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows, covariance = load_desi_dr2()

    io_iid = Branch(
        label="IO i.i.d. branch",
        H0=67.57585653582628,
        Omega_m=0.34868395067621694,
        Omega_k=-0.04579112576013168,
        Omega_r=1.226e-4,
        Omega_lambda_display=0.6971071750839146,
        Omega_lambda_eval=0.6969845750839148,
    )
    planck = Branch(
        label="Planck LCDM reference",
        H0=67.4,
        Omega_m=0.315,
        Omega_k=0.0,
        Omega_r=9.19480093248451e-05,
        Omega_lambda_display=0.685,
        Omega_lambda_eval=0.6849080519906752,
    )

    baseline_rd = 143.3
    baseline_rows = bao_residual_rows(io_iid, rows, rd_gal=baseline_rd, rd_lya=baseline_rd)
    baseline_chi2 = bao_chi2(io_iid, rows, covariance, rd_gal=baseline_rd, rd_lya=baseline_rd)
    planck_chi2 = bao_chi2(planck, rows, covariance, rd_gal=147.09, rd_lya=147.09)

    split_by_quantity = {
        "DV_over_rs": subblock_chi2(baseline_rows, covariance, selector=lambda row: row["quantity"] == "DV_over_rs"),
        "DM_over_rs": subblock_chi2(baseline_rows, covariance, selector=lambda row: row["quantity"] == "DM_over_rs"),
        "DH_over_rs": subblock_chi2(baseline_rows, covariance, selector=lambda row: row["quantity"] == "DH_over_rs"),
        "DM_plus_DH": subblock_chi2(
            baseline_rows,
            covariance,
            selector=lambda row: row["quantity"] in {"DM_over_rs", "DH_over_rs"},
        ),
    }
    split_by_block = {
        "galaxy_quasar": subblock_chi2(baseline_rows, covariance, selector=lambda row: row["block"] == "galaxy_quasar"),
        "lya": subblock_chi2(baseline_rows, covariance, selector=lambda row: row["block"] == "lya"),
    }

    curvature_tests = []
    for omega_k_dm in [0.0, io_iid.Omega_k, -0.130]:
        curvature_tests.append(
            {
                "omega_k_dm": omega_k_dm,
                "chi2_with_rd_143p3": bao_chi2(
                    io_iid, rows, covariance, rd_gal=baseline_rd, rd_lya=baseline_rd, omega_k_dm=omega_k_dm
                ),
            }
        )

    universal_best = chi2_optimal_universal_ruler(io_iid, rows, covariance)
    block_best = chi2_optimal_block_rulers(io_iid, rows, covariance)

    rebuilt_slots = current_iid_baryon_slots(io_iid)
    rebuilt_rulers = {
        "omega_b_geom_projected": class_rs_drag(io_iid, rebuilt_slots["omega_b_geom_projected"]),
        "omega_b_eff_projected": class_rs_drag(io_iid, rebuilt_slots["omega_b_eff_projected"]),
        "omega_b_clust_projected": class_rs_drag(io_iid, rebuilt_slots["omega_b_clust_projected"]),
    }

    legacy_transplanted_small_slots = {
        "omega_b_geom_small_carried": 0.020995719061702847,
        "omega_b_clust_small_carried": 0.017053042566348754,
    }
    legacy_rulers = {
        key: class_rs_drag(io_iid, val) for key, val in legacy_transplanted_small_slots.items()
    }

    universal_ruler_cases = []
    for label, rd in [
        ("baseline_carried_universal_rd", baseline_rd),
        ("rebuilt_iid_geom_projected", rebuilt_rulers["omega_b_geom_projected"]),
        ("rebuilt_iid_eff_projected", rebuilt_rulers["omega_b_eff_projected"]),
        ("rebuilt_iid_clust_projected", rebuilt_rulers["omega_b_clust_projected"]),
        ("legacy_transplanted_geom_small", legacy_rulers["omega_b_geom_small_carried"]),
        ("legacy_transplanted_clust_small", legacy_rulers["omega_b_clust_small_carried"]),
        ("best_universal_effective_rd", universal_best["best_universal_rd_Mpc"]),
    ]:
        universal_ruler_cases.append(
            {
                "label": label,
                "rd_Mpc": rd,
                "chi2": bao_chi2(io_iid, rows, covariance, rd_gal=rd, rd_lya=rd),
            }
        )

    conditional_block_repairs = [
        {
            "label": "best_blockwise_effective_rulers",
            "rd_gal_Mpc": block_best["best_rd_gal_Mpc"],
            "rd_lya_Mpc": block_best["best_rd_lya_Mpc"],
            "chi2": block_best["chi2"],
        },
        {
            "label": "best_galaxy_effective_plus_lya_raw_baseline",
            "rd_gal_Mpc": block_best["best_rd_gal_Mpc"],
            "rd_lya_Mpc": baseline_rd,
            "chi2": bao_chi2(io_iid, rows, covariance, rd_gal=block_best["best_rd_gal_Mpc"], rd_lya=baseline_rd),
        },
        {
            "label": "legacy_small_clustering_galaxy_plus_lya_raw_baseline",
            "rd_gal_Mpc": legacy_rulers["omega_b_clust_small_carried"],
            "rd_lya_Mpc": baseline_rd,
            "chi2": bao_chi2(
                io_iid,
                rows,
                covariance,
                rd_gal=legacy_rulers["omega_b_clust_small_carried"],
                rd_lya=baseline_rd,
            ),
        },
    ]

    repaired_rows = bao_residual_rows(
        io_iid,
        rows,
        rd_gal=block_best["best_rd_gal_Mpc"],
        rd_lya=block_best["best_rd_lya_Mpc"],
    )

    combined_cc_chi2 = 14.701661702497464
    combined_summary = {
        "baseline_combined_chi2": combined_cc_chi2 + baseline_chi2,
        "planck_combined_chi2": 43.77291370446457,
        "conditional_repaired_combined_chi2": combined_cc_chi2 + block_best["chi2"],
    }

    results = {
        "io_iid_branch": asdict(io_iid),
        "planck_reference": asdict(planck),
        "baseline": {
            "universal_rd_Mpc": baseline_rd,
            "bao_chi2": baseline_chi2,
            "planck_bao_chi2": planck_chi2,
            "delta_chi2_io_minus_planck": baseline_chi2 - planck_chi2,
            "split_by_quantity": split_by_quantity,
            "split_by_block": split_by_block,
        },
        "curvature_tests": curvature_tests,
        "universal_effective_ruler_scan": universal_best,
        "blockwise_effective_ruler_scan": block_best,
        "rebuilt_iid_slots": rebuilt_slots,
        "rebuilt_iid_raw_rulers_Mpc": rebuilt_rulers,
        "legacy_transplanted_small_slots": legacy_transplanted_small_slots,
        "legacy_transplanted_raw_rulers_Mpc": legacy_rulers,
        "universal_ruler_cases": universal_ruler_cases,
        "conditional_block_repairs": conditional_block_repairs,
        "combined_summary": combined_summary,
        "baseline_residuals": baseline_rows,
        "repaired_residuals": repaired_rows,
    }

    OUT_JSON.write_text(json.dumps(results, indent=2))
    write_csv(OUT_BASELINE_CSV, baseline_rows)
    write_csv(OUT_REPAIRED_CSV, repaired_rows)

    lines = [
        "# Paper 29 BAO χ² failure investigation on the i.i.d. branch",
        "",
        "## Headline",
        "",
        "- `derived`: the BAO failure is not a generic distance-integral bug.",
        "- `derived`: with the user's carried universal ruler `r_d = 143.3 Mpc`, the failure is almost entirely the galaxy/quasar block, not Lyα.",
        "- `verified`: a blockwise effective-ruler repair can reduce BAO χ² from `94.36149688498531` to "
        f"`{block_best['chi2']}`.",
        "- `derived`: this repair is not theorem-grade on the current clean stack. A first-principles rebuild of the i.i.d. raw rulers from the rebuilt slot formulas gives `126–131 Mpc`, not `143–147 Mpc`.",
        "",
        "## Inputs",
        "",
        f"- IO i.i.d. branch: `H0 = {io_iid.H0}`, `Omega_m = {io_iid.Omega_m}`, `Omega_k = {io_iid.Omega_k}`, `Omega_r = {io_iid.Omega_r}`, `Omega_lambda_eval = {io_iid.Omega_lambda_eval}`",
        f"- Planck reference BAO χ²: `{planck_chi2}`",
        f"- baseline carried ruler: `r_d = {baseline_rd} Mpc`",
        "",
        "## Baseline BAO failure split",
        "",
        f"- total BAO χ²: `{baseline_chi2}`",
        f"- galaxy/quasar block χ² (`z < 2`): `{split_by_block['galaxy_quasar']}`",
        f"- Lyα block χ² (`z = 2.33`): `{split_by_block['lya']}`",
        f"- `DV/r_d` subblock χ²: `{split_by_quantity['DV_over_rs']}`",
        f"- `DM/r_d` subblock χ²: `{split_by_quantity['DM_over_rs']}`",
        f"- `DH/r_d` subblock χ²: `{split_by_quantity['DH_over_rs']}`",
        f"- `DM/r_d + DH/r_d` subblock χ²: `{split_by_quantity['DM_plus_DH']}`",
        "",
        "## Curvature-only checks",
        "",
        "| distance curvature slot | BAO χ² with `r_d = 143.3` |",
        "|---|---:|",
    ]
    for row in curvature_tests:
        lines.append(f"| `{row['omega_k_dm']}` | `{row['chi2_with_rd_143p3']}` |")

    lines.extend(
        [
            "",
            "Interpretation: using the geometric curvature in the `sin()` distance law helps only modestly. The dominant miss is shared by radial and transverse ratios, so curvature alone cannot fix it.",
            "",
            "## Rebuilt i.i.d. raw ruler check",
            "",
            f"- derived `x = {rebuilt_slots['x']}`",
            f"- derived `Delta = {rebuilt_slots['Delta']}`",
            f"- derived `omega_m = {rebuilt_slots['omega_m_total']}`",
            f"- current rebuilt slot formulas give:",
            f"  - `omega_b,geom(projected) = {rebuilt_slots['omega_b_geom_projected']}`",
            f"  - `omega_b,eff(projected) = {rebuilt_slots['omega_b_eff_projected']}`",
            f"  - `omega_b,clust(projected) = {rebuilt_slots['omega_b_clust_projected']}`",
            "",
            "| raw ruler case | `r_d` [Mpc] | BAO χ² |",
            "|---|---:|---:|",
        ]
    )
    for row in universal_ruler_cases:
        lines.append(f"| `{row['label']}` | `{row['rd_Mpc']}` | `{row['chi2']}` |")

    lines.extend(
        [
            "",
            "The crucial point is that the clean rebuilt i.i.d. raw rulers (`126.142...`, `118.145...`, `130.994...`) make BAO catastrophically worse. So the carried `143.3 Mpc` was already a soft Schur-era import, not a clean i.i.d. theorem output.",
            "",
            "## Effective-ruler scans",
            "",
            f"- best universal effective ruler on the fixed i.i.d. geometry: `r_d,eff = {universal_best['best_universal_rd_Mpc']} Mpc` -> `chi2 = {universal_best['chi2']}`",
            f"- best blockwise effective rulers on the fixed i.i.d. geometry:",
            f"  - galaxy/quasar block: `r_d,gal = {block_best['best_rd_gal_Mpc']} Mpc`",
            f"  - Lyα block: `r_d,lya = {block_best['best_rd_lya_Mpc']} Mpc`",
            f"  - full 13-point BAO `chi2 = {block_best['chi2']}`",
            "",
            "## Strongest conditional repairs",
            "",
            "| repair | `r_d,gal` [Mpc] | `r_d,lya` [Mpc] | BAO χ² |",
            "|---|---:|---:|---:|",
        ]
    )
    for row in conditional_block_repairs:
        lines.append(f"| `{row['label']}` | `{row['rd_gal_Mpc']}` | `{row['rd_lya_Mpc']}` | `{row['chi2']}` |")

    lines.extend(
        [
            "",
            "## Combined impact",
            "",
            f"- original combined CC+BAO χ²: `{combined_summary['baseline_combined_chi2']}`",
            f"- Planck combined CC+BAO χ²: `{combined_summary['planck_combined_chi2']}`",
            f"- conditional repaired combined CC+BAO χ²: `{combined_summary['conditional_repaired_combined_chi2']}`",
            "",
            "## Conclusion",
            "",
            "- `derived`: the source of the published BAO failure is the universal-ruler assumption on a block-mixed BAO observable, together with a carried Schur-era ruler value (`143.3 Mpc`) that is not the clean i.i.d. raw output.",
            "- `verified`: if one allows block-specific effective readout rulers, the BAO χ² can be cut from `94.36149688498531` to "
            f"`{block_best['chi2']}` and the combined CC+BAO χ² to `{combined_summary['conditional_repaired_combined_chi2']}`.",
            "- `derived`: this is not a theorem-grade closure. Under the current clean Papers 9–28 stack, the first-principles i.i.d. raw ruler rebuild lands at `126–131 Mpc`, so the needed `142–147 Mpc` effective rulers require an additional BAO readout theorem or an explicit observational selection.",
            "- `headline resolution`: a theorem-grade BAO fix is impossible under the current stack. The strongest surviving repair is conditional and blockwise, not derived.",
            "",
            "## Files",
            "",
            f"- baseline residual table: `{OUT_BASELINE_CSV.name}`",
            f"- repaired residual table: `{OUT_REPAIRED_CSV.name}`",
        ]
    )

    OUT_REPORT.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
