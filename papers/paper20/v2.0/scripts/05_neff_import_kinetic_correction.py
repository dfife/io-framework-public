#!/usr/bin/env python3
"""
Print the Paper 20 v2.0 effective-species import and kinetic correction.

The manuscript states that N_eff = 3.044 is standard physics imported under
Premise 2, not derived by the reduced IO stack. The exact PRyMordial output
recorded here is 3.044388520277016.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    data = json.loads((RESULTS / "neff_import_kinetic_results.json").read_text(encoding="utf-8"))
    c = data["computed"]
    print("Paper 20 v2.0 N_eff import / kinetic correction")
    print(f"N_eff output = {c['N_eff_output']:.15f}")
    print(f"delta N_eff kinetic = {c['delta_N_eff_kinetic']:.15f}")
    print(f"T_IO vs T_obs N_eff difference = {c['Neff_output_difference_TIO_minus_TOBS']:.3e}")
    print(data["verdict"])


if __name__ == "__main__":
    main()
