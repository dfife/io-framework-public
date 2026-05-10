# Paper 22 v1.5/v1.6 kappa-style structural audit

Status: verified / structural-audit / no manuscript edits

Date: 2026-05-04

Target: Paper 22, "The Spatial Hodge Complex and the Rate-Dressing Bridge"

## Executive verdict

No unlabelled continuous fitted kappa parameter was found in the active Paper 22 claim stack.

The adverse result is scope visibility, not hidden fitting. Paper 22 contains a large derived mathematical infrastructure stack, but the rate-dressing bridge remains conditional in exactly the places v1.5 says it is conditional:

- GMP is a `NEW PREMISE / CONDITIONAL`, not a theorem.
- TBS is a `PREMISE / CONDITIONAL`; the TT carrier and multiplicity are derived, but the assignment of the full modular budget `<K>` to the lowest TT block is not forced by the current stack.
- WMR is resolved only relative to the Paper 25 `H1-H3` premise package. The weak payload `K_gauge` is not an unconditional consequence of Paper 22 alone.
- The suppressive orientation of the rate-dressing operator is a discrete convention that should remain visible; it is not a continuous fitted scalar.

Correct current status:

```text
Paper 22 derives the spatial Hodge/TT/channel infrastructure and a no-go
landscape that kills energy-density injection routes. The zero-parameter
amplitude construction and formal bridge operator are DERIVED/CONDITIONAL
within the stated bridge-premise package. No observation-fitted scalar was
found.
```

## Audit method

This repeats the kappa-style field-redefinition method used for Papers 22.23, 24, 32, 34, and 35:

1. expose each numerical or structural choice as a candidate field;
2. replace it by a free variable or alternate admissible value;
3. ask whether existing theorems, symmetries, or scoped premise packages force the original value;
4. classify the field as `DERIVED`, `DERIVED/SCOPED`, `DERIVED/CONDITIONAL`, `RECONSTRUCTION`, `FITTED`, or `HIDDEN PARAMETER`.

A hidden parameter is a free degree of freedom that is not visibly declared as conditional, open, scoped, or reconstructed. A visible premise can be high leverage without being hidden.

## Catalog and rigidity tests

### A. Spatial Hilbert module and Hodge spectrum

Candidate fields:

- the use of round `S^3` spatial slices;
- the de Rham complex `Omega^0 -> Omega^1 -> Omega^2 -> Omega^3`;
- the Hodge eigenvalue/multiplicity tables;
- the projectors onto exact/coexact branches;
- the extension `H_IO^(spatial) = H_IO tensor H_spatial`.

Rigidity result: forced by the OS interior round `k=+1` slice once the IO geometry is accepted. The Hodge spectra and multiplicities are standard harmonic analysis on round `S^3`.

Classification: `DERIVED/THEOREM` within the IO OS spatial-slice scope.

Hidden-parameter verdict: none.

### B. Peter-Weyl bridge and diagonal SU(2) restriction

Candidate fields:

- the identification `S^3 ~= SU(2)`;
- scalar branch `(n/2,n/2)`;
- coexact vector branch `((n+1)/2,(n-1)/2)` plus parity conjugate;
- diagonal SU(2) restriction and the absence of `J=0` in the coexact vector branch.

Rigidity result: forced by Peter-Weyl decomposition and Clebsch-Gordan restriction. There is no continuous coefficient to tune.

Classification: `DERIVED`.

Hidden-parameter verdict: none.

### C. TT branch and Channel Floor Theorem

Candidate fields:

- TT branch representation `((n+2)/2,(n-2)/2)` plus parity conjugate;
- lowest TT multiplicity `mult_TT(n=2)=2(n-1)(n+3)=10`;
- rough and Lichnerowicz eigenvalues;
- channel floor `J_min=s`.

Rigidity result: representation-theoretic on the principal transverse branch. The audit preserves the manuscript caveat: derivative descendants from lower-spin branches do not obey the same floor.

Classification: `DERIVED/THEOREM` with principal-branch hypothesis.

Hidden-parameter verdict: none.

### D. Homogeneous gauge placement

Candidate fields:

- the standard homogeneous left-invariant gauge;
- placement of `A=Gamma+gamma K` in the lowest coexact 1-form channel;
- exact pieces under gauge transformations.

Rigidity result: in the chosen homogeneous gauge, the invariant coframe is coclosed and has `Delta_1 e^i = 4/a^2 e^i`, so the background connection sits in the lowest coexact/vector channel. Under general gauge transformations exact artifacts can appear.

Classification: `DERIVED` as a gauge-fixed statement.

Hidden-parameter verdict: none, but the gauge caveat must remain visible.

### E. Candidate `R_spatial` response architecture

Candidate fields:

- joint spectral dependence on spatial channel and puncture spin;
- nonseparability;
- channel-dependent `s <= J` selection;
- physical delivery kernels.

Rigidity result: the channel architecture is forced by the Hodge/TT/Peter-Weyl/channel-floor stack. The physical delivery kernels are not derived by Paper 22.

Classification: channel architecture `DERIVED`; physical response operator `RECONSTRUCTION / CONDITIONAL`.

Hidden-parameter verdict: no hidden scalar, because the manuscript explicitly says it does not derive full `P_resp`.

### F. Energy decay and injection no-go landscape

Candidate fields:

- vector `a^-4` scaling;
- scalar/TT oscillatory versus frozen regimes;
- stress scalarization `V_J tensor V_J contains V_0`;
- boundary permanence;
- positive-power connection gates;
- injection-only and uniform-radiation routes.

Rigidity result: the vector Maxwell result is conformal-invariance forced. Stress scalarization is representation-theoretic. The injection no-gos follow once a route promotes `F_abs` into a homogeneous background scalar or radiation energy-density slot.

Classification: `DERIVED` / `DERIVED/NO-GO`, with scalar/TT dynamics scoped to the stated realization.

Hidden-parameter verdict: none. The audit also confirms the active claim boundary: `F_abs` is not an active expansion-rate energy-density correction.

### G. BBN response and rate-dressing paradigm

Candidate fields:

- full-radiation multiplier versus rate dressing;
- compact BBN-window theta-suppression;
- one-window obstruction;
- weak and nuclear lever directions;
- broad nuclear-network suppression versus branch-resolved later work.

Rigidity result: the public arithmetic verifies the no-go/response ledger values, but the exact physical delivery kernel remains outside Paper 22. The two-window and full-nuclear near-closure rows are not theorem-grade proof of the bridge; they are diagnostic support for the rate-dressing paradigm.

Classification: no-go and response matrix `DERIVED/VERIFIED`; near-closure rows `VERIFIED / diagnostic`; bridge interpretation `CONDITIONAL`.

Hidden-parameter verdict: no hidden fitted scalar in the active theorem statements. Do not promote diagnostic grid amplitudes to derived constants.

### H. Theorem 22.23 amplitude construction

Candidate fields:

- `L_1`, `L_2`;
- `K_gauge`;
- `<K>/10`;
- denominator `10`;
- weak and nuclear coupling order;
- sign/orientation convention;
- `j=1` versus `j=2` assignment;
- multiplicative separability.

Rigidity result: see the dedicated audit `paper22_theorem_22_23_kappa_audit_report.md`.

Summary classification:

- `L_1`, `L_2`, `K_gauge`, `<K>`, and `mult_TT(n=2)=10` are established constants in their source scopes.
- `K_gauge * L_1` is `DERIVED/CONDITIONAL` only after accepting WMR(H1-H3) plus GMP-mediated carrier assignment.
- `(<K>/10) * L_2` remains `RECONSTRUCTION / PREMISE-CONDITIONAL` under TBS.
- The suppressive signs are discrete orientation conventions, not continuous fits.

Hidden-parameter verdict: no unlabelled continuous hidden parameter.

### I. Theorem 22.24 Li-7 internal consistency

Candidate fields:

- the zero-parameter row used for Li-7;
- the uniform-`DeltaN_eff=F_abs` benchmark;
- the fractional consistency measure;
- the observational Li-7 sigma.

Rigidity result: the corrected v1.4/v1.5 row gives `Li7/H = 5.363e-10`, `+12.20 sigma`, and `0.51%` fractional consistency with the uniform benchmark. This is a reproducible out-of-sample consistency check, not a lithium solution.

Classification: `DERIVED/CONDITIONAL on GMP + TBS`, inherited from Theorem 22.23.

Hidden-parameter verdict: none.

### J. Theorem 22.25 formal bridge operator

Candidate fields:

- GMP carrier mediation;
- WMR weak payload;
- TBS TT modular budget;
- TT1 parity/isotropy;
- sector split between weak and nuclear terms;
- operator sign and block structure.

Rigidity result: TT1 is derived through the heat-kernel spatial KMS construction. WMR is resolved conditionally on `H1-H3`. GMP and TBS remain open. The operator block structure follows once the premise package is accepted.

Classification: `DERIVED/CONDITIONAL on GMP + TBS`, with WMR(H1-H3) inherited and TT1 derived.

Hidden-parameter verdict: no hidden continuous fitted parameter because the open premises are visible.

## Hidden-parameter ranking

No hidden continuous fitted parameter was found. The high-leverage open fields are:

| Rank | Field | Classification | Visibility | Promotion path |
|---:|---|---|---|---|
| 1 | TBS / TT modular budget `<K>/10` | `PREMISE / CONDITIONAL` | visible in v1.5 | modular intertwining theorem, modular Gauss law, or modular-energy transport theorem |
| 2 | GMP bridge mediation | `NEW PREMISE / CONDITIONAL` | visible in v1.5 | equivariant bridge uniqueness theorem |
| 3 | WMR weak payload `K_gauge` | `DERIVED/CONDITIONAL on H1-H3` | visible, but short theorem labels should inherit it explicitly | physical selection theorem for the Paper 25 two-time KMS/CCR bridge observable |
| 4 | suppressive orientation signs | discrete convention | partly implicit | positivity/suppression orientation theorem |

## Conditional-visibility findings

Paper 22 v1.5 mostly satisfies IO Conventions v2.0. It correctly marks GMP and TBS as conditional/open and corrects the older v1.3/v1.4 status drift.

Remaining hygiene recommendation for v1.6 manuscript wording:

```text
Theorem 22.23 should be cited as DERIVED/CONDITIONAL on GMP + TBS,
with weak payload closure inherited from WMR(H1-H3).
```

This avoids flattening Paper 25's conditional weak-sector support into an unconditional Paper 22 result.

## Bundle scope recommendation

Public bundle scripts should reproduce:

- Hodge and TT channel formulae;
- channel-floor and gauge-placement checks;
- live no-go/response ledger values;
- corrected YPCMB scorecard arithmetic;
- Theorem 22.23/22.24 amplitude/comparator arithmetic;
- the audit summary.

Public bundle scripts should not rerun every private dead-route scan. Those route scans are provenance and no-go support, not active theorem evidence. They remain documented in the private results and audit reports.

## Final claim boundary

Safe to say:

- Paper 22 derives the scalar/vector/tensor spatial channel infrastructure.
- Paper 22 derives no-go results that kill `F_abs` as a homogeneous energy-density/radiation correction.
- Paper 22 constructs a zero-fitted-parameter rate-dressing amplitude package.
- The active corrected scorecard is `D/H_sigma=-0.55`, `Y_p_sigma=+0.70`, `chi2(D/H+Y_p)=0.80`, and `Li7/H=5.363e-10 (+12.20 sigma)`.
- No unlabelled continuous fitted kappa parameter was found.

Not safe to say:

- Paper 22 unconditionally derives `P_resp`.
- Paper 22 unconditionally derives TBS or GMP.
- The BBN scorecard proves TBS.
- The old v1.3 YPBBN row is active.
- `F_abs` is an active Friedmann/radiation-density correction.

## Source artifacts reviewed

- `results/paper22/Interior_Observer_Paper22_v1_5_extracted.txt`
- `results/paper22/paper22_spatial_hodge_complex_results.json`
- `results/paper22/paper22_channel_decay_profiles_results.json`
- `results/paper22/paper22_shutoff_problem_results.json`
- `results/paper22/paper22_algebraic_dressing_hypothesis_results.json`
- `results/paper22/paper22_yp_wall_response_matrix_results.json`
- `results/paper22/paper22_channel_interaction_coupling_round10_results.json`
- `results/paper22/paper22_vertex_operator_round12_results.json`
- `results/paper22/paper22_constructions_round20_results.json`
- `results/paper22/paper22_hostile_review_tests_round26_results.json`
- `results/paper22/paper22_v14_ypbbn_to_ypcmb_correction_results.json`
- `results/paper22/paper22_theorem_22_23_kappa_audit_report.md`
