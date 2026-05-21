# Paper 31: Spectral-Weight Route to `g_eff = Delta`

## Executive Status

- `derived`: on `S^1_beta x S^3`, a uniform multiplicative weight on the one-particle spectral multiplicities rescales the entire thermal partition function and the radiation energy density by the same factor.
- `derived`: within the Paper 15 / Paper 18 object class, the unique positive boundary-to-bulk norm-squared weight is

  `Delta = x^4 (1 + gamma^2) = 5.624216852624`.

- `conditional`: if the full unreduced Hawking bath uses that Paper 15 / Paper 18 weight as its one-particle covariance measure before reduction, then the compact-space radiation multiplicity coefficient is

  `g_eff^IO = Delta`.

- `not established`: the later Paper 20 / Paper 30 BBN-normalized parameter called `N_eff` is not yet proved to be the same object as this total compact-space multiplicity coefficient.

## Why This Route Is Different

This route does **not** repeat the dead attempts based on direct microstate counting, Bekenstein bounds, modular-flow scalarization, boundary equipartition, central-charge matching, KK truncation, entropy matching, or fixed-point selection.

Instead, it treats `Delta` as a **uniform one-particle spectral-measure weight** on the unreduced Hawking bath.

That object type matters. Paper 20 proved that the **reduced** observer algebra cannot determine the BBN radiation slot internally. The present route stays outside that reduced algebra and works at the level of the full one-particle thermal spectrum.

## Standard Compact Thermal-QFT Step

For a free bosonic bath on `S^1_beta x S^3`, the standard one-particle partition function is

```text
Z_1(q) = sum_n d_n q^(omega_n),   q = exp(-beta),
```

and the grand partition function is

```text
ln Z(q) = sum_(m>=1) Z_1(q^m) / m.
```

Therefore if the multiplicities are uniformly reweighted by a constant `c`,

```text
d_n -> c d_n,
Z_1 -> c Z_1,
ln Z -> c ln Z,
U = -d_beta ln Z -> c U,
rho -> c rho.
```

So `c` is exactly an effective relativistic degree-of-freedom count in the compact thermal bath.

## IO Step

Paper 15 and Paper 18 already provide the two ingredients of the unique positive boundary-to-bulk weight:

```text
geometric half-density weight: x^2 on amplitudes -> x^4 on norm-squared measure,
gauge quaternionic norm: 1 + gamma^2.
```

Thus the unique norm-squared spectral weight is

```text
dmu_IO = Delta dmu_can,
Delta = x^4 (1 + gamma^2).
```

Paper 1 supplies `Gamma(omega) = 1`, so there is no additional mode-dependent greybody suppression inside the horizon.

Paper 22 supplies `S^3 ~= SU(2)`, so the same `SU(2)` label set organizes both the boundary carrier and the bulk spatial mode ladder. The weight is therefore uniform across the one-particle spectrum rather than a shell-dependent distortion.

Under the extra premise that the **physical unreduced Hawking covariance** is exactly this weighted pushforward, the thermal bath satisfies

```text
Z_1^IO(q) = Delta Z_1^can(q),
ln Z_IO(q) = Delta ln Z_can(q),
rho_IO(T) = Delta rho_can(T),
g_eff^IO = Delta.
```

## Explicit `S^3` Verification

For a conformally coupled scalar on unit `S^3`,

```text
omega_n = n + 1,
d_n = (n + 1)^2,
Z_1(q) = sum_(n>=0) (n+1)^2 q^(n+1) = q(1+q)/(1-q)^3.
```

The exact multiplicity scaling check:

| `q` | `Z_1` closed-form error | `Z_1(Delta)/Z_1(1)` | `ln Z(Delta)/ln Z(1)` |
| --- | --- | --- | --- |
| 0.606530659713 | -1.776e-15 | 5.624216852624 | 5.624216852624 |
| 0.367879441171 | 0.000e+00 | 5.624216852624 | 5.624216852624 |
| 0.135335283237 | -2.776e-17 | 5.624216852624 | 5.624216852624 |

The exact energy-density scaling check on unit `S^3`:

| `T` | `rho(Delta)/rho(1)` | `rho(1) / [(pi^2/30) T^4]` | `rho(Delta) / [Delta (pi^2/30) T^4]` |
| --- | --- | --- | --- |
| 1.0 | 5.624216852624 | 0.999358376109 | 0.999358376109 |
| 2.0 | 5.624216852624 | 0.999959898507 | 0.999959898507 |
| 5.0 | 5.624216852624 | 0.999998973402 | 0.999998973402 |
| 10.0 | 5.624216852624 | 0.999999935838 | 0.999999935838 |

These checks show two facts:

1. the compact-space thermal coefficient scales **exactly** by `Delta`,
2. the baseline unit-`S^3` scalar bath reproduces the Stefan-Boltzmann coefficient in the expected high-temperature limit.

## Honest Boundary

The late stack still matters.

Paper 20 and Paper 30 use the standard BBN neutrino-normalized parameter

```text
rho_r = rho_gamma [1 + 0.22710731766 N_eff].
```

In that normalization:

- `N_eff = 3.044` corresponds to total `g = 3.382629349914`,
- `N_eff = 3.41293` corresponds to total `g = 3.550202755323`,
- `g = Delta` would correspond to standard `N_eff = 7.979084271626`.

So this Paper 31 route does **not** yet overturn the Paper 20 / Paper 30 boundary. What it gives is:

- a clean derivation of why `exp(<K>) = Delta` is the correct **partition-function weight** for the unreduced Hawking bath,
- and an exact derivation of `g_eff^IO = Delta` **if** that bath is the object that gravitates as the homogeneous radiation fluid.

What remains open is the normalization bridge from that full compact Hawking multiplicity to the later BBN parameter called `N_eff`.

## Literature Used

- Beccaria, Bekaert, Tseytlin, "Partition function of free conformal higher spin theory," JHEP 08 (2014) 113:
  - repository: https://repo.scoap3.org/records/3732
  - PDF: https://scoap3-prod-backend.s3.cern.ch/media/files/3732/10.1007/JHEP08%282014%29113_a.pdf
- Yuri V. Gusev, "Finite temperature quantum field theory in the heat kernel method":
  - https://arxiv.org/abs/1612.03023
- Ivan Avramidi, "Heat Kernel Approach in Quantum Field Theory":
  - https://arxiv.org/abs/math-ph/0107018
