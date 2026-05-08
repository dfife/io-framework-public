# External Data Sources

External datasets are not redistributed in this bundle.

## BOSS DR12 Full-Shape Power Spectrum

Used by:

- `scripts/04_boss_fullshape_baryon_audit.py`
- `scripts/05_scalarization_jacobian.py`
- `scripts/06_corrected_scorecard.py`
- `scripts/07_self_consistent_background.py`

Fetch behavior:

```text
https://fbeutler.github.io/static/Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz
```

The scripts download this archive into:

```text
data/external/boss_fullshape_tmp/
```

## DESI BAO Mean and Covariance

Used by:

- `scripts/06_corrected_scorecard.py`
- `scripts/07_self_consistent_background.py`

Not redistributed. Set:

```bash
export BAO_MEAN_PATH=/path/to/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
export BAO_COV_PATH=/path/to/desi_2024_gaussian_bao_ALL_GCcomb_cov.txt
```

or place files under:

```text
data/external/desi_bao/
```

## PRyMordial

Used by:

- `scripts/08_bbn_scorecard.py`

Not redistributed. Set:

```bash
export PRYM_ROOT=/path/to/PRyMordial
```

