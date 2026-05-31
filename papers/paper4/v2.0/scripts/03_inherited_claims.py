#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads(Path(path).read_text())


def main() -> None:
    paper28 = load("/opt/cosmology-lab/tmp/io-framework-public/papers/paper28/v2.0/results/jwst_clock_map_results.json")
    paper32 = load("/opt/cosmology-lab/results/paper32/paper32_s8_current_stack_closure_results.json")
    paper32_amp = load("/opt/cosmology-lab/results/paper32/paper32_s8_amplitude_selector_candidate_results.json")
    paper24 = load("/opt/cosmology-lab/tmp/io-framework-public/papers/paper24/v3.0/results/excited_state_import_recomputation_results.json")
    paper20 = load("/opt/cosmology-lab/tmp/io-framework-public/papers/paper20/v2.0/results/acoustic_theorems_results.json")

    preferred_bbn = paper24["import_cases"][0]
    result = {
        "paper": "Paper 4",
        "version": "v2.0",
        "status": "inherited frozen-output support for Paper 4 reported claims",
        "jwst_formation_clock": {
            "status": paper28["status"],
            "source": "/opt/cosmology-lab/tmp/io-framework-public/papers/paper28/v2.0/results/jwst_clock_map_results.json",
            "rows": paper28["rows"],
            "scope": paper28["scope"]
        },
        "s8_growth": {
            "status": "DERIVED/CONDITIONAL_VERIFIED on active solver stack",
            "source": "/opt/cosmology-lab/results/paper32/paper32_s8_current_stack_closure_results.json",
            "sigma8": paper32_amp["rows"][2]["sigma8"],
            "S8": paper32["theorem_supported"]["S8"],
            "pull_sigma_vs_weak_lensing": paper32["theorem_supported"]["pull_sigma"],
            "native_pull_sigma": paper32_amp["rows"][0]["pull_sigma_vs_WL"]
        },
        "bbn_scorecard": {
            "status": "DERIVED/CONDITIONAL_VERIFIED inherited from Paper 24 v3.0",
            "source": "/opt/cosmology-lab/tmp/io-framework-public/papers/paper24/v3.0/results/excited_state_import_recomputation_results.json",
            "D_H": preferred_bbn["D_H"],
            "D_H_sigma": preferred_bbn["D_H_sigma"],
            "Y_p": preferred_bbn["Y_p"],
            "Y_p_sigma": preferred_bbn["Y_p_sigma"],
            "Li7_H": preferred_bbn["Li7_H"],
            "Li7_sigma": preferred_bbn["Li7_sigma"]
        },
        "acoustic_scale": {
            "status": "DERIVED/CONDITIONAL_VERIFIED inherited from Paper 20 v2.0",
            "source": "/opt/cosmology-lab/tmp/io-framework-public/papers/paper20/v2.0/results/acoustic_theorems_results.json",
            "theta_star_pred_deg_current_rounded_row": paper20["exact_rows"]["current_bipartite_rounded_row"]["theta_obs_deg"],
            "theta_star_sigma_offset_current_rounded_row": paper20["exact_rows"]["current_bipartite_rounded_row"]["sigma_offset"],
            "theta_planck_deg": paper20["theorems"]["20.2"]["theta_planck_deg"],
            "theta_planck_sigma_deg": paper20["theorems"]["20.2"]["theta_planck_sigma_deg"]
        }
    }
    out = ROOT / "results" / "inherited_claims_results.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(out)


if __name__ == "__main__":
    main()
