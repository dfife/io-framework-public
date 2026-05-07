# Paper 18 v1.6 Reproducibility Bundle

This bundle supports Paper 18 v1.6 of the Interior Observer framework:
*Modular Completion: Operator-Level Closure of the Conformal Modular Principle
and the Baryon Dictionary Principle via Relative Modular Operators and
Gauge-Sector Projection*.

Paper 18 v1.6 is the R4/FIRAS hygiene repair for Paper 18. CMP, BDP, and
`V(alpha)` remain R4-independent theorem claims in their stated reduced-sector
scopes. The old independent CMB-temperature prediction wording is retired:
observer-side thermal calculations now inherit Paper 17 v1.5's
FIRAS-fixed readout normalization `R4_FIRAS = 1.0031014644`.

## Quickstart

From the repository root:

```bash
python3 papers/paper18/v1.6/scripts/17_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=30 pass_count=30 fail_count=0
```

## Detailed Reproduction

The numbered scripts can be run one at a time from this bundle root:

```bash
python3 scripts/01_cmp_theorem.py
python3 scripts/02_bdp_theorem.py
python3 scripts/03_bdp_gap_closure.py
python3 scripts/04_v_alpha_uniqueness.py
python3 scripts/05_neff_entropy_rank.py
python3 scripts/06_bogoliubov_coefficients.py
python3 scripts/07_modular_bogoliubov_upgrade.py
python3 scripts/09_jwst_age_recalculation.py
python3 scripts/11_zeq_kruskal_audit.py
python3 scripts/12_curvature_implementation_resolution.py
python3 scripts/13_bdp_epoch_independence_audit.py
python3 scripts/14_structural_attacks_audit.py
python3 scripts/15_r4_impact_audit.py
python3 scripts/16_kappa_audit_summary.py
```

Scripts `08_legacy_observables_recalculation.py` and
`10_matter_power_shape_test.py` are included for full external reruns. They
require non-redistributed DESI/BOSS data and CLASS/CAMB dependencies. The
default validator checks their frozen audited JSON outputs.

## Claim Discipline

- CMP is `DERIVED/THEOREM` within the reduced observer algebra and C1-C5 scope.
- BDP is `DERIVED/THEOREM` within the reduced observer algebra and standard
  minimal-coupling matter class.
- `V(alpha)` is `DERIVED/THEOREM` within the reduced gauge center.
- Entropy-rank `Delta` is theorem-grade as a mathematical acoustic-sector
  result; the physical identification `N_eff = Delta` as the Friedmann
  radiation parameter is withdrawn by the P(k) no-go.
- The Bogoliubov spectrum is a Planck/KMS-form theorem in the reduced quasi-free
  sector, with observer temperature inherited from Paper 17 v1.5
  `R4_FIRAS`. It is not an independent CMB-temperature prediction.
- External P(k) nuisance fits are diagnostic comparison parameters, not hidden
  IO framework parameters.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 18 v1.6*. Zenodo.
https://zenodo.org/records/19054258/latest

Associated release:

`paper18-v1.6`
