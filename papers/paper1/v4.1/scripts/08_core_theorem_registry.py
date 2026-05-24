#!/usr/bin/env python3
"""Paper 1 v4.1 script 08: core theorem registry audit.

Purpose:
    Verify that the public v4.1 bundle contains the post-Cosmo theorem registry
    memos and the guardrail wording needed for downstream citation.

Inputs:
    reports/*.md

Outputs:
    results/core_theorem_registry_results.json

Claim boundary:
    This is a reproducibility-facing registry audit. It verifies presence of
    theorem text, status labels, and guardrails in the public bundle; it is not
    an independent proof engine.
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
REPORTS = BUNDLE_ROOT / "reports"
RESULTS = BUNDLE_ROOT / "results"


THEOREM_FILES = {
    "1.X": "paper1_v4_0_finite_horizon_readable_quotient_theorem_memo.md",
    "1.Y": "paper1_v4_1_theorem_1Y_registry_memo.md",
    "1.ZWVTU": "paper1_v4_1_core_inheritance_theorems_memo.md",
    "closed_s3_cosmo_reconciliation": "paper1_v4_1_closed_s3_reduction_cosmo_reconciliation.md",
}


REQUIRED_PHRASES = {
    "1.X": [
        "Finite Horizon-Readable Quotient",
        "DERIVED/CONDITIONAL_VERIFIED",
        "N_{\\rm read}",
        "exp(S_H",
    ],
    "1.Y": [
        "exterior Schwarzschild mass charge, treated as the global/quasi-local mass-energy parameter of the matched IO geometry",
        "This average is a bookkeeping definition on a specified closed slice.",
        "Nor does \\(\\rho_{\\rm avg}(R)\\) identify a local stress-energy component",
        "DERIVED/THEOREM` within the Paper 1 P1/P2 Schwarzschild-interior mass-accounting and closed-\\(S^3\\) geometry setting",
    ],
    "1.Z": [
        "Theorem 1.Z - Closed \\(K=+1\\) Interior Geometry",
        "DERIVED/THEOREM` within the IO homogeneous Oppenheimer-Snyder interior chassis",
        "This theorem fixes the background chassis. It does not exclude perturbations",
    ],
    "1.W": [
        "Theorem 1.W - Horizon-Contained Dynamics / No Asymptotic-Infinity Readout",
        "IO observables may not be treated as operationally measured at exterior asymptotic infinity",
        "Asymptotic-infinity or S-matrix constructions may be used as imported mathematical tools",
    ],
    "1.V": [
        "Theorem 1.V - Typed Observable / No Cross-Class Substitution",
        "DERIVED/CONDITIONAL_VERIFIED` on the typed observable architecture banked in Papers 19, 21, 32, 33, and 35",
        "This theorem does not license post-hoc class definitions",
    ],
    "1.U": [
        "Theorem 1.U - Native Closed-\\(S^3\\) Spatial Mode Reduction Principle",
        "Local tangent-space Fourier transforms remain valid for local physics under P2",
        "not a standalone universal \"closed curve space\" theorem",
    ],
    "1.T": [
        "Theorem 1.T - Schwarzschild Parent Neutrality",
        "Parent neutrality does not prohibit internal charged sectors",
        "cannot be borrowed from a Kerr or Reissner-Nordstrom parent parameter",
    ],
    "closed_s3_cosmo_reconciliation": [
        "Cosmo approved the IO closed \\(K=+1\\), compact \\(S^3\\) reduction principles with terminology guardrails",
        "Cosmo did not approve a standalone theorem named \"IO closed curve space\"",
        "Theorem 1.V remains the controlling guardrail for cross-class use",
    ],
}


def load_text(key: str) -> str:
    if key in {"1.Z", "1.W", "1.V", "1.U", "1.T"}:
        filename = THEOREM_FILES["1.ZWVTU"]
    elif key == "closed_s3_cosmo_reconciliation":
        filename = THEOREM_FILES["closed_s3_cosmo_reconciliation"]
    else:
        filename = THEOREM_FILES[key]
    return (REPORTS / filename).read_text()


def main() -> None:
    theorem_checks = {}
    all_pass = True
    for theorem, phrases in REQUIRED_PHRASES.items():
        text = load_text(theorem)
        phrase_results = {phrase: phrase in text for phrase in phrases}
        theorem_pass = all(phrase_results.values())
        all_pass = all_pass and theorem_pass
        theorem_checks[theorem] = {
            "pass": theorem_pass,
            "required_phrase_results": phrase_results,
        }

    output = {
        "script": "08_core_theorem_registry.py",
        "classification": "registry-audit / post-Cosmo theorem wording",
        "all_required_registry_phrases_present": all_pass,
        "theorem_checks": theorem_checks,
        "approved_closed_s3_reduction_chain": ["Theorem 1.Z", "Theorem 1.U", "Theorem 1.V"],
        "not_approved": [
            "standalone universal closed curve space theorem",
            "automatic cross-class closed-S3 substitution",
            "ban on local tangent-space Fourier methods",
            "claim that continuum QFT is invalid",
        ],
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "core_theorem_registry_results.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({"all_required_registry_phrases_present": all_pass}, indent=2))


if __name__ == "__main__":
    main()
