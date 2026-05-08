# Paper 19 v1.6 Reproducibility Bundle

Classification: `verified / public-reproducibility-support`

This bundle supports Paper 19 v1.6 of the Interior Observer framework. It
reproduces the live baryon-scalarization arithmetic, the BOSS DR12 full-shape
audit outputs, the corrected BBN scorecard arithmetic, and the v1.6 R4/FIRAS
kappa-style audit.

The bundle is intentionally not a mirror of the private research lab. Failed
route logs and scratch automation are excluded unless they are necessary to
audit a live theorem or a live no-go claim.

## Quickstart

```bash
git clone https://github.com/dfife/io-framework-public.git
cd io-framework-public/papers/paper19/v1.6
python3 scripts/11_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=12 pass_count=12 fail_count=0
```

The quick validator uses only Python standard-library modules and the frozen
JSON outputs included in this bundle.

## Full Reproduction

Lightweight scripts:

```bash
python3 scripts/01_bridge_theorems.py
python3 scripts/02_modular_scalarization_audit.py
python3 scripts/03_bdp_domain_no_go.py
python3 scripts/09_r4_impact_audit.py
python3 scripts/10_kappa_audit_summary.py
python3 scripts/11_validate_expected_outputs.py
```

Heavy optional scripts:

```bash
python3 scripts/04_boss_fullshape_baryon_audit.py
python3 scripts/05_scalarization_jacobian.py
python3 scripts/06_corrected_scorecard.py
python3 scripts/07_self_consistent_background.py
```

Scripts 04-07 require CAMB/CLASS/scipy/numpy and external datasets. External
datasets are fetched or supplied by the user; they are not redistributed here.

PRyMordial rerun:

```bash
export PRYM_ROOT=/path/to/PRyMordial
python3 scripts/08_bbn_scorecard.py
```

PRyMordial is not redistributed in this repository.

## Headline Reproduced Values

```text
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255 K

omega_b(alpha=3/2) = 0.017053042566348755
BOSS DR12 alpha=3/2 chi2 = 73.03360608958111
Lambda-CDM BOSS reference chi2 = 70.32360985979422

D/H = 2.5233039701421276e-5  (-0.1232009953 sigma)
Y_p = 0.24779423821196234    (+0.6985595530 sigma)
chi2(D/H + Y_p) = 0.5031639343080561

Age-closed diagnostic branch:
N_mode = 0.33602494442479497
H0 = 66.33390065663168 km/s/Mpc
Omega_m = 0.36236276919825583
Omega_k = -0.08523706674322795
```

The age-closed branch is not a zero-fitted-parameter prediction in this bundle.
It is flagged as `OPEN/PREMISE_GAP` unless theorem-fixed elsewhere.

## Claim Boundary

- `DERIVED/CONDITIONAL_VERIFIED`: alpha=3/2 baryon scalarization if Paper 19
  v1.6 states the proper-time comoving-dust metric-measure premise chain.
- `VERIFIED`: frozen-output validation, BOSS/BBN scorecard arithmetic, and
  R4 impact ledger.
- `IMPORTED/EMPIRICAL`: FIRAS observer-side thermal datum, BOSS DR12 data,
  DESI BAO data if used, and standard comparison inputs.
- `OPEN/PREMISE_GAP`: age-closed `N_mode = 0.336` background branch unless a
  later theorem fixes it.

The observed CMB temperature is not counted as an independent Paper 19
prediction. Paper 19 v1.6 inherits Paper 17 v1.5: FIRAS fixes the readout
normalization once, then the frozen value is propagated without retuning.

## Citation

If you use this bundle, cite the Paper 19 v1.6 manuscript and this GitHub
release:

```text
David Fife, Paper 19 v1.6 Reproducibility Bundle,
Interior Observer Framework public reproducibility repository,
GitHub release paper19-v1.6, May 2026.
https://github.com/dfife/io-framework-public/releases/tag/paper19-v1.6
```

Machine-readable citation metadata is provided in `CITATION.cff`.

