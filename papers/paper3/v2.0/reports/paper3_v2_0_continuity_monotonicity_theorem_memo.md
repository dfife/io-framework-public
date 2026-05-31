# Paper 3 v2.0 Continuity and Monotonicity Theorem Memo

## Compact Statement

On the admitted active Paper 10 / Paper 29 branch, the Friedmann radicand is
strictly positive across the entire expanding IO half-cycle. The Paper 3
transfer function for `R`, `T`, `H`, and `a0` is analytic for every observer
coordinate with `eta in (0, pi)`, with `R` strictly increasing, `T` and `H`
strictly decreasing, and `a0` constant.

## Status

`DERIVED/THEOREM` inside the admitted active branch.

If the active branch constants are later revised, this theorem must be rerun
with the revised constants. This memo does not prove the upstream Paper 10 /
Paper 29 branch itself.

## P1/P2 Dependency Chain

- P1: the observable universe exists inside a Schwarzschild black hole. This
  supplies the closed `K=+1` interior support, fixed parent Schwarzschild radius
  `r_s`, expanding support radius `R in (0, r_s]`, and observer-side domain
  `y = R_U/R >= R_U/r_s = 1/x`.
- P2: physics inside the horizon equals physics outside. This licenses standard
  GR/FRW differentiability and the active Friedmann-form readout once the typed
  Paper 10 / Paper 29 active branch is admitted inside P1.
- Paper 1 v4.1: supplies the P1 container, Schwarzschild radius convention, and
  typed-observable discipline.
- Paper 10 / Paper 29: supply the admitted active projection branch constants
  used here.

## Assumptions

The active branch constants are:

```text
x = 1.51899
Omega_r = 9.1575e-5
Omega_m = 0.349
Omega_k = -0.046
Omega_Lambda = 0.697
```

The domain is `y >= 1/x`.

## Radicand Positivity Derivation

The active radicand is

```text
Q(y) = Omega_r y^4 + Omega_m y^3 + Omega_k y^2 + Omega_Lambda.
```

Group the only negative coefficient with the matter term:

```text
Q(y) = Omega_r y^4 + y^2(Omega_m y + Omega_k) + Omega_Lambda.
```

For `y >= 1/x`,

```text
Omega_m y + Omega_k >= Omega_m/x + Omega_k
                         = 0.1837579312569536 > 0.
```

Also `Omega_r > 0`, `Omega_Lambda > 0`, and `y^2 > 0`. Therefore
`Q(y) > 0` on the full active domain. This is a domain inequality, not a point
check.

The endpoint sanity check is:

```text
Q(1/x) = 0.7766581202434925.
```

## Monotonicity Derivation

The support radius is

```text
R(eta) = (r_s/2)(1 - cos eta),
dR/deta = (r_s/2) sin eta > 0
```

for `eta in (0, pi)`, so `R` is strictly increasing.

The temperature is `T=C/R` with `C>0`, so `T` is strictly decreasing as `R`
increases.

The expansion readout is `H=H0 sqrt(Q(y))`, where `y=R_U/R`. Since `R`
strictly increases, `y` strictly decreases. It remains to prove `Q` strictly
increases with `y`:

```text
dQ/dy = 4 Omega_r y^3 + 3 Omega_m y^2 + 2 Omega_k y
      = y(4 Omega_r y^2 + 3 Omega_m y + 2 Omega_k).
```

For `y >= 1/x`,

```text
3 Omega_m y + 2 Omega_k >= 3 Omega_m/x + 2 Omega_k
                              = 0.5972737937708609 > 0.
```

The radiation contribution is positive and `y>0`, so `dQ/dy>0` on the full
domain. Therefore `H` strictly decreases with `eta`.

Finally,

```text
a0 = c^2/r_s
```

is constant because the P1 parent Schwarzschild radius is fixed.

## Evidence

- Reproducible script:
  `scripts/03_radicand_positivity_and_monotonicity.py`
- Frozen result:
  `results/radicand_positivity_monotonicity_results.json`
- Validator:
  `scripts/05_validate_expected_outputs.py`

The validator checks the positivity lower bound, the monotonicity lower bound,
the endpoint sanity values, and the theorem status flag.
