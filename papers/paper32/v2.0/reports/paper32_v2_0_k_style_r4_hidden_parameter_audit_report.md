# Paper 32 v2.0 K-Style R4 / Hidden-Parameter Audit

Date: 2026-05-21

Draft audited: `/opt/cosmology-lab/results/Full Papers/Interior_Observer_Paper32_v2_0.docx`

Public bundle audited: `/opt/cosmology-lab/tmp/io-framework-public/papers/paper32/v2.0`

## Executive Verdict

Paper 32 v2.0 numerically inherits the Paper 32 v1.6 R4/FIRAS repair. The active scripts use
`R4_FIRAS = 1.0031014644105183` in the observer-side thermal readout family and retain
`R4 = 1` only as a historical diagnostic. No active Paper 32 v2.0 script retunes R4 against
downstream observables, and no fitted continuous parameter was found in the public scripts.

The main remaining manuscript issue is label discipline: the current v2.0 draft still uses
retired status strings, especially `DERIVED/SCOPED`, throughout the body and appendix. The
public v2.0 bundle support text has been migrated to canonical labels where the bundle itself
states current scope boundaries; the DOCX manuscript should receive the same pass before final
publication.

## R4 Usage In Calculations

- `scripts/01_compute_framework_constants.py` computes the FIRAS-fixed normalization from
  `R4_FIRAS = ln(T_FIRAS/T_IO) / (K_gauge ln x)` and verifies
  `T_obs(R4_FIRAS) = 2.7255 K`.
- The same script records `T_obs(R4=1) = 2.725306096638128 K` only as a historical diagnostic.
- `scripts/09_r4_firas_impact_audit.py` explicitly audits the old `R4=1` damage and records that
  the active thermal readout is FIRAS-normalized.
- `scripts/10_validate_expected_outputs.py` validates `R4_FIRAS`, `sigma_R4_FIRAS_only`,
  `T_obs_FIRAS_fixed_K`, and the historical `T_obs_R4_equals_1_K` diagnostic.
- The scalar-index, scalar-amplitude, `x_crit`, recollapse, cycle-time, and KB7/P4 scripts do
  not depend on the optical thermal R4 normalization.

## Hidden Fitted Parameter Audit

- `R4_FIRAS`: not a hidden fitted cosmological parameter if used under the Paper 17 rule. It is
  fixed once by the FIRAS empirical CMB-temperature datum and then frozen. The bundle confirms it
  is not retuned against `n_s`, `A_s`, late-time recollapse, BAO, BBN, Hubble tension, or any
  downstream observable.
- `gamma_BI = 0.2375`: imported from LQG black-hole entropy counting, not fitted to cosmological
  data. The draft states this distinction explicitly.
- `M_U = 4.50e53 kg`: treated as measured mass-energy input, not a fit to Paper 32 outputs.
- KB7/P4 source-block normalization: the bundle support text now states the canonical scope as
  `DERIVED/CONDITIONAL_VERIFIED` on the active reduced scalar source block. It does not derive
  Paper 17 optical R4 and does not apply universally to arbitrary thermal, drag, recombination,
  or history observables.
- Bounce/restart selectors: remain conditional scope packages. They are not numerical fits in
  the current scripts, but the manuscript should avoid labels that imply raw-stack uniqueness
  outside the stated selector package.

No active fitted parameter was found in the v2.0 public reproducibility scripts.

## CMB/CMD Temperature Claim Audit

- No `CMD` phrase was found in the extracted Paper 32 v2.0 text or public bundle.
- The v2.0 abstract/scope/prerequisites correctly state that the observed CMB temperature is not
  counted as an independent IO prediction; it is a FIRAS empirical datum fixing the optical
  readout normalization via Paper 17 v1.5 Theorem 17.2.
- The bundle still contains historical audit references to old `T_CMB` prediction damage, but
  those references are explicitly framed as retired damage and repair guidance.
- Recommendation: keep the current body language that says FIRAS fixes `R4_FIRAS`; do not use
  wording such as "IO predicts the FIRAS CMB temperature."

## Manuscript Label Discipline Findings

Raw count in the extracted v2.0 draft:

- `DERIVED/SCOPED`: 152
- `DERIVED/CONDITIONAL_VERIFIED`: 0
- `DERIVED/NO-GO`: 2
- `VERIFIED`: 6
- `IMPORTED/EMPIRICAL`: 0
- `RECONSTRUCTION`: 4
- `OPEN/PREMISE_GAP`: 0
- `SUPERSEDED`: 3
- `CONDITIONAL/SCOPED`: 5
- `DERIVED/CONDITIONAL`: 24
- `HOLDING`: 0
- `RECALIBRATED`: 0

Recommended canonical migration:

- Replace load-bearing `DERIVED/SCOPED` claims with `DERIVED/CONDITIONAL_VERIFIED` when the scope
  closes to P1, P2, imported empirical inputs, or named banked theorem inputs.
- Replace scoped no-go statements with `DERIVED/NO-GO`.
- Replace `DERIVED/CONDITIONAL` and `CONDITIONAL/SCOPED` with
  `DERIVED/CONDITIONAL_VERIFIED` when the conditional package is explicit and verified.
- Replace prose-only statuses such as `PROMOTED`, `PROMOTED (CLEAN)`, `WEAKENED`, `RESOLVED`,
  and `CONDITIONAL/RECONSTRUCTION` with canonical labels plus explanatory prose.
- Mark FIRAS, LQG `gamma_BI`, `M_U`, and branch-resolved A=7 nuclear inputs as
  `IMPORTED/EMPIRICAL` or clearly named imported/frozen inputs where they terminate chains.

Specific stale or high-priority examples:

- Step 492 says C2q Hawking state selection remains semiclassical and has status
  `CONDITIONAL/SCOPED`, while later Paper 32 entries promote C2q. This should be reconciled.
- Steps 528-529 use `DERIVED/CONDITIONAL`, a retired label form.
- Steps 531-548 and 560-570 repeatedly use `DERIVED/SCOPED`; these should use
  `DERIVED/CONDITIONAL_VERIFIED` or `DERIVED/NO-GO` with the scope stated inline.
- Step 496 remains `RECONSTRUCTION/CONDITIONAL` for the CMB Weyl half-order kernel. If retained
  in Paper 32, make clear it is not promoted by Paper 32 v2.0 unless a later theorem is cited.

## Abbreviations And IO Slang To Review

Frequent abbreviations or local terms that should be expanded at first use or replaced by
standard physics terminology where possible:

- Framework abbreviations: `IO`, `CMP`, `BDP`, `GTTP`, `GMP`, `BFP`, `PSRP`, `TBS`, `C2q`,
  `C1b`, `AV1`, `KB7`, `P4`, `SP-1` through `SP-4`.
- Cosmology/physics abbreviations: `CMB`, `BAO`, `BBN`, `DESI`, `FRW`, `OS`, `LQG`, `PG`,
  `KMS`, `CCR`, `TT`, `EE`, `DtN`, `S8`.
- IO-local phrases: "source block", "one-slot", "hard restart", "soft restart", "observer dies",
  "support clamp", "hidden support variable", "Schur contamination", "Rosetta identity",
  "bridge-readable quotient", "parasitic", "killed", and "semantic restoration".

These terms are not all wrong, but Paper 32 should assume the reader has not read the prior
papers. The first body occurrence should define the term or use standard physics language.

## Bundle Repair Actions Taken

- Created Paper 32 v2.0 public bundle from the v1.6 R4-repaired bundle.
- Regenerated all public v2.0 frozen JSON outputs from scripts.
- Migrated public bundle support labels from `DERIVED/SCOPED` / `DERIVED/CONDITIONAL` /
  `CONDITIONAL/SCOPED` to canonical `DERIVED/CONDITIONAL_VERIFIED` where applicable.
- Re-ran validator: `18/18 PASS`.

## Remaining Manuscript Work

The public scripts are R4-safe and validated. The manuscript still needs a label-convention pass
and a readability pass for abbreviations and IO slang. No numerical rerun is required for the R4
repair because Paper 32 v2.0 states that theorem content and numerical values are unchanged from
v1.6.
