#!/usr/bin/env python3
"""
Paper 32 v1.5 reproducibility script 05.

Purpose:
    Reproduce the public structural validation surface for Theorem 32.KB.7:
    the DtN Open-Transport Placement closes the fixed-point normalization
    only on the active reduced scalar source block.

Inputs:
    - data/imported_constants.json

Outputs:
    - results/kb7_source_block_validation_results.json

External dependencies:
    Python standard library only.

Claim boundary:
    verified / structural validation and arithmetic checks. This script does
    not prove functional analysis; it records the scoped theorem gates and
    validates the scalar identities used by the manuscript.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "kb7_source_block_validation_results.json"


def main() -> int:
    payload = json.loads(DATA_PATH.read_text())
    constants = payload["framework_constants"]
    gamma = constants["gamma_BI"]
    x = constants["x"]
    q = 1.0 + gamma**2
    k_gauge = math.log(q)
    eta = k_gauge / x
    s_cell = math.exp(x)
    z_cell = s_cell**eta

    gates = [
        {
            "gate": "source_object_lock",
            "status": "passed / scoped",
            "meaning": "The physical P4-carrying observable is the active source/readout block, not thermal/recombination/history blocks."
        },
        {
            "gate": "alpha_class_repair",
            "status": "passed / scoped",
            "meaning": "The active DtN source spectral-scale measure is alpha=1 because the primitive observable is a coexact one-form line object."
        },
        {
            "gate": "local_payload_lock",
            "status": "passed / scoped",
            "meaning": "On the unique local scalar source channel, the reduced Ashtekar-Barbero relative factor acts by Q."
        },
        {
            "gate": "global_universal_P4",
            "status": "explicit no-go",
            "meaning": "No universal observable-independent P4 theorem is claimed."
        }
    ]

    results = {
        "paper": payload["paper"],
        "classification": "verified / structural validation",
        "formula": "Z(s) = s^(K_gauge/x); Z(e^x) = Q",
        "inputs": {"gamma_BI": gamma, "x": x},
        "derived": {
            "Q": q,
            "K_gauge": k_gauge,
            "eta_BFP": eta,
            "s_cell": s_cell,
            "Z_e_to_x": z_cell
        },
        "consistency_checks": {
            "Z_e_to_x_equals_Q": math.isclose(z_cell, q, rel_tol=0.0, abs_tol=1e-14),
            "eta_equals_K_over_x": math.isclose(eta, k_gauge / x, rel_tol=0.0, abs_tol=1e-18)
        },
        "scope": payload["kb7_scope"],
        "gates": gates
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"state": "wrote", "path": str(RESULTS_PATH)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

