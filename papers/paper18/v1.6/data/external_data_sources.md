# Paper 18 v1.6 External Data Sources

No external observational dataset is redistributed in this bundle.

## DESI DR1 Gaussian BAO

Used by `scripts/08_legacy_observables_recalculation.py`.

Required local files:

```text
desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
desi_2024_gaussian_bao_ALL_GCcomb_cov.txt
```

Place them under:

```text
papers/paper18/v1.6/data/external/
```

or set:

```text
PAPER18_DESI_BAO_MEAN=/path/to/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
PAPER18_DESI_BAO_COV=/path/to/desi_2024_gaussian_bao_ALL_GCcomb_cov.txt
```

The frozen JSON in `results/` records the audited run used for the bundle.

## BOSS DR12 Full-Shape Monopole

Used by `scripts/10_matter_power_shape_test.py`.

The script fetches the public Beutler et al. DR12 combined full-shape archive at runtime:

```text
https://fbeutler.github.io/static/Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz
```

The fetched archive is cached under `data/boss_fullshape_tmp/` and is not committed to the repository.

## External Codes

`scripts/08_legacy_observables_recalculation.py` uses CLASS through the Python `classy` module.

`scripts/10_matter_power_shape_test.py` uses CAMB through the Python `camb` module.

The default validator does not require these external reruns. It validates the frozen audited outputs and reruns the core standard theorem scripts.
