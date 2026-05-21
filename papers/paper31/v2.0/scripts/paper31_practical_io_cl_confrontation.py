#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from classy import Class


ROOT = Path("/opt/cosmology-lab")
OUT = ROOT / "results" / "paper31"
TMP = ROOT / "tmp" / "planck-lite-py"

if str(TMP) not in sys.path:
    sys.path.insert(0, str(TMP))

from planck_lite_py import PlanckLitePy  # type: ignore  # noqa: E402


L_MAX = 2508
X = 1.519
GAMMA = 0.2375
F_GAMMA = 1.0 / (1.0 + GAMMA**2)
F_GAMMA2 = F_GAMMA**2
F_GAMMA3 = F_GAMMA**3
K_GAUGE = math.log(1.0 + GAMMA**2)
TAU_COV_PROXY = K_GAUGE / 2.0
J_PHI = X ** (-0.5)
ETA_IO = 2.0 * J_PHI - 1.0

A_S_NATIVE = 2.0072459972737347e-9

OMEGA_B_GEOM = 0.02108
OMEGA_B_EFF = 0.02910
OMEGA_B_CONTROL = 0.02710
OMEGA_B_CLUSTERING = 0.017053042566349
OMEGA_M_ONEFLUID = 0.15939026836
WEIGHT_STRUCT = ETA_IO * (1.0 + F_GAMMA) / 2.0
OMEGA_B_STRUCT = OMEGA_B_GEOM + WEIGHT_STRUCT * (OMEGA_B_EFF - OMEGA_B_GEOM)
H0_IO_ACTIVE = 68.91
OMEGA_K_IO_ACTIVE = -0.005613722564239

PLANCK_DATA = TMP / "data"

ELL_SAMPLES = {
    "TT": [220, 546, 800, 1000, 1500, 2000],
    "TE": [150, 300, 450, 800, 1200],
    "EE": [150, 300, 450, 800, 1200],
}


@dataclass(frozen=True)
class Case:
    key: str
    label: str
    status: str
    notes: str
    params: dict[str, Any]


BASE_IO = {
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
}

CASES = [
    Case(
        key="io_backbone_control",
        label="IO derived backbone + inherited recombination (control compression)",
        status="conditional / scoped practical",
        notes=(
            "Closed S^3 background and exact curved Weyl kernel are fixed. "
            "A_s is the native IO value. No astrophysical reionization history is inserted "
            "into the CLASS layer here, because Paper 31 does not license identifying the "
            "source-side tau_cov proxy with CLASS tau_reio. Exact Stage-2 local "
            "renormalization and exact R-loading slot remain open. The background package "
            "is the active Schur branch, not the retired 67.58 mixed branch."
        ),
        params={
            **BASE_IO,
            "omega_b": OMEGA_B_CONTROL,
            "omega_cdm": OMEGA_M_ONEFLUID - OMEGA_B_CONTROL,
        },
    ),
    Case(
        key="io_conditional_structured",
        label="IO practical structured branch + optical-history complement candidate",
        status="conditional / scoped practical",
        notes=(
            "Uses the Paper 31 structured branch candidate: omega_b,struct plus "
            "(c_vis, d_drag, h_hier) = (f_Gamma^2, 1, f_Gamma^3). This is the best "
            "current practical high-ell CMB branch. No astrophysical reionization history is "
            "inserted into the CLASS layer here. It remains conditional because the "
            "post-bridge optical-history complement and exact typed thermodynamics law are not "
            "derived. The background package is the active Schur branch, not the retired "
            "67.58 mixed branch."
        ),
        params={
            **BASE_IO,
            "omega_b": OMEGA_B_STRUCT,
            "omega_cdm": OMEGA_M_ONEFLUID - OMEGA_B_STRUCT,
            "io_visibility_opacity_factor": F_GAMMA2,
            "io_acoustic_drag_factor": 1.0,
            "io_acoustic_hierarchy_factor": F_GAMMA3,
        },
    ),
    Case(
        key="lcdm_planck_reference",
        label="Flat LCDM Planck 2018 reference",
        status="external reference",
        notes=(
            "Fixed Planck-like LCDM reference used only to calibrate the residual machinery. "
            "This is not an IO prediction."
        ),
        params={
            "output": "tCl,pCl,lCl",
            "lensing": "yes",
            "l_max_scalars": L_MAX,
            "H0": 67.36,
            "T_cmb": 2.7255,
            "Omega_k": 0.0,
            "N_ur": 3.044,
            "N_ncdm": 0,
            "YHe": 0.2454,
            "omega_b": 0.02237,
            "omega_cdm": 0.1200,
            "n_s": 0.9649,
            "A_s": 2.1005e-9,
            "tau_reio": 0.0544,
            "reio_parametrization": "reio_camb",
        },
    ),
]


def make_plik() -> PlanckLitePy:
    return PlanckLitePy(
        data_directory=str(PLANCK_DATA),
        year=2018,
        spectra="TTTEEE",
        use_low_ell_bins=True,
    )


def planck_data_files() -> dict[str, str]:
    return {
        "plik_lite": str(PLANCK_DATA / "planck2018_plik_lite" / "cl_cmb_plik_v22.dat"),
        "plik_covariance": str(PLANCK_DATA / "planck2018_plik_lite" / "c_matrix_plik_v22.dat"),
        "commander_low_ell_tt_bins": str(PLANCK_DATA / "planck2018_low_ell" / "CTT_bin_low_ell_2018.dat"),
        "commander_low_ell_readme": str(PLANCK_DATA / "planck2018_low_ell" / "readme.txt"),
    }


def block_slices(plik: PlanckLitePy) -> dict[str, slice]:
    tt_low_n = plik.nbintt_low_ell
    tt_all_n = plik.nbintt
    te_start = tt_all_n
    ee_start = te_start + plik.nbinte
    return {
        "tt_low": slice(0, tt_low_n),
        "tt_high": slice(tt_low_n, tt_all_n),
        "tt_all": slice(0, tt_all_n),
        "te": slice(te_start, te_start + plik.nbinte),
        "ee": slice(ee_start, ee_start + plik.nbinee),
    }


def slice_index(s: slice) -> np.ndarray:
    return np.arange(s.start, s.stop, dtype=int)


def binned_model(plik: PlanckLitePy, dl_tt: np.ndarray, dl_te: np.ndarray, dl_ee: np.ndarray, ellmin: int = 2) -> dict[str, np.ndarray]:
    ls = np.arange(len(dl_tt)) + ellmin
    fac = ls * (ls + 1.0) / (2.0 * math.pi)
    cl_tt = dl_tt / fac
    cl_te = dl_te / fac
    cl_ee = dl_ee / fac

    cl_tt_bin = np.zeros(plik.nbintt)
    for i in range(plik.nbintt):
        lo = plik.blmin_TT[i] + plik.plmin_TT - ellmin
        hi = plik.blmax_TT[i] + plik.plmin_TT + 1 - ellmin
        wlo = plik.blmin_TT[i]
        whi = plik.blmax_TT[i] + 1
        cl_tt_bin[i] = np.sum(cl_tt[lo:hi] * plik.bin_w_TT[wlo:whi])

    cl_te_bin = np.zeros(plik.nbinte)
    cl_ee_bin = np.zeros(plik.nbinee)
    for i in range(plik.nbinte):
        lo = plik.blmin[i] + plik.plmin - ellmin
        hi = plik.blmax[i] + plik.plmin + 1 - ellmin
        wlo = plik.blmin[i]
        whi = plik.blmax[i] + 1
        cl_te_bin[i] = np.sum(cl_te[lo:hi] * plik.bin_w[wlo:whi])
        cl_ee_bin[i] = np.sum(cl_ee[lo:hi] * plik.bin_w[wlo:whi])

    x_model = np.zeros(plik.nbin_tot)
    x_model[: plik.nbintt] = cl_tt_bin / plik.calPlanck**2
    x_model[plik.nbintt : plik.nbintt + plik.nbinte] = cl_te_bin / plik.calPlanck**2
    x_model[plik.nbintt + plik.nbinte :] = cl_ee_bin / plik.calPlanck**2

    return {
        "tt": x_model[: plik.nbintt],
        "te": x_model[plik.nbintt : plik.nbintt + plik.nbinte],
        "ee": x_model[plik.nbintt + plik.nbinte :],
        "full": x_model,
    }


def compute_cls(case: Case, plik: PlanckLitePy) -> dict[str, Any]:
    cosmo = Class()
    try:
        cosmo.set(case.params)
        cosmo.compute()
        cls = cosmo.lensed_cl(L_MAX)
        ell = cls["ell"][2:]
        t_cmb = float(case.params["T_cmb"])
        pref = ell * (ell + 1.0) / (2.0 * math.pi) * (t_cmb * 1.0e6) ** 2
        dl_tt = pref * cls["tt"][2:]
        dl_te = pref * cls["te"][2:]
        dl_ee = pref * cls["ee"][2:]
        binned = binned_model(plik, dl_tt, dl_te, dl_ee, ellmin=2)
        chi2 = -2.0 * float(plik.loglike(dl_tt, dl_te, dl_ee, ellmin=2))
        derived_names = ["100*theta_s", "z_rec", "rs_rec", "age"]
        derived = cosmo.get_current_derived_parameters(derived_names)
        return {
            "params": case.params,
            "ell": ell.tolist(),
            "Dl_TT": dl_tt.tolist(),
            "Dl_TE": dl_te.tolist(),
            "Dl_EE": dl_ee.tolist(),
            "binned": {k: v.tolist() for k, v in binned.items()},
            "derived": {k: float(derived[k]) for k in derived_names},
            "chi2_total": chi2,
            "A_eff_proxy": None,
        }
    finally:
        try:
            cosmo.struct_cleanup()
            cosmo.empty()
        except Exception:
            pass


def diagonal_summary(diff: np.ndarray, sigma: np.ndarray) -> dict[str, float]:
    z = diff / sigma
    return {
        "chi2_diag": float(np.sum(z**2)),
        "mean_signed_sigma": float(np.mean(z)),
        "mean_abs_sigma": float(np.mean(np.abs(z))),
        "rms_sigma": float(np.sqrt(np.mean(z**2))),
        "max_abs_sigma": float(np.max(np.abs(z))),
        "n_bins": int(len(z)),
    }


def block_covariance_decomposition(diff: np.ndarray, fisher: np.ndarray, slices: dict[str, slice]) -> dict[str, float]:
    keys = ["tt_low", "tt_high", "te", "ee"]
    out: dict[str, float] = {}
    for key in keys:
        idx = slice_index(slices[key])
        out[key] = float(diff[idx] @ fisher[np.ix_(idx, idx)] @ diff[idx])
    for i, key_i in enumerate(keys):
        idx_i = slice_index(slices[key_i])
        for key_j in keys[i + 1 :]:
            idx_j = slice_index(slices[key_j])
            out[f"{key_i}__{key_j}_cross"] = float(2.0 * diff[idx_i] @ fisher[np.ix_(idx_i, idx_j)] @ diff[idx_j])
    out["sum_all_terms"] = float(sum(out.values()))
    return out


def top_bins(case_key: str, spectrum: str, ell_eff: np.ndarray, data: np.ndarray, model: np.ndarray, sigma: np.ndarray, top_n: int = 8) -> list[dict[str, Any]]:
    z = (model - data) / sigma
    order = np.argsort(np.abs(z))[::-1][:top_n]
    rows = []
    for idx in order:
        rows.append(
            {
                "case": case_key,
                "spectrum": spectrum,
                "ell_eff": float(ell_eff[idx]),
                "planck_data_bin": float(data[idx]),
                "model_bin": float(model[idx]),
                "model_minus_planck": float(model[idx] - data[idx]),
                "sigma": float(sigma[idx]),
                "io_minus_planck_sigma": float(z[idx]),
            }
        )
    return rows


def sample_points(ell: np.ndarray, dl: np.ndarray, targets: list[int]) -> list[dict[str, float]]:
    rows = []
    for target in targets:
        idx = int(np.argmin(np.abs(ell - target)))
        rows.append({"target_ell": float(target), "ell": float(ell[idx]), "Dl": float(dl[idx])})
    return rows


def analyze_case(case: Case, run: dict[str, Any], plik: PlanckLitePy) -> dict[str, Any]:
    slices = block_slices(plik)
    x_data = plik.X_data
    x_sig = plik.X_sig
    x_model = np.asarray(run["binned"]["full"], dtype=float)
    diff = x_model - x_data
    fisher = plik.fisher

    bval_tt = plik.bval[slices["tt_all"]]
    bval_te = plik.bval[slices["te"]]
    bval_ee = plik.bval[slices["ee"]]

    analysis = {
        "status": case.status,
        "notes": case.notes,
        "chi2_total": float(run["chi2_total"]),
        "A_eff_proxy": run["A_eff_proxy"],
        "derived": run["derived"],
        "diagonal_summary": {
            "tt_low": diagonal_summary(diff[slices["tt_low"]], x_sig[slices["tt_low"]]),
            "tt_high": diagonal_summary(diff[slices["tt_high"]], x_sig[slices["tt_high"]]),
            "tt_all": diagonal_summary(diff[slices["tt_all"]], x_sig[slices["tt_all"]]),
            "te": diagonal_summary(diff[slices["te"]], x_sig[slices["te"]]),
            "ee": diagonal_summary(diff[slices["ee"]], x_sig[slices["ee"]]),
        },
        "block_covariance": block_covariance_decomposition(diff, fisher, slices),
        "top_residual_bins": {
            "tt": top_bins(
                case.key,
                "TT",
                np.asarray(bval_tt),
                x_data[slices["tt_all"]],
                x_model[slices["tt_all"]],
                x_sig[slices["tt_all"]],
            ),
            "te": top_bins(
                case.key,
                "TE",
                np.asarray(bval_te),
                x_data[slices["te"]],
                x_model[slices["te"]],
                x_sig[slices["te"]],
            ),
            "ee": top_bins(
                case.key,
                "EE",
                np.asarray(bval_ee),
                x_data[slices["ee"]],
                x_model[slices["ee"]],
                x_sig[slices["ee"]],
            ),
        },
        "sample_Dl": {
            "TT": sample_points(np.asarray(run["ell"], dtype=float), np.asarray(run["Dl_TT"], dtype=float), ELL_SAMPLES["TT"]),
            "TE": sample_points(np.asarray(run["ell"], dtype=float), np.asarray(run["Dl_TE"], dtype=float), ELL_SAMPLES["TE"]),
            "EE": sample_points(np.asarray(run["ell"], dtype=float), np.asarray(run["Dl_EE"], dtype=float), ELL_SAMPLES["EE"]),
        },
    }
    return analysis


def inferred_a_eff_proxy(case: Case) -> float | None:
    if case.key.startswith("io_"):
        return float(A_S_NATIVE * math.exp(-2.0 * TAU_COV_PROXY))
    if "A_s" in case.params and "tau_reio" in case.params:
        return float(case.params["A_s"] * math.exp(-2.0 * float(case.params["tau_reio"])))
    return None


def write_cls_csv(path: Path, case_runs: dict[str, dict[str, Any]]) -> None:
    order = list(case_runs)
    ell = np.asarray(case_runs[order[0]]["ell"], dtype=int)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        header = ["ell"]
        for key in order:
            header.extend([f"Dl_TT_{key}", f"Dl_TE_{key}", f"Dl_EE_{key}"])
        writer.writerow(header)
        for i, ell_i in enumerate(ell):
            row: list[float | int] = [int(ell_i)]
            for key in order:
                row.extend(
                    [
                        float(case_runs[key]["Dl_TT"][i]),
                        float(case_runs[key]["Dl_TE"][i]),
                        float(case_runs[key]["Dl_EE"][i]),
                    ]
                )
            writer.writerow(row)


def write_residual_csv(path: Path, plik: PlanckLitePy, case_runs: dict[str, dict[str, Any]]) -> None:
    slices = block_slices(plik)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "case",
                "spectrum",
                "bin_center_ell",
                "planck_data_bin",
                "model_bin",
                "model_minus_planck",
                "sigma",
                "io_minus_planck_sigma",
            ]
        )
        for key, run in case_runs.items():
            model = np.asarray(run["binned"]["full"], dtype=float)
            for spectrum, s in (("TT", slices["tt_all"]), ("TE", slices["te"]), ("EE", slices["ee"])):
                for i in range(s.start, s.stop):
                    writer.writerow(
                        [
                            key,
                            spectrum,
                            float(plik.bval[i]),
                            float(plik.X_data[i]),
                            float(model[i]),
                            float(model[i] - plik.X_data[i]),
                            float(plik.X_sig[i]),
                            float((model[i] - plik.X_data[i]) / plik.X_sig[i]),
                        ]
                    )


def plot_residuals(path: Path, plik: PlanckLitePy, case_runs: dict[str, dict[str, Any]]) -> None:
    slices = block_slices(plik)
    fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=False)
    styles = {
        "io_backbone_control": {"color": "#b22222", "label": "IO backbone control"},
        "io_conditional_structured": {"color": "#0b5d9a", "label": "IO conditional structured"},
        "lcdm_planck_reference": {"color": "#555555", "label": "LCDM reference"},
    }
    for ax, (spectrum, s) in zip(axes, [("TT", slices["tt_all"]), ("TE", slices["te"]), ("EE", slices["ee"])]):
        ell_eff = plik.bval[s]
        ax.axhline(0.0, color="black", linewidth=0.8, alpha=0.6)
        for key, run in case_runs.items():
            model = np.asarray(run["binned"]["full"], dtype=float)[s]
            resid = (model - plik.X_data[s]) / plik.X_sig[s]
            style = styles[key]
            ax.plot(ell_eff, resid, marker="o", markersize=2.5, linewidth=1.0, color=style["color"], label=style["label"])
        ax.set_ylabel(f"{spectrum} sigma")
        ax.grid(alpha=0.2)
        ax.set_title(f"{spectrum} binned residuals")
    axes[-1].set_xlabel("Effective ell")
    axes[0].legend(frameon=False, ncol=3, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def build_report(results: dict[str, Any]) -> str:
    io_control = results["cases"]["io_backbone_control"]
    io_struct = results["cases"]["io_conditional_structured"]
    lcdm = results["cases"]["lcdm_planck_reference"]

    lines: list[str] = []
    lines.extend(
        [
            "# Paper 31 Practical IO C_l Confrontation",
            "",
            "Date: 2026-04-03",
            "",
            "## Scope",
            "",
            "This is a direct fixed-parameter confrontation against the local Planck 2018",
            "Plik-lite TTTEEE package with low-ell TT bins. It is **not** a fit.",
            "The TE/EE confrontation is therefore high-ell only; low-ell EE is not binned here.",
            "The IO cases also omit astrophysical reionization in the CLASS layer on purpose.",
            "",
            "The practical calculator uses exactly the surviving Paper 31 ingredients:",
            "",
            "- closed `S^3` / curved FRW transfer backbone",
            "- derived baryon-assignment map",
            "- exact curved Weyl kernel",
            "- inherited recombination class under Premise 2",
            "- optical-history complement only as a conditional candidate branch",
            "- explicit labeling of the open Stage-2 thermodynamics seam",
            "",
            "## Fixed constants",
            "",
            f"- `x = {X}`",
            f"- `gamma = {GAMMA}`",
            f"- `f_Gamma = 1/(1+gamma^2) = {F_GAMMA}`",
            f"- `K_gauge = log(1+gamma^2) = {K_GAUGE}`",
            f"- `tau_cov,IO = K_gauge/2 = {TAU_COV_PROXY}`",
            f"- `A_s^native = {A_S_NATIVE:.16e}`",
            f"- `lcmb_rescale = x^(-1/2) = {J_PHI}`",
            f"- `lcmb_curved_shift = -3`",
            f"- `lcmb_curved_order = -1/4`",
            f"- active Schur background: `H0 = {H0_IO_ACTIVE}`, `Omega_k = {OMEGA_K_IO_ACTIVE}`",
            "",
            "## Baryon map used",
            "",
            f"- chemistry / local opacity inventory: `omega_b,geom = {OMEGA_B_GEOM}` (`derived / scoped`)",
            f"- reduced visibility/readout class: `omega_b,eff = {OMEGA_B_EFF}` (`derived / scoped`)",
            f"- clustering branch: `omega_b,clustering = {OMEGA_B_CLUSTERING}` (`derived / no-go` for CMB metric source)",
            "- `R`-loading exact slot: `open`",
            "",
            "The practical calculator therefore compares two IO compressions:",
            "",
            f"1. control compression: `omega_b = {OMEGA_B_CONTROL}`",
            f"2. structured conditional branch: `omega_b,struct = {OMEGA_B_STRUCT}` with `(c_vis, d_drag, h_hier) = (f_Gamma^2, 1, f_Gamma^3)`",
            "",
            "## Stage-2 boundary",
            "",
            "This run inherits the accepted exterior recombination class under Premise 2.",
            "The exact IO local Stage-2 atomic-radiative renormalization remains open.",
            "The geometry and harmonic layer are already non-flat: the local CLASS build uses",
            "closed-FRW transfer and hyperspherical-harmonic machinery when `Omega_k < 0`.",
            "The remaining practical leak is Stage-2 thermodynamics/recombination, not flat",
            "line-of-sight geometry.",
            "The inherited late reionization history is left out of the CLASS run here, because",
            "Paper 31 does not license identifying the source-side `tau_cov = K_gauge/2` with",
            "astrophysical `tau_reio` inside `reio_camb`.",
            "So these spectra are practical conditional confrontations, not a theorem-closed",
            "exact IO-native Boltzmann solution.",
            "Low-ell EE remains a separate inherited-reionization sector and is not directly",
            "binned by the local Plik-lite package used here.",
            "",
            "## Data path",
            "",
            f"- Plik-lite: `{results['planck_data_files']['plik_lite']}`",
            f"- covariance: `{results['planck_data_files']['plik_covariance']}`",
            f"- low-ell TT bins: `{results['planck_data_files']['commander_low_ell_tt_bins']}`",
            "",
            "## Main fixed-case residuals",
            "",
        ]
    )

    for key in ("io_backbone_control", "io_conditional_structured", "lcdm_planck_reference"):
        row = results["cases"][key]
        lines.extend(
            [
                f"### {row['label']}",
                "",
                f"- status: `{row['status']}`",
                f"- total `chi2_TTTEEE+lowTT = {row['analysis']['chi2_total']:.6f}`",
                (
                    f"- `A_eff source proxy = {row['analysis']['A_eff_proxy']:.16e}`"
                    if row["analysis"]["A_eff_proxy"] is not None
                    else "- `A_eff proxy`: not applicable"
                ),
                f"- `100*theta_s = {row['analysis']['derived']['100*theta_s']:.9f}`",
                f"- `z_rec = {row['analysis']['derived']['z_rec']:.6f}`",
                f"- `rs_rec = {row['analysis']['derived']['rs_rec']:.6f} Mpc`",
                f"- note: {row['notes']}",
                "",
                "Diagonal sigma residual summary `(model-Planck)/sigma`:",
                "",
                f"- TT low: mean `{row['analysis']['diagonal_summary']['tt_low']['mean_signed_sigma']:+.6f}`, rms `{row['analysis']['diagonal_summary']['tt_low']['rms_sigma']:.6f}`, max `|sigma| = {row['analysis']['diagonal_summary']['tt_low']['max_abs_sigma']:.6f}`",
                f"- TT high: mean `{row['analysis']['diagonal_summary']['tt_high']['mean_signed_sigma']:+.6f}`, rms `{row['analysis']['diagonal_summary']['tt_high']['rms_sigma']:.6f}`, max `|sigma| = {row['analysis']['diagonal_summary']['tt_high']['max_abs_sigma']:.6f}`",
                f"- TE: mean `{row['analysis']['diagonal_summary']['te']['mean_signed_sigma']:+.6f}`, rms `{row['analysis']['diagonal_summary']['te']['rms_sigma']:.6f}`, max `|sigma| = {row['analysis']['diagonal_summary']['te']['max_abs_sigma']:.6f}`",
                f"- EE: mean `{row['analysis']['diagonal_summary']['ee']['mean_signed_sigma']:+.6f}`, rms `{row['analysis']['diagonal_summary']['ee']['rms_sigma']:.6f}`, max `|sigma| = {row['analysis']['diagonal_summary']['ee']['max_abs_sigma']:.6f}`",
                "",
            ]
        )

    delta_struct_vs_control = io_struct["analysis"]["chi2_total"] - io_control["analysis"]["chi2_total"]
    delta_struct_vs_lcdm = io_struct["analysis"]["chi2_total"] - lcdm["analysis"]["chi2_total"]
    tt_high_delta = io_struct["analysis"]["block_covariance"]["tt_high"] - io_control["analysis"]["block_covariance"]["tt_high"]
    te_delta = io_struct["analysis"]["block_covariance"]["te"] - io_control["analysis"]["block_covariance"]["te"]
    ee_delta = io_struct["analysis"]["block_covariance"]["ee"] - io_control["analysis"]["block_covariance"]["ee"]
    lines.extend(
        [
            "## Fixed-case comparison",
            "",
            f"- structured conditional minus IO backbone control: `Delta chi2 = {delta_struct_vs_control:+.6f}`",
            f"- structured conditional minus LCDM reference: `Delta chi2 = {delta_struct_vs_lcdm:+.6f}`",
            f"- covariance-block change TT high: `{tt_high_delta:+.6f}`",
            f"- covariance-block change TE: `{te_delta:+.6f}`",
            f"- covariance-block change EE: `{ee_delta:+.6f}`",
            "",
            "So the structured fixed branch gains most strongly in `TE` and `EE`, while the",
            "remaining dominant failure is still a negative high-ell `TT` shape wall.",
            "",
            "## Largest residual bins on the practical IO branch",
            "",
        ]
    )

    for spectrum in ("tt", "te", "ee"):
        lines.append(f"### {spectrum.upper()}")
        lines.append("")
        for row in io_struct["analysis"]["top_residual_bins"][spectrum][:8]:
            lines.append(
                f"- `ell~{int(row['ell_eff'])}`: model `{row['model_bin']}`, data `{row['planck_data_bin']}`, residual `{row['io_minus_planck_sigma']:+.6f} sigma`"
            )
        lines.append("")

    lines.extend(
        [
            "## Exact D_l samples on the practical IO branch",
            "",
            "### TT",
            "",
        ]
    )
    for row in io_struct["analysis"]["sample_Dl"]["TT"]:
        lines.append(f"- target `{int(row['target_ell'])}` -> `ell = {int(row['ell'])}`, `Dl = {row['Dl']}`")
    lines.extend(["", "### TE", ""])
    for row in io_struct["analysis"]["sample_Dl"]["TE"]:
        lines.append(f"- target `{int(row['target_ell'])}` -> `ell = {int(row['ell'])}`, `Dl = {row['Dl']}`")
    lines.extend(["", "### EE", ""])
    for row in io_struct["analysis"]["sample_Dl"]["EE"]:
        lines.append(f"- target `{int(row['target_ell'])}` -> `ell = {int(row['ell'])}`, `Dl = {row['Dl']}`")

    lines.extend(
        [
            "",
            "## Verdict",
            "",
            "- `verified`: a practical fixed-IO `C_l` calculator now exists on the local patched CLASS stack.",
            "- `derived / scoped`: the exact curved Weyl kernel is active in the confrontation.",
            "- `conditional / scoped`: the best practical IO branch remains the structured optical-history candidate.",
            "- `open`: the exact Stage-2 atomic-radiative renormalization law and the exact `R`-loading slot.",
            "",
            "So this deliverable is an honest confrontation layer: fixed IO values, fixed conditional branch choice where Paper 31 requires it, no illicit `tau_cov -> tau_reio` identification, and explicit residuals against Planck.",
            "",
            "## Archive files",
            "",
            f"- [paper31_practical_io_cl_confrontation_results.json]({OUT / 'paper31_practical_io_cl_confrontation_results.json'})",
            f"- [paper31_practical_io_cl_confrontation_cls.csv]({OUT / 'paper31_practical_io_cl_confrontation_cls.csv'})",
            f"- [paper31_practical_io_cl_confrontation_residual_bins.csv]({OUT / 'paper31_practical_io_cl_confrontation_residual_bins.csv'})",
            f"- [paper31_practical_io_cl_confrontation_residuals.png]({OUT / 'paper31_practical_io_cl_confrontation_residuals.png'})",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    plik = make_plik()
    case_runs: dict[str, dict[str, Any]] = {}
    case_results: dict[str, Any] = {}

    for case in CASES:
        run = compute_cls(case, plik)
        case_runs[case.key] = run
        analysis = analyze_case(case, run, plik)
        analysis["A_eff_proxy"] = inferred_a_eff_proxy(case)
        case_results[case.key] = {
            "label": case.label,
            "status": case.status,
            "notes": case.notes,
            "params": case.params,
            "analysis": analysis,
        }

    write_cls_csv(OUT / "paper31_practical_io_cl_confrontation_cls.csv", case_runs)
    write_residual_csv(OUT / "paper31_practical_io_cl_confrontation_residual_bins.csv", plik, case_runs)
    plot_residuals(OUT / "paper31_practical_io_cl_confrontation_residuals.png", plik, case_runs)

    results = {
        "planck_data_files": planck_data_files(),
        "constants": {
            "x": X,
            "gamma": GAMMA,
            "f_gamma": F_GAMMA,
            "f_gamma_squared": F_GAMMA2,
            "f_gamma_cubed": F_GAMMA3,
            "K_gauge": K_GAUGE,
            "tau_cov_proxy": TAU_COV_PROXY,
            "A_s_native": A_S_NATIVE,
            "j_phi": J_PHI,
            "eta_io": ETA_IO,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_control": OMEGA_B_CONTROL,
            "omega_b_struct": OMEGA_B_STRUCT,
            "omega_b_clustering": OMEGA_B_CLUSTERING,
        },
        "cases": case_results,
        "archive_files": {
            "cls_csv": str(OUT / "paper31_practical_io_cl_confrontation_cls.csv"),
            "residual_bins_csv": str(OUT / "paper31_practical_io_cl_confrontation_residual_bins.csv"),
            "residual_plot_png": str(OUT / "paper31_practical_io_cl_confrontation_residuals.png"),
        },
    }

    (OUT / "paper31_practical_io_cl_confrontation_results.json").write_text(json.dumps(results, indent=2) + "\n")
    (OUT / "paper31_practical_io_cl_confrontation_report.md").write_text(build_report(results))


if __name__ == "__main__":
    main()
