# Paper 21 kappa-style structural audit

Status: verified / structural-audit / no manuscript edits

Date: 2026-05-04

Target: Paper 21 v1.6, "The AC1 Derivation, the SU(2) Geometric Weight, and the Radiation Response Problem"

## Executive conclusion

The audit does **not** find an unlabelled continuous fitted kappa parameter in the active Paper 21 v1.6 claims.

Paper 21's active load-bearing contribution is narrower than the historical radiation-response search that occupies much of Part II:

1. the AC1/acoustic phase-calibration closure for `theta_*` in the reduced scalar/longitudinal acoustic sector;
2. the one-puncture SU(2) Gibbs partition and the singleton puncture loads later used by Paper 22;
3. the optical-filtration and `T_IO` branch-assignment boundaries that prevent GTTP/observer readout factors from being misapplied to BBN;
4. a documented no-go/provenance ledger for the failed radiation-response routes.

The strongest adverse finding is **not hidden fitting**. It is scope visibility. Paper 21 v1.6 already marks the Part II radiation-response route as superseded by Paper 22 v1.5, but future public bundle material should make the distinction impossible to miss:

- `L_1` and `L_2` are derived Paper 21 puncture-load values.
- The later use of `L_1` and `L_2` as rate-dressing amplitudes is **not** derived by Paper 21 alone; it inherits Paper 22/Paper 25 conditional bridge premises.
- `F_abs = 0.36878514007842433` and the `lambda=4` bounded-Casimir near-hit are research-provenance diagnostics, not the active BBN resolution.
- The nineteen killed `P_resp` routes remain valid no-go/provenance artifacts, but they are superseded as the active D/H strategy.

Blunt classification:

```text
No hidden continuous kappa parameter found.
No active Paper 21 scorecard value is classified as FITTED.
AC1/theta_* closure is DERIVED/THEOREM only in the reduced scalar/longitudinal acoustic sector.
L_1 and L_2 are DERIVED puncture-load values; their Paper 22 rate-dressing use is inherited conditional structure.
F_abs/lambda=4 is STRUCTURALLY SUPPORTED / RECONSTRUCTION-PROVENANCE, not an active theorem.
The old radiation-response campaign is Historical/SUPERSEDED as an active BBN route but remains useful no-go evidence.
```

## Audit method

This repeats the kappa-style field-redefinition methodology used on Paper 22, Paper 32, Paper 34, and Paper 35:

1. expose every numerical or structural choice as a candidate field;
2. replace that field by a free variable or alternate admissible value;
3. ask whether current theorems, symmetries, scoped premises, or computational checks force the original value;
4. classify each field as `DERIVED`, `DERIVED/SCOPED`, `DERIVED/CONDITIONAL`, `RECONSTRUCTION`, `FITTED`, or `HIDDEN PARAMETER`.

A hidden parameter means a free degree of freedom that is not visibly declared as conditional, scoped, historical, or open. A visible scoped premise can be high-leverage without being hidden.

## Active numerical surface

The active Paper 21 v1.6 audit uses these local artifacts:

```text
Paper text: /tmp/io_full_papers_text/Interior_Observer_Paper21_v1_6.txt
Paper folder: /opt/cosmology-lab/results/paper21
AC1/theta artifacts:
  paper21_ac1_opening_investigation_results.json
  paper21_a4_bridge_theorem_results.json
  paper21_two_formalization_theorems_results.json
Puncture-load artifacts:
  paper21_sharpening_03622_results.json
  paper21_pmultlift_tensor_weight_projection_results.json
  paper21_vN+1_ypbbn_to_ypcmb_correction_results.json
BBN correction artifact:
  paper21_vN+1_ypbbn_to_ypcmb_correction_results.json
```

Core values:

```text
gamma_BI = 0.2375
x = 1.51899
K_gauge = ln(1 + gamma_BI^2) = 0.05487281774291466
sqrt(1 + gamma_BI^2) = 1.0278162530335857
J_geom = x^(-1/2) = 0.8113767196882199
J_theta = x^(-1/2) sqrt(1 + gamma_BI^2) = 0.8339461798286282
theta_* residual against strict ratio = 0.4294211437022577 percent
Z_punc = 1.4221...
L_1 = 0.22416889162576648
L_2 = 0.13805247907094412
L_1 + L_2 = 0.36222137069671057
F_abs = 0.36878514007842433
target Delta N_eff used in old radiation-response search = 0.368541479723
corrected Path C scorecard: Y_p = 0.247818144172843, D/H = 2.510410594955e-05, chi^2(D/H + Y_p) = 0.802
```

## Candidate field catalog and rigidity tests

### 1. `theta_*` observable typing

Candidate field: replace the observed acoustic angle typing by a primitive single-rung scalar, a degree-2 intensity, or a gauge-neutral geometric-only observable.

Rigidity test: Paper 20 already forces `theta_*` to be composite. Paper 21's A1-A5/B0-B6 chain further localizes the surviving gauge-sensitive stage to a primitive one-slot boundary-to-bulk phase/ruler readout, while the denominator and later collection/harmonic stages are gauge-neutral in the reduced scalar/longitudinal acoustic sector.

Numerical discriminator:

```text
J_geom only = 0.8113767196882199
J_theta degree 1 = 0.8339461798286282
J_theta degree 2 = 0.8571434377831335
strict theta_obs/theta_bare ratio = 0.8303803510281642
```

The degree-1 construction is the only one of the tested typed choices that lands near the strict acoustic ratio without importing a fitted scalar.

Classification: `DERIVED/THEOREM within reduced scalar/longitudinal acoustic sector`.

Hidden-parameter verdict: not hidden. The sector restriction is visible in v1.6 and in the A4 bridge theorem artifact.

### 2. The `x^(-1/2)` geometric factor

Candidate field: replace `x^(-1/2)` by `x^p`.

Rigidity test: Paper 20's Acoustic History Reduction fixes `J_r = x^(1/2)` and the angular readout ratio gives `J_theta,geom = x^(-1/2)`. Changing `p` breaks the inherited acoustic-history reduction rather than merely reparameterizing Paper 21.

Classification: `DERIVED`.

Hidden-parameter verdict: not hidden.

### 3. The `sqrt(1 + gamma_BI^2)` gauge factor

Candidate field: replace `sqrt(1 + gamma_BI^2)` by `1`, `1 + gamma_BI^2`, `K_gauge`, or another gauge scalar.

Rigidity test: Paper 21 uses the tangential transfer/one-form response branch inherited from the quaternionic and transfer-degree stack. Within the local bilinear acoustic carrier, the one-form response is the square-root transfer. The degree-2 response is explicitly checked and is worse for `theta_*`.

Classification: `DERIVED/THEOREM within the one-form acoustic response scope`.

Hidden-parameter verdict: not hidden.

### 4. A4 bridge theorem and no-new-slot rule

Candidate field: allow direction collection or spherical harmonic projection to introduce a new gauge-sensitive slot.

Rigidity test: `paper21_a4_bridge_theorem_results.json` records that gauge-neutral direction-resolved collection and spherical-harmonic projection preserve one-slot degree-1 typing; the quadratic self-intensity appears only at the `C_l` stage and cannot introduce a new primitive gauge leg for the peak position.

Classification: `DERIVED/THEOREM within reduced scalar/longitudinal acoustic sector`.

Hidden-parameter verdict: not hidden. The missing extension is vector/tensor/lensing/general CMB observables, not a free scalar in the published `theta_*` claim.

### 5. Puncture Gibbs spectrum

Candidate field: change the physical puncture spectrum from `j in {1/2, 1, 3/2, 2, ...}` to include `j=0` as a physical puncture level or to restrict to a hand-picked finite subset.

Rigidity test: Paper 21 Theorem 21.I treats `j=0` only as a bookkeeping central sector when comparing reduced optical algebra to puncture excitations. Physical puncture weights begin at `j=1/2`; changing that alters the ABCK/SU(2) puncture construction rather than a free fit.

Classification: `DERIVED/SCOPED`.

Hidden-parameter verdict: not hidden.

### 6. Puncture energy weight formula

Candidate field: replace

```text
chi_j (2j+1) exp(-chi_j),   chi_j = 2 pi gamma_BI sqrt(j(j+1))
```

by a plain partition fraction, a different degeneracy, or a temperature-dependent factor.

Rigidity test: Theorem 21.I distinguishes the one-puncture partition from the internal-energy comparator. For any linear radiation map built from a Gibbs expectation of the puncture Hamiltonian, the energy-weighted fraction is the correct comparator. The weights are geometric constants and do not depend on PRyMordial output or the later YPBBN/YPCMB correction.

Classification: `DERIVED/THEOREM`.

Hidden-parameter verdict: not hidden.

### 7. Singleton puncture loads `L_1` and `L_2`

Candidate field: replace `L_1` or `L_2` by arbitrary amplitudes.

Rigidity test: The correction memo verifies that `L_1` and `L_2` are energy-weighted isolated-horizon puncture spectral fractions computed from `gamma_BI` and the SU(2) puncture weights:

```text
L_1 = 0.22416889162576648
L_2 = 0.13805247907094412
```

They are independent of PRyMordial's helium output index and survive the v1.5/v1.6 wrapper correction unchanged.

Classification: standalone values `DERIVED`.

Boundary: using them as Paper 22 weak/nuclear rate-dressing amplitudes is not a Paper 21 theorem. That use inherits Paper 22 GMP/TBS and Paper 25 WMR conditionality.

Hidden-parameter verdict: not hidden in Paper 21.

### 8. The `{j=1, j=2}` near-hit subset

Candidate field: replace `{1,2}` by a different low-spin subset or continuous response weights `r_j`.

Rigidity test: The old radiation-response search found that `{1,2}` is physically motivated as first vector plus first tensor multiplets and gives:

```text
L_1 + L_2 = 0.36222137069671057
target Delta N_eff = 0.368541479723
```

However, Paper 21 also records that arbitrary low-spin subsets or response weights can move the value. The current stack does **not** prove a theorem-grade response operator `P_resp = P_1 + P_2`.

Classification: `STRUCTURALLY SUPPORTED CONSTRUCTION / RESEARCH-PROVENANCE`, not active theorem.

Hidden-parameter verdict: not hidden because v1.6 explicitly supersedes the Part II radiation-response route as the active BBN strategy.

### 9. Optical filtration theorem

Candidate field: allow reduced RT/BY optical readouts to see noncentral SU(2) puncture data.

Rigidity test: Paper 21 Theorem 21.J states that optical readout observables in the reduced RT/BY class pass through the fixed-point algebra and are blind to noncentral SU(2) data. This is why the old "BBN sees punctures while theta_* does not" split required a separate bulk thermodynamic coupling theorem; it could not be obtained by smuggling puncture weights through the optical class.

Classification: `DERIVED/SCOPED`.

Hidden-parameter verdict: not hidden.

### 10. `T_IO` versus `T_obs` BBN branch assignment

Candidate field: evaluate BBN on `T_obs = T_IO x^K_gauge` rather than local bulk `T_IO`.

Rigidity test: Theorem 21.L localizes GTTP to the RT/BY optical readout class. BBN is local bulk thermodynamics, so it uses `T_IO`. The `T_obs` run is a class-mismatched cross-check, not a competing physical branch.

Classification: `DERIVED/SCOPED` for the branch assignment; `DERIVED/CONDITIONAL` for any scorecard that additionally supplies a radiation-response value.

Hidden-parameter verdict: not hidden.

### 11. `lambda=4` bounded Casimir family

Candidate field: replace `h(C_2)=C_2/(4+C_2)` by `h_lambda(C_2)=C_2/(lambda+C_2)`.

Rigidity test: The local artifacts show that the target selects `lambda ~= 4.00508`; `lambda=4` is motivated by spacetime dimension and gives a close value, but the family itself is monotone and a continuous `lambda` can be tuned. Paper 21's `lambda=4` statement is therefore only a conditional uniqueness result **inside** the bounded resolvent family with an admitted dimension interpretation, not a theorem that Nature chooses this kernel.

Classification: `RECONSTRUCTION / CONDITIONAL FAMILY-SCOPE`.

Hidden-parameter verdict: not hidden because the route is historical/superseded as the active BBN solution and the family scope is stated in the support report.

### 12. `F_abs` as a radiation source

Candidate field: promote

```text
F_abs = Tr[rho_loc H_punc C2/(4+C2)] / Tr[rho_loc H_punc]
      = 0.36878514007842433
```

to the physical `Delta N_eff` source.

Rigidity test: `F_abs` is a reproducible scalar load and an impressive near-hit to the old target, but Paper 21 does not derive the stress/radiation map that injects this scalar into the homogeneous bare radiation slot. Exact PRyMordial tests of the old uniform-radiation route are now superseded by Paper 22 v1.5 rate dressing.

Classification: `STRUCTURALLY SUPPORTED CONSTRUCTION / RESEARCH-PROVENANCE`.

Hidden-parameter verdict: not hidden. It would become hidden only if a future manuscript presented `F_abs` as active evidence without the missing response theorem.

### 13. Nineteen `P_resp` routes

Candidate field: treat any old near-hit route as an active solution despite control failure or missing theorem map.

Rigidity test: The paper and local reports document route failures across assembly gap radiation, freeze-in, local expansion variance, local interaction dressing, nonseparable weak-sector tests, conformal-probe projection, stiff dilution, and follow-up routes. The value of these scripts is the no-go ledger, not a promoted solution.

Classification: killed routes are `DERIVED/NO-GO` or `COMPUTATIONAL NO-GO`; occasional near-hits are `RECONSTRUCTION / PROVENANCE`.

Hidden-parameter verdict: not hidden because v1.6 explicitly marks the active strategy as superseded by Paper 22 v1.5.

### 14. YPBBN -> YPCMB correction and Path C amplitude alignment

Candidate field: keep reading `PRyMresults()[4]` as observational helium or retain the old Paper 21 amplitude branch.

Rigidity test: The v1.5/v1.6 correction artifact verifies that observational compilations compare to `YPCMB` / `PRyMresults()[3]`, not `YPBBN` / `PRyMresults()[4]`. It also aligns the Paper 21 scorecard with the modern Paper 22/Paper 24 amplitude standard. The old YPBBN value is retained only as an audit field.

Classification: `VERIFIED / WRAPPER-CORRECTION / PATH C ALIGNMENT`.

Hidden-parameter verdict: not hidden.

### 15. Corrected BBN scorecard in Paper 21 v1.6

Candidate field: treat the corrected Paper 21 Path C scorecard as an independent Paper 21 BBN derivation.

Rigidity test: The corrected row is a cross-paper consistency row:

```text
Y_p = 0.247818144172843 (+0.705 sigma)
D/H = 2.510410594955e-05 (-0.553 sigma)
Li-7/H = 5.363335812719e-10 (+12.204 sigma)
chi^2(D/H + Y_p) = 0.802
```

It verifies wrapper and amplitude convention alignment. It is not the active lithium solution and not a new Paper 21 derivation of the rate-dressing amplitudes.

Classification: `VERIFIED / CROSS-PAPER CONSISTENCY`.

Hidden-parameter verdict: not hidden.

## Conditional-visibility check

Paper 21 v1.6 passes the main conditional-visibility test for the active claims:

- AC1 is scoped to the reduced scalar/longitudinal acoustic sector.
- The BBN/radiation-response Part II route is explicitly superseded by Paper 22 v1.5.
- The corrected wrapper scorecard states the YPBBN/YPCMB correction and the Path C amplitude alignment.
- `L_1` and `L_2` are verified as independent of PRyMordial wrapper output.

Recommended hygiene for a future Paper 21 v1.7 or public bundle README:

1. Add a short "active versus historical artifacts" note: AC1 and puncture loads are active; `F_abs`, `lambda=4`, and the nineteen `P_resp` probes are historical/provenance.
2. State that `L_1` and `L_2` are derived in Paper 21 but their later rate-dressing use is conditional on Paper 22/Paper 25 bridge premises.
3. Replace any "scripts available upon request / will be published" language when the public bundle is created.
4. Keep the Conventions v1 historical URL for already-published scorecard corrections, but cite Conventions v2.0 for new-publication labeling/versioning discipline.

## Cross-paper dependency check

No stale dependency was found that changes Paper 21's active mathematical claims.

Recent corrections affect Paper 21 as follows:

- Papers 19-25 YPBBN->YPCMB correction: already incorporated in Paper 21 v1.5/v1.6 scorecard. Does not affect `L_1`/`L_2`.
- Paper 22 v1.5 chi-square correction: already reflected in Paper 21 v1.6 version history.
- Paper 24 v2.3 Henderson row alignment: does not change Paper 21 AC1 or puncture-load derivations.
- Paper 34 v1.1 conditional-visibility hygiene: relevant as a style standard only.
- Conventions v2.0: should be used for future public bundle wording and any later Paper 21 revision.

## Final verdict

Paper 21 is a good reproducibility-bundle candidate if the bundle is framed correctly:

- publish AC1/theta closure scripts as active theorem-support artifacts;
- publish puncture partition/load scripts as active inputs to later papers;
- publish only `P_resp` campaign scripts that directly reproduce a Paper 21 theorem/no-go label or quoted number, and frame them as a no-go/provenance registry rather than active BBN evidence;
- include the YPBBN->YPCMB correction audit as the scorecard hygiene artifact.

No manuscript-level emergency was found. The required work is documentation and bundle discipline, not a physics correction.
