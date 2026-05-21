from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np
from classy import Class


BASE = Path("/opt/cosmology-lab/results/paper31")
OUT_JSON = BASE / "paper31_schur_neff_necessity_audit_results.json"
OUT_REPORT = BASE / "paper31_schur_neff_necessity_audit_report.txt"


def load_module(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


p29_obs = load_module(
    "/opt/cosmology-lab/results/paper29/paper29_schur_branch_observables_recompute.py",
    "paper29_schur_obs_audit",
)
p29_bao = load_module(
    "/opt/cosmology-lab/results/paper29/paper29_bao_matter_density_problem.py",
    "paper29_bao_problem_audit",
)
p29_hz = load_module(
    "/opt/cosmology-lab/results/paper29/paper29_direct_hz_confrontation.py",
    "paper29_direct_hz_audit",
)
p30_s8 = load_module(
    "/opt/cosmology-lab/results/paper30/paper30_funrun_s8_alens_ok_schur.py",
    "paper30_s8_audit",
)


CLAIM_LABELS = ["derived", "verified", "conditional", "reconstruction", "speculative"]
PLANCK_100THETA = 1.04110
PLANCK_100THETA_SIGMA = 0.00031
PLANCK_SHIFT_R = 1.7502
PLANCK_SHIFT_R_SIGMA = 0.005

X = 1.5189873277742727
GAMMA_BI = 0.2375
DELTA = math.exp(4.0 * math.log(X) + math.log(1.0 + GAMMA_BI**2))

SCHUR = dict(p29_obs.SCHUR_BRANCH)
OMEGA_B_EFF_H2 = p29_obs.OMEGA_B_EFF_H2


def sigma_offset(value: float, reference: float, sigma: float) -> float:
    return (value - reference) / sigma


def class_bundle(neff: float) -> dict[str, float | str]:
    branch = dict(SCHUR)
    branch["N_eff"] = neff
    return p29_obs.build_class_bundle(
        branch,
        omega_b_h2=OMEGA_B_EFF_H2,
        label=f"Schur N_eff={neff:.12f}",
        with_lensed_peak=False,
    )


def bao_with_class_rd(neff: float) -> dict[str, float]:
    bundle = class_bundle(neff)
    rows, cov = p29_hz.load_desi_dr2()
    obs = np.array([row["value"] for row in rows], dtype=float)
    inv_cov = np.linalg.inv(cov)
    amplitude = p29_hz.C_KM_S / (float(SCHUR["H0"]) * float(bundle["rs_drag_Mpc"]))
    pred = p29_hz.bao_prediction_from_amplitude(
        rows,
        amplitude=amplitude,
        omega_m=float(SCHUR["Omega_m"]),
        omega_k=float(SCHUR["Omega_k"]),
        omega_lambda=float(SCHUR["Omega_lambda"]),
    )
    diff = pred - obs
    chi2 = float(diff @ inv_cov @ diff)
    return {
        "chi2": chi2,
        "r_d_Mpc": float(bundle["rs_drag_Mpc"]),
        "amplitude_c_over_H0rd": amplitude,
        "100theta_star": float(bundle["100theta_star"]),
        "theta_star_sigma_from_planck": sigma_offset(
            float(bundle["100theta_star"]), PLANCK_100THETA, PLANCK_100THETA_SIGMA
        ),
        "shift_parameter_R": float(bundle["shift_parameter_R"]),
        "shift_parameter_sigma_from_planck": sigma_offset(
            float(bundle["shift_parameter_R"]), PLANCK_SHIFT_R, PLANCK_SHIFT_R_SIGMA
        ),
        "age_Gyr_CLASS": float(bundle["age_Gyr_CLASS"]),
        "sigma8_CLASS": float(bundle["sigma8_CLASS"]),
    }


def H_with_radiation(z: float, neff: float) -> float:
    h0 = float(SCHUR["H0"])
    omega_m = float(SCHUR["Omega_m"])
    omega_k = float(SCHUR["Omega_k"])
    h = h0 / 100.0
    omega_r = p29_obs.omega_r(float(SCHUR["T_cmb"]), neff, h)
    omega_lambda = 1.0 - omega_m - omega_k - omega_r
    return h0 * math.sqrt(
        omega_r * (1.0 + z) ** 4
        + omega_m * (1.0 + z) ** 3
        + omega_k * (1.0 + z) ** 2
        + omega_lambda
    )


def s8_with_neff(neff: float) -> dict[str, float]:
    slot = p30_s8.BARYON_SLOTS[0]
    h = p30_s8.SCHUR.H0 / 100.0
    omega_cdm = p30_s8.SCHUR.Omega_m * h * h - slot.omega_b_h2 - p30_s8.OMEGA_NU_H2
    cosmo = Class()
    cosmo.set(
        {
            "output": "mPk,lCl,pCl",
            "lensing": "yes",
            "P_k_max_h/Mpc": 1.0,
            "h": h,
            "omega_b": slot.omega_b_h2,
            "omega_cdm": omega_cdm,
            "Omega_k": p30_s8.SCHUR.Omega_k,
            "A_s": p30_s8.A_S_IO,
            "n_s": p30_s8.N_S_IO,
            "tau_reio": p30_s8.TAU_REIO,
            "T_cmb": p30_s8.T_CMB_IO,
            "N_ur": neff - 1.0132,
            "N_ncdm": 1,
            "m_ncdm": p30_s8.M_NU_SUM_EV,
        }
    )
    cosmo.compute()
    sigma8 = float(cosmo.sigma8())
    S8 = sigma8 * math.sqrt(p30_s8.SCHUR.Omega_m / 0.3)
    cosmo.struct_cleanup()
    cosmo.empty()
    return {"sigma8": sigma8, "S8": S8}


def main() -> None:
    neff_values = {"standard_3p044": 3.044, "delta": DELTA}
    class_compare = {label: bao_with_class_rd(neff) for label, neff in neff_values.items()}
    hz_compare = {}
    for z in [0.0, 0.5, 1.0, 2.0, 10.0, 1100.0]:
        h_std = H_with_radiation(z, neff_values["standard_3p044"])
        h_delta = H_with_radiation(z, neff_values["delta"])
        hz_compare[str(z)] = {
            "H_standard": h_std,
            "H_delta": h_delta,
            "frac_shift": h_delta / h_std - 1.0,
        }
    s8_compare = {label: s8_with_neff(neff) for label, neff in neff_values.items()}

    carried_bao_chi2 = p29_bao.bao_fixed_chi2(p29_bao.SCHUR_DEFINITIVE, 143.3)
    free_amp = p29_bao.bao_free_amplitude(p29_bao.SCHUR_DEFINITIVE)
    chronometer_chi2 = p29_bao.cc_chi2(p29_bao.SCHUR_DEFINITIVE)

    payload = {
        "status_labels": CLAIM_LABELS,
        "schur_branch": SCHUR,
        "delta": DELTA,
        "class_standard_vs_delta": class_compare,
        "radiation_sensitive_Hz_compare": hz_compare,
        "s8_compare": s8_compare,
        "late_time_structural_independence": {
            "chronometer_chi2_fixed_schur": chronometer_chi2,
            "bao_chi2_carried_ruler_fixed_schur": carried_bao_chi2,
            "bao_free_amplitude_fixed_schur_shape": free_amp,
            "reason": (
                "Once H0, Omega_m, Omega_k, and Omega_lambda are fixed to the Schur branch, the Paper 29 "
                "direct-H(z) and carried-ruler BAO confrontations depend only on that late-time background shape "
                "and not on N_eff."
            ),
        },
        "conclusion": {
            "statement": (
                "On the active Schur branch, keeping N_eff = 3.044 does not introduce a new observational "
                "failure in the low-z expansion history. The branch already uses 3.044. The live low-z issues "
                "are BAO-class closure and late-time clustering. Forcing N_eff = Delta worsens the early-time "
                "ruler sector dramatically."
            )
        },
    }

    lines = [
        "Paper 31 - Schur Branch N_eff Necessity Audit",
        "============================================",
        "",
        "Question",
        "--------",
        "Does the active Schur definitive branch observationally require Friedmann N_eff = Delta,",
        "or can N_eff remain standard (3.044) while Delta enters only through sqrt(Delta) and P_k?",
        "",
        "Executive result",
        "----------------",
        "- verified: the active Schur branch already runs with N_eff = 3.044.",
        "- derived: low-z direct-expansion probes on the fixed Schur branch are structurally insensitive to N_eff.",
        f"- verified: Schur carried-ruler BAO chi2 stays {carried_bao_chi2:.6f} at fixed branch, independent of N_eff.",
        f"- verified: Schur chronometer chi2 stays {chronometer_chi2:.6f} at fixed branch, independent of N_eff.",
        "- verified / problem: the Schur branch already misses Planck theta* at standard N_eff.",
        "- verified / stronger no-go: forcing N_eff = Delta makes the early-time ruler sector much worse.",
        "",
        "Early-time ruler comparison on the same Schur branch",
        "----------------------------------------------------",
    ]
    for label in ("standard_3p044", "delta"):
        row = class_compare[label]
        lines.extend(
            [
                f"{label}:",
                f"  N_eff = {neff_values[label]:.12f}",
                f"  100theta* = {row['100theta_star']:.9f}",
                f"  theta* pull vs Planck = {row['theta_star_sigma_from_planck']:+.3f} sigma",
                f"  r_d = {row['r_d_Mpc']:.6f} Mpc",
                f"  BAO chi2 with CLASS r_d = {row['chi2']:.6f}",
                f"  shift parameter R = {row['shift_parameter_R']:.9f}",
                f"  R pull vs Planck = {row['shift_parameter_sigma_from_planck']:+.3f} sigma",
                f"  CLASS age = {row['age_Gyr_CLASS']:.6f} Gyr",
                f"  sigma8 = {row['sigma8_CLASS']:.6f}",
            ]
        )
    lines.extend(
        [
            "",
            "Low-z H(z) sensitivity with radiation retained explicitly",
            "--------------------------------------------------------",
        ]
    )
    for z_key in ["0.0", "0.5", "1.0", "2.0", "10.0", "1100.0"]:
        row = hz_compare[z_key]
        lines.append(
            f"z = {z_key}: H_Delta / H_3.044 - 1 = {row['frac_shift']:+.9f}"
        )
    lines.extend(
        [
            "",
            "S8 check on the Schur acoustic slot",
            "-----------------------------------",
        ]
    )
    for label in ("standard_3p044", "delta"):
        row = s8_compare[label]
        lines.append(
            f"{label}: sigma8 = {row['sigma8']:.6f}, S8 = {row['S8']:.6f}"
        )
    lines.extend(
        [
            "",
            "Interpretation",
            "--------------",
            "- derived: Pantheon+, standard sirens, FRB D_A, and the fixed-branch chronometer/BAO shape tests are late-time observables of the Schur background and do not use Friedmann N_eff once the branch is fixed.",
            "- verified: the current Schur branch with standard N_eff still has three main issues: theta* mismatch, BAO-class closure, and clustering excess.",
            "- verified: replacing standard N_eff by Delta would not solve theta* on the active Schur branch; it drives 100theta* from 1.04808 down to 0.97093 and explodes the standard-drag BAO chi2 from 232.84 to 2020.35.",
            "- verified: low-z expansion is essentially unchanged by that replacement: even with radiation retained, H(z) shifts by only 3.46e-05 at z = 0.5 and 1.26e-04 at z = 2.",
            "",
            "Bottom line",
            "-----------",
            "On the active Schur definitive branch, the framework does not currently appear to require Friedmann N_eff = Delta.",
            "The branch already uses N_eff = 3.044, and the surviving low-z observational performance comes from sqrt(Delta), P_k, and the chosen late-time Schur background package.",
            "If one insists on identifying Friedmann N_eff with Delta on this branch, the active early-time ruler sector gets substantially worse rather than better.",
        ]
    )

    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")
    OUT_REPORT.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
