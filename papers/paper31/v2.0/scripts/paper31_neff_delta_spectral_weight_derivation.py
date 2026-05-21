#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT_PATH = ROOT / "paper31_neff_delta_spectral_weight_report.md"
JSON_PATH = ROOT / "paper31_neff_delta_spectral_weight_results.json"

X = 1.519
GAMMA_BI = 0.2375
DELTA = X**4 * (1.0 + GAMMA_BI**2)
LN_DELTA = math.log(DELTA)
S3_VOLUME_UNIT = 2.0 * math.pi**2
STANDARD_NEFF_COEFF = 0.22710731766


def scalar_one_particle_z_closed(q: float, weight: float = 1.0) -> float:
    return weight * q * (1.0 + q) / (1.0 - q) ** 3


def scalar_one_particle_z_mode_sum(q: float, *, nmax: int = 5000, weight: float = 1.0) -> float:
    return weight * sum((n + 1) ** 2 * q ** (n + 1) for n in range(nmax))


def log_grand_partition_function(q: float, *, weight: float = 1.0, mmax: int = 2000) -> float:
    return sum(scalar_one_particle_z_closed(q**m, weight=weight) / m for m in range(1, mmax + 1))


def bose_factor(x: float) -> float:
    if x > 700.0:
        return 0.0
    return 1.0 / math.expm1(x)


def scalar_energy_density_unit_s3(temperature: float, *, weight: float = 1.0, nmax: int = 40000) -> float:
    beta = 1.0 / temperature
    total = 0.0
    for n in range(nmax):
        omega_n = n + 1.0
        degeneracy_n = (n + 1.0) ** 2
        total += weight * degeneracy_n * omega_n * bose_factor(beta * omega_n)
    return total / S3_VOLUME_UNIT


def stefan_boltzmann_scalar(temperature: float, *, weight: float = 1.0) -> float:
    return weight * (math.pi**2 / 30.0) * temperature**4


def standard_total_g_from_neff(neff: float) -> float:
    return 2.0 * (1.0 + STANDARD_NEFF_COEFF * neff)


def standard_neff_from_total_g(total_g: float) -> float:
    return (0.5 * total_g - 1.0) / STANDARD_NEFF_COEFF


def build_results() -> dict:
    q_samples = [math.exp(-0.5), math.exp(-1.0), math.exp(-2.0)]
    z_checks = []
    for q in q_samples:
        z_mode = scalar_one_particle_z_mode_sum(q)
        z_closed = scalar_one_particle_z_closed(q)
        z_delta = scalar_one_particle_z_closed(q, weight=DELTA)
        logz_base = log_grand_partition_function(q)
        logz_delta = log_grand_partition_function(q, weight=DELTA)
        z_checks.append(
            {
                "q": q,
                "z_mode_sum": z_mode,
                "z_closed_form": z_closed,
                "closed_form_error": z_mode - z_closed,
                "z_delta_closed_form": z_delta,
                "z_delta_over_z_base": z_delta / z_closed,
                "logZ_base": logz_base,
                "logZ_delta": logz_delta,
                "logZ_delta_over_logZ_base": logz_delta / logz_base,
            }
        )

    temperature_samples = [1.0, 2.0, 5.0, 10.0]
    thermal_checks = []
    for temperature in temperature_samples:
        rho_base = scalar_energy_density_unit_s3(temperature, weight=1.0)
        rho_delta = scalar_energy_density_unit_s3(temperature, weight=DELTA)
        rho_sb = stefan_boltzmann_scalar(temperature, weight=1.0)
        thermal_checks.append(
            {
                "temperature_unit_radius": temperature,
                "rho_base": rho_base,
                "rho_delta": rho_delta,
                "rho_delta_over_rho_base": rho_delta / rho_base,
                "rho_base_over_stefan_boltzmann_limit": rho_base / rho_sb,
                "rho_delta_over_delta_times_stefan_boltzmann_limit": rho_delta / stefan_boltzmann_scalar(temperature, weight=DELTA),
            }
        )

    return {
        "title": "Paper 31 spectral-weight route to g_eff = Delta",
        "date": "2026-04-01",
        "inputs": {
            "x": X,
            "gamma_BI": GAMMA_BI,
            "Delta": DELTA,
            "ln_Delta": LN_DELTA,
        },
        "claim_status": {
            "thermal_multiplicity_scaling_on_S1xS3": "derived",
            "io_boundary_weight_equals_Delta": "derived_from_Paper15_Paper18_object_type",
            "g_eff_IO_equals_Delta_if_unreduced_hawking_covariance_uses_that_weight": "conditional",
            "standard_BBN_N_eff_equals_Delta": "not_established",
        },
        "theorem_31A": {
            "status": "derived",
            "statement": "For a compact free bosonic thermal bath on S^1_beta x S^3, a uniform spectral multiplicity weight c rescales the one-particle partition function, the grand partition function, the thermal energy, and the radiation energy density by the same factor c.",
            "proof_identity": [
                "Z_1(q) = sum_n d_n q^{omega_n}",
                "if d_n -> c d_n, then Z_1 -> c Z_1",
                "ln Z(q) = sum_{m>=1} Z_1(q^m)/m, so ln Z -> c ln Z",
                "U = - d/d beta ln Z, so U -> c U",
                "rho = U / Vol(S^3), so rho -> c rho",
            ],
        },
        "theorem_31B": {
            "status": "derived",
            "statement": "Within the Paper 15 / Paper 18 object class, the unique positive boundary-to-bulk norm-squared weight on the horizon carrier is Delta = x^4 (1 + gamma^2).",
            "proof_identity": [
                "half-density amplitude transgression contributes x^2",
                "covariance / spectral measure is norm-squared, giving x^4",
                "quaternionic SU(2) norm contributes 1 + gamma^2",
                "hence the total weight is Delta = x^4 (1 + gamma^2)",
            ],
        },
        "theorem_31C": {
            "status": "conditional",
            "premises": [
                "all interior radiation is the Paper 1 Hawking bath",
                "Gamma(omega) = 1, so there is no mode-dependent greybody suppression inside the horizon",
                "the physically relevant unreduced one-particle Hawking covariance is the Paper 15 / Paper 18 weighted pushforward, before reduced-algebra projection",
                "Paper 22 S^3 ~= SU(2) lets that weight act uniformly across the bulk mode ladder",
            ],
            "statement": "Under these premises, the IO compact-space radiation multiplicity coefficient is g_eff^IO = Delta.",
        },
        "scalar_unit_S3_checks": {
            "one_particle_partition_function": "Z_1(q) = sum_{n>=0} (n+1)^2 q^(n+1) = q (1+q) / (1-q)^3",
            "grand_partition_function": "ln Z(q) = sum_{m>=1} Z_1(q^m) / m",
            "energy_density_unit_S3": "rho(T) = (1 / (2 pi^2)) sum_{n>=0} (n+1)^3 / (exp[(n+1)/T] - 1)",
            "q_samples": z_checks,
            "temperature_samples": thermal_checks,
        },
        "normalization_boundary": {
            "standard_total_g_from_Neff_3_044": standard_total_g_from_neff(3.044),
            "standard_total_g_from_DH_matching_Neff_3_41293": standard_total_g_from_neff(3.41293),
            "standard_Neff_equivalent_if_total_g_equals_Delta": standard_neff_from_total_g(DELTA),
            "interpretation": "The later Paper 20 / Paper 30 BBN slot uses the standard neutrino-normalized N_eff parameter. That is not automatically the same object as the total compact-space multiplicity coefficient g_eff used in this derivation.",
        },
        "literature_notes": {
            "compact_partition_function": "Beccaria, Bekaert, Tseytlin (2014), JHEP 08 (2014) 113, https://repo.scoap3.org/records/3732 and PDF https://scoap3-prod-backend.s3.cern.ch/media/files/3732/10.1007/JHEP08%282014%29113_a.pdf",
            "heat_kernel_free_energy": "Gusev (2015), https://arxiv.org/abs/1612.03023",
            "heat_kernel_vector_bundles": "Avramidi (2001), https://arxiv.org/abs/math-ph/0107018",
        },
    }


def build_report(results: dict) -> str:
    q_rows = []
    for row in results["scalar_unit_S3_checks"]["q_samples"]:
        q_rows.append(
            "| "
            + " | ".join(
                [
                    f"{row['q']:.12f}",
                    f"{row['closed_form_error']:.3e}",
                    f"{row['z_delta_over_z_base']:.12f}",
                    f"{row['logZ_delta_over_logZ_base']:.12f}",
                ]
            )
            + " |"
        )

    t_rows = []
    for row in results["scalar_unit_S3_checks"]["temperature_samples"]:
        t_rows.append(
            "| "
            + " | ".join(
                [
                    f"{row['temperature_unit_radius']:.1f}",
                    f"{row['rho_delta_over_rho_base']:.12f}",
                    f"{row['rho_base_over_stefan_boltzmann_limit']:.12f}",
                    f"{row['rho_delta_over_delta_times_stefan_boltzmann_limit']:.12f}",
                ]
            )
            + " |"
        )

    return f"""# Paper 31: Spectral-Weight Route to `g_eff = Delta`

## Executive Status

- `derived`: on `S^1_beta x S^3`, a uniform multiplicative weight on the one-particle spectral multiplicities rescales the entire thermal partition function and the radiation energy density by the same factor.
- `derived`: within the Paper 15 / Paper 18 object class, the unique positive boundary-to-bulk norm-squared weight is

  `Delta = x^4 (1 + gamma^2) = {results['inputs']['Delta']:.12f}`.

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
{chr(10).join(q_rows)}

The exact energy-density scaling check on unit `S^3`:

| `T` | `rho(Delta)/rho(1)` | `rho(1) / [(pi^2/30) T^4]` | `rho(Delta) / [Delta (pi^2/30) T^4]` |
| --- | --- | --- | --- |
{chr(10).join(t_rows)}

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

- `N_eff = 3.044` corresponds to total `g = {results['normalization_boundary']['standard_total_g_from_Neff_3_044']:.12f}`,
- `N_eff = 3.41293` corresponds to total `g = {results['normalization_boundary']['standard_total_g_from_DH_matching_Neff_3_41293']:.12f}`,
- `g = Delta` would correspond to standard `N_eff = {results['normalization_boundary']['standard_Neff_equivalent_if_total_g_equals_Delta']:.12f}`.

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
"""


def main() -> None:
    results = build_results()
    REPORT_PATH.write_text(build_report(results), encoding="utf-8")
    JSON_PATH.write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {JSON_PATH}")


if __name__ == "__main__":
    main()
