# Paper 24 v2.2 Q_trans,ex Formula Documentation Memo

Classification: `verified / documentation_audit / PAPER24_V22_QTRANS_EX_FORMULA`

## Scope

This memo supplies the missing Section 7.2 intermediate converting imported
Henderson `B(E2 down)` strength and the Paper 24 amplitude-weighted Coulomb
kernel into the manuscript quantity:

```text
Q_trans,ex,imp = 0.02088 b.
```

Bundle sources checked:

- `scripts/02_recompute_excited_state_import.py`
- `results/excited_state_import_recomputation_results.json`
- `scripts/03_run_final_bbn_scorecard.py`
- `results/final_excited_branch_results.json`

## Convention Resolution

The checked-in recomputation script stores the excited-state imported scale as:

```text
q_script = sqrt(B(E2 down)) * <F0>_amp,ex / 100
```

and then uses it directly in:

```text
Xi_ex = ((q_script / x) / Q_d) * nu_34(T9).
```

The manuscript notation in Section 7.4 instead writes:

```text
Q_eff,ex = Q_trans,ex,imp * chi_ME / x.
```

Therefore the manuscript `Q_trans,ex,imp` is the pre-`chi_ME` transition
quadrupole scale, while the script's `q_script` is the already-`chi_ME`-weighted
scale. The conversion is:

```text
q_script = chi_ME * Q_trans,ex,imp
```

so:

```text
Q_trans,ex,imp = q_script / chi_ME.
```

## Symbolic Formula

With the manuscript convention:

```text
Q_trans,ex,imp
  = sqrt(B(E2 down)[e^2 fm^4]) * <F0>_amp,ex / (100 * chi_ME)
```

Equivalently:

```text
Q_trans,ex,imp
  = sqrt(B(E2 down)) * <F0>_amp,ex
    * (1 b / 100 fm^2)
    * (1 / chi_ME).
```

For Paper 24 v2.2:

```text
chi_ME = 21/25 = 0.84.
```

## Numerical Evaluation

Inputs:

```text
B(E2 down) = 52 e^2 fm^4
<F0>_amp,ex = 0.24320694787438585
chi_ME = 0.84
sqrt(52) = 7.211102550927978
```

Script-level chi-weighted scale:

```text
q_script
  = sqrt(52) * 0.24320694787438585 / 100
  = 0.01753790242220392 b.
```

Manuscript pre-chi transition scale:

```text
Q_trans,ex,imp
  = q_script / chi_ME
  = 0.01753790242220392 / 0.84
  = 0.020878455264528476 b
  = 0.02088 b.
```

Direct single-line form:

```text
Q_trans,ex,imp
  = sqrt(52) * 0.24320694787438585 / (100 * 0.84)
  = 0.020878455264528476 b
  ≈ 0.02088 b.
```

Using the rounded kernel requested in the audit note:

```text
sqrt(52) * 0.2432 / (100 * 0.84)
  = 0.020877858814115288 b
  ≈ 0.02088 b.
```

## Downstream Check

The Section 7.4 conversion then gives:

```text
Q_eff,ex
  = Q_trans,ex,imp * chi_ME / x
  = 0.020878455264528476 * 0.84 / 1.519
  = 0.011545689547204687 b
  ≈ 0.01155 b.
```

This is exactly the same effective quantity as the script's direct route:

```text
q_script / x
  = 0.01753790242220392 / 1.519
  = 0.011545689547204687 b.
```

Using `Q_d = 0.0028578 b` and `nu_34(T9_eff)=5.324728611585001`:

```text
Xi_ex
  = (Q_eff,ex / Q_d) * nu_34(T9_eff)
  = 21.512234401455196.
```

Then:

```text
R_ex
  = exp(-epsilon_n * Xi_ex)
  = 0.5987463992430407.
```

This matches the local v2.2 recomputation output for the Henderson corrected
de-excitation import case.

## Physical Interpretation

`Q_trans,ex,imp` is the pre-`chi_ME` branch-projected transition quadrupole
scale for the imported excited-state E2 response. The square root of `B(E2)`
supplies the reduced E2 transition-amplitude scale, and `<F0>_amp,ex` projects
that amplitude through the same amplitude-weighted Coulomb readout kernel used
by the excited-branch capture response model.

## Unit Tracking

`B(E2)` has units:

```text
e^2 fm^4
```

Taking the square root gives:

```text
sqrt(B(E2)) -> e fm^2.
```

The electromagnetic charge factor is the transition-strength normalization
already carried by the imported response scale. The remaining geometric unit is
`fm^2`.

The Coulomb projection `<F0>_amp,ex` is dimensionless.

The factor `chi_ME` is dimensionless.

Since:

```text
1 b = 100 fm^2
```

the conversion is:

```text
sqrt(B(E2))[fm^2] * <F0>_amp,ex / (100 * chi_ME) -> b.
```

## Suggested Section 7.2 Equation Block

```text
The imported Henderson de-excitation strength gives

  B(E2; 1/2^- -> 3/2^-) = 52 e^2 fm^4,

so the reduced transition-amplitude scale is sqrt(52) e fm^2. The
amplitude-weighted Coulomb projection gives the chi-weighted quadrupole scale

  q_chi,ex = sqrt(52) * <F0>_amp,ex / 100
           = sqrt(52) * 0.24320694787438585 / 100
           = 0.01753790242220392 b.

Because Section 7.4 defines Q_eff,ex = Q_trans,ex,imp chi_ME / x, the imported
Q_trans,ex,imp is the pre-chi_ME scale:

  Q_trans,ex,imp = q_chi,ex / chi_ME
                 = sqrt(52) * 0.24320694787438585 / (100 * 0.84)
                 = 0.020878455264528476 b
                 ≈ 0.02088 b.
```

## Claim Boundary

- `verified`: the local script's chi-weighted scale
  `q_script = 0.01753790242220392 b`.
- `verified`: Section 7.4's manuscript convention converts this to the
  pre-`chi_ME` scale `Q_trans,ex,imp = 0.020878455264528476 b`.
- `conditional`: the physical import rule mapping measured `B(E2)` to the
  Paper 24 branch-projected transition quadrupole scale.
- `audit note`: future text should distinguish `q_chi,ex` from
  `Q_trans,ex,imp`; otherwise the same apparent mismatch will recur.
