# Calculator Phase 4 Source/Readout Foundation

Date: 2026-04-14

This release bundle is a narrow public slice of the live calculator source tree.
It contains only the theorem-grade Phase 4 source/readout modules and the
minimal dependencies needed to run their verification tests.

Included source modules:

- `src/aio_calculator/__init__.py`
- `src/aio_calculator/constants.py`
- `src/aio_calculator/model.py`
- `src/aio_calculator/s3_modes.py`
- `src/aio_calculator/recombination.py`
- `src/aio_calculator/source_block.py`
- `src/aio_calculator/closed_shell_power.py`
- `src/aio_calculator/los_transfer.py`
- `src/aio_calculator/readout_functionals.py`

Included tests:

- `tests/test_source_block.py`
- `tests/test_closed_shell_power.py`
- `tests/test_los_transfer.py`
- `tests/test_readout_functionals.py`

## Scope

This is not a full `C_ell` solver release.

It publishes the theorem-grade source/readout side that sits above the Phase 3
carriers:

- modular-DtN source block on the active scalar-source sector
- exact closed-`S^3` shell-power definitions
- closed LOS transfer carriers and explicit shell-weighted `C_l` assembly
- null-family acoustic readout carrier and peak functional

The following objects remain explicitly open and are not replaced by defaults:

- exact Stage-2 dynamic-network operator
- final typed source/acoustic operator on the closed `S^3` hierarchy
- exact LOS projector `y^(md,ic,q)(tau) -> Delta_l^X(q)`
- exact peak/readout identification `A_peak -> theta_peak`

## Reproducibility

From this directory:

```bash
PYTHONPATH=src python -m pytest tests -q
```

Expected result at release time:

```text
16 passed
```
