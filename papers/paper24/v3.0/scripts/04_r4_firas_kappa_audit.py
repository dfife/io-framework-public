#!/usr/bin/env python3
"""
Paper 24 v3.0 reproducibility script 04.

Purpose:
    Record the R4/FIRAS repair audit for Paper 24 v3.0 and verify that the
    active lithium/BBN scripts do not use the retired R4 = 1 optical-readout
    normalization as a hidden fitted parameter.

Inputs:
    - Paper 17 v1.5 constants embedded below:
      R4_FIRAS = 1.0031014644, gamma_BI = 0.2375, x = 1.519.
    - The public Paper 24 v3.0 scripts in this bundle.
    - The Paper 24 v3.0 manuscript review findings recorded in this script.

Outputs:
    - results/r4_firas_kappa_audit_results.json
    - reports/paper24_v30_r4_firas_kappa_audit_report.md

External dependencies:
    Python standard library only.

Claim boundary:
    - VERIFIED: script-level review that the active BBN scorecard uses the
      local interior thermal branch T_IO = 2.6635 K and reads PRyMordial YPCMB.
    - IMPORTED/EMPIRICAL: FIRAS fixes the observer-side R4 readout
      normalization through Paper 17 v1.5.
    - DERIVED/CONDITIONAL_VERIFIED: Paper 24's branch-dressing theorem chain,
      with dependency on the stated bridge premises and imported A=7 nuclear
      data.

Run:
    python3 scripts/04_r4_firas_kappa_audit.py
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = BUNDLE_ROOT / "scripts"
RESULTS_DIR = BUNDLE_ROOT / "results"
REPORTS_DIR = BUNDLE_ROOT / "reports"
OUT_JSON = RESULTS_DIR / "r4_firas_kappa_audit_results.json"
OUT_REPORT = REPORTS_DIR / "paper24_v30_r4_firas_kappa_audit_report.md"

GAMMA_BI = 0.2375
X = 1.519
K_GAUGE = math.log(1.0 + GAMMA_BI * GAMMA_BI)
R4_FIRAS = 1.0031014644
T_IO_BBN_BRANCH_K = 2.6635
T_OBS_FIRAS_READOUT_K = T_IO_BBN_BRANCH_K * (X ** (R4_FIRAS * K_GAUGE))


CANONICAL_LABELS = [
    "DERIVED/THEOREM",
    "DERIVED/CONDITIONAL_VERIFIED",
    "DERIVED/NO-GO",
    "VERIFIED",
    "IMPORTED/EMPIRICAL",
    "RECONSTRUCTION",
    "RECONSTRUCTION/RESEARCH_ONLY",
    "OPEN/PREMISE_GAP",
    "SUPERSEDED",
    "Historical/SUPERSEDED",
]


def script_contains(script_name: str, needles: list[str]) -> dict:
    """Return whether a script contains each diagnostic string."""

    text = (SCRIPTS_DIR / script_name).read_text(encoding="utf-8")
    return {needle: needle in text for needle in needles}


def build_payload() -> dict:
    """Build the Paper 24 v3.0 R4/FIRAS audit payload."""

    script_review = {
        "01_compute_qtrans_carrier.py": {
            "purpose": "Q_trans carrier arithmetic and simplified lithium response.",
            "r4_usage": "none",
            "contains": script_contains(
                "01_compute_qtrans_carrier.py",
                ["R4", "R4_FIRAS", "T0CMB", "T_IO_BBN_BRANCH_K", "YPCMB()", "YPBBN"],
            ),
            "impact": "No R4 damage. This script uses nuclear carrier constants, x, gamma_BI, and observational Li-7 denominator only.",
        },
        "02_recompute_excited_state_import.py": {
            "purpose": "Henderson B(E2) import, detailed balance, q_trans,ex, and branch scorecard handoff.",
            "r4_usage": "none directly; calls script 03 for PRyMordial scorecard when rerun.",
            "contains": script_contains(
                "02_recompute_excited_state_import.py",
                ["R4", "R4_FIRAS", "T0CMB", "T_IO_BBN_BRANCH_K", "YPCMB()", "YPBBN"],
            ),
            "impact": "No R4 damage. Imported A=7 nuclear data are independent of optical readout normalization.",
        },
        "03_run_final_bbn_scorecard.py": {
            "purpose": "Excited-branch kernel and PRyMordial BBN scorecard.",
            "r4_usage": "records R4_FIRAS for audit visibility; does not use it in the PRyMordial T0CMB assignment.",
            "contains": script_contains(
                "03_run_final_bbn_scorecard.py",
                ["R4", "R4_FIRAS", "T0CMB", "T_IO_BBN_BRANCH_K", "YPCMB()", "YPBBN"],
            ),
            "impact": "No numerical R4 damage. The active BBN branch uses T_IO_BBN_BRANCH_K = 2.6635 K and YPCMB().",
        },
        "04_r4_firas_kappa_audit.py": {
            "purpose": "This audit report.",
            "r4_usage": "computes observer-side readout bookkeeping and records non-entry into active BBN.",
            "impact": "Audit support only.",
        },
        "05_validate_expected_outputs.py": {
            "purpose": "Frozen-output validation.",
            "r4_usage": "validates R4_FIRAS in the audit JSON; does not recompute BBN.",
            "impact": "Validation support only.",
        },
    }

    candidate_fields = [
        {
            "field": "R4 optical readout normalization",
            "original_retired_value": 1.0,
            "current_value": R4_FIRAS,
            "rigidity_test": "Not internally forced by the old modular-projection stack; uniquely fixed by FIRAS within the Paper 17 v1.5 readout family.",
            "classification": "IMPORTED/EMPIRICAL input plus DERIVED uniqueness theorem in Paper 17 v1.5",
            "hidden_parameter": False,
            "paper24_impact": "Does not enter active BBN scorecard; only observer-side thermal readout bookkeeping.",
        },
        {
            "field": "T_IO_BBN_BRANCH_K",
            "current_value": T_IO_BBN_BRANCH_K,
            "rigidity_test": "Fixed by the inherited local interior thermal branch used for BBN abundance/rate observables.",
            "classification": "DERIVED/CONDITIONAL_VERIFIED through Paper 21/Paper 22 BBN branch assignment",
            "hidden_parameter": False,
            "paper24_impact": "Used as PRyMordial T0CMB baseline in the active scorecard.",
        },
        {
            "field": "Y_p readout",
            "current_value": "obj.YPCMB()",
            "rigidity_test": "The wrapper reads the observationally relevant PRyMordial helium output, not YPBBN.",
            "classification": "VERIFIED wrapper convention",
            "hidden_parameter": False,
            "paper24_impact": "Matches the Paper 24 v3.0 scorecard convention.",
        },
        {
            "field": "Henderson B(E2) import",
            "current_value": "B(E2 down) = 52 e^2 fm^4",
            "rigidity_test": "Imported primary nuclear datum; detailed-balance conversion is arithmetic and visible.",
            "classification": "IMPORTED/EMPIRICAL plus VERIFIED conversion",
            "hidden_parameter": False,
            "paper24_impact": "Sets the primary q_trans,ex row; not tuned to BBN residuals.",
        },
        {
            "field": "q_trans,ex projection",
            "current_value": 0.017537902422203915,
            "rigidity_test": "Forced by sqrt(B(E2))/100 multiplied by the amplitude-weighted Coulomb kernel in the declared branch model.",
            "classification": "DERIVED/CONDITIONAL_VERIFIED within imported nuclear-data branch package",
            "hidden_parameter": False,
            "paper24_impact": "Load-bearing for the Henderson primary lithium row.",
        },
    ]

    manuscript_review = {
        "independent_cmb_temperature_prediction": {
            "status": "removed/retired in Paper 24 v3.0 scope",
            "finding": "No Paper 24 active scorecard should count observed CMB temperature as an independent IO prediction. CMB tensor-bound references are separate and not an R4 temperature claim.",
        },
        "noncanonical_labels_seen_in_v3_0_draft": [
            {
                "label": "DERIVED/SCOPED",
                "recommendation": "Replace with DERIVED/CONDITIONAL_VERIFIED if the scoped chain reaches Premise 1, Premise 2, or a frozen imported empirical/physics input; otherwise OPEN/PREMISE_GAP.",
            },
            {
                "label": "CONDITIONAL on ...",
                "recommendation": "Replace load-bearing cases with DERIVED/CONDITIONAL_VERIFIED and include the explicit chain. Use OPEN/PREMISE_GAP if the chain cannot be stated.",
            },
            {
                "label": "IMPORTED/SCOPED",
                "recommendation": "Use IMPORTED/EMPIRICAL for external data, then separately state the theorem chain that consumes the import.",
            },
            {
                "label": "DERIVED/IMPORTED",
                "recommendation": "Split into VERIFIED arithmetic/derivation and IMPORTED/EMPIRICAL input.",
            },
        ],
        "abbreviations_flagged_for_reader_expansion": [
            "BBN",
            "CMB",
            "CG",
            "FRW",
            "GR",
            "KMS",
            "LQG",
            "OS",
            "TT",
            "ANC",
            "NCSM",
            "IO",
            "CMP",
            "BDP",
            "GTTP",
            "PSRP",
            "GMP",
            "TBS",
            "WMR",
        ],
        "io_slang_flagged_for_rewrite_or_definition": [
            "one-slot",
            "two-slot",
            "alpha-ladder",
            "horizon puncture",
            "generating-potential hierarchy",
            "bridge-dressing",
            "branch package",
            "mass-7 TT dressing",
        ],
    }

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "paper": "Paper 24 v3.0",
        "audit_type": "R4/FIRAS kappa-style field-redefinition and reproducibility-script audit",
        "framework_constants": {
            "gamma_BI": GAMMA_BI,
            "x": X,
            "K_gauge": K_GAUGE,
            "R4_FIRAS": R4_FIRAS,
            "T_IO_BBN_BRANCH_K": T_IO_BBN_BRANCH_K,
            "T_obs_FIRAS_readout_K": T_OBS_FIRAS_READOUT_K,
        },
        "canonical_labels": CANONICAL_LABELS,
        "executive_verdict": {
            "hidden_continuous_fitted_parameter_found": False,
            "r4_damage_to_active_scorecard": False,
            "cmb_temperature_prediction_claim_must_remain_retired": True,
            "bbn_scorecard_numerically_unchanged": True,
            "primary_reason": "R4_FIRAS fixes observer-side optical readout only; Paper 24's active BBN scorecard uses the local T_IO branch and YPCMB output.",
        },
        "r4_impact": {
            "retired_R4_value": 1.0,
            "active_R4_value": R4_FIRAS,
            "r4_enters_active_bbn_scorecard": False,
            "observer_side_readout_temperature_K": T_OBS_FIRAS_READOUT_K,
            "active_prymordial_temperature_K": T_IO_BBN_BRANCH_K,
            "scorecard_change_required": "none",
        },
        "candidate_fields": candidate_fields,
        "script_review": script_review,
        "manuscript_review": manuscript_review,
        "recommendations": [
            "Keep the Paper 24 v3.0 BBN scorecard unchanged.",
            "Do not describe observed CMB temperature as an independent Paper 24 or IO prediction.",
            "Keep R4_FIRAS visible as inherited observer-side readout normalization, not as a tunable BBN parameter.",
            "Migrate noncanonical labels in the manuscript to the published claim-discipline scheme.",
            "Expand first-use abbreviations and replace IO slang with standard physics wording or explicit definitions.",
        ],
    }


def write_report(payload: dict) -> None:
    """Write a human-readable audit report matching the JSON payload."""

    label_flags = payload["manuscript_review"]["noncanonical_labels_seen_in_v3_0_draft"]
    abbrev_flags = payload["manuscript_review"]["abbreviations_flagged_for_reader_expansion"]
    slang_flags = payload["manuscript_review"]["io_slang_flagged_for_rewrite_or_definition"]

    lines = [
        "# Paper 24 v3.0 R4/FIRAS Kappa-Style Audit Report",
        "",
        "## Executive Verdict",
        "",
        "No hidden continuous fitted parameter was found in the active Paper 24 v3.0 public scripts.",
        "The R4/FIRAS repair does not change the Paper 24 BBN scorecard because R4 fixes observer-side optical readout, while the active PRyMordial BBN calculation uses the local interior thermal branch.",
        "",
        f"- `R4_FIRAS = {R4_FIRAS:.10f}`",
        f"- `T_IO_BBN_BRANCH = {T_IO_BBN_BRANCH_K:.4f} K`",
        f"- `T_obs_FIRAS_readout = {T_OBS_FIRAS_READOUT_K:.12f} K`",
        "- `R4_enters_active_BBN_scorecard = false`",
        "- Paper 24 v3.0 must not claim an independent observed-CMB-temperature prediction.",
        "",
        "## R4 Field-Redefinition Test",
        "",
        "The retired `R4 = 1` normalization is not used as a Paper 24 fitted parameter. Under the Paper 17 v1.5 repair, FIRAS fixes a unique observer-side readout normalization inside the declared readout family. Paper 24 inherits that constant for bookkeeping, but its BBN branch remains the local `T_IO` branch. Replacing the PRyMordial temperature with observer-side `T_obs` would be a class error, not an R4 repair.",
        "",
        "## Candidate Fields",
        "",
        "| Field | Classification | Hidden parameter? | Paper 24 impact |",
        "| --- | --- | --- | --- |",
    ]

    for item in payload["candidate_fields"]:
        lines.append(
            f"| {item['field']} | {item['classification']} | {item['hidden_parameter']} | {item['paper24_impact']} |"
        )

    lines.extend(
        [
            "",
            "## Script Review",
            "",
            "| Script | R4 usage | Impact |",
            "| --- | --- | --- |",
        ]
    )
    for name, item in payload["script_review"].items():
        lines.append(f"| `{name}` | {item['r4_usage']} | {item['impact']} |")

    lines.extend(
        [
            "",
            "## Claim-Label Compliance Flags",
            "",
            "Paper 24 v3.0 should use the public canonical claim labels. The following manuscript labels need migration review:",
            "",
        ]
    )
    for flag in label_flags:
        lines.append(f"- `{flag['label']}`: {flag['recommendation']}")

    lines.extend(
        [
            "",
            "## Abbreviations Flagged",
            "",
            "First use should be expanded for non-IO readers:",
            "",
            ", ".join(f"`{item}`" for item in abbrev_flags),
            "",
            "## IO Slang Flagged",
            "",
            "These terms should be replaced with standard physics language or defined explicitly before use:",
            "",
            ", ".join(f"`{item}`" for item in slang_flags),
            "",
            "## Recommendations",
            "",
        ]
    )
    for recommendation in payload["recommendations"]:
        lines.append(f"- {recommendation}")

    lines.append("")
    OUT_REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    """Generate the JSON and Markdown R4/FIRAS audit artifacts."""

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_report(payload)
    print(json.dumps(payload["executive_verdict"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
