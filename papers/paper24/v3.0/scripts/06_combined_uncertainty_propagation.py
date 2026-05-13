#!/usr/bin/env python3
"""
Paper 24 v3.0 reproducibility script 06.

Purpose:
    Propagate the combined imported nuclear-input uncertainty for the Paper 24
    Henderson primary lithium row. The script samples the ground-state
    quadrupole input Q_GS and the Henderson excited-state B(E2) input, pushes
    both through the Paper 24 branch-sum rate formula, and maps the resulting
    R_34,tot variation to Li-7/H using the banked PRyMordial local sensitivity
    exponent.

Inputs:
    - data/imported_constants.json
    - results/final_excited_branch_results.json
    - results/excited_state_import_recomputation_results.json

Outputs:
    - results/combined_uncertainty_propagation_results.json

External dependencies:
    Python standard library only. This script intentionally does not run
    PRyMordial for every Monte Carlo sample; 100,000 full network solves would
    be unnecessary for a reviewer-facing uncertainty propagation. The mapping
    Li7/H(sample) = Li7/H(central) * (R34_tot(sample)/R34_tot(central))^0.963
    uses the Paper 24 banked PRyMordial sensitivity matrix for the
    3He(alpha,gamma)7Be channel.

Claim boundary:
    VERIFIED: Monte Carlo propagation of imported Q_GS and Henderson B(E2)
    uncertainties through the frozen Paper 24 v3.0 branch-sum arithmetic.
    IMPORTED/EMPIRICAL: Q_GS and Henderson B(E2) source values.
    DERIVED/CONDITIONAL_VERIFIED: branch-sum formula and rate-dressing
    structure, with dependency on the Paper 24 theorem chain.

Run:
    python3 scripts/06_combined_uncertainty_propagation.py
    python3 scripts/05_validate_expected_outputs.py
"""
from __future__ import annotations

import json
import math
import random
import time
from pathlib import Path
from typing import Iterable


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_JSON = BUNDLE_ROOT / "data" / "imported_constants.json"
FINAL_RESULTS_JSON = BUNDLE_ROOT / "results" / "final_excited_branch_results.json"
IMPORT_RESULTS_JSON = BUNDLE_ROOT / "results" / "excited_state_import_recomputation_results.json"
OUT_JSON = BUNDLE_ROOT / "results" / "combined_uncertainty_propagation_results.json"

N_SAMPLES = 100_000
SEED = 240630


def timestamp() -> str:
    """Return a stable UTC timestamp string for result provenance."""

    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def percentile(sorted_values: list[float], percent: float) -> float:
    """Return a linearly interpolated percentile from an already sorted list."""

    if not sorted_values:
        raise ValueError("percentile requires at least one value")
    if not 0.0 <= percent <= 100.0:
        raise ValueError("percent must be in [0, 100]")
    if len(sorted_values) == 1:
        return sorted_values[0]
    position = (percent / 100.0) * (len(sorted_values) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return (1.0 - weight) * sorted_values[lower] + weight * sorted_values[upper]


def summarize(values: Iterable[float]) -> dict[str, float]:
    """Return median, one-sigma, and two-sigma percentile summaries."""

    sorted_values = sorted(values)
    return {
        "p2_3": percentile(sorted_values, 2.3),
        "p16": percentile(sorted_values, 16.0),
        "median": percentile(sorted_values, 50.0),
        "p84": percentile(sorted_values, 84.0),
        "p97_7": percentile(sorted_values, 97.7),
        "mean": sum(sorted_values) / len(sorted_values),
        "min": sorted_values[0],
        "max": sorted_values[-1],
    }


def sample_positive_gaussian(rng: random.Random, mean: float, sigma: float) -> float:
    """Sample a positive Gaussian variate by rejection.

    The imported nuclear quantities are physical magnitudes. Negative draws are
    discarded rather than clipped so the output is not biased by a pile-up at
    zero. Rejection rates are tiny for Q_GS and Henderson B(E2).
    """

    while True:
        value = rng.gauss(mean, sigma)
        if value > 0.0:
            return value


def sample_henderson_b_up(rng: random.Random, mean: float, stat_sigma: float, sys_sigma: float) -> float:
    """Sample Henderson B(E2 up) with separate statistical and systematic terms."""

    while True:
        value = mean + rng.gauss(0.0, stat_sigma) + rng.gauss(0.0, sys_sigma)
        if value > 0.0:
            return value


def r_gs(q_gs_barn: float, constants: dict[str, float]) -> float:
    """Ground-state branch dressing from Q_GS through the Paper 24 formula."""

    q_gs_proj = constants["chi_ME_7Be"] * q_gs_barn / constants["x"]
    xi = (q_gs_proj / constants["Q_d_barn"]) * constants["nu_34_T9eff"]
    return math.exp(-constants["epsilon_n"] * xi)


def r_ex_from_b_up(b_up_e2fm4: float, constants: dict[str, float], amp_weighted_f0: float) -> tuple[float, float, float]:
    """Excited-state branch dressing from Henderson B(E2 up).

    Returns:
        (R_ex, q_trans_ex_barn, B_down_e2fm4)
    """

    b_down = 2.0 * b_up_e2fm4
    q_scale_b = math.sqrt(b_down) / 100.0
    q_trans_ex = q_scale_b * amp_weighted_f0
    xi = ((q_trans_ex / constants["x"]) / constants["Q_d_barn"]) * constants["nu_34_T9eff"]
    return math.exp(-constants["epsilon_n"] * xi), q_trans_ex, b_down


def r34_total(r_gs_value: float, r_ex_value: float, f_gs: float) -> float:
    """Paper 24 branch-sum rate multiplier."""

    return f_gs * r_gs_value + (1.0 - f_gs) * r_ex_value


def compute() -> dict[str, object]:
    """Run the combined uncertainty propagation and return a JSON payload."""

    constants_payload = json.loads(DATA_JSON.read_text())
    final_payload = json.loads(FINAL_RESULTS_JSON.read_text())
    import_payload = json.loads(IMPORT_RESULTS_JSON.read_text())

    constants = dict(constants_payload["framework_constants"])
    obs = constants_payload["observational_denominators"]
    henderson = constants_payload["henderson_2019"]
    central_case = import_payload["import_cases"][0]
    amp_weighted_f0 = final_payload["kernel_excited_state"]["amp_weighted_avg_F0"]

    central_r34 = central_case["R_34_tot_T9eff"]
    central_li7 = central_case["Li7_H"]
    sensitivity_exp = constants["Li7_R34_sensitivity_exponent"]

    rng = random.Random(SEED)
    r_values: list[float] = []
    li_values: list[float] = []
    q_samples: list[float] = []
    b_up_samples: list[float] = []
    b_down_samples: list[float] = []
    q_trans_samples: list[float] = []

    for _ in range(N_SAMPLES):
        q_gs_sample = sample_positive_gaussian(
            rng,
            constants["Q_GS_7Be_barn"],
            constants["Q_GS_7Be_sigma_barn"],
        )
        b_up_sample = sample_henderson_b_up(
            rng,
            henderson["B_E2_up_e2fm4"],
            henderson["B_E2_stat_e2fm4"],
            henderson["B_E2_sys_e2fm4"],
        )
        rg = r_gs(q_gs_sample, constants)
        re, q_trans, b_down = r_ex_from_b_up(b_up_sample, constants, amp_weighted_f0)
        r_total = r34_total(rg, re, constants["f_gs"])
        li7 = central_li7 * ((r_total / central_r34) ** sensitivity_exp)

        r_values.append(r_total)
        li_values.append(li7)
        q_samples.append(q_gs_sample)
        b_up_samples.append(b_up_sample)
        b_down_samples.append(b_down)
        q_trans_samples.append(q_trans)

    li_summary = summarize(li_values)
    r_summary = summarize(r_values)
    obs_li = obs["Li7_H_obs"]
    obs_sigma = obs["Li7_H_sigma"]

    return {
        "paper": "Paper 24 v3.0",
        "classification": "VERIFIED / Monte Carlo combined uncertainty propagation",
        "generated_utc": timestamp(),
        "method": {
            "samples": N_SAMPLES,
            "seed": SEED,
            "Q_GS_sampling": "positive Gaussian, mean 0.068 b, sigma 0.005 b",
            "Henderson_B_E2_sampling": "B_up = 26 + N(0,6_stat) + N(0,3_sys) e^2 fm^4, reject non-positive draws, B_down = 2*B_up",
            "nonlinear_propagation": "q_trans = sqrt(B_down)/100 * <F0>_amp,ex; R = exp(-epsilon_n * Xi); output quantiles are not symmetrized",
            "Li7_mapping": "Li7/H(sample) = Li7/H(central) * (R34_tot(sample)/R34_tot(central))^0.963",
            "full_network_note": "Full PRyMordial network reruns for 100000 samples are not shipped; the public propagation uses the banked Paper 24 PRyMordial sensitivity exponent for the 3He(alpha,gamma)7Be channel.",
        },
        "inputs": {
            "Q_GS_7Be_barn": constants["Q_GS_7Be_barn"],
            "Q_GS_7Be_sigma_barn": constants["Q_GS_7Be_sigma_barn"],
            "Henderson_B_E2_up_e2fm4": henderson["B_E2_up_e2fm4"],
            "Henderson_B_E2_stat_e2fm4": henderson["B_E2_stat_e2fm4"],
            "Henderson_B_E2_sys_e2fm4": henderson["B_E2_sys_e2fm4"],
            "Henderson_B_E2_down_central_e2fm4": henderson["B_E2_down_corrected_e2fm4"],
            "amp_weighted_avg_F0": amp_weighted_f0,
            "epsilon_n": constants["epsilon_n"],
            "x": constants["x"],
            "Q_d_barn": constants["Q_d_barn"],
            "chi_ME_7Be": constants["chi_ME_7Be"],
            "f_gs": constants["f_gs"],
            "nu_34_T9eff": constants["nu_34_T9eff"],
            "central_R34_tot": central_r34,
            "central_Li7_H": central_li7,
            "Li7_R34_sensitivity_exponent": sensitivity_exp,
        },
        "sample_summaries": {
            "Q_GS_7Be_barn": summarize(q_samples),
            "Henderson_B_E2_up_e2fm4": summarize(b_up_samples),
            "Henderson_B_E2_down_e2fm4": summarize(b_down_samples),
            "q_trans_ex_barn": summarize(q_trans_samples),
            "R34_tot_T9eff": r_summary,
            "Li7_H": li_summary,
        },
        "comparison_to_observation": {
            "observed_Li7_H": obs_li,
            "observed_Li7_sigma": obs_sigma,
            "central_residual_sigma": (central_li7 - obs_li) / obs_sigma,
            "median_residual_sigma": (li_summary["median"] - obs_li) / obs_sigma,
            "observation_inside_predicted_1sigma_band": li_summary["p16"] <= obs_li <= li_summary["p84"],
            "observation_inside_predicted_2sigma_band": li_summary["p2_3"] <= obs_li <= li_summary["p97_7"],
        },
        "chain": [
            "Premise 1: IO closed-interior geometry fixes x and the branch projection used in the Paper 24 rate-dressing chain.",
            "Premise 2: A=7 nuclear response inputs are imported from accepted exterior nuclear physics without IO retuning.",
            "Navratil et al. 2011 / NCSM input: |Q_GS(7Be)| = 0.068 +/- 0.005 b as used in Paper 24 v3.0.",
            "Henderson et al. 2019, Phys. Rev. C 99, 064320: B(E2; 3/2- -> 1/2-) = 26(6)_stat(3)_syst e^2 fm^4; detailed balance gives B_down = 2 B_up.",
            "Paper 24 v3.0 branch-sum formula: R34_tot = f_gs R_gs + (1-f_gs) R_ex.",
            "Paper 24 banked PRyMordial sensitivity exponent: d ln(Li7/H) / d ln(R34_tot) = 0.963 for this channel.",
            "Standard Monte Carlo propagation with fixed random seed.",
        ],
    }


def main() -> int:
    """Write the combined uncertainty propagation JSON."""

    payload = compute()
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "state": "written",
        "path": str(OUT_JSON.relative_to(BUNDLE_ROOT)),
        "samples": N_SAMPLES,
        "Li7_H": payload["sample_summaries"]["Li7_H"],
        "R34_tot_T9eff": payload["sample_summaries"]["R34_tot_T9eff"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
