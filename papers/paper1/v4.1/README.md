# Paper 1 v4.1 Reproducibility Bundle

This bundle supports Paper 1 v4.1 of the Interior Observer framework. The
original Paper 1 script set was not found as a complete saved bundle, so the
foundation arithmetic scripts remain reverse-engineered from the Paper 1 v4.0
manuscript and current public bundle conventions. Version v4.1 adds the
post-Cosmo core theorem registry package and the total-energy/density-accounting
separation audit surface.

The bundle reproduces the local Paper 1 arithmetic for the Schwarzschild radius,
line-scale ratio, geometric boost factor, local Hawking thermal scale,
interior-observer greybody theorem flag, and torsion/effective dark-energy
formula. It also records cross-paper source pointers for claims inherited from
Paper 17 v1.5, Paper 32 v2.0, Paper 34 v1.2, and Paper 35 v2.0, and archives
the Paper 1 v4.1 registry memos for Theorems 1.X, 1.Y, 1.Z, 1.W, 1.V, 1.U, and
1.T.

## Quickstart

```bash
git clone https://github.com/dfife/io-framework-public.git
cd io-framework-public/papers/paper1/v4.1
python3 scripts/06_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=41 pass_count=41 fail_count=0
```

## Regenerating Outputs

```bash
python3 scripts/01_foundation_constants.py
python3 scripts/02_temperature_chain.py
python3 scripts/03_spectral_theorem_flags.py
python3 scripts/04_dark_energy_chain.py
python3 scripts/05_cross_paper_consistency.py
python3 scripts/07_total_energy_density_accounting.py
python3 scripts/08_core_theorem_registry.py
python3 scripts/06_validate_expected_outputs.py
```

## v4.1 Registry Additions

The v4.1 bundle adds:

- Theorem 1.X, Finite Horizon-Readable Quotient.
- Theorem 1.Y, Total Energy / Density Accounting Separation.
- Theorems 1.Z, 1.W, 1.V, 1.U, and 1.T in the core inheritance memo.
- Cosmo reconciliation for the closed \(K=+1\), compact \(S^3\) reduction package.

Cosmo approved the closed-space reduction only as the chain
`Theorem 1.Z -> Theorem 1.U`, guarded by `Theorem 1.V`. It is not a standalone
universal "closed curve space" theorem.

## Audit Boundary

This bundle intentionally records two manuscript synchronization findings:

- With the v4.0 stated constants `M_U = 4.50e53 kg` and `R_U = 4.40e26 m`, the
  §5 dark-energy formula gives `rho_Lambda,eff = 5.8176e-27 kg/m^3`, not the
  manuscript-quoted legacy value `6.05e-27 kg/m^3`.
- The Paper 1 v4.0 manuscript cites Paper 32 v2.0 bundle SHA prefix `fadeea1d`;
  the current public repository manifest records `2e1ff99e...` for
  `paper32-v2.0`.

These are treated as explicit audit flags, not hidden validation failures.

## Citation

```text
David Fife, Paper 1 v4.1 Reproducibility Bundle,
Interior Observer Framework public reproducibility repository,
GitHub release paper1-v4.1, May 2026.
https://github.com/dfife/io-framework-public/releases/tag/paper1-v4.1
```
