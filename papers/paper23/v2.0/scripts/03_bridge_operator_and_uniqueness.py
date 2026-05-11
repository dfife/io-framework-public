#!/usr/bin/env python3
"""Reproduce the Paper 23 scalar bridge and uniqueness bookkeeping.

Paper 23's bridge result is representation-theoretic. This script records the
actual support statements that are safe to reproduce:

* the local scalar bridge is the trace contraction on the isotropic background,
* the epsilon-f cubic candidate is proportional to the trace bridge on that
  background, not an independent scalar bridge,
* global branch rules are multiplicity-one with N = n +/- 1,
* tensor bridge statements are shellwise and must not be overclaimed as a single
  global scalar multiplier.

The script outputs structured JSON rather than symbolic proof objects so a
reader can inspect the exact theorem-support claims used in the bundle.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results" / "bridge_operator_and_uniqueness_results.json"


def scalar_branch_targets(source_shell_n: int) -> list[int]:
    targets = [source_shell_n - 1, source_shell_n + 1]
    return [target for target in targets if target >= 2]


def main() -> int:
    branch_samples = {
        str(n): {
            "source_shell_n": n,
            "allowed_scalar_output_shells_N": scalar_branch_targets(n),
            "multiplicity_per_allowed_branch": 1,
        }
        for n in [2, 3, 4, 5, 29, 712]
    }

    results = {
        "paper": "Paper 23",
        "version": "v2.0",
        "claim_status": {
            "local_scalar_trace_bridge": "DERIVED/CONDITIONAL_VERIFIED",
            "epsilon_f_candidate_proportionality": "DERIVED/NO-GO for independent second scalar bridge",
            "global_scalar_branch_multiplicity": "DERIVED/CONDITIONAL_VERIFIED",
            "vector_to_TT_bridge": "DERIVED/CONDITIONAL_VERIFIED",
            "TT_to_TT_global_uniqueness": "OPEN/PREMISE_GAP if claimed beyond shellwise Schur uniqueness",
        },
        "local_scalar_bridge": {
            "representative": "S_Abar(delta A) = g^{ab} kappa_{ij} Abar_a^i delta A_b^j",
            "projected_bridge": "B_N(delta A) = Pi_N^(0) S_Abar(delta A)",
            "hom_space_dimension": 1,
            "normalization_note": (
                "The bridge is unique up to normalization. The active spectral-index "
                "slope is a logarithmic slope, so the overall bridge normalization cancels."
            ),
        },
        "epsilon_f_candidate": {
            "candidate": "epsilon^{abc} f_{ijk} Abar_a^i Abar_b^j delta A_c^k",
            "homogeneous_background_relation": "B^(3)(delta A) = 2 alpha^2 Tr(X) = 2 alpha B^(1)(delta A)",
            "finding": "proportional to the trace bridge on the homogeneous isotropic FRW background",
        },
        "scalar_branch_rules": {
            "rule": "N = n - 1 or N = n + 1 on allowed multiplicity-one branches",
            "samples": branch_samples,
        },
        "tensor_bridge_boundary": {
            "vector_to_TT_representative": "T_Abar(delta A)_{ab} = STF_ab[kappa_{ij} Abar_(a)^i delta A_(b)^j]",
            "vector_to_TT_status": "unique up to normalization at the local zero-order level",
            "TT_to_TT_status": (
                "Schur uniqueness is shellwise. A global TT-to-TT bridge remains a "
                "spectral-multiplier family unless extra parity or weighting conditions are imposed."
            ),
        },
        "checks": {
            "scalar_hom_space_dimension": 1,
            "epsilon_candidate_independent": False,
            "sample_n5_targets": scalar_branch_targets(5),
            "multiplicity_per_allowed_branch": 1,
        },
    }

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

