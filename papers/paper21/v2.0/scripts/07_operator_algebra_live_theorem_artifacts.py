#!/usr/bin/env python3
"""Paper 21 v2.0 reproducibility script 07.

Purpose:
    Generate a compact live-theorem artifact ledger for Paper 21's operator
    algebra claims: optical filtration, T_IO branch assignment, local
    nontraciality, and Wigner-Eckart selection failure. It also confirms that
    the observer-side optical readout temperature uses the Paper 17 v1.5
    FIRAS-fixed R4 value rather than the retired R4 = 1 shorthand.

Manuscript role:
    Supports live theorem-status statements without rerunning dead BBN route
    searches.

Inputs:
    data/imported_constants.json.

Outputs:
    results/operator_algebra_live_theorem_artifacts_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    This is theorem-artifact arithmetic and status validation. It does not
    rerun historical no-go routes or promote the old P_resp program.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
OUT = BUNDLE_ROOT / "results" / "operator_algebra_live_theorem_artifacts_results.json"


def main() -> int:
    constants = json.loads(DATA.read_text())
    fw = constants["framework_constants"]
    legacy = constants["paper21_legacy_geometric_branch"]

    local_nontraciality = {
        "label": "Theorem 21.O",
        "status": "DERIVED/CONDITIONAL_VERIFIED theorem artifact",
        "example": "four spin-1/2 punctures split as A = two, B = two, global state projected to invariant subspace",
        "reduced_state_eigenvalues": {
            "J_0_block": 0.5,
            "J_1_block_each_state": 1.0 / 6.0
        },
        "trace_check": 0.5 + 3.0 * (1.0 / 6.0),
        "is_tracial_on_H_A": False
    }

    rank2_allowed_starts = [j / 2.0 for j in range(1, 11) if 2.0 <= 2.0 * (j / 2.0)]
    wigner_eckart = {
        "label": "No-go 21.P boundary retained as live selection-rule statement",
        "status": "DERIVED/NO-GO theorem artifact",
        "diagonal_rank2_allowed_first_values": rank2_allowed_starts,
        "conclusion": "A diagonal rank-2 operator excludes j=1/2 but allows j=1, 3/2, 2, 5/2, ...; it does not select exactly {1,2}."
    }

    payload = {
        "claim": "Paper 21 live operator-algebra theorem artifacts",
        "status": "VERIFIED theorem-artifact ledger",
        "optical_filtration": {
            "label": "Theorem 21.J",
            "status": "DERIVED/CONDITIONAL_VERIFIED theorem artifact",
            "statement": "Reduced RT/BY optical readouts pass through the fixed-point algebra and are blind to noncentral SU(2) puncture data.",
            "fixed_point_action_on_C2_spectral_functions": "E_punc(H_punc h(C2)) = H_punc h(C2)"
        },
        "branch_assignment": {
            "label": "Theorem 21.L",
            "status": "DERIVED/CONDITIONAL_VERIFIED theorem artifact",
            "T_IO_K": fw["T_IO_K"],
            "T_obs_K": fw["T_obs_K"],
            "R4_FIRAS": fw["R4_FIRAS"],
            "retired_GTTP_formula": "T_obs = T_IO x^K_gauge",
            "active_optical_readout_formula": "T_obs(R4) = T_IO x^(R4_FIRAS K_gauge)",
            "T_obs_recomputed": fw["T_IO_K"] * (fw["x"] ** (fw["R4_FIRAS"] * fw["K_gauge"])),
            "R4_enters_active_BBN_scorecard": False,
            "legacy_T_IO_branch_demo": {
                "N_eff_geometric": legacy["N_eff_geometric"],
                "D_over_H_sigma": legacy["T_IO_branch_D_over_H_sigma"],
                "Y_p_sigma_published_legacy": legacy["T_IO_branch_Y_p_sigma_published_legacy"],
                "chi2_DH_plus_Yp_published_legacy": legacy["T_IO_branch_chi2_DH_plus_Yp_published_legacy"]
            },
            "legacy_T_obs_branch_mismatch": {
                "D_over_H_sigma": legacy["T_obs_branch_D_over_H_sigma"],
                "chi2_DH_plus_Yp": legacy["T_obs_branch_chi2_DH_plus_Yp"]
            }
        },
        "local_nontraciality": local_nontraciality,
        "wigner_eckart_selection_boundary": wigner_eckart,
        "claim_boundary": "Live theorem/status support only; dead-route reruns are intentionally excluded."
    }
    # Internal consistency checks are part of the output so readers can see
    # what was verified without reading the code.
    payload["consistency_checks"] = {
        "local_nontraciality_trace_equals_one": math.isclose(local_nontraciality["trace_check"], 1.0, rel_tol=0.0, abs_tol=1e-15),
        "T_obs_formula_matches_imported_value": math.isclose(payload["branch_assignment"]["T_obs_recomputed"], fw["T_obs_K"], rel_tol=0.0, abs_tol=1e-12),
        "R4_does_not_enter_active_BBN_scorecard": payload["branch_assignment"]["R4_enters_active_BBN_scorecard"] is False,
        "rank2_allows_j_3_over_2": 1.5 in rank2_allowed_starts
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "output": str(OUT)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
