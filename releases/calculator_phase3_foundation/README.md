# Calculator Phase 3 Foundation

Date: 2026-04-14

This release bundle is a narrow public slice of the live calculator source tree.
It contains only the theorem-grade Phase 3 foundation modules and the minimal
dependencies needed to run their verification tests.

Included source modules:

- `src/aio_calculator/constants.py`
- `src/aio_calculator/model.py`
- `src/aio_calculator/recombination.py`
- `src/aio_calculator/s3_modes.py`
- `src/aio_calculator/perturbation_types.py`
- `src/aio_calculator/scalar_hierarchy.py`
- `src/aio_calculator/thomson_history_contract.py`

Included tests:

- `tests/test_s3_modes.py`
- `tests/test_perturbation_types.py`
- `tests/test_scalar_hierarchy.py`
- `tests/test_thomson_history_contract.py`

## Scope

This is not a full CMB solver release.

It publishes the theorem-grade perturbation foundation only:

- closed `S^3` mode ladders
- typed perturbation carrier grammar
- scalar hierarchy shell carrier
- coupled Thomson-history tuple contract

The following objects remain explicitly open and are not replaced by defaults:

- exact Stage-2 dynamic-network operator
- final typed source/acoustic operator on the closed `S^3` hierarchy
- exact IO-native operator on the coupled Thomson-history tuple

## Reproducibility

From this directory:

```bash
PYTHONPATH=src python -m pytest tests -q
```

Expected result at release time:

```text
17 passed
```
