# Paper 18 v1.6 Construction Summary

## Script Inventory

- `01_cmp_theorem.py`: reproduces `K_geom + K_gauge = ln Delta`.
- `02_bdp_theorem.py`: reproduces `f_b = 2 gamma / x` and `f_b F = <K>/4`.
- `03_bdp_gap_closure.py`: reproduces the BDP 1-form, derivative-selection, and scaling arithmetic.
- `04_v_alpha_uniqueness.py`: checks the `V(alpha)` symbolic identities and ODE rigidity.
- `05_neff_entropy_rank.py`: reproduces the math-only entropy-rank `N_eff = Delta` theorem.
- `06_bogoliubov_coefficients.py`: computes Planck/KMS Bogoliubov packet coefficients with FIRAS-fixed `R4_FIRAS`.
- `07_modular_bogoliubov_upgrade.py`: verifies modular pushforward covariance using `R4_FIRAS*K_gauge`.
- `08_legacy_observables_recalculation.py`: optional DESI/CLASS rerun for the conditional branch; frozen output included.
- `09_jwst_age_recalculation.py`: recomputes the conditional JWST-age branch with FIRAS-fixed observer `T0`.
- `10_matter_power_shape_test.py`: optional BOSS/CAMB full-shape no-go rerun; frozen output included.
- `11_zeq_kruskal_audit.py`: recomputes equality-redshift and Kruskal comparisons with FIRAS-fixed observer `T0`.
- `12_curvature_implementation_resolution.py`: reproduces Paper 10 i.i.d. vs Paper 18 Schur curvature branch ledger.
- `13_bdp_epoch_independence_audit.py`: documents the naive time-dependent BDP attack.
- `14_structural_attacks_audit.py`: records structural attack checks.
- `15_r4_impact_audit.py`: emits the v1.6 R4 blast-radius ledger.
- `16_kappa_audit_summary.py`: emits the concise kappa-audit summary.
- `17_validate_expected_outputs.py`: referee-facing validator.

## R4 Repair

Patched R4-bearing scripts:

- `06_bogoliubov_coefficients.py`
- `07_modular_bogoliubov_upgrade.py`
- `08_legacy_observables_recalculation.py`
- `09_jwst_age_recalculation.py`
- `10_matter_power_shape_test.py`
- `11_zeq_kruskal_audit.py`

Unchanged by R4:

- CMP, BDP, BDP gap closure, V(alpha), entropy-rank math, curvature branch algebra, BDP epoch audit, and structural attack audit.

## External Dependency Boundary

The default validator does not fetch external datasets. DESI/CLASS and
BOSS/CAMB reruns are available as optional scripts. Frozen audited JSON outputs
are included so reviewers can inspect the exact numbers used by the bundle.
