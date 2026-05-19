# Paper 30 v2.0 K-Style Audit and R4/FIRAS Impact Report

Date: 2026-05-19

## Scope

Reviewed the Paper 30 v2.0 working draft in `results/Full Papers/Interior_Observer_Paper30_v2_0.docx`, the active extracted text, the Paper 30 private script/result inventory, and the public bundle candidate at `tmp/io-framework-public/papers/paper30/v2.0`.

The public bundle is intentionally restricted to the active recomputation path. Historical `paper30_funrun_*` artifacts remain in `data/legacy_context/` only where the active recomputation script needs frozen comparison values; they are not live theorem support.

## R4/FIRAS Damage Review

Result: no active Paper 30 computation uses `R4 = 1` or treats R4 as a tunable parameter.

The active recomputation script records `R4_FIRAS = 1.0031014644` as a dependency boundary and uses `T_CMB = 2.7253 K` as the FIRAS-fixed observer thermal datum. The value enters radiation-density and temperature-propagation calculations as an empirical thermal input, not as an independent CMB-temperature prediction.

Manuscript wording still needing cleanup:

- `P0062`: "The framework prediction is T(z) = 2.7253(1+z) K" should be reworded as FIRAS-normalized thermal propagation, not an independent CMB-temperature prediction.
- `P0063`: "framework prediction T = 20.00 K" for HFLS3 should likewise be phrased as a FIRAS-normalized propagation value.
- `P0066`: Figure caption should not call the black line a standalone framework prediction without the FIRAS-normalization qualifier.
- `P0146` / `T13R008`: `T_CMB(z)` row is acceptable as a tied propagation check if explicitly marked as FIRAS-normalized.
- `P0169`: "cosmic microwave background temperature at all epochs" should be narrowed to "FIRAS-normalized CMB temperature scaling at high redshift."
- `P0200`: `T(z) = T_IO(1+z)` is stale if read as the observed CMB-temperature chain; use Paper 17 v1.5's FIRAS-fixed readout boundary.
- `P0229`: "Match: -0.3σ" still reads like the retired independent CMB-temperature prediction. The master table row `T14R033` is better: "Observer CMB temperature (FIRAS-fixed readout)."

## Fitted-Parameter Audit

No hidden fitted framework parameter was found in the active bundle.

Disclosed nuisance or diagnostic fits:

- Pantheon+ nuisance magnitude `M`: fitted in `fit_pantheon_with_nuisance`; standard supernova nuisance parameter, disclosed in §10.5.
- `T_CMB(z)` deformation `beta`: diagnostic one-parameter deformation test, not used in the framework prediction.
- Compact-radio-source ruler length `l_m`: diagnostic/literature nuisance fit; not in the active public recomputation script.
- FRB diagnostic baryon scan: reports the best-fit `omega_b = 0.02305` for transparency, but the claim compares pre-specified framework baryon slots.
- `LambdaCDM free-fit Omega_m`: comparator only; not an Interior Observer parameter.

Potential fitted-parameter language risk:

- `P0020`, `P0135`, `P0167`, and similar "zero fitted framework parameters" statements are defensible only with the §10.5 nuisance-fit disclosure retained nearby.
- `P0149` states LambdaCDM can free-fit BAO `Omega_m`; this is correctly labeled as comparator context.

## Label-Discipline Audit

The active bundle generated output now uses canonical labels for its baryon-slot claims:

- `omega_b_geom`: `DERIVED/CONDITIONAL_VERIFIED`
- `omega_b_eff`: `DERIVED/CONDITIONAL_VERIFIED`
- `omega_b_clustering`: `DERIVED/CONDITIONAL_VERIFIED`
- `omega_b_naive_bdp`: `DERIVED/NO-GO diagnostic`

Manuscript noncanonical or weak labels still present:

- Several appendix entries use bare `STATUS: DERIVED` without `/THEOREM`, `/CONDITIONAL_VERIFIED`, or `/NO-GO`. These should be canonicalized if they remain load-bearing.
- `P0272` and `P0290` say `STATUS: DERIVED/THEOREM (conditional on ...)`; under current discipline this should usually be `DERIVED/CONDITIONAL_VERIFIED` unless the named conditions have fully closed.
- `P0476` Step 333 reports `STATUS: DERIVED` while explicitly conditional on `C1 + C2c`; this should be `DERIVED/CONDITIONAL_VERIFIED downstream of C1 + C2c`, with `C1` and `C2c` kept as `OPEN/PREMISE_GAP`.
- `P0479`, `P0480`, `P0486`, `P0487`, `P0488`, `P0491`, and `P0494` use bare `DERIVED`; recommend canonical upgrade/downgrade by source-paper status.
- `P0481` Step 352 says `STATUS: DERIVED` for an inventory containing conditional inputs; recommend `RECONSTRUCTION` or `DERIVED/CONDITIONAL_VERIFIED` only if the chain is explicit.

## Abbreviations and IO Slang

The v2.0 draft has already expanded most body abbreviations. Remaining abbreviations that may still need first-use confirmation or simplification:

- `GCcomb`, `pte`, `UVB`, `DM_cosmic`, `τ_eff`, `HII`, `ELT`, `ANDES`, `D_M`, `D_Δt`, `F_AP`, `A_eff`, `CCR`, `KMS`, `DtN`, `PG`, `TT`.
- Appendix terms still read as IO/internal slang for a cold reader: `alpha-ladder`, `bare`, `slot`, `Schur`, `readout`, `legacy branch`, `rung`, `bridge`, `payload`, `source-side`, `observer-frame`.

Recommendation: keep standard physics abbreviations after first definition; replace or define IO slang in-line when it appears in the body or in load-bearing appendix entries.

## Script Inventory Decision

Included as active bundle script:

- `scripts/01_full_twenty_test_recompute.py`: reproduces the active Paper 30 v2.0 numerical confrontation and headline branch constants.
- `scripts/02_validate_expected_outputs.py`: reruns the recomputation and checks the frozen output.

Excluded from live script set:

- `paper30_funrun_*` scripts with retired Schur-branch constants (`H0=68.91`, `Omega_k=-0.006`) are not valid v2.0 active-branch support scripts.
- Exploratory figure/proxy scripts for NANOGrav, 21 cm, old stellar-age tension, and old Schur branch tests are historical context, not live Paper 30 v2.0 claim support.

## Validation

Public bundle validator: `python3 scripts/02_validate_expected_outputs.py`

State: PASS, 18 checks.

