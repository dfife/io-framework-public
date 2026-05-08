# Paper 20 v1.8 R4/FIRAS Kappa-Style Structural Audit

Date: May 2026

## Executive Verdict

No new hidden continuous fitted parameter was found in Paper 20's live acoustic
Jacobian, BBN wrapper-correction scorecard, or radiation-sector no-go scripts
after the Paper 17 v1.5 R4/FIRAS repair.

The audit did find manuscript-level R4 damage:

- Paper 20 v1.7 still presents `T_obs = T_IO x^K_gauge = 2.7253 K` as an active
  temperature prediction.
- Paper 20 v1.7 still lists `R4 normalization` as pending.
- Appendix inherited Paper 17 steps still label the old R4=1 optical readout as
  `DERIVED`.
- The universal-transport no-go language still uses a `20.15 sigma` CMB
  temperature failure as if the CMB temperature were an independent IO
  prediction.

Required v1.8 boundary:

```text
T_obs(R4) = T_IO * x^(R4*K_gauge)
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255 K
```

FIRAS is an `IMPORTED/EMPIRICAL` observer-side thermal datum. Paper 17 v1.5
provides the uniqueness theorem inside the readout family. The CMB temperature
must not be counted as an independent Paper 20 prediction.

## R4 Impact Ledger

| Surface | R4 Use | v1.8 Status |
|---|---:|---|
| Temperature scorecard row | Old `R4=1` formula reported as prediction | Retire as prediction; keep FIRAS-fixed readout datum only |
| BBN scorecard | Uses early-time `T_IO`, not observer-side `T_obs` | Numerically unchanged by R4 repair |
| Acoustic angle `theta*` | Uses `J_theta = x^(-1/2) sqrt(1+gamma^2)` | R4-independent |
| Torsion-Lambda bare branch | Uses observer-side `T_obs` in late-time radiation bookkeeping | Updated to `2.7255 K`; effect is negligible for late-time branch values |
| Radiation-sector construction theorems | Use `T_IO` for pre-decoupling thermal state | R4-independent |
| Universal-transport no-go appendix | Uses CMB-temperature residual as active kill criterion | Must be reframed as historical/SUPERSEDED after Paper 17 v1.5 |

## Recomputed / Refreshed Outputs

The repaired scripts now use the FIRAS-fixed observer-side thermal datum:

```text
R4_FIRAS = 1.0031014644
T_obs = 2.7255 K
old R4=1 factor x^K_gauge = 1.023204472362383
FIRAS-fixed factor x^(R4*K_gauge) = 1.023277271400324
```

The live v1.6/v1.7 BBN correction row remains:

```text
D/H = 2.510410594954571e-5, residual -0.5529801682 sigma
Y_p = 0.24781814417284279, residual +0.7045360432 sigma
Li-7/H = 5.363335812719e-10, residual +12.2043090733 sigma
chi2(D/H + Y_p) = 0.8021581026
```

The Paper 19 inherited modern-amplitude diagnostic row used by some Paper 20
support diagnostics is:

```text
D/H = 2.5233039701421276e-5, residual -0.1232009953 sigma
Y_p = 0.24779423821196234, residual +0.6985595530 sigma
Li-7/H = 5.331502875744094e-10, residual +12.1016221798 sigma
```

These two rows have different scope. The first is the Paper 20 published
wrapper-correction row at `omega_b_h2 = 0.02108`; the second is inherited from
the Paper 19 modern-amplitude diagnostic scripts.

## Kappa-Style Candidate Field Tests

### R4 optical readout normalization

- Candidate field: replace `R4=1` by free `kappa_R4`.
- Rigidity test: Paper 17 v1.5 showed the modular-projection stack admits a
  continuous readout family until FIRAS fixes the observer-side datum.
- Classification: `IMPORTED/EMPIRICAL` FIRAS datum plus `DERIVED/THEOREM`
  uniqueness inside the stated readout family.
- Paper 20 impact: no independent CMB-temperature prediction remains.

### Acoustic phase-calibration factor

- Candidate field: replace `J_theta = x^(-1/2) sqrt(1+gamma^2)` by free
  `kappa_theta`.
- Rigidity test: local theorem depends on AH1-AH7 plus AC1 and Paper 16
  composite uniqueness. Paper 20 v1.7 text says AC1 is not locally derived but
  later closed in Paper 21.
- Classification recommendation: `DERIVED/CONDITIONAL_VERIFIED` only if Paper
  21 v1.7 closure is cited explicitly; otherwise `OPEN/PREMISE_GAP`.
- Hidden-fit risk: AC1 must not remain hidden under bare `CONDITIONAL THEOREM`.

### Torsion-Lambda bare branch

- Candidate field: replace `H0_bare = 39.649873...` by free `kappa_H`.
- Rigidity test: the script derives the branch from `M_U`, OS geometry, Paper 1
  torsion Lambda, and imported standard-model radiation. The branch is
  algebraically fixed once those inputs are accepted.
- Classification: branch arithmetic `DERIVED/THEOREM`; branch selection and
  observational adequacy remain `OPEN/PREMISE_GAP`.

### BBN wrapper correction

- Candidate field: replace helium output index, weak amplitude, nuclear
  amplitude, or observational denominators.
- Rigidity test: YPCMB index and denominators are convention-fixed; amplitudes
  are inherited from Paper 22/Paper 24.
- Classification: `DERIVED/CONDITIONAL_VERIFIED` through upstream amplitude
  theorem package plus `VERIFIED` numerical wrapper output.
- Hidden-fit risk: none found in Paper 20 itself; the upstream amplitude package
  carries its own GMP/TBS conditional-verified dependency.

### Radiation-sector construction theorems

- Candidate field: replace species count, reheating bookkeeping, or CAR/CCR
  algebra selection.
- Rigidity test: Paper 20 constructs compatibility with standard thermal
  physics; it does not derive the species count internally.
- Classification recommendation:
  - RAD1: `DERIVED/CONDITIONAL_VERIFIED` as construction under stated imported
    standard-model radiation inputs.
  - RAD2: `DERIVED/CONDITIONAL_VERIFIED` as consistency construction under the
    same inputs.
  - RAD3: `DERIVED/NO-GO`.

## Manuscript Locations Requiring v1.8 Attention

- Paragraph 17: `CONDITIONAL THEOREM` label for Theorem 20.2.
- Paragraph 40: same `CONDITIONAL THEOREM` label and AC1 language.
- Paragraph 67: active `T_CMB` prediction row must be removed or rewritten as
  FIRAS-fixed normalization.
- Paragraph 91/109/110: Paper 22 references use retired
  `DERIVED/CONDITIONAL` wording and should migrate to the canonical label used
  after the claim-discipline update.
- Paragraph 121: `R4 normalization ... [Pending verification]` is stale.
- Paragraphs 153, 276-280, 324-326: master-reference table still presents old
  GTTP/R4 temperature prediction material.
- Appendix Steps 35-36, 39-41, 51, 81-82, 96: inherited Paper 17 R4 surfaces
  require Paper 17 v1.5 replacement text or `Historical/SUPERSEDED` framing.
- Appendix A.6.4-A.6.5: universal-transport no-go must not use CMB-temperature
  residual as an active independent-prediction kill criterion.

## Noncanonical Label Findings

Paper 20 v1.7 uses labels outside the current public claim-discipline scheme:

- `CONDITIONAL THEOREM`
- `SCOPE-BOUNDARY RESULT`
- `TORSION-Lambda BARE BRANCH ALGEBRAICALLY SPECIFIED`
- `CONSTRUCTION THEOREM`
- `CONSTRUCTION/CONSISTENCY THEOREM`
- bare `THEOREM`
- bare `DERIVED`
- `DERIVED/CONDITIONAL`
- `[CONDITIONAL]`

Recommended migrations:

- Theorem 20.1: `DERIVED/THEOREM`.
- Theorem 20.2: `DERIVED/CONDITIONAL_VERIFIED` if explicitly routed through
  Paper 21's AC1 closure chain; otherwise `OPEN/PREMISE_GAP`.
- Radiation scope boundary: `DERIVED/NO-GO` or `OPEN/PREMISE_GAP`, depending on
  whether the statement is presented as a no-go theorem or a remaining scope
  boundary.
- Torsion-Lambda bare branch: arithmetic `DERIVED/THEOREM`; branch-selection
  status `OPEN/PREMISE_GAP`.
- RAD1/RAD2: `DERIVED/CONDITIONAL_VERIFIED`.
- RAD3 and the radiation null routes: `DERIVED/NO-GO`.
- FIRAS temperature datum: `IMPORTED/EMPIRICAL`; uniqueness of R4 in the readout
  family: `DERIVED/THEOREM`.

## Abbreviation / IO-Slang Hygiene

The companion slang report lists manuscript locations where a non-IO reader
will likely need replacement or first-use expansion. High-priority terms:

- `IO`, `GTTP`, `CMP`, `BDP`, `H_IO`, `M_red`, `Z_g`
- `slot`, `rung`, `branch`, `scorecard`, `kill`, `fossil`
- `AC1`, `AH1-AH7`, `RT/BY`, `P1-P6`, `B1-B5`
- `Schur`, when used as shorthand without the relevant Schur-complement
  construction

## Bottom Line

Paper 20 v1.8 can be repaired without changing the live acoustic or BBN
calculation outputs. The required change is claim discipline:

1. Retire independent CMB-temperature prediction language.
2. Replace old R4/GTTP inherited text with Paper 17 v1.5 FIRAS-fixed
   normalization.
3. Migrate noncanonical labels to the public claim-discipline scheme.
4. Expose AC1 as `DERIVED/CONDITIONAL_VERIFIED` through Paper 21 or as
   `OPEN/PREMISE_GAP`; do not leave it as a vague conditional.
