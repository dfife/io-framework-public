#!/usr/bin/env python3
"""Paper 1 v4.0 script 05: cross-paper consistency registry.

Purpose:
    Archive the inherited values Paper 1 v4.0 cites from later public bundles,
    without pretending to rederive those later-paper theorem chains locally.

Inputs:
    data/imported_constants.json

Outputs:
    results/cross_paper_consistency_results.json

Claim boundary:
    Cross-paper source registry and consistency flags only. Use the referenced
    paper-specific bundles for full reproduction of those downstream claims.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS = BUNDLE_ROOT / "results"


def main() -> None:
    constants = json.loads(DATA.read_text())
    sources = constants["cross_paper_sources"]
    quoted = constants["manuscript_quoted_values"]

    output = {
        "script": "05_cross_paper_consistency.py",
        "inherited_values": {
            "paper17_v1_5_R4_FIRAS": sources["paper17_v1_5"],
            "paper32_v2_0_lifecycle": {
                **sources["paper32_v2_0"],
                "recollapse_time_Gyr": quoted["recollapse_time_Gyr"],
                "cycle_time_Gyr": quoted["cycle_time_Gyr"],
                "x_crit": quoted["x_crit"],
                "R_bounce_m": quoted["R_bounce_m"]
            },
            "paper34_v1_2_hubble_scorecard": sources["paper34_v1_2"],
            "paper35_v2_0_four_problems_anchor": sources["paper35_v2_0"]
        },
        "audit_flags": {
            "paper32_manuscript_sha_prefix_matches_current_repo_manifest": (
                sources["paper32_v2_0"]["manuscript_sha_prefix"]
                == sources["paper32_v2_0"]["current_repo_manifest_sha256"][:8]
            ),
            "paper32_sha_sync_note": "Paper 1 v4.0 manuscript cites prefix fadeea1d; current public repo manifest records 2e1ff99e... for paper32-v2.0."
        }
    }

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "cross_paper_consistency_results.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output["audit_flags"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

