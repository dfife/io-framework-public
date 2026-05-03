# Paper 24 v2.2 Reproducibility Bundle

Classification: `verified / public-reproducibility-support`

This bundle contains the curated scripts, frozen outputs, and calculation
reports needed to audit the Paper 24 v2.2 lithium result.

It is intentionally not a mirror of the private research lab. Exploratory
GSM/AZURE2 class-search automation, failed route searches, private scratch
state, and PRyMordial itself are excluded.

## Paper Version

Paper:

```text
Paper 24 v2.2
The Lithium Problem Solved - Channel-Resolved BBN, Quadrupole Isolation,
and the Mass-7 TT Dressing
```

Public paper record:

```text
https://zenodo.org/records/19219282/latest
```

Convention reference for new papers:

```text
https://dfife.github.io/data/conventions_v2.md
```

Historical observational convention used by already-published correction
papers:

```text
https://dfife.github.io/data/observational_conventions_v1.md
```

## Contents

- `scripts/README.md`
  - Script inventory, run order, dependencies, outputs, and claim boundaries.
- `scripts/01_compute_qtrans_carrier.py`
  - Recomputes the final-state quadrupole carrier audit and the `Q_trans`
    target translation.
- `scripts/02_recompute_excited_state_import.py`
  - Recomputes the Henderson excited-state import and spin-multiplicity
    correction.
  - Requires the final BBN scorecard output.
  - Full rerun requires PRyMordial because it imports
    `scripts/03_run_final_bbn_scorecard.py`.
- `scripts/03_run_final_bbn_scorecard.py`
  - Recomputes the Paper 24 excited-branch kernel and PRyMordial network
    scorecard.
  - Requires an external PRyMordial checkout.
- `scripts/04_validate_expected_outputs.py`
  - Fast validation of the frozen result files included in this bundle.

Frozen outputs are in `results/`. Human-readable reports are in `reports/`.

## Quick Validation

From this directory:

```bash
python3 scripts/04_validate_expected_outputs.py
```

Expected output:

```json
{
  "checks": 8,
  "state": "passed"
}
```

This validates the frozen support outputs without requiring PRyMordial.

## Recompute Non-PRyMordial Carrier Audit

```bash
python3 scripts/01_compute_qtrans_carrier.py
python3 scripts/04_validate_expected_outputs.py
```

The first command rewrites:

```text
results/qtrans_carrier_results.json
```

## Full PRyMordial Rerun

PRyMordial is not vendored in this repository. Install or clone it separately,
then set:

```bash
export PRYM_ROOT=/path/to/PRyMordial
```

Run:

```bash
python3 scripts/03_run_final_bbn_scorecard.py
python3 scripts/02_recompute_excited_state_import.py
python3 scripts/04_validate_expected_outputs.py
```

The scripts write:

```text
results/final_excited_branch_results.json
results/final_excited_branch_report.txt
results/excited_state_import_recomputation_results.json
reports/excited_state_import_recomputation_memo.md
```

The public bundle includes frozen outputs generated in the lab so reviewers can
audit the exact numbers even before installing PRyMordial.

## Headline Values

Primary Henderson de-excitation import:

```text
B(E2; 1/2- -> 3/2-) = 52 e^2 fm^4
q_trans,ex = 0.017537902422203915 b
R_ex(T9_eff) = 0.5987463992430407
Li7/H = 1.7239845810965594e-10
Li7 sigma = +0.46446639063406275
D/H = 2.5072194689896718e-05
D/H sigma = -0.6593510336776072
Y_p = 0.24770877169172603
Y_p sigma = +0.677192922931509
```

The earlier amplitude-weighted branch scorecard gives:

```text
Li7/H = 1.7513106468462057e-10
Li7 sigma = +0.5526149898264701
D/H = 2.5072211748471435e-05
D/H sigma = -0.6592941717618847
Y_p = 0.24770877171605302
Y_p sigma = +0.6771929290132552
```

## Claim Boundary

- `verified`: arithmetic, spin-multiplicity conversion, frozen output
  validation, and local PRyMordial reruns in the private lab.
- `conditional`: mapping the imported `B(E2)` response into the Paper 24
  branch-dressing scale.
- `not included`: private class-search automation, exploratory GSM/AZURE2
  searches, failed route memos, and PRyMordial source code.
- `not theorem evidence`: reconstructed AZURE2/R-matrix scaffolds are not used
  in this public support bundle.

## References

- Henderson et al., Phys. Rev. C 99, 064320 (2019),
  DOI `10.1103/PhysRevC.99.064320`.
- Lichtenstadt et al., Phys. Lett. B 219, 394-398 (1989),
  DOI `10.1016/0370-2693(89)91083-6`.
- Tilley et al., Nucl. Phys. A 708, 3-163 (2002),
  DOI `10.1016/S0375-9474(02)00597-3`.
- Odell et al., Front. Phys. 10:888476 (2022),
  DOI `10.3389/fphy.2022.888476`.
