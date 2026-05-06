#!/usr/bin/env python3
"""
Paper 32 v1.6 reproducibility script 09.

Purpose:
    Generate the R4/FIRAS impact ledger for the Paper 32 v1.6 repair.

    This script is intentionally not a theorem prover.  It records the exact
    numerical impact of replacing the retired unit optical readout

        R4 = 1

    with the Paper 17 v1.5 FIRAS-fixed value

        R4_FIRAS = ln(T_FIRAS/T_IO) / (K_gauge * ln x)
                 = 1.0031014644105183.

    It also classifies each Paper 32 public script by whether that R4 repair
    changes its calculation.

Inputs:
    - data/imported_constants.json

Outputs:
    - results/r4_firas_impact_audit_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / impact-audit ledger.  The kappa-style structural conclusions
    are in reports/paper32_v16_r4_firas_kappa_audit_report.md.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "r4_firas_impact_audit_results.json"


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    c = payload["framework_constants"]

    gamma = c["gamma_BI"]
    x = c["x"]
    t_io = c["T_IO_K"]
    t_firas = c["T_FIRAS_K"]
    sigma_t_firas = c["sigma_T_FIRAS_K"]

    q = 1.0 + gamma**2
    k_gauge = math.log(q)
    ln_x = math.log(x)
    r4_firas = math.log(t_firas / t_io) / (k_gauge * ln_x)
    t_r4_1 = t_io * x**k_gauge
    t_r4_firas = t_io * x ** (r4_firas * k_gauge)

    script_impacts = [
        {
            "script": "01_compute_framework_constants.py",
            "r4_damage_status": "impacted_and_repaired",
            "reason": "v1.5 computed T_obs = T_IO*x^K_gauge as active observed CMB value; v1.6 computes T_obs(R4_FIRAS) and keeps R4=1 only as historical diagnostic."
        },
        {
            "script": "02_recollapse_acceleration.py",
            "r4_damage_status": "not_impacted",
            "reason": "Uses c and r_s only; no optical readout normalization."
        },
        {
            "script": "03_x_crit_identity.py",
            "r4_damage_status": "not_impacted",
            "reason": "Uses Q and x in Delta boundary identity; no T_obs or R4."
        },
        {
            "script": "04_recollapse_cycle_timescales.py",
            "r4_damage_status": "not_impacted",
            "reason": "Uses r_s, c, and bounce attachment ledger; no T_obs or R4."
        },
        {
            "script": "05_kb7_source_block_validation.py",
            "r4_damage_status": "wording_boundary_only",
            "reason": "KB7 validates P4 on the active reduced scalar source block; it must not be read as deriving Paper 17 optical thermal R4."
        },
        {
            "script": "06_n_s_derivation_chain.py",
            "r4_damage_status": "not_impacted",
            "reason": "Uses n_s = 1 - K_gauge/x; no optical R4."
        },
        {
            "script": "07_a_s_derivation_chain.py",
            "r4_damage_status": "not_impacted",
            "reason": "Uses Hawking boundary-state amplitude formula; no optical R4."
        },
        {
            "script": "08_universal_gmp_classification.py",
            "r4_damage_status": "not_impacted",
            "reason": "Classifies GMP domains; no CMB-temperature calculation."
        },
        {
            "script": "10_validate_expected_outputs.py",
            "r4_damage_status": "impacted_and_repaired",
            "reason": "Validation expectations changed from T_obs_K at R4=1 to T_obs_FIRAS_fixed_K and R4_FIRAS."
        }
    ]

    manuscript_damage_locations = [
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraph": 305,
            "damage": "Claims zero-free-parameter predictions for T_CMB.",
            "v1_6_action": "Retire independent T_CMB prediction wording; state T_IO is derived and observed CMB is FIRAS-normalized through Paper 17 v1.5."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraph": 350,
            "damage": "States T_obs = T_IO*x^K_gauge = 2.7253 K as active formula.",
            "v1_6_action": "Replace with T_obs(R4)=T_IO*x^(R4*K_gauge), R4_FIRAS=1.0031014644105183."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraph": 442,
            "damage": "Code/Data section points to v1.5 bundle and unqualified T_obs reproduction.",
            "v1_6_action": "Update to v1.6 bundle and describe T_obs as FIRAS-fixed readout."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraph": 446,
            "damage": "Open Problems list merges R4/P4 normalization and marks it closed by KB7.",
            "v1_6_action": "Split P4 source-block closure from Paper 17 optical R4. P4 remains DERIVED/SCOPED by KB7; R4 is FIRAS-fixed by Paper 17 v1.5."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraph": 703,
            "damage": "States T_obs = T_IO*exp(K_gauge/2) = T_IO*sqrt(1+gamma^2) = 2.7253 K.",
            "v1_6_action": "Retire as erroneous/historical; use Paper 17 v1.5 readout family."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraph": 704,
            "damage": "Temperature Transfer Theorem says structural pieces force T_obs = T_IO*x^K_gauge.",
            "v1_6_action": "Downgrade to forcing the readout family and gauge payload; R4 fixed separately by FIRAS."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraphs": [713, 715, 791],
            "damage": "Uses ln(T_obs/T_IO)=K_gauge*ln x or equivalent.",
            "v1_6_action": "Replace with ln(T_obs/T_IO)=R4*K_gauge*ln x for the optical readout family."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraph": 717,
            "damage": "Treats gamma_BI prediction from FIRAS inversion as DERIVED.",
            "v1_6_action": "Reframe as consistency diagnostic, not derivation of gamma_BI from FIRAS."
        },
        {
            "source": "Paper 32 v1.5 extracted text",
            "paragraphs": [764, 765, 766],
            "damage": "R1-R4 / one-e-fold normalization language implies optical R4 forced by modular stack.",
            "v1_6_action": "Separate R1-R3/gauge payload from FIRAS-fixed optical R4."
        }
    ]

    results = {
        "paper": "Paper 32 v1.6",
        "audit": "R4_FIRAS_impact_audit",
        "classification": "verified / impact ledger",
        "numeric_change": {
            "K_gauge": k_gauge,
            "ln_x": ln_x,
            "K_gauge_ln_x": k_gauge * ln_x,
            "R4_unit_historical": 1.0,
            "R4_FIRAS": r4_firas,
            "R4_shift": r4_firas - 1.0,
            "T_IO_K": t_io,
            "T_FIRAS_K": t_firas,
            "sigma_T_FIRAS_K": sigma_t_firas,
            "T_obs_R4_equals_1_K": t_r4_1,
            "T_obs_FIRAS_fixed_K": t_r4_firas,
            "T_obs_R4_equals_1_minus_FIRAS_K": t_r4_1 - t_firas,
            "T_obs_R4_equals_1_minus_FIRAS_sigma": (t_r4_1 - t_firas) / sigma_t_firas,
            "relative_transfer_shift_FIRAS_vs_R4_equals_1": (t_r4_firas / t_r4_1) - 1.0
        },
        "script_impacts": script_impacts,
        "manuscript_damage_locations": manuscript_damage_locations,
        "global_verdict": {
            "hidden_new_parameter_added": False,
            "cmb_prediction_retired": True,
            "downstream_R4_rule": "R4_FIRAS is fixed once by FIRAS and cannot be adjusted against downstream observables.",
            "paper32_core_results_changed": False,
            "paper32_core_results_unchanged": [
                "Rddot and Lambda dropout",
                "x_crit",
                "111/222 Gyr timescale arithmetic",
                "KB7 active source-block validation",
                "n_s",
                "A_s",
                "universal GMP characterization"
            ]
        }
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
