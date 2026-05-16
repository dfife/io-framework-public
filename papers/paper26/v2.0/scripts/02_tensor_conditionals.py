#!/usr/bin/env python3
"""Emit the conditional Paper 26 v2.0 tensor branch numbers.

Paper 26 includes a conditional tensor-to-scalar estimate from the same
Hawking-state idea used for the scalar amplitude. It is not a theorem-grade
closure because tensor bridge payload, boundary carrier, and transport remain
open. The public bundle preserves that boundary while exposing the numerical
range quoted by the audit artifacts.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_PATH = BUNDLE_ROOT / "results" / "tensor_conditionals_results.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    tensor = data["tensor_conditionals"]["rank2_tensor_like_lambda4"]

    result = {
        "paper": "Paper 26 v2.0",
        "tensor_case": "rank2_tensor_like_lambda4",
        "betaomega_tensor": tensor["betaomega_tensor"],
        "g_tensor": tensor["g_tensor"],
        "omega_hat_tensor": tensor["omega_hat_tensor"],
        "r_canonical_g_over_omega_ratio": tensor["r_canonical_g_over_omega_ratio"],
        "r_raw_g_ratio": tensor["r_raw_g_ratio"],
        "quoted_range": {
            "r_min": tensor["r_canonical_g_over_omega_ratio"],
            "r_max": tensor["r_raw_g_ratio"]
        },
        "status": data["tensor_conditionals"]["status"],
        "claim_boundary": "Conditional estimate only; not an unconditional theorem-grade primordial tensor prediction."
    }

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {RESULTS_PATH.relative_to(BUNDLE_ROOT)}")


if __name__ == "__main__":
    main()
