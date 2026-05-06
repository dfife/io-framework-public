# Paper 35 v1.2 R4/FIRAS Kappa-Style Impact Audit

Date: May 2026

## Executive Verdict

No hidden continuous fitted parameter was found inside Paper 35 after replacing the retired implicit optical readout normalization `R4 = 1` with the Paper 17 v1.5 FIRAS-fixed value

`R4_FIRAS = 1.0031014644105183`.

However, R4 damage was real in Paper 35 v1.1: the late-time eta route used the observer photon bath temperature inherited from the optical readout. That route must now be described as FIRAS-fixed through Paper 17 v1.5, not as an independent CMB-temperature prediction. The affected numerical target values have been recomputed in the v1.2 bundle.

## Active Boundary

Paper 35 v1.2 uses the Paper 17 v1.5 readout theorem:

`T_obs(R4) = T_IO x_R4_source^(R4 K_gauge) = T_FIRAS`.

The CMB temperature is not counted as an IO prediction. FIRAS supplies the empirical observer-side thermal datum. R4 is fixed once by FIRAS and is not retuned against eta, DESI, JWST timing, dark-sector tests, or baryogenesis targets.

## Numeric Impact Table

| Quantity | v1.1 implicit R4=1 | v1.2 FIRAS-fixed R4 | Impact |
|---|---:|---:|---|
| `T_obs` | 2.7253048490552736 K | 2.7255 K | repaired input normalization |
| `x^(3 R4 K_gauge)` conversion | 1.071240943860573 | 1.0714710854379792 | repaired |
| `eta_late` mean-baryon-mass convention | 5.748778515173695e-10 | 5.74754373341092e-10 | repaired |
| `eta_late` proton-mass convention | 5.74179586430453e-10 | 5.740562582347311e-10 | repaired |
| `eta_BBN` proton-mass convention | 6.150846821132321e-10 | 6.150846821132321e-10 | invariant after consistent recomputation |
| `Y_B` target | 8.165878572689907e-11 | 8.16412462132233e-11 | repaired |
| `epsilon_1 kappa_f` target | 5.905280726708112e-8 | 5.9040123297910706e-8 | repaired |
| Poplawski eta-target scale | 2.20039385974778e13 GeV | 2.2001575354474027e13 GeV | repaired target slice |
| Chiral diagnostic `T_f = K_gauge^4 M_Pl` | 2.20039385974778e13 GeV | 2.20039385974778e13 GeV | unchanged |
| JWST z=10 time ratio | 1.478575721721601 | 1.4785718590092163 | tiny radiation-input hygiene shift |
| JADES z=14 delta | 135.78694162866518 Myr | 135.78545472450128 Myr | tiny radiation-input hygiene shift |

## Script-Level Audit

| Script | R4 status | Finding |
|---|---|---|
| `01_eta_derivation_chain.py` | impacted and repaired | Late-time eta uses `T_obs`; v1.2 uses FIRAS-fixed readout. |
| `02_temperature_assignment.py` | impacted and repaired | Conversion uses `x_R4_source^(3 R4_FIRAS K_gauge)`; local eta_BBN remains invariant. |
| `03_chiral_source_diagnostic.py` | not impacted | Uses powers of `K_gauge` and the diagnostic Planck scale, not optical R4. |
| `04_leptogenesis_target_reduction.py` | impacted and repaired | Target reductions inherit the updated late-time eta. The chiral diagnostic scale is kept separate from the eta-derived Poplawski target scale. |
| `05_baryogenesis_registry_summary.py` | not impacted | Registry counts stay 15 CLEAN and 33 CONDITIONAL_VERIFIED. |
| `06_jwst_formation_time_table.py` | minor hygiene | Radiation-density input now uses FIRAS `T_cmb = 2.7255 K`; no CMB prediction is claimed. |
| `07_desi_confrontation.py` | not impacted | DESI active-branch calculation does not use optical thermal readout. |
| `08_dark_matter_null_forecast.py` | not impacted | Uses `f_b = 2 gamma / x` and external limit checks only. |
| `09_r4_firas_impact_audit.py` | new v1.2 audit | Records the blast radius and old/new values. |
| `10_validate_expected_outputs.py` | repaired validator | Validates all v1.2 frozen outputs. |

## Kappa-Style Classification

### Optical readout normalization R4

Classification: DERIVED uniqueness theorem plus VERIFIED FIRAS empirical input, inherited from Paper 17 v1.5.

R4 is not internally derived from the unaugmented modular-projection stack. It is uniquely fixed by FIRAS within the IO optical readout family. It is not a downstream fitted parameter because it is fixed once and then frozen.

### Late-time eta

Classification: DERIVED/SCOPED arithmetic within the FIRAS-fixed observer-side thermal readout.

The free field test exposes `T_obs` as the only R4-sensitive input. After replacing the old implicit unit normalization with `R4_FIRAS`, the eta value shifts from `5.748778515173695e-10` to `5.74754373341092e-10` under the mean-baryon-mass convention.

### BBN eta temperature assignment

Classification: DERIVED/SCOPED typed-observable calculation; invariant under consistent R4 repair.

Although the observer-to-local conversion factor changes, the product reduces to the local `T_IO` photon-density calculation. The shipped validator confirms `eta_BBN = 6.150846821132321e-10` unchanged.

### Chiral source-era diagnostic

Classification: CONDITIONAL/CONSTRUCTED; not R4-sensitive.

`g_chi = K_gauge^4`, `T_f = K_gauge^4 M_Pl`, and `eta_chiral = 7.04 K_gauge^8` do not use the optical readout normalization. Their conditional status is unchanged.

### External leptogenesis target reduction

Classification: DERIVED/CONDITIONAL on the standard external hierarchical thermal-leptogenesis class.

The reduction inherits the updated `eta_late`. The v1.2 bundle separates the unchanged chiral diagnostic scale from the eta-derived Poplawski target-compatibility scale to avoid carrying a stale hard-coded v1.1 value.

### JWST, DESI, and dark-sector sections

Classification: no R4 damage to DESI or dark-sector calculations; minor JWST input hygiene.

JWST timing uses FIRAS as the standard empirical radiation-density input. DESI and dark-sector scripts do not depend on the optical CMB readout normalization.

## Manuscript-Hygiene Requirements

Paper 35 v1.2 should not say that IO predicts the observed CMB temperature. It may say that Paper 17 v1.5 fixes a unique empirical observer-side thermal readout normalization from FIRAS and that Paper 35 propagates that normalization without retuning.

The late-time eta, external leptogenesis target, and JWST timing numbers should use the v1.2 bundle values above. The baryogenesis theorem-registry counts and status labels are unchanged.

## Validation

The public bundle validator passes:

`SUMMARY total_checks=38 pass_count=38 fail_count=0`.

