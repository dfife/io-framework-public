# Paper 25 v2.0 R4 and Kappa-Style Structural Audit

Date: 2026-05-14

Scope: `Interior_Observer_Paper25_v2_0.docx` in `results/Full Papers/`, the
existing Paper 25 support artifacts, and the public bundle under
`papers/paper25/v2.0/`.

## Executive Verdict

No hidden continuous fitted parameter was found in the active Paper 25 v2.0
weak-sector support surface.

The active calculations are not R4-dependent. The live scripts use
`gamma_BI`, `K_gauge = ln(1 + gamma_BI^2)`, the Paper 21 puncture load `L_1`,
the inherited nuclear payload `(<K>/10) L_2`, and frozen PRyMordial BBN rows
aligned to Paper 24 v3.0. They do not use `R4 = 1`, `R4_FIRAS`, `T_obs`, or
the observed CMB temperature as computational inputs.

The R4 damage in Paper 25 v2.0 is manuscript hygiene in inherited
master-reference material, not an active Paper 25 numerical dependency. The
appendix/master table still contains old CMB-temperature prediction wording
(`T_obs = T_IO x^K_gauge = 2.7253 K`, `gamma_required (FIRAS)`, and `sigma =
K_gauge ... R4 premise`). Those entries should be rewritten or removed before
publication because the current Paper 17 v1.5 boundary is: FIRAS fixes
`R4_FIRAS = 1.0031014644`; CMB temperature is not counted as an independent IO
prediction.

The v2.0 manuscript also has one numerical hygiene issue: the version-history
paragraph says combined three-observable `chi2 = 1.13`, while the live Paper
24 v3.0 Pastore row and the body/table round to `chi2 = 1.17`
(`1.1650691917465592` exact from the frozen sigmas).

## Candidate Kappa Fields and Rigidity Tests

| Candidate field | Rigidity test | Classification |
| --- | --- | --- |
| `gamma_BI = 0.2375` | Imported framework-wide Barbero-Immirzi input; Paper 25 does not tune it against BBN. Changing it is a framework-wide input change. | `IMPORTED/EMPIRICAL` upstream input |
| `K_gauge = ln(1+gamma_BI^2)` | Forced algebraically once `gamma_BI` is fixed. Paper 25 tests class membership, not the functional form. | `DERIVED/THEOREM` upstream |
| `V' = 2 gamma_BI` | Forced as the first tangent covector of the Paper 18 generating potential. It is an allowed comparator, then structurally excluded for rates. | `DERIVED/THEOREM` comparator |
| `V'' = 2(1+gamma_BI^2)` | Forced as the curvature/intensity rung of the same generating potential; excluded by rate-ratio computation on the constructed extension. | `DERIVED/CONDITIONAL_VERIFIED` exclusion on H1/H2 |
| `L_1` | Inherited from Paper 21 puncture-load construction. Paper 25 does not fit it. | `DERIVED/THEOREM` upstream |
| Weak amplitude order `L_1` vs `sqrt(L_1)` | Forced by the rate-as-two-time-correlator formulation: the physical rate is quadratic in the bridge field, so the old one-point amplitude branch is superseded. | `DERIVED/CONDITIONAL_VERIFIED` on H1-H3 |
| H1 | Explicit spatial KMS extension identified as the physical bridge state. This is visible, not hidden; it is the main conditional input. | `DERIVED/CONDITIONAL_VERIFIED` if accepted through Paper 22 Construction 1 + Paper 23 Lemma 23.A |
| H2 | Minimal spatial canonical-commutation-relation lift identified as the weak perturbation sector. Visible class-membership input. | `DERIVED/CONDITIONAL_VERIFIED` |
| H3 | Physical weak freeze-out rate represented by a centered two-time Kubo-Martin-Schwinger correlator. Supported by standard rate physics/Fermi Golden Rule. | `DERIVED/CONDITIONAL_VERIFIED` |
| `R(gamma)=1` | Computed on the explicit constructed extension from `beta_IO`, quasi-free uniqueness, and gamma-blind weak shell eigenvalue. | `DERIVED/CONDITIONAL_VERIFIED` on H1/H2 |
| `epsilon_n = (<K>/10) L_2` | Inherited upstream from the Paper 22/Paper 24 nuclear channel. Not fitted in Paper 25. | `DERIVED/CONDITIONAL_VERIFIED` upstream |
| BBN scorecard row | Frozen PRyMordial output row after theorem-selected branch; validates consequence, does not select branch. | `VERIFIED` |
| `R4_FIRAS = 1.0031014644` | Not used by active Paper 25 scripts. Recorded only for dependency hygiene. | No active Paper 25 degree of freedom |

## R4 Damage Review

Active script review:

- `01_v_vs_vprime_constants.py`: no R4 use.
- `02_core_theorem_ledger.py`: no R4 use.
- `03_two_time_correlator_closure.py`: uses fixed BBN branch temperature
  language through the constructed-extension chain; no observer-side CMB
  readout and no `R4 = 1`.
- `04_bbn_branch_scorecards.py`: frozen PRyMordial BBN rows; no CMB prediction
  or R4 normalization.
- `05_paper22_correction_boundary.py`: weak amplitude correction only; no R4.
- `06_kappa_audit_summary.py`: records R4 boundary only.
- `07_validate_expected_outputs.py`: validates R4 boundary metadata only.

Manuscript R4/CMB hygiene flags:

- Master table entry `T_obs = T_IO x^K_gauge = 2.7253 K` should not be stated
  as a GTTP temperature prediction. Current repair language should say FIRAS
  fixes `R4_FIRAS` in the observer-side readout family.
- Master table entry `gamma_required (FIRAS) = 0.23789` is stale in the current
  R4 repair frame and should not be used as evidence for an independent CMB
  prediction.
- Master table entry `a = dim(S^2)/2 = 1` should not be allowed to imply
  derivation of the optical readout normalization.
- Master table entry `sigma = K_gauge ... R4 premise` should point to Paper 17
  v1.5 FIRAS-fixed readout normalization, not an open R4 premise.
- Appendix Step 11 language explaining COBE/FIRAS perfection should be narrowed
  to blackbody/greybody structure if retained; do not count the CMB temperature
  as predicted.

## Label Drift

The v2.0 draft still contains noncanonical labels:

- `CONDITIONAL/THEOREM` in live theorem statements.
- `CONDITIONAL on ...` in the channel-budget status.
- bare `STATUS: DERIVED` throughout the appendix and some body text.
- `FRAMEWORK CORRECTION` for the Paper 22 weak-amplitude correction.

Recommended canonical migrations:

- Use `DERIVED/THEOREM` for theorem-grade results with no conditional physical
  class-membership package.
- Use `DERIVED/CONDITIONAL_VERIFIED` for H1-H3-dependent weak-sector closure
  and constructed-extension results.
- Use `VERIFIED` for PRyMordial scorecard rows.
- Use `SUPERSEDED` for the old `K_gauge * sqrt(L_1)` amplitude branch.

## Abbreviations and IO Slang Flags

Abbreviations that should be expanded on first use or avoided in a standalone
paper: `IO`, `BBN`, `GTTP`, `BDP`, `CMP`, `WMR`, `GMP`, `TBS`, `TBSb`, `KMS`,
`CCR`, `CAR`, `TT`, `RN`, `YPCMB`, `PRyMordial`, `H_IO`, `Z_g`, `F_0`, `LQG`.

IO-specific or nonstandard phrases that should be explained in standard
physics language before use: `identity pin`, `V-vs-V'`, `weak modular readout`,
`channel-budget equation`, `scalarization`, `bridge`, `puncture load`,
`A-vacuum`, `one-cell normalization`, `spatial KMS extension`, `minimal spatial
CCR lift`, `bridge Riesz vector`, `weak observable class`.

## Bundle Reconciliation

The v1.3 bundle froze the older Paper 24 v2.2/Henderson-only support row:

- `D/H = 2.509938817767262e-5`
- `Y_p = 0.24771903130174175`
- `Li-7/H = 1.7508826463710944e-10`
- `chi2 = 1.0893566013769407`

The v2.0 bundle now freezes the Paper 24 v3.0 Pastore branch:

- `D/H = 2.5072097840055007e-5`
- `Y_p = 0.24770877182909237`
- `Li-7/H = 1.7414708079857392e-10`
- `chi2 = 1.1650691917465592`

This is a support-row update, not a change to the Paper 25 theorem proof. The
theorem selects the quadratic weak branch; the BBN scorecard verifies the
selected branch against the active Paper 24 v3.0 network row.

## Final Classification

Paper 25 v2.0 survives the kappa-style audit for its active support surface:
no hidden fitted scalar was found. The theorem-grade claim remains scoped:
weak-sector closure is `DERIVED/CONDITIONAL_VERIFIED` on H1-H3. Universal GMP
outside the currently covered transverse-traceless and weak observable classes
remains open at full Paper 22 bridge scope.
