#!/usr/bin/env python3
"""Paper 1 v4.0 script 03: spectral-theorem flags.

Purpose:
    Archive the reproducibility-facing status of the Paper 1 interior-observer
    greybody claim. The computation is exact at the stated theorem boundary:
    the relevant interior observer has no exterior scattering potential in the
    reduced channel, so Gamma(omega)=1 in the scoped interior channel.

Inputs:
    None beyond the manuscript theorem statement.

Outputs:
    results/spectral_theorem_flags_results.json

Claim boundary:
    The JSON records a theorem-scope flag, not a numerical simulation of
    exterior greybody factors.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    output = {
        "script": "03_spectral_theorem_flags.py",
        "theorem_scope": "interior observer channel inside the Schwarzschild horizon",
        "Gamma_omega": 1.0,
        "greybody_attenuation_present": False,
        "status_label": "DERIVED/THEOREM in manuscript scope",
        "not_claimed": [
            "Exterior-observer greybody factors are unity",
            "Arbitrary exterior scattering channels vanish",
            "The theorem replaces standard exterior black-hole greybody physics"
        ],
        "chain_summary": "P1 Schwarzschild-interior observer placement + P2 local QFT equivalence + no exterior potential barrier in the reduced interior channel"
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "spectral_theorem_flags_results.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

