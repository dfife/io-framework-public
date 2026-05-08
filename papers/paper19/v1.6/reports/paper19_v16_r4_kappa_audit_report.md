# Paper 19 v1.6 R4/FIRAS and Kappa-Style Structural Audit

Date: May 2026

Target: Paper 19 v1.5, repaired toward Paper 19 v1.6

Scope: review Paper 19 scripts and manuscript claims for R4 damage, hidden fitted parameters, CMB-temperature overclaiming, noncanonical theorem labels, and reader-facing abbreviation/IO-slang issues. This is a structural audit and bundle-preparation report, not a manuscript edit.

## Executive Verdict

Paper 19 has real R4 damage inherited from the pre-Paper-17-v1.5 temperature-readout claim. The damage is localized but visible:

- The manuscript repeatedly says `T_obs = T_IO*x^K_gauge = 2.7253 K` or `T_CMB = 2.7253 K` as if the observed CMB temperature were independently predicted.
- Support scripts used `T0 = 2.7253` or computed `T0 = T_IO*x^K_gauge`, equivalent to implicit `R4 = 1`.
- The Open Problems list already knew the normalization was not derived: "R4 normalization ... not derived ... load-bearing for GTTP."

The v1.6 repair is the same boundary adopted in Paper 17 v1.5:

```text
T_obs(R4) = T_IO*x^(R4*K_gauge)
R4_FIRAS = 1.0031014644
T_obs(R4_FIRAS) = T_FIRAS = 2.7255 K
```

The CMB temperature is not an independent Paper 19 prediction. It is an imported empirical FIRAS datum that fixes the observer-side readout normalization once. R4 is then frozen and propagated through Paper 19 calculations without retuning.

After this repair, no hidden continuous fitted parameter was found in the Baryon Scalarization Theorem itself. However, the audit flags one separate fitted-parameter risk: the age-closed `N_mode = 0.336` background branch is observationally selected unless an upstream theorem fixes it. It must not be presented as a zero-fitted-parameter prediction in v1.6.

## Repaired Script Inventory

The following scripts were updated from implicit `R4 = 1` or hard-coded old CMB values:

| Script | Old behavior | v1.6 behavior |
| --- | --- | --- |
| `paper19_corrected_scorecard_checks.py` | `T0_IO = 2.7253` and CMB row framed as unchanged prediction | `T0_IO = 2.7255`, with explicit `IMPORTED/EMPIRICAL` FIRAS-fixed status |
| `paper19_self_consistent_background_recompute_checks.py` | `T0_OBS = T_IO*(X**K_GAUGE)` | `T0_OBS = T_FIRAS`, with `R4_FIRAS` metadata |
| `paper19_matter_classification_fork_checks.py` | `T0_OBS = T_IO*(X**K_GAUGE)` | `T0_OBS = T_FIRAS`, with `R4_FIRAS` metadata |
| `paper19_h2_global_factor_scan_checks.py` | `T0_OBS = T_IO*(X**K_GAUGE)` | `T0_OBS = T_FIRAS`, with `R4_FIRAS` metadata |
| `paper19_hamiltonian_readout_audit_checks.py` | `T0_OBS = T_IO*(X**K_GAUGE)` | `T0_OBS = T_FIRAS`, with `R4_FIRAS` metadata |
| `paper19_baryon_mapping_audit.py` | BOSS scenarios used `T0 = 2.7253` | BOSS scenarios use `T0 = T_FIRAS` |
| `paper19_schur_n_audit.py` | BOSS scenarios used `T0 = 2.7253` | BOSS scenarios use `T0 = T_FIRAS` |
| `paper19_scalarization_jacobian_checks.py` | BOSS scenarios used `T0 = 2.7253` | BOSS scenarios use `T0 = T_FIRAS` |
| `paper19_four_track_baryon_scan.py` | BOSS grid used `T0 = 2.7253` | BOSS grid uses `T0 = T_FIRAS` |
| `paper19_paper16_p6_revalidation_checks.py` | Treated `T_IO*x^K_gauge` as published GTTP temperature | Uses `x^(R4*K_gauge)` and states this is not an independent CMB prediction |
| `paper19_paper14_killshotA_revalidation_checks.py` | `T0_IO = 2.725305112137207` | `T0_IO = 2.7255` with FIRAS/R4 metadata |
| `paper19_paper11_stress_revalidation_checks.py` | `T0_IO = 2.725305112` | `T0_IO = 2.7255` with FIRAS/R4 metadata |
| `paper19_modular_scalarization_audit_checks.py` | Thermal multiplicative comparison used `x^K_gauge` | Thermal comparison uses `x^(R4*K_gauge)` |
| `paper19_a_vacuum_h2_readout_checks.py` | GTTP-like labels used `x^K_gauge` and `x^(2K_gauge)` | Labels and values use FIRAS-fixed `x^(R4*K_gauge)` forms |

The PRyMordial BBN recomputation script was not changed in its temperature conversion: it explicitly uses the interior BBN branch temperature `T_IO = 2.6635 K` for the `omega_b -> eta` conversion and `2.7255 K` only as the standard reference convention. That is not R4 damage.

## Numerical Impact

Selected repaired outputs:

| Quantity | v1.5 displayed or implicit value | v1.6 repaired value | Comment |
| --- | ---: | ---: | --- |
| Observer-side thermal datum | `2.7253 K` | `2.7255 K` | FIRAS-fixed imported datum, not prediction |
| BOSS DR12 alpha=3/2 clustering chi2 | `73.06` | `73.0336060896` | Same conclusion; update if quoting two decimals |
| Lambda-CDM BOSS reference chi2 | `70.32` | `70.3236098598` | unchanged within display precision |
| Equality redshift on Paper 18 branch | `2825` | `2823.879425` | update if table reports precise value |
| Corrected D/H | `2.523 x 10^-5` | `2.5233039701421276e-5` | BBN branch unchanged by R4 repair |
| Corrected D/H sigma | `-0.12` | `-0.1232009953` | unchanged at one decimal |
| Corrected Y_p | `0.24779` | `0.2477942382` | unchanged at shown precision |
| Corrected Y_p sigma | `+0.70` | `+0.6985595530` | unchanged at shown precision |
| chi2(D/H + Y_p) | `0.50` | `0.5031639343` | unchanged at shown precision |
| Li-7/H diagnostic | not active Paper 19 headline | `5.3315028757e-10` (`+12.1016 sigma`) | keep out of Paper 19 headline unless explicitly diagnostic |
| Age-closed background branch | `N_mode = 0.3360`, `H0 = 66.33` | `N_mode = 0.3360249444`, `H0 = 66.3339006566` | age-closed branch remains open/fitted unless theorem-fixed |

## Kappa Catalog and Classification

| Candidate field | Rigidity test | Classification |
| --- | --- | --- |
| `R4` optical readout normalization | Not forced by Paper 19. Inherited from Paper 17 v1.5 where FIRAS uniquely fixes it inside the readout family. | `IMPORTED/EMPIRICAL` plus `DERIVED/CONDITIONAL_VERIFIED` uniqueness theorem upstream |
| CMB temperature row | Same datum fixes R4, so it cannot also be counted as a prediction. | Retire prediction wording |
| `gamma_BI = 0.2375` | Imported Barbero-Immirzi value used across the framework, not varied in Paper 19. | Imported framework constant |
| `x = r_s/R_U` | Inherited Schwarzschild-interior geometry branch. | Upstream derived/geometric input |
| `alpha = 3/2` clustering assignment | Derived from timelike dust-current scalarization within the proper-time comoving-dust metric-measure extension; not selected by best BOSS fit. BOSS alone does not choose it. | `DERIVED/CONDITIONAL_VERIFIED` if the extension chain is made explicit |
| `omega_b = 0.017053...` | Algebraically follows from `omega_b(alpha=1)*x^(-1/2)` once alpha=3/2 is fixed. | `DERIVED/CONDITIONAL_VERIFIED` with same dependency as alpha |
| BOSS nuisance coefficients | Linear nuisance marginalization is fitted to the BOSS data, but these are test nuisance coefficients, not framework constants. Must be visible. | Diagnostic fitted nuisances, not hidden framework parameters |
| `A_s`, `n_s`, `tau_reio` in BOSS/CAMB checks | Borrowed standard comparison inputs for the matter-power audit. | `IMPORTED/EMPIRICAL` / diagnostic inputs |
| `N_eff = Delta` physical identification | Paper 19 shows the identification is not supported as Friedmann radiation. | `SUPERSEDED` / `DERIVED/NO-GO` for physical identification |
| Schur `N_mode` | `N_mode = 0.336` is chosen to close age unless a later theorem fixes it. | `OPEN/PREMISE_GAP` if presented as live framework branch |
| `sqrt(Delta)` local-energy recertification | Valid only after class membership is certified; not a universal projector. | `DERIVED/CONDITIONAL_VERIFIED` where class chain is explicit |
| Full homogeneous Friedmann readout | Built from RT/Brown-York/isolated-horizon/Paper 16 premise package; v1.5 labels do not match current taxonomy. | `DERIVED/CONDITIONAL_VERIFIED` or `OPEN/PREMISE_GAP` depending on whether v1.6 states the premise chain |

## Hidden Fitted-Parameter Finding

The Baryon Scalarization Theorem does not hide a fitted parameter after the R4 repair. The audit specifically checked whether `alpha = 3/2` was chosen because it best fits BOSS. It was not: the BOSS grid shows degeneracy, and the paper's derivation path fixes `alpha = 3/2` from the timelike dust-current scalarization route.

The age-closed background branch is different. If v1.6 presents `N_mode = 0.336` as an active prediction, that is a hidden empirical selector. The safe label is `OPEN/PREMISE_GAP` or explicitly `IMPORTED/EMPIRICAL age-closed diagnostic branch`. It cannot support a zero-fitted-parameter claim until an upstream theorem fixes `N_mode`.

## CMB Prediction Removal

The following Paper 19 v1.5 locations must be edited in v1.6:

- Version/history and scorecard prose that says `T_CMB = 2.7253 K` is unchanged as a prediction.
- Section 15.2 photon radiation line: replace `T_obs = T_IO*x^(K_gauge)` with the Paper 17 v1.5 family `T_obs(R4)=T_IO*x^(R4*K_gauge)`, FIRAS-fixed.
- Section 15.3 typed skeleton: same replacement for the photon/radiation projector wording.
- Open Problem 1: replace "R4 pending" with "R4 fixed by Paper 17 v1.5 FIRAS uniqueness theorem; inherited as imported empirical readout normalization."
- Master Mathematical Reference Step 35/36/82/96 and summary rows: remove "forces T_obs = 2.7253 K" and state Planck/KMS form with FIRAS-fixed observer-side datum.
- Appendix A.6 universal transport no-go: keep the no-go, but reframe it as rejection of alternative readout classes against the FIRAS-fixed datum, not as protection of an independent CMB prediction.

Safe replacement sentence:

```text
Paper 19 inherits the Paper 17 v1.5 FIRAS-fixed observer readout theorem:
within the readout family T_obs(R4)=T_IO*x^(R4*K_gauge), FIRAS fixes the
unique normalization R4_FIRAS=1.0031014644. The observed CMB temperature is
therefore an imported empirical thermal datum, not an independent Paper 19
prediction.
```

## Noncanonical Status Labels Found

Paper 19 v1.5 predates the current claim-discipline taxonomy. The following labels need migration in v1.6:

| v1.5 label/text | Recommended v1.6 label |
| --- | --- |
| `DERIVED/THEOREM, conditional on ...` | `DERIVED/CONDITIONAL_VERIFIED` if the chain to Premise 1, Premise 2, or imported physics is stated |
| `DERIVED/CONDITIONAL` | `DERIVED/CONDITIONAL_VERIFIED` or `OPEN/PREMISE_GAP`; do not leave bare conditional |
| `CONDITIONALLY RE-CERTIFIED` | `DERIVED/CONDITIONAL_VERIFIED` if class-membership chain is explicit |
| `CONDITIONAL` / `CONDITIONAL/THEOREM` | `DERIVED/CONDITIONAL_VERIFIED` only if the premise chain is explicit; otherwise `OPEN/PREMISE_GAP` |
| `DERIVED/PARTIAL` | `VERIFIED` for the reduced local result plus `OPEN/PREMISE_GAP` for the missing global theorem |
| `OBSERVATIONALLY KILLED` | `DERIVED/NO-GO` with imported empirical constraint named |
| `OBSERVATIONALLY SELECTED` | `OPEN/PREMISE_GAP` or `IMPORTED/EMPIRICAL diagnostic branch`; not a theorem label |
| `DERIVED/STRUCTURAL PREDICTION` | `DERIVED/CONDITIONAL_VERIFIED` for the structural split; `CONDITIONAL FORECAST` wording only in prose |
| `CLOSED at reduced-core scope` | `VERIFIED` / `DERIVED/CONDITIONAL_VERIFIED` at reduced-core scope, with full unreduced scope marked `OPEN/PREMISE_GAP` |
| `TRANSFORMED, NOT CLOSED` | `OPEN/PREMISE_GAP` |

## Abbreviation, Nonstandard-Term, and IO-Slang Flags

Paper 19 is not self-contained for a reader who has not read the prior papers. v1.6 should expand or replace:

- `IO`: expand as "Interior Observer" at first use, then use sparingly.
- `CMP`: expand as "Conformal Modular Principle" and state whether it is active, superseded, or local-class only.
- `BDP`: expand as "Baryon Dictionary Principle."
- `GTTP`: replace with "gauge thermal transfer/readout theorem" or expand every time in theorem-facing prose.
- `N_eff`, `P(k)`, `BAO`, `BOSS`, `BBN`, `CMB`, `CLASS`, `CAMB`, `FIRAS`: standard physics acronyms, but expand on first use.
- `Schur N-slot`: use "Schur-complement curvature mode parameter" or define once.
- `slot`, `rung`, `branch`, `scorecard`, `fossil`, `kill shot`, `dead path`: avoid in the main paper body or define as audit terminology.
- `H_IO`, `M_red`, `Z_g`, `K_hat_g`, `A-vacuum`: define before use or move to appendix notation ledger.
- `Open/Closed tracking`, `foundation punch list`, `typed skeleton`: rephrase in standard physics terminology.

## Final Recommendation

Proceed with Paper 19 v1.6 as an R4/FIRAS hygiene, label-migration, and reproducibility update.

Keep:

- Baryon Scalarization Theorem, with `alpha = 3/2` labeled `DERIVED/CONDITIONAL_VERIFIED`.
- BOSS DR12 full-shape result, updated to `chi2 = 73.0336` if quoted precisely.
- Universal projector no-go.
- Paper 19 BBN wrapper-corrected scorecard values.

Change:

- Remove independent CMB-temperature prediction language.
- Replace all `T_obs = T_IO*x^K_gauge` observer-temperature claims with FIRAS-fixed readout-family language.
- Migrate labels to the canonical claim-discipline taxonomy.
- Flag the `N_mode = 0.336` age-closed background branch as an open premise gap unless a later paper's theorem is explicitly cited as closing it.
