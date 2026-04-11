from __future__ import annotations

import csv
import json
import math
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.stats import chi2 as chi2_dist


ROOT = Path("/opt/cosmology-lab/results/paper29")
DATA_DIR = ROOT / "data_cache"
OUT_JSON = ROOT / "paper29_iid_branch_chi2_recompute_results.json"
OUT_REPORT = ROOT / "paper29_iid_branch_chi2_recompute_report.md"
OUT_CC_CSV = ROOT / "paper29_iid_branch_cc_residuals.csv"
OUT_BAO_CSV = ROOT / "paper29_iid_branch_bao_residuals.csv"

C_KM_S = 299792.458

DESI_DR2_MEAN_URL = (
    "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/"
    "desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt"
)
DESI_DR2_COV_URL = (
    "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/"
    "desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt"
)

CC35_SOURCE = "Jia et al. (2025), MNRAS 542, 1063, Table A1"
DESI_SOURCE = "DESI DR2 GCcomb Gaussian likelihood (official mean/covariance files)"


@dataclass(frozen=True)
class Branch:
    label: str
    H0: float
    Omega_m: float
    Omega_k: float
    Omega_r: float
    Omega_lambda_display: float
    Omega_lambda_eval: float
    r_d_Mpc: float
    notes: str


CC_35 = [
    {"z": 0.07, "H": 69.0, "sigma": 19.6, "source": "Zhang et al. (2014)"},
    {"z": 0.09, "H": 69.0, "sigma": 12.0, "source": "Simon, Verde & Jimenez (2005)"},
    {"z": 0.12, "H": 68.6, "sigma": 26.2, "source": "Zhang et al. (2014)"},
    {"z": 0.17, "H": 83.0, "sigma": 8.0, "source": "Simon et al. (2005)"},
    {"z": 0.179, "H": 75.0, "sigma": 4.0, "source": "Moresco et al. (2012)"},
    {"z": 0.199, "H": 75.0, "sigma": 5.0, "source": "Moresco et al. (2012)"},
    {"z": 0.2, "H": 72.9, "sigma": 29.6, "source": "Zhang et al. (2014)"},
    {"z": 0.27, "H": 77.0, "sigma": 14.0, "source": "Simon et al. (2005)"},
    {"z": 0.28, "H": 88.8, "sigma": 36.6, "source": "Zhang et al. (2014)"},
    {"z": 0.352, "H": 83.0, "sigma": 14.0, "source": "Moresco et al. (2012)"},
    {"z": 0.3802, "H": 83.0, "sigma": 13.5, "source": "Moresco et al. (2016)"},
    {"z": 0.4, "H": 95.0, "sigma": 17.0, "source": "Simon et al. (2005)"},
    {"z": 0.4004, "H": 77.0, "sigma": 10.2, "source": "Moresco et al. (2016)"},
    {"z": 0.4247, "H": 87.1, "sigma": 11.2, "source": "Moresco et al. (2016)"},
    {"z": 0.4497, "H": 92.8, "sigma": 12.9, "source": "Moresco et al. (2016)"},
    {"z": 0.47, "H": 89.0, "sigma": 50.0, "source": "Ratsimbazafy et al. (2017)"},
    {"z": 0.4783, "H": 80.9, "sigma": 9.0, "source": "Moresco et al. (2016)"},
    {"z": 0.48, "H": 97.0, "sigma": 62.0, "source": "Ratsimbazafy et al. (2017)"},
    {"z": 0.593, "H": 104.0, "sigma": 13.0, "source": "Moresco et al. (2012)"},
    {"z": 0.68, "H": 92.0, "sigma": 8.0, "source": "Moresco et al. (2012)"},
    {"z": 0.75, "H": 98.8, "sigma": 33.6, "source": "Borghi et al. (2022)"},
    {"z": 0.75, "H": 105.0, "sigma": 7.9, "source": "Jimenez et al. (2023)"},
    {"z": 0.781, "H": 105.0, "sigma": 12.0, "source": "Moresco et al. (2012)"},
    {"z": 0.8, "H": 113.1, "sigma": 15.1, "source": "Jiao et al. (2023)"},
    {"z": 0.875, "H": 125.0, "sigma": 17.0, "source": "Moresco et al. (2012)"},
    {"z": 0.88, "H": 90.0, "sigma": 40.0, "source": "Ratsimbazafy et al. (2017)"},
    {"z": 0.9, "H": 117.0, "sigma": 23.0, "source": "Simon et al. (2005)"},
    {"z": 1.037, "H": 154.0, "sigma": 20.0, "source": "Moresco et al. (2012)"},
    {"z": 1.26, "H": 135.0, "sigma": 65.0, "source": "Tomasetti et al. (2023b)"},
    {"z": 1.3, "H": 168.0, "sigma": 17.0, "source": "Simon et al. (2005)"},
    {"z": 1.363, "H": 160.0, "sigma": 33.6, "source": "Moresco (2015)"},
    {"z": 1.43, "H": 177.0, "sigma": 18.0, "source": "Simon et al. (2005)"},
    {"z": 1.53, "H": 140.0, "sigma": 14.0, "source": "Simon et al. (2005)"},
    {"z": 1.75, "H": 202.0, "sigma": 40.0, "source": "Simon et al. (2005)"},
    {"z": 1.965, "H": 186.5, "sigma": 50.4, "source": "Moresco (2015)"},
]


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def cached_download(url: str, target: Path) -> Path:
    ensure_dir(target.parent)
    if not target.exists():
        urllib.request.urlretrieve(url, target)
    return target


def omega_r_from_tcmb_neff(h: float, T_cmb: float, N_eff: float) -> float:
    omega_gamma = 2.469e-5 * (T_cmb / 2.7255) ** 4 / (h * h)
    factor = 1.0 + N_eff * (7.0 / 8.0) * (4.0 / 11.0) ** (4.0 / 3.0)
    return omega_gamma * factor


def load_desi_dr2() -> tuple[list[dict[str, float | str]], np.ndarray]:
    mean_path = cached_download(DESI_DR2_MEAN_URL, DATA_DIR / "desi_dr2_all_gccomb_mean.txt")
    cov_path = cached_download(DESI_DR2_COV_URL, DATA_DIR / "desi_dr2_all_gccomb_cov.txt")
    rows: list[dict[str, float | str]] = []
    for raw_line in mean_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        z, value, quantity = line.split()
        rows.append({"z": float(z), "value": float(value), "quantity": quantity})
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


def h_z(z: float, branch: Branch) -> float:
    return branch.H0 * e_z(z, branch)


def dimless_chi(z: float, branch: Branch) -> float:
    result, _ = quad(
        lambda zp: 1.0 / e_z(zp, branch),
        0.0,
        z,
        epsabs=1.0e-11,
        epsrel=1.0e-11,
        limit=600,
    )
    return result


def transverse_distance_mpc(z: float, branch: Branch) -> float:
    chi = dimless_chi(z, branch)
    if abs(branch.Omega_k) < 1.0e-15:
        return (C_KM_S / branch.H0) * chi
    if branch.Omega_k < 0.0:
        rootk = math.sqrt(-branch.Omega_k)
        return (C_KM_S / branch.H0) * math.sin(rootk * chi) / rootk
    rootk = math.sqrt(branch.Omega_k)
    return (C_KM_S / branch.H0) * math.sinh(rootk * chi) / rootk


def hubble_distance_mpc(z: float, branch: Branch) -> float:
    return C_KM_S / h_z(z, branch)


def dv_distance_mpc(z: float, branch: Branch) -> float:
    d_m = transverse_distance_mpc(z, branch)
    d_h = hubble_distance_mpc(z, branch)
    return (z * d_m * d_m * d_h) ** (1.0 / 3.0)


def cc_residuals(branch: Branch) -> tuple[float, list[dict[str, float | str]]]:
    rows = []
    chi2 = 0.0
    for row in CC_35:
        pred = h_z(float(row["z"]), branch)
        residual = pred - float(row["H"])
        pull = residual / float(row["sigma"])
        chi2 += pull * pull
        rows.append(
            {
                "z": float(row["z"]),
                "source": str(row["source"]),
                "H_obs": float(row["H"]),
                "sigma": float(row["sigma"]),
                "H_model": pred,
                "residual": residual,
                "pull": pull,
            }
        )
    return chi2, rows


def bao_residuals(
    branch: Branch, rows: list[dict[str, float | str]], covariance: np.ndarray
) -> tuple[float, list[dict[str, float | str]]]:
    obs = np.array([float(row["value"]) for row in rows], dtype=float)
    pred = []
    residual_rows = []
    for i, row in enumerate(rows):
        z = float(row["z"])
        quantity = str(row["quantity"])
        if quantity == "DM_over_rs":
            model = transverse_distance_mpc(z, branch) / branch.r_d_Mpc
        elif quantity == "DH_over_rs":
            model = hubble_distance_mpc(z, branch) / branch.r_d_Mpc
        elif quantity == "DV_over_rs":
            model = dv_distance_mpc(z, branch) / branch.r_d_Mpc
        else:
            raise ValueError(quantity)
        pred.append(model)
        sigma_diag = float(math.sqrt(covariance[i, i]))
        residual_rows.append(
            {
                "z": z,
                "quantity": quantity,
                "obs": float(row["value"]),
                "sigma_diag": sigma_diag,
                "model": model,
                "residual": model - float(row["value"]),
                "naive_pull": (model - float(row["value"])) / sigma_diag,
            }
        )
    pred_vec = np.array(pred, dtype=float)
    diff = pred_vec - obs
    inv_cov = np.linalg.inv(covariance)
    chi2 = float(diff @ inv_cov @ diff)
    return chi2, residual_rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def format_markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    sep = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(f"`{row[col]}`" for col in columns) + " |")
    return "\n".join([header, sep, *body])


def main() -> None:
    # Exact i.i.d. branch constants from the Paper 10 corrected-projection rebuild,
    # evaluated with the user-requested low-z radiation term and closure-corrected Omega_Lambda.
    io_h0 = 67.57585653582628
    io_omega_m = 0.34868395067621694
    io_omega_k = -0.04579112576013168
    io_omega_r = 1.226e-4
    io_omega_lambda_display = 0.6971071750839146
    io_omega_lambda_eval = 1.0 - io_omega_m - io_omega_k - io_omega_r

    planck_h0 = 67.4
    planck_omega_m = 0.315
    planck_omega_k = 0.0
    planck_omega_r = omega_r_from_tcmb_neff(planck_h0 / 100.0, 2.7255, 3.046)
    planck_omega_lambda_display = 0.685
    planck_omega_lambda_eval = 1.0 - planck_omega_m - planck_omega_k - planck_omega_r

    io_branch = Branch(
        label="IO i.i.d. branch",
        H0=io_h0,
        Omega_m=io_omega_m,
        Omega_k=io_omega_k,
        Omega_r=io_omega_r,
        Omega_lambda_display=io_omega_lambda_display,
        Omega_lambda_eval=io_omega_lambda_eval,
        r_d_Mpc=143.3,
        notes="Exact Paper 10 corrected-projection branch with user-requested IO radiation term inserted and Omega_Lambda closure-corrected for E(0)=1.",
    )
    planck_branch = Branch(
        label="Planck LCDM fixed reference",
        H0=planck_h0,
        Omega_m=planck_omega_m,
        Omega_k=planck_omega_k,
        Omega_r=planck_omega_r,
        Omega_lambda_display=planck_omega_lambda_display,
        Omega_lambda_eval=planck_omega_lambda_eval,
        r_d_Mpc=147.09,
        notes="User-requested flat Planck reference with standard radiation closure from T_cmb=2.7255 and N_eff=3.046.",
    )

    bao_rows, bao_cov = load_desi_dr2()

    io_cc_chi2, io_cc_rows = cc_residuals(io_branch)
    pl_cc_chi2, pl_cc_rows = cc_residuals(planck_branch)
    io_bao_chi2, io_bao_rows = bao_residuals(io_branch, bao_rows, bao_cov)
    pl_bao_chi2, pl_bao_rows = bao_residuals(planck_branch, bao_rows, bao_cov)

    n_cc = len(CC_35)
    n_bao = len(bao_rows)
    n_total = n_cc + n_bao

    results = {
        "metadata": {
            "title": "Paper 29 chi2 recomputation on the i.i.d. branch",
            "cc_dataset": CC35_SOURCE,
            "bao_dataset": DESI_SOURCE,
            "sources": {
                "cc_compilation": "https://academic.oup.com/mnras/article/542/2/1063/8230790",
                "desi_dr2_readme": "https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/README.html",
                "desi_dr2_mean": DESI_DR2_MEAN_URL,
                "desi_dr2_cov": DESI_DR2_COV_URL,
            },
            "notes": [
                "CC uses the 35-point compilation with diagonal published uncertainties, matching the prior Paper 29 confrontation file.",
                "BAO uses the official 13-point DESI DR2 GCcomb mean vector and full covariance.",
                "When the radiation term is included, Omega_Lambda is closure-corrected in the evaluator so that E(0)=1.",
            ],
        },
        "branches": {
            "io_iid": asdict(io_branch),
            "planck_lcdm": asdict(planck_branch),
        },
        "chi2_summary": {
            "cc": {
                "N_data": n_cc,
                "dof": n_cc,
                "io_chi2": io_cc_chi2,
                "io_chi2_per_dof": io_cc_chi2 / n_cc,
                "io_pte": float(chi2_dist.sf(io_cc_chi2, n_cc)),
                "planck_chi2": pl_cc_chi2,
                "planck_chi2_per_dof": pl_cc_chi2 / n_cc,
                "planck_pte": float(chi2_dist.sf(pl_cc_chi2, n_cc)),
                "delta_chi2_io_minus_planck": io_cc_chi2 - pl_cc_chi2,
            },
            "bao": {
                "N_data": n_bao,
                "dof": n_bao,
                "io_chi2": io_bao_chi2,
                "io_chi2_per_dof": io_bao_chi2 / n_bao,
                "io_pte": float(chi2_dist.sf(io_bao_chi2, n_bao)),
                "planck_chi2": pl_bao_chi2,
                "planck_chi2_per_dof": pl_bao_chi2 / n_bao,
                "planck_pte": float(chi2_dist.sf(pl_bao_chi2, n_bao)),
                "delta_chi2_io_minus_planck": io_bao_chi2 - pl_bao_chi2,
            },
            "combined": {
                "N_data": n_total,
                "dof": n_total,
                "io_chi2": io_cc_chi2 + io_bao_chi2,
                "io_chi2_per_dof": (io_cc_chi2 + io_bao_chi2) / n_total,
                "io_pte": float(chi2_dist.sf(io_cc_chi2 + io_bao_chi2, n_total)),
                "planck_chi2": pl_cc_chi2 + pl_bao_chi2,
                "planck_chi2_per_dof": (pl_cc_chi2 + pl_bao_chi2) / n_total,
                "planck_pte": float(chi2_dist.sf(pl_cc_chi2 + pl_bao_chi2, n_total)),
                "delta_chi2_io_minus_planck": (io_cc_chi2 + io_bao_chi2) - (pl_cc_chi2 + pl_bao_chi2),
            },
        },
        "cc_residuals": {
            "io_iid": io_cc_rows,
            "planck_lcdm": pl_cc_rows,
        },
        "bao_residuals": {
            "io_iid": io_bao_rows,
            "planck_lcdm": pl_bao_rows,
        },
        "legacy_comparison": {
            "paper29_dead_schur_claims": {
                "cc_chi2": 15.57,
                "bao_chi2": 26.91,
                "combined_chi2": 42.48,
            },
            "replacement_branch": "io_iid",
        },
    }

    write_csv(
        OUT_CC_CSV,
        [
            {
                "branch": "io_iid",
                **row,
            }
            for row in io_cc_rows
        ]
        + [
            {
                "branch": "planck_lcdm",
                **row,
            }
            for row in pl_cc_rows
        ],
    )
    write_csv(
        OUT_BAO_CSV,
        [
            {
                "branch": "io_iid",
                **row,
            }
            for row in io_bao_rows
        ]
        + [
            {
                "branch": "planck_lcdm",
                **row,
            }
            for row in pl_bao_rows
        ],
    )

    cc_report_rows_io = [
        {
            "z": row["z"],
            "H_obs": row["H_obs"],
            "sigma": row["sigma"],
            "H_model": row["H_model"],
            "residual": row["residual"],
            "pull": row["pull"],
            "source": row["source"],
        }
        for row in io_cc_rows
    ]
    cc_report_rows_planck = [
        {
            "z": row["z"],
            "H_obs": row["H_obs"],
            "sigma": row["sigma"],
            "H_model": row["H_model"],
            "residual": row["residual"],
            "pull": row["pull"],
            "source": row["source"],
        }
        for row in pl_cc_rows
    ]
    bao_report_rows_io = [
        {
            "z": row["z"],
            "quantity": row["quantity"],
            "obs": row["obs"],
            "sigma_diag": row["sigma_diag"],
            "model": row["model"],
            "residual": row["residual"],
            "naive_pull": row["naive_pull"],
        }
        for row in io_bao_rows
    ]
    bao_report_rows_planck = [
        {
            "z": row["z"],
            "quantity": row["quantity"],
            "obs": row["obs"],
            "sigma_diag": row["sigma_diag"],
            "model": row["model"],
            "residual": row["residual"],
            "naive_pull": row["naive_pull"],
        }
        for row in pl_bao_rows
    ]

    report = f"""# Paper 29 χ² recomputation on the i.i.d. branch

## Inputs

- IO i.i.d. branch exact evaluation values:
  - `H0 = {io_branch.H0}`
  - `Omega_m = {io_branch.Omega_m}`
  - `Omega_k = {io_branch.Omega_k}`
  - `Omega_r = {io_branch.Omega_r}`
  - `Omega_lambda_display = {io_branch.Omega_lambda_display}`
  - `Omega_lambda_eval = {io_branch.Omega_lambda_eval}`
  - `r_d = {io_branch.r_d_Mpc} Mpc`

- Planck LCDM fixed reference:
  - `H0 = {planck_branch.H0}`
  - `Omega_m = {planck_branch.Omega_m}`
  - `Omega_k = {planck_branch.Omega_k}`
  - `Omega_r = {planck_branch.Omega_r}`
  - `Omega_lambda_display = {planck_branch.Omega_lambda_display}`
  - `Omega_lambda_eval = {planck_branch.Omega_lambda_eval}`
  - `r_d = {planck_branch.r_d_Mpc} Mpc`

## Dataset summary

- CC35: `{n_cc}` points from `{CC35_SOURCE}`
- DESI DR2 GCcomb: `{n_bao}` points with full covariance from `{DESI_SOURCE}`
- Combined: `{n_total}` points

## χ² summary

| dataset | N_data | dof | IO χ² | IO χ²/dof | Planck χ² | Planck χ²/dof | Δχ² = IO - Planck |
|---|---:|---:|---:|---:|---:|---:|---:|
| CC | `{n_cc}` | `{n_cc}` | `{results['chi2_summary']['cc']['io_chi2']}` | `{results['chi2_summary']['cc']['io_chi2_per_dof']}` | `{results['chi2_summary']['cc']['planck_chi2']}` | `{results['chi2_summary']['cc']['planck_chi2_per_dof']}` | `{results['chi2_summary']['cc']['delta_chi2_io_minus_planck']}` |
| BAO | `{n_bao}` | `{n_bao}` | `{results['chi2_summary']['bao']['io_chi2']}` | `{results['chi2_summary']['bao']['io_chi2_per_dof']}` | `{results['chi2_summary']['bao']['planck_chi2']}` | `{results['chi2_summary']['bao']['planck_chi2_per_dof']}` | `{results['chi2_summary']['bao']['delta_chi2_io_minus_planck']}` |
| Combined | `{n_total}` | `{n_total}` | `{results['chi2_summary']['combined']['io_chi2']}` | `{results['chi2_summary']['combined']['io_chi2_per_dof']}` | `{results['chi2_summary']['combined']['planck_chi2']}` | `{results['chi2_summary']['combined']['planck_chi2_per_dof']}` | `{results['chi2_summary']['combined']['delta_chi2_io_minus_planck']}` |

## Replacement of dead Schur numbers

| dataset | old dead Schur χ² | new i.i.d. χ² | delta new-old |
|---|---:|---:|---:|
| CC | `15.57` | `{results['chi2_summary']['cc']['io_chi2']}` | `{results['chi2_summary']['cc']['io_chi2'] - 15.57}` |
| BAO | `26.91` | `{results['chi2_summary']['bao']['io_chi2']}` | `{results['chi2_summary']['bao']['io_chi2'] - 26.91}` |
| Combined | `42.48` | `{results['chi2_summary']['combined']['io_chi2']}` | `{results['chi2_summary']['combined']['io_chi2'] - 42.48}` |

## Residual tables

- full CC residuals: `{OUT_CC_CSV.name}`
- full BAO residuals: `{OUT_BAO_CSV.name}`

### CC residuals — IO i.i.d.

{format_markdown_table(cc_report_rows_io, ['z', 'H_obs', 'sigma', 'H_model', 'residual', 'pull', 'source'])}

### CC residuals — Planck LCDM

{format_markdown_table(cc_report_rows_planck, ['z', 'H_obs', 'sigma', 'H_model', 'residual', 'pull', 'source'])}

### BAO residuals — IO i.i.d.

{format_markdown_table(bao_report_rows_io, ['z', 'quantity', 'obs', 'sigma_diag', 'model', 'residual', 'naive_pull'])}

### BAO residuals — Planck LCDM

{format_markdown_table(bao_report_rows_planck, ['z', 'quantity', 'obs', 'sigma_diag', 'model', 'residual', 'naive_pull'])}

## Notes

- BAO total χ² uses the full published covariance.
- The BAO row table records raw residuals and diagonal-error naive pulls for inspectability; those are not the total correlated χ² contributions.
- The evaluator includes the requested radiation term. Because the user-specified branch display values omit radiation from closure, `Omega_lambda_eval` is closure-corrected so that `E(0)=1`.
"""

    OUT_JSON.write_text(json.dumps(results, indent=2))
    OUT_REPORT.write_text(report)


if __name__ == "__main__":
    main()
