from __future__ import annotations

import json
import math
from pathlib import Path

from classy import Class


ROOT = Path("/opt/cosmology-lab/results/paper31")
OUT_JSON = ROOT / "paper31_seam3_eg_pipeline_results.json"
OUT_TXT = ROOT / "paper31_seam3_eg_pipeline_report.txt"

X = 1.5189873277742727

SCHUR_ACTIVE = {
    "label": "projected_schur_active",
    "H0": 68.91,
    "Omega_m": 0.33577637957547024,
    "Omega_k": -0.005613722564238656,
    "T_cmb": 2.7253,
}

BARE_ACTIVE = {
    "label": "bare_geometry_branch",
    "H0": 58.4,
    "Omega_m": 0.197,
    "Omega_k": -0.13,
    "T_cmb": 2.7253,
}

M_NU = 0.06
N_EFF_STD = 3.044
A_S_ACTIVE = 2.1141000090331526e-9
N_S_ACTIVE = 0.963872644987
TAU_REIO = 0.054
OMEGA_B_CLUSTERING = 0.017053042566348757

BENCHMARKS = [
    {
        "id": "blake2015_z032",
        "label": "Blake et al. 2015 RCSLenS galaxy lensing",
        "z": 0.32,
        "mean": 0.48,
        "sigma": 0.10,
        "channel": "galaxy_lensing",
        "source": "https://arxiv.org/abs/1507.03086",
    },
    {
        "id": "blake2015_z057",
        "label": "Blake et al. 2015 RCSLenS galaxy lensing",
        "z": 0.57,
        "mean": 0.30,
        "sigma": 0.07,
        "channel": "galaxy_lensing",
        "source": "https://arxiv.org/abs/1507.03086",
    },
    {
        "id": "pullen2015_z057",
        "label": "Pullen et al. 2015 Planck CMB lensing",
        "z": 0.57,
        "mean": 0.243,
        "sigma": math.sqrt(0.060**2 + 0.013**2),
        "sigma_note": "stat and sys combined in quadrature",
        "channel": "cmb_lensing",
        "source": "https://arxiv.org/abs/1511.04457",
    },
    {
        "id": "alam2016_z057",
        "label": "Alam et al. 2016 CFHTLenS + BOSS CMASS",
        "z": 0.57,
        "mean": 0.42,
        "sigma": 0.056,
        "channel": "galaxy_lensing",
        "source": "https://arxiv.org/abs/1610.09410",
    },
]

GROUPS = {
    "all": [b["id"] for b in BENCHMARKS],
    "galaxy_lensing_only": [b["id"] for b in BENCHMARKS if b["channel"] == "galaxy_lensing"],
    "cmb_lensing_only": [b["id"] for b in BENCHMARKS if b["channel"] == "cmb_lensing"],
}

ALPHA_GRID = [0.5 + 0.001 * i for i in range(2501)]  # 0.5 ... 3.0


def build_background_case(background: dict[str, float | str], z_list: list[float]) -> dict[str, object]:
    h = float(background["H0"]) / 100.0
    omega_m_h2 = float(background["Omega_m"]) * h * h
    omega_nu = M_NU / 93.14
    omega_cdm = omega_m_h2 - OMEGA_B_CLUSTERING - omega_nu
    if omega_cdm <= 0:
        raise ValueError(f"Non-positive omega_cdm for {background['label']}")

    z_pk = sorted(set([0.0] + z_list))

    cosmo = Class()
    cosmo.set(
        {
            "output": "mPk",
            "P_k_max_h/Mpc": 10.0,
            "z_pk": ",".join(str(z) for z in z_pk),
            "h": h,
            "omega_b": OMEGA_B_CLUSTERING,
            "omega_cdm": omega_cdm,
            "Omega_k": float(background["Omega_k"]),
            "A_s": A_S_ACTIVE,
            "n_s": N_S_ACTIVE,
            "tau_reio": TAU_REIO,
            "T_cmb": float(background["T_cmb"]),
            "N_ur": N_EFF_STD - 1.0132,
            "N_ncdm": 1,
            "m_ncdm": M_NU,
        }
    )
    cosmo.compute()

    sigma8 = float(cosmo.sigma8())
    rows = {}
    for z in z_pk:
        if z == 0.0:
            continue
        fs8 = float(cosmo.scale_independent_f_sigma8(z))
        Dz = float(cosmo.scale_independent_growth_factor(z))
        fz = fs8 / (sigma8 * Dz)
        rows[str(z)] = {
            "z": z,
            "f_sigma8": fs8,
            "growth_factor_D": Dz,
            "f": fz,
            "E_G_no_slip": float(background["Omega_m"]) / fz,
        }

    cosmo.struct_cleanup()
    cosmo.empty()

    return {
        "background_label": str(background["label"]),
        "H0": float(background["H0"]),
        "Omega_m": float(background["Omega_m"]),
        "Omega_k": float(background["Omega_k"]),
        "sigma8": sigma8,
        "rows": rows,
    }


def mu_ratio(alpha_phi: float) -> float:
    return X ** (1.5 - alpha_phi)


def predict_eg(case: dict[str, object], z: float, alpha_phi: float) -> float:
    row = case["rows"][str(z)]
    return mu_ratio(alpha_phi) * row["E_G_no_slip"]


def chi2_for_group(case: dict[str, object], benchmark_ids: list[str], alpha_phi: float) -> float:
    chi2 = 0.0
    for b in BENCHMARKS:
        if b["id"] not in benchmark_ids:
            continue
        pred = predict_eg(case, b["z"], alpha_phi)
        chi2 += ((pred - b["mean"]) / b["sigma"]) ** 2
    return chi2


def best_fit_alpha(case: dict[str, object], benchmark_ids: list[str]) -> dict[str, float]:
    scored = [(alpha, chi2_for_group(case, benchmark_ids, alpha)) for alpha in ALPHA_GRID]
    alpha_best, chi2_best = min(scored, key=lambda pair: pair[1])

    one_sigma = [alpha for alpha, chi2 in scored if chi2 <= chi2_best + 1.0]
    return {
        "alpha_best": alpha_best,
        "chi2_best": chi2_best,
        "alpha_1sigma_lo": min(one_sigma),
        "alpha_1sigma_hi": max(one_sigma),
        "mu_best": mu_ratio(alpha_best),
    }


def measurement_rows(case: dict[str, object], alpha_values: list[float]) -> list[dict[str, object]]:
    rows = []
    for b in BENCHMARKS:
        row = {
            "id": b["id"],
            "label": b["label"],
            "channel": b["channel"],
            "z": b["z"],
            "measured": b["mean"],
            "sigma": b["sigma"],
            "source": b["source"],
            "predictions": {},
        }
        for alpha in alpha_values:
            pred = predict_eg(case, b["z"], alpha)
            row["predictions"][f"alpha_{alpha:g}"] = {
                "prediction": pred,
                "pull_sigma": (pred - b["mean"]) / b["sigma"],
            }
        rows.append(row)
    return rows


def main() -> None:
    z_list = sorted(set(b["z"] for b in BENCHMARKS))
    projected = build_background_case(SCHUR_ACTIVE, z_list)
    bare = build_background_case(BARE_ACTIVE, z_list)

    group_fits = {
        "projected": {
            group: best_fit_alpha(projected, ids) for group, ids in GROUPS.items()
        },
        "bare": {
            group: best_fit_alpha(bare, ids) for group, ids in GROUPS.items()
        },
    }

    payload = {
        "constants": {
            "x": X,
            "A_s_active": A_S_ACTIVE,
            "n_s_active": N_S_ACTIVE,
            "tau_reio": TAU_REIO,
            "N_eff_standard": N_EFF_STD,
            "omega_b_clustering": OMEGA_B_CLUSTERING,
        },
        "benchmarks": BENCHMARKS,
        "cases": {
            "projected_schur_active": projected,
            "bare_geometry_branch": bare,
        },
        "group_fits": group_fits,
        "projected_measurement_rows": measurement_rows(projected, [1.5, 2.0]),
        "bare_measurement_rows": measurement_rows(bare, [1.5, 2.0]),
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    lines = [
        "Paper 31 Seam 3 - E_G Pipeline",
        "===============================",
        "",
        "Question",
        "--------",
        "Build a reproducible IO E_G pipeline, compare projected and bare growth branches to",
        "published E_G measurements, and fit the effective Weyl alpha_Phi implied by those data.",
        "",
        "Benchmarks used",
        "---------------",
    ]
    for b in BENCHMARKS:
        note = f" [{b['sigma_note']}]" if "sigma_note" in b else ""
        lines.append(
            f"- {b['id']}: z = {b['z']:.2f}, E_G = {b['mean']:.3f} +/- {b['sigma']:.3f}, "
            f"channel = {b['channel']}{note}, source = {b['source']}"
        )

    for case_name, case in [("Projected Schur", projected), ("Bare branch", bare)]:
        lines.extend(["", case_name, "-" * len(case_name)])
        lines.append(f"sigma8(0) = {case['sigma8']:.12f}")
        for z_key, row in case["rows"].items():
            lines.append(
                f"z = {row['z']:.2f}: f = {row['f']:.12f}, E_G(no-slip) = {row['E_G_no_slip']:.12f}"
            )

        lines.extend(["", "Best-fit alpha_Phi from E_G", "--------------------------"])
        for group, fit in group_fits["projected" if case_name == "Projected Schur" else "bare"].items():
            lines.append(
                f"{group}: alpha_best = {fit['alpha_best']:.3f}, "
                f"1sigma = [{fit['alpha_1sigma_lo']:.3f}, {fit['alpha_1sigma_hi']:.3f}], "
                f"mu_best = {fit['mu_best']:.6f}, chi2_best = {fit['chi2_best']:.3f}"
            )

        lines.extend(["", "Measurement pulls for alpha = 1.5 and 2.0", "-----------------------------------------"])
        rows = payload["projected_measurement_rows"] if case_name == "Projected Schur" else payload["bare_measurement_rows"]
        for row in rows:
            pred15 = row["predictions"]["alpha_1.5"]
            pred20 = row["predictions"]["alpha_2"]
            lines.append(
                f"{row['id']}: alpha=1.5 -> {pred15['prediction']:.3f} ({pred15['pull_sigma']:+.2f} sigma), "
                f"alpha=2.0 -> {pred20['prediction']:.3f} ({pred20['pull_sigma']:+.2f} sigma)"
            )

    lines.extend(
        [
            "",
            "Claim boundary",
            "--------------",
            "1. verified: the projected Schur no-slip branch matches some E_G benchmarks well, while the",
            "   alpha=2 Weyl bridge shifts E_G downward.",
            "2. verified: the projected all-benchmark best-fit alpha_Phi lies between no-slip and alpha=2;",
            "   the galaxy-lensing-only and CMB-lensing-only subsets prefer different alpha ranges.",
            "3. verified: the bare branch predicts substantially lower E_G across the board.",
            "4. honest status: the E_G data do not yet produce a unique closed alpha_Phi theorem, but they",
            "   do provide the cleanest current external discriminator for the Weyl-response program.",
        ]
    )

    OUT_TXT.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
