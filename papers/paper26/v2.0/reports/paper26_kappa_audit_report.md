# Paper 26 v2.0 R4 / Kappa-Style Structural Audit

Date: 2026-05-16

Source manuscript: `/opt/cosmology-lab/results/Full Papers/Interior_Observer_Paper26_v2_0.docx`

Extracted text used for this audit: `/opt/cosmology-lab/results/paper26/Interior_Observer_Paper26_v2_0_extracted.txt`

Public bundle target: `/opt/cosmology-lab/tmp/io-framework-public/papers/paper26/v2.0/`

## Executive Verdict

No hidden continuous fitted parameter was found in the active Paper 26 v2.0 scripted claims.

The R4 repair does not numerically change Paper 26's active scripted outputs. Paper 26 does not use the observed CMB temperature as a computed prediction in its bundle scripts. The active scripts compute:

- `A_s = 2.0072459972737347e-9`, conditional on `C1 + C2c`;
- `tau_eff,IO = K_gauge/2 = 0.02743640887145733`, from Theorem 26.C3's reduced source-covariance class;
- `A_eff = A_s exp(-K_gauge) = 1.9000701645543414e-9`;
- the CMB baryon-class diagnostic rows;
- the high-l TT reionization-shape diagnostic.

R4 now enters Paper 26 only as inherited metadata from Paper 17 v1.5:

```text
R4_FIRAS = 1.0031014644
```

The observed CMB temperature is an `IMPORTED/EMPIRICAL` FIRAS datum used to fix the optical-readout normalization in Paper 17 v1.5. It is not an independent Interior Observer prediction.

## R4 Damage Review

### Script-Level Review

Result: no live script used `R4 = 1`.

Checked bundle script surfaces:

- `01_scalar_amplitude_chain.py`: no R4 dependence.
- `02_tensor_conditionals.py`: no R4 dependence.
- `03_cmb_baryon_class_diagnostic.py`: no R4 dependence; emits frozen CLASS diagnostic rows.
- `04_tau_eff_and_damping.py`: no R4 dependence; uses `K_gauge/2` from Theorem 26.C3.
- `05_reionization_shape_tt_check.py`: no R4 dependence; emits frozen high-l TT diagnostic.
- `06_kappa_audit_summary.py`: updated to record `R4_FIRAS` as metadata and to state that CMB temperature is not an IO prediction.
- `07_validate_expected_outputs.py`: updated to validate the R4 metadata and the C2c forward-check guard.
- `scripts/c2c_analysis/01_c2c_as_forward_check.py`: no R4 dependence.

The frozen reports `paper26_io_native_recombination_results.json` and `paper26_reionization_shape_elimination_audit_results.json` contain `T_cmb = 2.7253` as a standard CLASS/CMB input. That is acceptable only as an external empirical CMB temperature used by CLASS-like thermodynamics, not as an IO prediction.

### Manuscript-Level R4 / CMB Temperature Review

The v2.0 draft mostly applies the Paper 17 v1.5 R4/FIRAS boundary correctly. The version-history line, Step 34, and the master table correctly state that `R4_FIRAS` is fixed by FIRAS and that the CMB temperature is not counted as an independent IO prediction.

Two inherited appendix lines still require review before publication:

1. Step 35 Piece 5 says:

```text
Exact identity ln(T_obs/T_IO) = K_gauge * ln(x) -- ALGEBRAICALLY EXACT
```

Recommended correction:

```text
Exact identity within the FIRAS-normalized readout family:
ln(T_obs/T_IO) = R4_FIRAS * K_gauge * ln(x), with R4_FIRAS imported from Paper 17 v1.5.
```

2. Step 88 says:

```text
T_obs = T_IO * x^K_gauge
```

Recommended correction:

```text
T_obs(R4) = T_IO * x^(R4 K_gauge), with R4 = R4_FIRAS fixed by FIRAS in Paper 17 v1.5. This is not an independent CMB-temperature prediction.
```

These are manuscript hygiene issues, not script failures. They should be corrected or removed in Paper 26 v2.0 before publication.

## Candidate Kappa Fields and Classifications

| Target | Candidate free field | Rigidity test | Classification |
|---|---:|---|---|
| `gamma_BI = 0.2375` | replace by `kappa_gamma` | Imported once from the Barbero-Immirzi/LQG convention used throughout IO; not fit in Paper 26. | `IMPORTED/EMPIRICAL` upstream input |
| `R4_FIRAS` | replace by `R4 = 1` or fitted `R4` | Paper 17 v1.5 fixes R4 from FIRAS. Paper 26 does not use R4 to predict CMB temperature or tune outputs. | `IMPORTED/EMPIRICAL` metadata inherited from Paper 17 |
| Dust conversion `25/9` | replace by arbitrary `kappa_R` | Forced by standard dust superhorizon relation `R = (5/3) Phi` on the stated branch. | `DERIVED/CONDITIONAL_VERIFIED` on dust superhorizon branch |
| `S^2 ell=1` carrier | replace by radial/time-frequency route or higher shell | Lemma C2.1 separates background and perturbation channels; Lemma C2.2 identifies the carrier. | C2a/C2b `DERIVED/THEOREM`; C2c remains `OPEN/PREMISE_GAP` |
| Hawking exponent `4 pi sqrt(2)` | replace by arbitrary `beta omega` | Forced once the S2 coexact carrier and Hawking state are selected. State selection remains C2c. | `DERIVED/CONDITIONAL_VERIFIED` on C2c |
| Bose occupation | use another occupation law | Forced for a bosonic Hawking thermal state once C2c is admitted. | `DERIVED/CONDITIONAL_VERIFIED` on C2c |
| Canonical source normalization `1/sqrt(2)` | replace by arbitrary normalization | Standard canonical oscillator variance `n/omega`; not selected from Planck. | `DERIVED/THEOREM` within stated coordinate convention |
| Extrinsic fraction `gamma^2/(1+gamma^2)` | replace by fitted fraction | Paper 15 proves background partition; C1 extends it to fluctuation covariance. | `DERIVED/CONDITIONAL_VERIFIED` on C1; C1 itself `OPEN/PREMISE_GAP` |
| `A_s` formula | introduce fitted amplitude scalar | All factors are structural/imported; value remains -4.4 percent from Planck, not tuned to Planck. | `DERIVED/CONDITIONAL_VERIFIED` on C1 + C2c |
| Tensor branch | choose tensor carrier/range by fit | Manuscript labels as conditional; not used as unconditional closure. | `DERIVED/CONDITIONAL_VERIFIED` on C2c plus tensor extension |
| Three baryon densities | tune densities independently | Values inherited from Papers 12/18/19; Paper 26 tests class authorization, not fit. | upstream `DERIVED/CONDITIONAL_VERIFIED` or `VERIFIED` as applicable |
| Thomson kernel | split visibility/acoustic primitive by hand | Same primitive `a n_e sigma_T` appears in standard equations and CLASS. | `DERIVED/THEOREM` |
| AV1 | assign visibility to acoustic class | Shared primitive opacity does not itself force class membership. | Theorem 26.AV' is `DERIVED/CONDITIONAL_VERIFIED`; AV1 is `OPEN/PREMISE_GAP` |
| C3 / `tau_eff = K_gauge/2` | replace with `K_gauge`, `f_K`, or fitted tau | Theorem 26.C3 gives one inverse-kernel covariance factor `exp(-K_gauge)` on the reduced centered Gaussian source-covariance class; convention `exp(-2 tau)` gives `K_gauge/2`. | `DERIVED/CONDITIONAL_VERIFIED` on reduced source-covariance class + Definition 26.C3.3 |
| `A_eff = A_s exp(-K_gauge)` | fit TT amplitude | Follows from active `A_s` and Theorem 26.C3 damping; not optimized against Planck. | `DERIVED/CONDITIONAL_VERIFIED` + `VERIFIED` arithmetic |
| Reionization shape high-l TT | fit shape to TT | Frozen CLASS sweep shows high-l TT shape changes below 0.4 in chi-square; low-l EE remains open. | `VERIFIED`; low-l EE remains `OPEN/PREMISE_GAP` |

## Anti-Fit Backstop

No continuous parameter is tuned against Planck, CLASS, or CMB temperature in the active Paper 26 v2.0 scripts.

The highest-risk surfaces are not hidden fits; they are visible open structural identifications:

- `C1`: fluctuation covariance inherits the background gauge partition.
- `C2c`: the boundary one-particle covariance on the proved carrier is the Hawking thermal covariance.
- `AV1`: Thomson-gated scalar CMB visibility/readout belongs to the acoustic baryon class.

The former broad `C3` open premise is narrowed and closed as Theorem 26.C3 only for the reduced centered Gaussian source-covariance class. It does not close reionization history, astrophysical optical depth, low-l EE, full Boltzmann transfer, C1, or C2c.

## Label Discipline Review

Active Paper 26 v2.0 body claims mostly use the canonical public labels:

- `DERIVED/THEOREM`
- `DERIVED/CONDITIONAL_VERIFIED`
- `DERIVED/NO-GO`
- `VERIFIED`
- `IMPORTED/EMPIRICAL`
- `OPEN/PREMISE_GAP`

Items requiring manuscript review:

1. Step 35 Piece 5 uses "ALGEBRAICALLY EXACT" rather than a canonical status and omits `R4_FIRAS` from the readout identity.
2. Step 88 still uses the old `T_obs = T_IO x^K_gauge` statement and should be superseded by the Paper 17 v1.5 FIRAS-normalized family.
3. Step 383 still says the bridge-gain cancellation leaves only the Levi-Civita perturbation. That should be reconciled with body Theorem 26.1, which states that the scalar bridge reads `gamma delta K` and `delta Gamma` vanishes under isotropic contraction.
4. Inherited catalog rows still use source-paper shorthand `STATUS: DERIVED`. The v2.0 draft explicitly says inherited rows retain source shorthand unless updated. That is acceptable for inherited catalog material, but load-bearing active Paper 26 citations should use canonical labels.

## Abbreviations and IO Slang Review

Abbreviations still present and should be expanded on first use or avoided in body prose when possible:

- `IO`: Interior Observer.
- `CMB`: Cosmic Microwave Background.
- `BBN`: Big Bang nucleosynthesis.
- `CLASS`: Cosmic Linear Anisotropy Solving System.
- `LambdaCDM` / `LCDM`: Lambda Cold Dark Matter.
- `GTTP`: Gauge Thermal Transfer Principle.
- `CMP`: Conformal Modular Principle.
- `BDP`: Baryon Dictionary Principle.
- `GMP`: Geometric Mediation Principle.
- `TBS`, `TBSb`, `WMR`, `PSRP`, `TT1`: inherited IO-framework theorem packages; these should be expanded or replaced by theorem names where load-bearing.
- `KMS`, `CCR`: standard mathematical-physics abbreviations, but should still be expanded on first use.
- `OS`, `FRW`, `LQG`, `TT`, `TE`, `EE`: standard to physicists but should be expanded once.
- `C1`, `C2c`, `AV1`, `C3`, `H1`, `H2`, `R4`: framework-local labels; every occurrence in body text should be near a definition or in a premise ledger.

IO-specific phrasing still present and worth minimizing in body prose:

- "slot"
- "readout"
- "branch"
- "rung"
- "alpha-ladder"
- "bridge"
- "no-doubling"
- "puncture"
- "one-slot" / "two-slot"
- "Rosetta"

Some of these are legitimate technical terms inside the IO framework, but a non-IO reader will not know them. The best manuscript practice is: use standard physics language in section prose, and define IO terms only where technically unavoidable.

## Script Documentation Review

The public v2.0 scripts have been updated so that:

- every script identifies the Paper 26 v2.0 claim it supports;
- conditional claims use `DERIVED/CONDITIONAL_VERIFIED`, not retired `DERIVED/CONDITIONAL`;
- the R4/FIRAS boundary is recorded in the kappa-summary output;
- C3 is no longer counted as an open premise in the validator;
- the C2c forward-check script is included in public validation.

## Final Classification

Paper 26 v2.0 is publishable as a conditional support paper if the manuscript keeps the open-premise endpoints visible.

No hidden continuous fitted parameter was found.

The active open endpoints are:

- `C1` - `OPEN/PREMISE_GAP`;
- `C2c` - `OPEN/PREMISE_GAP`;
- `AV1` - `OPEN/PREMISE_GAP`;
- low-l EE / ionization-history completion - `OPEN/PREMISE_GAP`.

The broad old `C3` premise is replaced by:

```text
Theorem 26.C3 (Reduced Source-Covariance Propagator)
Status: DERIVED/CONDITIONAL_VERIFIED on the reduced centered Gaussian source-covariance class and Definition 26.C3.3.
```

