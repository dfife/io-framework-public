# Paper 22 v2.0 R4/FIRAS and Kappa-Style Structural Audit

Date: 2026-05-10  
Target manuscript: `/opt/cosmology-lab/results/Full Papers/Interior_Observer_Paper22_v2_0.docx`  
Public bundle target: `papers/paper22/v2.0/`

## Executive Verdict

No new hidden continuous fitted parameter was found in Paper 22's active v2.0 claim stack.

Paper 22's live numerical scorecard is the rate-dressing Big Bang nucleosynthesis row:

- `epsilon_w = K_gauge * L_1 = 0.012300778733811872`
- `epsilon_n = (<K>/10) * L_2 = 0.02384221534546833`
- `D/H_sigma = -0.5529801681809717`
- `Y_p_sigma = +0.7045360432106975`
- `chi2(D/H + Y_p) = 0.8021581025844415`
- `Li7/H = 5.363335812718549e-10`, `Li7_sigma = +12.204309073285641`

That scorecard does **not** use the optical readout normalization `R4`; the public v2.0 bundle records this explicitly. Paper 22's R4 damage is manuscript-hygiene damage inherited through appendix and reference material, not a live scorecard recomputation issue.

The active open fields remain visible:

- `GMP` should be labeled `OPEN/PREMISE_GAP`.
- `TBS` should be labeled `OPEN/PREMISE_GAP`.
- Theorem 22.23/22.24/22.25 should be labeled `DERIVED/CONDITIONAL_VERIFIED` only with explicit dependency on `GMP + TBS` and weak-side inheritance from `WMR(H1-H3)`.

## R4 / CMB Damage

Paper 17 v1.5 retired the independent CMB-temperature prediction. The correct active readout is:

```text
T_obs(R4) = T_IO * x^(R4 * K_gauge)
R4_FIRAS = 1.0031014644
```

with FIRAS supplying the empirical observer-side thermal datum. The older `R4 = 1` formula is not theorem-grade. The older `exp(K_gauge/2)` formula is also not the active readout and evaluates to approximately `2.7376 K`, not `2.7255 K`.

Manuscript locations in the extracted v2.0 draft that require cleanup:

- Line 538: master table lists `T_obs = T_IO × x^K_gauge` and `2.7253 K`. Replace with the FIRAS-fixed readout family or remove if not load-bearing for Paper 22.
- Lines 636-642, Step 34/35: states `T_obs = T_IO × exp(K_gauge/2) = ... = 2.7253 K`, then states five pieces forcing `T_obs = T_IO × x^K_gauge`. This is stale and should be replaced by Paper 17 v1.5 Theorem 17.2 language or removed from the appendix.
- Line 645, Step 38: `gamma_BI prediction from FIRAS inversion` should be retired or reframed. FIRAS fixes R4; it is not evidence that IO independently predicted `gamma_BI`.
- Line 646, Step 39: claims the normalization eliminates the last free parameter in the temperature formula. This is the old hidden-R4 overclaim and should be removed or rewritten as a historical failed claim outside the active appendix. The user has specified that the appendix is not a historical record, so removal is preferred.
- Lines 696-697, Steps 87-88: old `R1-R4` rigidity and `T_obs = T_IO × x^{K_gauge}` statements should be updated to the Paper 17 v1.5 FIRAS-fixed readout normalization or removed if not needed by Paper 22.
- Lines 938-944: historical/superseded Paper 21 radiation-target scorecards remain in the appendix. Under the current instruction that the appendix is not a historical record, these should be removed unless they are necessary active no-go evidence.

## Field-Redefinition Audit

| Candidate field | Rigidity test | Classification | Finding |
| --- | --- | --- | --- |
| `R4` optical readout normalization | Replace `R4` by a free real scalar in `T_obs = T_IO x^(R4 K_gauge)`. Paper 17 v1.5 fixes it uniquely from FIRAS, but the modular stack alone does not force `R4 = 1`. | `IMPORTED/EMPIRICAL` + `VERIFIED` uniqueness in Paper 17; not a Paper 22 fit. | Not active in Paper 22 scorecard; stale CMB prediction wording must be removed. |
| `K_gauge` in `epsilon_w` | Replacing with `2 gamma` or another gauge scalar breaks the Paper 25 WMR/Quadratic Thermal Covariance path. | `DERIVED/CONDITIONAL_VERIFIED` on `WMR(H1-H3) + GMP`. | Visible conditional dependency; not hidden. |
| `L_1` weak puncture load | Replacing with `sqrt(L_1)` is superseded by Paper 25's rate-vs-amplitude correction. | `DERIVED/CONDITIONAL_VERIFIED` once WMR package is accepted. | No hidden continuous parameter. |
| `<K>/10` nuclear payload | `10` is forced as the lowest TT multiplicity, but assigning the full modular budget `<K>` to that block remains TBS. | `OPEN/PREMISE_GAP` for TBS; computation inside package is `DERIVED/CONDITIONAL_VERIFIED`. | Visible open premise, not hidden. |
| `GMP` bridge mediation | Existing stack admits non-geometric bridge maps; GMP is not forced by topology alone. | `OPEN/PREMISE_GAP`. | Visible and load-bearing. |
| Branch sign/orientation | Orientation sign can be flipped, but physical suppression orientation is discrete and visibly conventional. | `VERIFIED` convention; no continuous fit. | Should remain explicit if discussed. |
| PRyMordial helium output component | `YPBBN` vs `YPCMB` was corrected in v1.4; active bundle uses `YPCMB / PRyMresults()[3]`. | `VERIFIED`. | No remaining index bug in active bundle. |

## Label Discipline Audit

Canonical public labels currently allowed:

`DERIVED/THEOREM`, `DERIVED/CONDITIONAL_VERIFIED`, `DERIVED/NO-GO`, `VERIFIED`, `IMPORTED/EMPIRICAL`, `RECONSTRUCTION`, `RECONSTRUCTION/RESEARCH_ONLY`, `OPEN/PREMISE_GAP`, `SUPERSEDED`, `Historical/SUPERSEDED`.

Noncanonical labels or wording found in the v2.0 draft:

- Line 333 and line 346: `NEW PREMISE / CONDITIONAL` for GMP. Recommended canonical label: `OPEN/PREMISE_GAP`.
- Line 348 and line 878: `PREMISE / CONDITIONAL` or `CONDITIONAL / OPEN` for TBS. Recommended canonical label: `OPEN/PREMISE_GAP`.
- Line 879: plain `STATUS: OPEN`. Recommended canonical label: `OPEN/PREMISE_GAP`.
- Version-history line 14: `CONDITIONAL/THEOREM` appears historically for WMR. Recommended active label: `DERIVED/CONDITIONAL_VERIFIED` where the H1-H3 dependency chain is shown.
- Multiple appendix entries use malformed chains such as `Premise 2..`, `Premise 2.on`, or `Premise 2.-GO`. These are editorial artifacts and should be cleaned before v2.0 publication.
- Plain `DERIVED` appears in historical text and several inline fragments. Active theorem claims should use the canonical two-part labels above.

## Abbreviation / IO-Slang Flags

The notation block helps, but the v2.0 draft still assumes substantial IO vocabulary. For a standalone reader, expand or translate these at first use in the body, not only in the notation block:

- `IO`, `GTTP`, `GMP`, `TBS`, `WMR`, `P_resp`, `F_abs`, `DeltaN_eff`, `YPCMB`, `YPBBN`, `PRyMordial`.
- `OS`, `TT`, `KMS`, `CCR`, `CAR`, `ADM`, `RT/BY`, `AQFT`, `LQG`.
- IO-specific phrases: `rate-dressing bridge`, `Channel Floor`, `spatial Hodge complex`, `puncture load`, `payload`, `singleton load`, `bridge operator`, `no-go landscape`, `route killed`, `theorem-grade`.

Recommendation: keep standard physics acronyms after expansion, but avoid IO slang in theorem statements. Prefer descriptive phrases such as "transverse-traceless tensor channel" over bare `TT` when the term first appears in a section.

## Appendix Scope

The appendix currently contains historical and superseded entries. The user instruction for the current repair pass is explicit: the appendix is **not** a historical record. Therefore:

- Remove superseded BBN scorecard steps unless they are active no-go evidence.
- Remove old CMB-temperature prediction steps rather than marking them historical.
- Keep only live theorem support, active no-go theorems, and current reproducible numerical values.
- Preserve historical provenance in the public bundle reports, not in the manuscript appendix.

## Public Bundle Changes Required

The v2.0 public bundle should add:

- `scripts/01_r4_firas_dependency_audit.py`
- `results/r4_firas_dependency_audit_results.json`
- this audit report and JSON under `reports/`
- updated `data/imported_constants.json` with `R4_FIRAS = 1.0031014644`
- validator checks confirming `R4` is recorded but not used in the active Paper 22 BBN scorecard.

## Final Recommendation

Proceed with Paper 22 v2.0 as a bundle-and-hygiene update. The active Paper 22 rate-dressing claims survive the R4/FIRAS correction. The manuscript should remove stale CMB prediction wording and migrate all noncanonical status labels to the public Claims Discipline set before publication.
