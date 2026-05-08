#!/usr/bin/env python3
"""
Generate the Paper 19 v1.6 R4/FIRAS impact ledger.

This script is intentionally standard-library only. It records the repaired
observer-side readout convention and the numerical changes that matter for
Paper 19's public manuscript update. It does not recompute BOSS or PRyMordial;
those heavy artifacts are frozen separately in ``results/``.

Output:
    ../results/r4_impact_audit_results.json
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
OUT = BUNDLE_ROOT / "results" / "r4_impact_audit_results.json"


def main() -> None:
    payload = {
        "r4_repair": {
            "T_obs_family": "T_obs(R4) = T_IO * x^(R4*K_gauge)",
            "R4_FIRAS": 1.0031014644,
            "T_IO_K": 2.6635,
            "T_FIRAS_K": 2.7255,
            "status": (
                "FIRAS fixes the observer-side thermal datum. Paper 19 v1.6 "
                "does not count the CMB temperature as an independent prediction."
            ),
        },
        "changed_outputs": {
            "boss_alpha_3_over_2_chi2": 73.03360608958111,
            "boss_lcdm_chi2": 70.32360985979422,
            "z_eq_paper18_branch": 2823.879425051597,
            "bbn_chi2_D_plus_Y": 0.5031639343080561,
            "age_closed_N_mode_open_gap": 0.33602494442479497,
        },
        "manuscript_actions": [
            "Remove independent CMB-temperature prediction language.",
            "Replace T_obs = T_IO*x^K_gauge with the FIRAS-fixed R4 family.",
            "Migrate retired claim labels to the canonical claim-discipline taxonomy.",
            "Label the age-closed N_mode branch as OPEN/PREMISE_GAP unless theorem-fixed elsewhere.",
        ],
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
