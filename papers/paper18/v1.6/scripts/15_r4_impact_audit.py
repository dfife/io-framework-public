"""Generate the Paper 18 v1.6 R4/FIRAS impact ledger.

This script records the exact blast radius of the Paper 17 v1.5 R4 repair on
Paper 18. It is intentionally a ledger rather than a new physics calculation:
the source scripts already recompute the affected quantities. The goal here is
to make the status boundary reviewable by a future reader.

Run with:

    /opt/cosmology-lab/env/bin/python paper18_v16_r4_impact_audit_checks.py
"""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT / "results"


def main() -> None:
    payload = {
        "paper": "Paper 18",
        "target_version": "v1.6",
        "audit_scope": "R4/FIRAS repair impact plus kappa-style hidden-parameter check",
        "r4_boundary": {
            "old_v1_5_boundary": "implicit R4 = 1; T_obs = T_IO*x^K_gauge counted as IO readout/prediction",
            "new_v1_6_boundary": "R4_FIRAS fixed by Paper 17 v1.5; CMB temperature is not counted as an independent IO prediction",
            "R4_FIRAS": 1.0031014644,
            "T_IO_bulk_K": 2.6635,
            "T_FIRAS_K": 2.7255,
            "T_obs_R4_equals_1_K": 2.725306096638128,
            "T_obs_R4_FIRAS_K": 2.7255,
        },
        "r4_usage_map": [
            {
                "artifact": "paper18_bogoliubov_coefficients_checks.py",
                "old_use": "T_obs = T_IO*x^K_gauge",
                "new_use": "T_obs = T_IO*x^(R4_FIRAS*K_gauge) = T_FIRAS",
                "impact": "observer packet frequencies shift from the R4=1 readout to FIRAS; Planck occupation factors and CCR checks remain exact",
            },
            {
                "artifact": "paper18_modular_bogoliubov_upgrade_checks.py",
                "old_use": "transported_temperature = T_IO*exp(K_gauge*lambda)",
                "new_use": "transported_temperature = T_IO*exp(R4_FIRAS*K_gauge*lambda)",
                "impact": "modular pushforward still matches direct observer KMS covariance after inserting R4_FIRAS",
            },
            {
                "artifact": "paper18_legacy_observables_recalculation_checks.py",
                "old_use": "T0_IO = 2.7253 in radiation density and CLASS calls",
                "new_use": "T0_IO = T_FIRAS computed through R4_FIRAS",
                "impact": "BAO, sigma8/S8, w0 apparent branch diagnostics shift slightly; branch remains conditional on withdrawn N_eff=Delta",
            },
            {
                "artifact": "paper18_jwst_age_recalculation_checks.py",
                "old_use": "IO branch T0 = 2.7253",
                "new_use": "IO branch T0 = T_FIRAS via R4_FIRAS",
                "impact": "high-z conditional age table shifts at sub-Myr level; sign and branch caveat unchanged",
            },
            {
                "artifact": "paper18_matter_power_shape_test.py",
                "old_use": "CAMB IO branch T0 = 2.7253",
                "new_use": "CAMB IO branch T0 = T_FIRAS via R4_FIRAS",
                "impact": "P(k) no-go remains catastrophic; IO amp_const chi2 updates from 1056.3648 to 1056.5532",
            },
            {
                "artifact": "paper18_zeq_kruskal_audit_checks.py",
                "old_use": "T0 = 2.7253",
                "new_use": "T0 = T_FIRAS via R4_FIRAS",
                "impact": "z_eq conditional branch shifts from 2824.7087 to 2823.8794; no status promotion",
            },
        ],
        "unaffected_artifacts": [
            "paper18_cmp_theorem_checks.py",
            "paper18_bdp_theorem_checks.py",
            "paper18_bdp_gap_closure_checks.py",
            "paper18_bdp_epoch_independence_audit_checks.py",
            "paper18_v_alpha_theorem_checks.py",
            "paper18_neff_delta_theorem_checks.py",
            "paper18_curvature_implementation_resolution_checks.py",
            "paper18_structural_attacks_audit_checks.py",
        ],
        "kappa_audit_verdict": {
            "hidden_continuous_fitted_parameter_found": False,
            "v1_5_hidden_overclaim_found": True,
            "hidden_overclaim": "R4 was visible as a premise/open problem in some locations but still used as if R4=1 produced a theorem-grade CMB-temperature prediction/readout.",
            "v1_6_repair": "Retire the independent CMB-temperature prediction; expose R4_FIRAS as FIRAS-fixed unique readout normalization inherited from Paper 17 v1.5.",
        },
        "classification_summary": {
            "CMP": "DERIVED/THEOREM within C1-C5 reduced observer algebra scope; R4-independent",
            "BDP": "DERIVED/THEOREM within reduced observer algebra and standard minimal-coupling matter class; R4-independent",
            "V_alpha": "DERIVED/THEOREM within reduced gauge center; R4-independent",
            "entropy_rank_Delta": "DERIVED/THEOREM as math-only acoustic entropy-rank; physical N_eff=Delta identification withdrawn",
            "Bogoliubov_spectrum": "DERIVED/CONDITIONAL_VERIFIED on Paper 17 v1.5 R4_FIRAS plus quasi-free CCR/gamma=1 scope",
            "legacy_observables": "CONDITIONAL diagnostic branch; N_eff=Delta is withdrawn as active Friedmann radiation parameter",
            "matter_power_shape_test": "NO-GO diagnostic with explicit nuisance fits; not a zero-parameter framework prediction",
        },
        "cmb_prediction_removed": True,
        "recommended_manuscript_change": "Paper 18 v1.6 should remove or reword every claim that IO predicts T_CMB/T_obs = 2.7253 K. The safe replacement is: FIRAS fixes the unique observer-side readout normalization R4_FIRAS within the Paper 17 thermal readout family.",
    }

    out = ROOT / "paper18_v16_r4_impact_audit_results.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
