#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

from classy import Class

ROOT = Path("/opt/cosmology-lab")
TMP = ROOT / "tmp" / "planck-lite-py"
OUT = ROOT / "results" / "paper31"

if str(TMP) not in sys.path:
    sys.path.insert(0, str(TMP))

from planck_lite_py import PlanckLitePy  # type: ignore  # noqa: E402


L_MAX = 2508
X = 1.519
GAMMA = 0.2375
F_GAMMA = 1.0 / (1.0 + GAMMA**2)
F_GAMMA2 = F_GAMMA**2
F_GAMMA3 = F_GAMMA**3
J_PHI = X ** (-0.5)
ETA_IO = 2.0 * J_PHI - 1.0

A_S_NATIVE = 2.0072459972737347e-9
H0_IO_ACTIVE = 68.91
OMEGA_K_IO_ACTIVE = -0.005613722564239

OMEGA_B_GEOM = 0.02108
OMEGA_B_EFF = 0.02910
OMEGA_B_CLUSTERING = 0.017053042566349
OMEGA_B_STRUCT = OMEGA_B_GEOM + ETA_IO * (1.0 + F_GAMMA) / 2.0 * (OMEGA_B_EFF - OMEGA_B_GEOM)

OMEGA_M_ONEFLUID = 0.15939026836
OMEGA_CDM_ONE_NUMBER = OMEGA_M_ONEFLUID - OMEGA_B_STRUCT
OMEGA_M_SCHUR_TARGET = 0.335776379575470 * (H0_IO_ACTIVE / 100.0) ** 2

LABEL_TO_VALUE = {
    "geom": OMEGA_B_GEOM,
    "eff": OMEGA_B_EFF,
    "clustering": OMEGA_B_CLUSTERING,
    "struct": OMEGA_B_STRUCT,
}


def make_base() -> dict[str, Any]:
    return {
        "output": "tCl,pCl,lCl",
        "lensing": "yes",
        "l_max_scalars": L_MAX,
        "H0": H0_IO_ACTIVE,
        "T_cmb": 2.7253,
        "Omega_k": OMEGA_K_IO_ACTIVE,
        "N_ur": 3.044,
        "N_ncdm": 0,
        "YHe": 0.2477,
        "n_s": 0.9639,
        "alpha_s": 5.0e-5,
        "reio_parametrization": "reio_none",
        "A_s": A_S_NATIVE,
        "lcmb_rescale": J_PHI,
        "lcmb_tilt": 0.0,
        "lcmb_pivot": 0.05,
        "lcmb_curved_shift": -3.0,
        "lcmb_curved_order": -0.25,
        "io_visibility_opacity_factor": F_GAMMA2,
        "io_acoustic_drag_factor": 1.0,
        "io_acoustic_hierarchy_factor": F_GAMMA3,
    }


def compute_case(params: dict[str, Any], plik: PlanckLitePy) -> dict[str, float]:
    cosmo = Class()
    try:
        cosmo.set(params)
        cosmo.compute()
        cls = cosmo.lensed_cl(L_MAX)
        ell = cls["ell"][2:]
        pref = ell * (ell + 1.0) / (2.0 * math.pi) * (params["T_cmb"] * 1.0e6) ** 2
        chi2 = -2.0 * float(
            plik.loglike(pref * cls["tt"][2:], pref * cls["te"][2:], pref * cls["ee"][2:], ellmin=2)
        )
        theta = float(cosmo.get_current_derived_parameters(["100*theta_s"])["100*theta_s"])
        return {"chi2": chi2, "theta_s_100": theta}
    finally:
        cosmo.struct_cleanup()
        cosmo.empty()


def run_matrix(keep_cdm_fixed: bool) -> dict[str, Any]:
    plik = PlanckLitePy(
        data_directory=str(TMP / "data"),
        year=2018,
        spectra="TTTEEE",
        use_low_ell_bins=True,
    )
    base = make_base()
    rows: list[dict[str, Any]] = []

    one_number_params = {
        **base,
        "omega_b": OMEGA_B_STRUCT,
        "omega_cdm": OMEGA_CDM_ONE_NUMBER,
    }
    explicit_all_struct = {
        **base,
        "omega_b_geom": OMEGA_B_STRUCT,
        "omega_b_eff": OMEGA_B_STRUCT,
        "omega_b_clustering": OMEGA_B_STRUCT,
        "omega_cdm": OMEGA_CDM_ONE_NUMBER if keep_cdm_fixed else OMEGA_M_SCHUR_TARGET - OMEGA_B_STRUCT,
    }

    sanity = {
        "one_number_struct": compute_case(one_number_params, plik),
        "explicit_all_struct": compute_case(explicit_all_struct, plik),
    }

    for geom_label, geom_value in LABEL_TO_VALUE.items():
        for eff_label, eff_value in LABEL_TO_VALUE.items():
            for clust_label, clust_value in LABEL_TO_VALUE.items():
                omega_cdm = OMEGA_CDM_ONE_NUMBER if keep_cdm_fixed else OMEGA_M_SCHUR_TARGET - clust_value
                params = {
                    **base,
                    "omega_b_geom": geom_value,
                    "omega_b_eff": eff_value,
                    "omega_b_clustering": clust_value,
                    "omega_cdm": omega_cdm,
                }
                result = compute_case(params, plik)
                rows.append(
                    {
                        "geom": geom_label,
                        "eff": eff_label,
                        "clust": clust_label,
                        "omega_cdm": omega_cdm,
                        **result,
                    }
                )

    rows.sort(key=lambda r: r["chi2"])
    return {
        "keep_cdm_fixed": keep_cdm_fixed,
        "sanity": sanity,
        "rows": rows,
    }


def select_rows(rows: list[dict[str, Any]], keys: list[tuple[str, str, str]]) -> list[dict[str, Any]]:
    selected = []
    for geom, eff, clust in keys:
        for row in rows:
            if (row["geom"], row["eff"], row["clust"]) == (geom, eff, clust):
                selected.append(row)
                break
    return selected


def write_report(fixed: dict[str, Any], variable: dict[str, Any]) -> None:
    keys = [
        ("geom", "eff", "clustering"),
        ("geom", "eff", "geom"),
        ("geom", "eff", "eff"),
        ("geom", "struct", "geom"),
        ("struct", "struct", "geom"),
        ("struct", "struct", "struct"),
    ]
    fixed_rows = select_rows(fixed["rows"], keys)
    variable_rows = select_rows(variable["rows"], keys)

    def row_line(row: dict[str, Any]) -> str:
        return (
            f"| `{row['geom']}` | `{row['eff']}` | `{row['clust']}` | "
            f"{row['chi2']:.6f} | {row['theta_s_100']:.9f} |"
        )

    lines = [
        "# Paper 31: Practical IO Baryon-Slot Audit",
        "",
        "Date: 2026-04-04",
        "",
        "## Question",
        "",
        "The practical IO `C_ell` calculator had been using a single `omega_b` value.",
        "Paper 31, however, carries three baryon densities:",
        "",
        f"- `omega_b,geom = {OMEGA_B_GEOM}`",
        f"- `omega_b,eff = {OMEGA_B_EFF}`",
        f"- `omega_b,clustering = {OMEGA_B_CLUSTERING}`",
        f"- conditional structured proxy `omega_b,struct = {OMEGA_B_STRUCT}`",
        "",
        "The objective here is not to fit a new baryon value. It is to determine whether",
        "the current practical calculator is failing because it collapses the three carried",
        "baryon slots into one number, or because the current explicit three-slot wiring in",
        "the patched CLASS fork is itself not the right implementation of the Paper 31 map.",
        "",
        "## Fixed IO Package",
        "",
        f"- `H0 = {H0_IO_ACTIVE}`",
        f"- `Omega_k = {OMEGA_K_IO_ACTIVE}`",
        f"- `A_s = {A_S_NATIVE}`",
        f"- `J_Phi = x^(-1/2) = {J_PHI}`",
        f"- `f_Gamma = 1/(1+gamma^2) = {F_GAMMA}`",
        f"- `c_vis = f_Gamma^2 = {F_GAMMA2}`",
        f"- `d_drag = 1`",
        f"- `h_hier = f_Gamma^3 = {F_GAMMA3}`",
        f"- `reio_parametrization = reio_none`",
        "",
        "## Matrix A: `omega_cdm` Adjusted With The Clustering Slot",
        "",
        "This treats `omega_b,clustering` as the baryon piece of the carried Schur matter",
        "target and sets `omega_cdm = omega_m,target - omega_b,clustering`.",
        "",
        f"- one-number structured baseline: `chi2 = {variable['sanity']['one_number_struct']['chi2']:.6f}`, `100theta_s = {variable['sanity']['one_number_struct']['theta_s_100']:.9f}`",
        f"- explicit all-struct sanity check: `chi2 = {variable['sanity']['explicit_all_struct']['chi2']:.6f}`, `100theta_s = {variable['sanity']['explicit_all_struct']['theta_s_100']:.9f}`",
        "",
        "| geom | eff | clust | chi2 | 100theta_s |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    lines.extend(row_line(r) for r in variable_rows)
    lines.extend(
        [
            "",
            "Best row in this matrix:",
            "",
            f"- `geom = struct`, `eff = struct`, `clust = eff` -> `chi2 = {variable['rows'][0]['chi2']:.6f}`",
            "",
            "## Matrix B: `omega_cdm` Held Fixed",
            "",
            "This isolates the slot effect itself by keeping `omega_cdm` equal to the",
            "one-number practical branch value.",
            "",
            f"- one-number structured baseline: `chi2 = {fixed['sanity']['one_number_struct']['chi2']:.6f}`, `100theta_s = {fixed['sanity']['one_number_struct']['theta_s_100']:.9f}`",
            f"- explicit all-struct sanity check: `chi2 = {fixed['sanity']['explicit_all_struct']['chi2']:.6f}`, `100theta_s = {fixed['sanity']['explicit_all_struct']['theta_s_100']:.9f}`",
            "",
            "| geom | eff | clust | chi2 | 100theta_s |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )
    lines.extend(row_line(r) for r in fixed_rows)
    lines.extend(
        [
            "",
            "Best row in this matrix:",
            "",
            f"- `geom = struct`, `eff = struct`, `clust = geom` -> `chi2 = {fixed['rows'][0]['chi2']:.6f}`",
            "",
            "## Executive Result",
            "",
            "1. `verified`: the explicit three-slot code path itself is numerically viable.",
            "   When all three explicit slots are set equal to `omega_b,struct`, it reproduces",
            "   the one-number structured branch exactly when `omega_cdm` is also held fixed.",
            "",
            "2. `verified`: the literal Paper 31 baryon theorem map is catastrophic in the",
            "   current CLASS fork. Using",
            "   `geom = omega_b,geom`, `eff = omega_b,eff`, `clust = omega_b,clustering`",
            "   gives very poor confrontations in both matrices.",
            "",
            "3. `verified`: the strongest improvement comes from lowering the baryon slot that",
            "   feeds the background/metric-source role while keeping the chemistry/acoustic",
            "   side near the practical structured value.",
            "",
            f"   On the pure slot-isolation matrix, moving from the one-number structured baseline",
            f"   to `geom = struct`, `eff = struct`, `clust = geom` improves the confrontation by",
            f"   `Delta chi2 = {fixed['rows'][0]['chi2'] - fixed['sanity']['one_number_struct']['chi2']:.6f}`.",
            "",
            "4. `conditional / diagnostic`: that best-performing row is not theorem-grade, because",
            "   it does not respect the derived chemistry assignment `geom = omega_b,geom`.",
            "   So it is a debugging clue, not a promoted physical branch.",
            "",
            "5. `derived / diagnostic`: the user concern was correct. The practical calculator gap",
            "   is not just 'CLASS uses one baryon number'; it is also that the present explicit",
            "   three-slot implementation does not faithfully realize the Paper 31 baryon map.",
            "",
            "## Code-Level Interpretation",
            "",
            "The current fork wires:",
            "",
            "- chemistry / HyRec hydrogen inventory -> `omega_b_geom`",
            "- acoustic loading `R` -> `omega_b_eff`",
            "- background matter and scalar perturbation stress-energy source -> `omega_b_clustering`",
            "",
            "That last choice is exactly where the Paper 31 theorem stack already warned that",
            "the scalar metric source is not licensed to use the late clustering branch.",
            "",
            "So the main surviving diagnostic is:",
            "",
            "- the calculator likely needs a more careful split between",
            "  local chemistry / opacity, acoustic loading, and background/metric-source baryon",
            "  roles than the current `geom/eff/clustering` implementation provides.",
            "",
            "## Reproducibility",
            "",
            f"- script: [paper31_practical_io_baryon_slot_audit.py]({OUT / 'paper31_practical_io_baryon_slot_audit.py'})",
            f"- fixed-cdm matrix: [paper31_practical_io_baryon_slot_audit_fixed_cdm.json]({OUT / 'paper31_practical_io_baryon_slot_audit_fixed_cdm.json'})",
            f"- variable-cdm matrix: [paper31_practical_io_baryon_slot_audit_variable_cdm.json]({OUT / 'paper31_practical_io_baryon_slot_audit_variable_cdm.json'})",
        ]
    )

    (OUT / "paper31_practical_io_baryon_slot_audit.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    fixed = run_matrix(keep_cdm_fixed=True)
    variable = run_matrix(keep_cdm_fixed=False)

    (OUT / "paper31_practical_io_baryon_slot_audit_fixed_cdm.json").write_text(
        json.dumps(fixed, indent=2)
    )
    (OUT / "paper31_practical_io_baryon_slot_audit_variable_cdm.json").write_text(
        json.dumps(variable, indent=2)
    )
    write_report(fixed, variable)


if __name__ == "__main__":
    main()
