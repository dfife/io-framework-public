# Cross-Paper Consistency Report

The following inherited values used by Paper 29 v2.0 match the current active
upstream artifacts reviewed during bundle construction:

| Quantity | Paper 29 value | Active upstream value | Status |
| --- | ---: | ---: | --- |
| `omega_b h^2` | `0.02100` | `0.020995719061702847` | PASS |
| `r_d` | `144.01 Mpc` | `144.01351425392883 Mpc` | PASS |
| `H0` | `67.58 km/s/Mpc` | `67.57585653582628 km/s/Mpc` | PASS |
| `Omega_m` | `0.349` | `0.34868395067621694` | PASS |
| `Omega_k` | `-0.046` | `-0.04579112576013168` | PASS |
| `Omega_lambda` | `0.697` | `0.6970157307777745` | PASS |
| `N_eff` | `3.044` | `3.044` | PASS |
| `z_dec` | `123.67` | `123.67217038722819` | PASS |

Primary upstream reconciliation source:
`/opt/cosmology-lab/results/paper30/paper30_full_recompute_legacy_branch_report.md`.

The CMB temperature is treated as a FIRAS-fixed empirical input inherited
through Paper 17 v1.5, not as a Paper 29 prediction.
