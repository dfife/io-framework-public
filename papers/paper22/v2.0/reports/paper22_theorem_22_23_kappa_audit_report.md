# Paper 22 Theorem 22.23 kappa-style structural audit

Status: verified / structural-audit / no manuscript edits

Date: 2026-05-03

Target: Paper 22 v1.5 Theorem 22.23, "Zero-Parameter Amplitude Construction"

## Executive conclusion

The audit does **not** find a new unlabelled continuous hidden parameter in Paper 22 v1.5. It does find two load-bearing free coefficient fields under the current theorem stack, but both are already visible as conditional/open structure in v1.5:

1. the weak payload selector, `K_gauge` rather than `V' = 2 gamma`, closed only conditional on the Paper 25 Quadratic Thermal Covariance/WMR premise package `H1-H3`;
2. the TT/nuclear budget scalar, currently set to `<K>/10`, still open as TBS.

The strongest manuscript-level issue is not a hidden parameter in the numerical formula. It is conditional-label inheritance: Theorem 22.23 is locally labeled `DERIVED/CONDITIONAL on GMP + TBS`, while its weak-side closure still inherits `WMR(H1-H3)`. Paper 22 v1.5 does state WMR's `H1-H3` conditionality in Section 17.2, Section 17.3, and Step 251, but the theorem's short status line should be treated as shorthand, not a complete dependency list.

Blunt classification:

- `L_1`, `L_2`, `K_gauge` as standalone constants, `<K>` as a standalone constant, and `mult_TT(n=2)=10` are derived or previously established within their stated source scopes.
- The **combinations** `K_gauge * L_1` and `(<K>/10) * L_2` are not theorem-grade unconditional derivations.
- `K_gauge * L_1` is `DERIVED/CONDITIONAL` only after accepting WMR's `H1-H3` premise package plus GMP carrier mediation.
- `(<K>/10) * L_2` is `RECONSTRUCTION / PREMISE-CONDITIONAL` because TBS remains open; the current stack proves TT localization and multiplicity, not full modular-budget saturation.
- No observation-fitted scalar was found in the Theorem 22.23 formula.

## Audit method

This repeats the kappa-style field-redefinition logic used in the Paper 24 Step D audit:

1. expose every numerical or structural choice as a candidate field;
2. replace that field by a free variable or alternate admissible value;
3. ask whether existing theorems, symmetries, or invariances force the original value;
4. classify the field as `DERIVED`, `RECONSTRUCTION`, `FITTED`, or `HIDDEN PARAMETER`.

A field is a hidden parameter only if it is free under the current theorem stack **and** not visibly declared as conditional/open in the paper. A visible premise can still be load-bearing and numerically high leverage, but it is not hidden.

## Formula under audit

Paper 22 v1.5 states:

```text
epsilon_w = K_gauge * L_1
          = 0.054873 * 0.22417
          = 0.012301

epsilon_n = (<K> / mult_TT(n=2)) * L_2
          = (1.72704 / 10) * 0.13805
          = 0.023842
```

Exact numerical audit values used here:

```text
gamma = 0.2375
K_gauge = ln(1 + gamma^2) = 0.05487281774291466
V' = 2 gamma = 0.475
L_1 = 0.22416889162576648
L_2 = 0.13805247907094412
<K> = 1.72704
mult_TT(n=2) = 10
epsilon_w = 0.012300778733811872
epsilon_n = 0.02384221534546833
```

## Candidate field catalog and rigidity tests

### 1. `L_1` value

Candidate field: replace `L_1` by `lambda_1`.

Rigidity test: Paper 21 derives the singleton puncture load `L_1` for the `j=1` channel. Changing it would change the already-derived Paper 21 load, not merely reparameterize Paper 22.

Classification: `DERIVED`.

Boundary: the value is derived; its use in the weak-rate bridge remains conditional on the bridge-map premises.

### 2. `L_2` value

Candidate field: replace `L_2` by `lambda_2`.

Rigidity test: Paper 21 derives the singleton puncture load `L_2` for the `j=2` channel. Changing it would break the inherited Paper 21 load construction.

Classification: `DERIVED`.

Boundary: the value is derived; its use as the nuclear rate-dressing load is conditional on the TT bridge localization and TBS.

### 3. Weak payload scalar `K_gauge`

Candidate field: replace `K_gauge` by a weak payload scalar `a_w`.

Field-redefinition test:

```text
epsilon_w(a_w) = a_w * L_1
```

The local Dirac first-variation route does not force `a_w = K_gauge`; it lands on `V' = 2 gamma`. Numerically:

```text
K_gauge * L_1 = 0.012300778733811872
(2 gamma) * L_1 = 0.10648022352223907
(2 gamma) / K_gauge = 8.656380691537084
```

So the choice of payload has high numerical leverage and is not forced by the local first-variation stack.

What closes it: Paper 25's Quadratic Thermal Covariance/WMR route excludes the local `V'` response only conditional on `H1-H3`: the explicit spatial KMS extension is the physical bridge state, the minimal spatial CCR lift is the physical perturbation sector, and the physical weak rate is a two-point function.

Classification: `DERIVED/CONDITIONAL` if `WMR(H1-H3)` is accepted; otherwise `RECONSTRUCTION`.

Hidden-parameter verdict: not hidden in Paper 22 v1.5, because WMR is explicitly marked `DERIVED/CONDITIONAL on H1-H3` in Section 17.2/17.3 and Step 251. The theorem's short label should be expanded or footnoted to make that inheritance impossible to miss.

### 4. Nuclear payload scalar `<K>/10`

Candidate field: replace `<K>/10` by a nuclear payload scalar `a_n`.

Field-redefinition test:

```text
epsilon_n(a_n) = a_n * L_2
```

The current stack derives:

- the total modular energy `<K> = ln Delta`;
- the lowest TT eigenspace localization;
- the lowest TT multiplicity `mult_TT(n=2)=10`;
- scalarity/equipartition **inside** the lowest TT block once a budget is assigned.

It does not force the active TT block to receive the full modular budget `<K>`. Prior Round 23 work exhibited budget-rescaling families compatible with the existing symmetry/KMS/localization data. Therefore the scalar `a_n` remains free until a modular-energy transport theorem, modular Gauss law, or equivalent TBS closure is proven.

Classification: `RECONSTRUCTION / PREMISE-CONDITIONAL`.

Hidden-parameter verdict: not hidden in Paper 22 v1.5, because TBS is explicitly marked `PREMISE / CONDITIONAL` and Step 252 states the underdetermination result.

### 5. Denominator `10`

Candidate field: replace the denominator by `m`.

Rigidity test:

```text
epsilon_n(m) = (<K> / m) * L_2
```

The number `10` is derived as `mult_TT(n=2)=2(n-1)(n+3)|_{n=2}`. However, using it as the divisor of the full modular budget requires the TBS statement that the active unconstrained TT response saturates `<K>` on that lowest 10-dimensional TT block.

Numerical sensitivity:

```text
m = 9  -> epsilon_n = 0.026491350383853703
m = 10 -> epsilon_n = 0.02384221534546833
m = 11 -> epsilon_n = 0.021674741223153028
```

Classification: multiplicity `10` is `DERIVED`; "divide `<K>` by 10 as the active nuclear payload" is `RECONSTRUCTION / PREMISE-CONDITIONAL` under TBS.

Hidden-parameter verdict: not hidden, because the budget-saturation dependency is visible as TBS.

### 6. Weak coupling order: `L_1` rather than `sqrt(L_1)`

Candidate field: replace weak load order by `L_1^p`.

Field-redefinition test:

```text
epsilon_w(p) = K_gauge * L_1^p
```

The old Paper 22 branch used `sqrt(L_1)`. Paper 22 v1.1/Paper 25 corrected the weak-rate dressing to the modern quadratic thermal covariance branch, so the current Theorem 22.23 uses `L_1`. Numerically:

```text
K_gauge * sqrt(L_1) = 0.025980346217022963
K_gauge * L_1       = 0.012300778733811872
```

Classification: `DERIVED/CONDITIONAL` under the Paper 25 Quadratic Thermal Covariance theorem and its `H1-H3` premise package.

Hidden-parameter verdict: not hidden in v1.5, but the dependency must be inherited when Theorem 22.23 is cited.

### 7. Nuclear coupling order: `L_2`

Candidate field: replace nuclear load order by `L_2^p`.

Rigidity test: Paper 22's TT Linear Volume No-Go and tensor-channel branch structure select a linear `L_2` response for the active TT/nuclear phase-space correction. The remaining open piece is not the `L_2` exponent; it is the TT modular budget assigned to that block.

Classification: `DERIVED/CONDITIONAL` on the TT carrier-localization stack plus TBS.

Hidden-parameter verdict: not hidden.

### 8. Sign convention of the weak amplitude

Candidate field: replace the bridge contribution by `s_w epsilon_w` with `s_w in {+1,-1}`.

Field-redefinition test: as a bare amplitude magnitude, `epsilon_w` is positive. The PRyMordial dressing uses it as a suppression direction. A global carrier-orientation flip can change formal signs unless the response operator orientation is fixed.

Classification: `RECONSTRUCTION / ORIENTATION-CONVENTION`.

Hidden-parameter verdict: discrete, not continuous. It is not the same kind of hidden kappa field that killed Paper 24 Step D, but it is worth documenting explicitly if Paper 22 is edited again: the theorem constructs positive dressing magnitudes; the suppressive sign belongs to the rate-dressing operator orientation.

### 9. Sign convention of the nuclear amplitude

Candidate field: replace the bridge contribution by `s_n epsilon_n` with `s_n in {+1,-1}`.

Rigidity test: same as the weak sign. The magnitude is determined by the formula under the premise package; the sign is attached to the physical suppression orientation of nuclear phase-space dressing.

Classification: `RECONSTRUCTION / ORIENTATION-CONVENTION`.

Hidden-parameter verdict: discrete, not a fitted continuous hidden parameter. Document as a convention if the manuscript is updated.

### 10. `j=1` versus `j=2` channel assignment

Candidate field: swap or reassign channel loads:

```text
j=1 -> weak, j=2 -> nuclear
```

Rigidity test: Paper 22's Channel Floor Theorem and GMP-mediated carrier map assign gauge-current couplings to the vector/coexact `j=1` channel and metric-dependent phase-space corrections to the TT `j=2` channel. The assignment is not free after GMP and the channel-floor infrastructure are accepted.

Classification: `DERIVED/CONDITIONAL on GMP + Channel Floor`.

Hidden-parameter verdict: not hidden.

### 11. Weak-vs-nuclear sector split

Candidate field: allow mixing:

```text
epsilon_w = a_11 L_1 + a_12 L_2
epsilon_n = a_21 L_1 + a_22 L_2
```

Rigidity test: the formal bridge operator is block-separated into weak and nuclear sectors. GMP plus channel-floor typing forbids arbitrary weak/nuclear mixing in the bridge primitive. Without GMP, such mixing is not excluded by the numerical BBN scorecard alone.

Classification: `DERIVED/CONDITIONAL on GMP`.

Hidden-parameter verdict: not hidden in v1.5 because GMP is explicitly a new conditional premise.

### 12. Multiplicative separability: payload times load

Candidate field: replace product form by a generic function:

```text
epsilon_w = f_w(K_gauge, L_1)
epsilon_n = f_n(<K>, L_2, mult_TT)
```

Rigidity test: the current bridge operator is linear in the spatial load projectors and scalar in the source payloads. This gives the product structure once the bridge operator is accepted. But the bridge operator itself is conditional on GMP plus TBS, with WMR entering the weak coefficient.

Classification: `DERIVED/CONDITIONAL` inside the bridge-operator premise package.

Hidden-parameter verdict: not hidden.

## Hidden-parameter ranking

No **unlabelled continuous hidden parameter** was found.

The following are the highest-leverage free fields, but they are visible conditional/open fields rather than hidden ones:

| Rank | Field | Freedom exposed by audit | Leverage | Visibility in v1.5 | Promotion path |
|---:|---|---|---|---|---|
| 1 | TT budget scalar `a_n` replacing `<K>/10` | Existing symmetry/KMS/localization data do not force the active TT block to receive `<K>` | High: `epsilon_n` scales linearly with `a_n`; denominator 9/10/11 shifts `epsilon_n` by order 10% | Visible as TBS; Step 252 says any `b >= 0` remains compatible with current modular data | modular intertwining theorem for `P_resp`, modular Gauss law, or modular-energy transport theorem |
| 2 | Weak payload scalar `a_w` replacing `K_gauge` | Local first variation gives `V'=2 gamma`, not `K_gauge`; WMR closure needs `H1-H3` | Very high: `2 gamma` payload is 8.656x `K_gauge` | Partly visible: WMR is labeled conditional on `H1-H3`; Theorem 22.23 short label omits that inheritance | theorem that physical weak rate is exactly the Paper 25 two-time KMS/CCR bridge observable |
| 3 | Suppressive sign/orientation | Carrier orientation can flip formal sign unless response orientation is fixed | High if reversed, but discrete | Not emphasized as an open problem; mostly implicit in rate-dressing convention | explicit orientation convention or positivity/suppression theorem for the rate-dressing operator |

## Conditional-visibility check

Paper 22 v1.5 is mostly honest under IO Conventions v2.0, but there is one label-hygiene issue.

Visible and acceptable:

- GMP is explicitly marked `NEW PREMISE / CONDITIONAL`.
- TBS is explicitly marked `PREMISE / CONDITIONAL`.
- Step 252 explicitly states the TT budget underdetermination result.
- WMR is explicitly marked `DERIVED/CONDITIONAL on H1-H3` in Step 251.
- The open-problem text states the future paths: equivariant bridge uniqueness for GMP and modular intertwining/Gauss-law transport for TBS.

Needs tightening if Paper 22 is edited again:

- Theorem 22.23's local status line says `DERIVED/CONDITIONAL on GMP + TBS`.
- Because `epsilon_w = K_gauge * L_1` uses WMR, the theorem also inherits WMR's `H1-H3` conditionality.
- The precise status should be one of:

```text
DERIVED/CONDITIONAL on GMP + TBS, with weak payload closure inherited from
WMR(H1-H3)
```

or:

```text
DERIVED/CONDITIONAL on GMP + TBS + WMR(H1-H3)
```

The first wording is cleaner because Paper 22 v1.5 treats WMR as resolved relative to Paper 25, but it preserves the conditional-dependency inheritance required by Conventions v2.0.

## Final verdict

The formal kappa-style audit does **not** retire Theorem 22.23. It also does **not** upgrade it to unconditional theorem status.

Correct current claim:

```text
Theorem 22.23 is a zero-fitted-parameter, framework-constant amplitude
construction that is DERIVED/CONDITIONAL within the stated bridge-premise
package. Its weak coefficient is closed only conditional on WMR(H1-H3);
its nuclear coefficient remains conditional on TBS. No observation-fitted
scalar is present. No unlabelled continuous hidden parameter was found.
```

What future work must not say:

- Do not say the current stack unconditionally derives `K_gauge * L_1`.
- Do not say the current stack unconditionally derives `(<K>/10) * L_2`.
- Do not say the BBN scorecard proves TBS.
- Do not hide the WMR `H1-H3` dependency when citing Theorem 22.23.

What future work may say:

- `L_1`, `L_2`, `K_gauge`, `<K>`, and `mult_TT(n=2)=10` are established framework constants in their source scopes.
- Theorem 22.23 uses zero fitted observational parameters.
- The weak payload issue is conditionally closed by Paper 25's WMR route.
- The TT/nuclear budget scalar is the surviving structural premise.
- The present audit found no Paper-24-Step-D-style unlabelled continuous hidden parameter in Paper 22 v1.5.

## Source artifacts reviewed

- `/opt/cosmology-lab/results/paper22/Interior_Observer_Paper22_v1_5_extracted.txt`
- `/opt/cosmology-lab/results/paper22/paper22_amplitude_energy_asymmetry_round13_report.txt`
- `/opt/cosmology-lab/results/paper22/paper22_physics_paths_round21_report.txt`
- `/opt/cosmology-lab/results/paper22/paper22_last_two_coefficients_round23_report.txt`
- `/opt/cosmology-lab/results/paper22/paper22_scalar_modular_readout_round24_results.json`
- `/opt/cosmology-lab/results/paper25/paper25_reverse_engineer_theorem22_23_report.txt`
- `/opt/cosmology-lab/results/paper25/paper25_paper22_weak_amplitude_audit_report.txt`
- `/opt/cosmology-lab/results/paper25/paper25_bridge_rigidity_joint_assessment_report.txt`
- `/opt/cosmology-lab/results/paper25/paper25_primitive_weak_insertion_construction_report.txt`
- `/opt/cosmology-lab/results/paper25/paper25_weak_two_time_correlator_report.txt`
