# Paper 24 v3.0 Reproducibility Bundle

Classification: `VERIFIED / public-reproducibility-support`

This bundle contains the curated scripts, frozen outputs, and calculation
reports needed to audit the Paper 24 v3.0 lithium result.

The v3.0 bundle reflects the final Paper 24 v3.0 Pastore/Henderson input
package: the ground-state quadrupole import is `|Q_GS(7Be)| = 0.067 +/- 0.001 b`
from Pastore et al. (2013), Table II, and the primary Henderson row gives
`Li7/H = 1.7414708079857392e-10` at `+0.520873574147546` observational sigma.
The bundle also adds the R4/FIRAS audit required by the current framework
convention: observed CMB temperature is not counted as an independent IO
prediction, and `R4_FIRAS = 1.0031014644` is recorded as an observer-side
readout normalization that does not enter the active PRyMordial BBN branch.

Scope note: the final Paper 24 v3.0 manuscript narrows the Geometric Mediation
Principle closure to the Paper 24 transverse-traceless observable class
(`Theorem 24.G1`). This bundle supports the lithium scorecard and associated
transverse-traceless rate-dressing computations only; it does not claim or
attempt universal Geometric Mediation Principle closure over the full abstract
local algebra.

It is intentionally not a mirror of the private research lab. Exploratory
GSM/AZURE2 class-search automation, failed route searches, private scratch
state, and PRyMordial itself are excluded.

## Paper Version

Paper:

```text
Paper 24 v3.0
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
- `scripts/04_r4_firas_kappa_audit.py`
  - Audits R4/FIRAS impact, hidden-parameter exposure, label discipline,
    abbreviations, and IO slang.
- `scripts/05_validate_expected_outputs.py`
  - Fast validation of the frozen result files included in this bundle.
- `scripts/06_combined_uncertainty_propagation.py`
  - Propagates the combined `Q_GS` and Henderson `B(E2)` uncertainty band
    through the branch-sum formula and the banked PRyMordial sensitivity map.

Frozen outputs are in `results/`. Human-readable reports are in `reports/`.

## Quick Validation

From this directory:

```bash
python3 scripts/04_r4_firas_kappa_audit.py
python3 scripts/06_combined_uncertainty_propagation.py
python3 scripts/05_validate_expected_outputs.py
```

Expected output:

```json
{
  "checks": 24,
  "state": "passed"
}
```

This validates the frozen support outputs without requiring PRyMordial.

## Recompute Non-PRyMordial Carrier Audit

```bash
python3 scripts/01_compute_qtrans_carrier.py
python3 scripts/04_r4_firas_kappa_audit.py
python3 scripts/06_combined_uncertainty_propagation.py
python3 scripts/05_validate_expected_outputs.py
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
python3 scripts/04_r4_firas_kappa_audit.py
python3 scripts/06_combined_uncertainty_propagation.py
python3 scripts/05_validate_expected_outputs.py
```

The scripts write:

```text
results/final_excited_branch_results.json
results/final_excited_branch_report.txt
results/excited_state_import_recomputation_results.json
reports/excited_state_import_recomputation_memo.md
results/r4_firas_kappa_audit_results.json
reports/paper24_v30_r4_firas_kappa_audit_report.md
results/combined_uncertainty_propagation_results.json
```

The public bundle includes frozen outputs generated in the lab so reviewers can
audit the exact numbers even before installing PRyMordial.

## Headline Values

Primary Henderson de-excitation import:

```text
B(E2; 1/2- -> 3/2-) = 52 e^2 fm^4
q_trans,ex = 0.017537902422203915 b
R_ex(T9_eff) = 0.5987463992430407
Li7/H = 1.7414708079857392e-10
Li7 sigma = +0.520873574147546
D/H = 2.5072097840055007e-05
D/H sigma = -0.659673866483311
Y_p = 0.24770877182909237
Y_p sigma = +0.6771929572730941
```

Combined `Q_GS` + Henderson `B(E2)` uncertainty propagation (`N = 100000`,
seed `240630`):

```text
R_34,tot median = 0.3101525034206116
R_34,tot 1sigma band = [0.29916180906504, 0.32325040678126793]
R_34,tot 2sigma band = [0.28962711454283396, 0.33999418351986627]
Li7/H median = 1.7420833548579086e-10
Li7/H 1sigma band = [1.6825948263859496e-10, 1.8128758354571006e-10]
Li7/H 2sigma band = [1.6309216298133606e-10, 1.9032198926995218e-10]
```

The earlier amplitude-weighted branch scorecard gives:

```text
Li7/H = 1.7755897504747163e-10
Li7 sigma = +0.6309346789506977
D/H = 2.507159147361074e-05
D/H sigma = -0.6613617546308731
Y_p = 0.247708772707705
Y_p sigma = +0.6771931769261608
```

## Claim Boundary

- `VERIFIED`: arithmetic, spin-multiplicity conversion, frozen output
  validation, combined uncertainty propagation, and local PRyMordial reruns in
  the private lab.
- `DERIVED/CONDITIONAL_VERIFIED`: mapping the imported `B(E2)` response into
  the Paper 24 branch-dressing scale, with dependency on the Paper 24
  transverse-traceless observable class closure and imported A=7 nuclear data.
- `IMPORTED/EMPIRICAL`: FIRAS fixes the observer-side `R4_FIRAS` readout
  normalization inherited from Paper 17 v1.5; it is not tuned against BBN.
- `not included`: private class-search automation, exploratory GSM/AZURE2
  searches, failed route memos, and PRyMordial source code.
- `RECONSTRUCTION/RESEARCH_ONLY`: reconstructed AZURE2/R-matrix scaffolds are
  not used as theorem evidence in this public support bundle.

## References

- Pastore et al., Phys. Rev. C 87, 035503 (2013), Table II,
  DOI `10.1103/PhysRevC.87.035503`.
- Henderson et al., Phys. Rev. C 99, 064320 (2019),
  DOI `10.1103/PhysRevC.99.064320`.
- Lichtenstadt et al., Phys. Lett. B 219, 394-398 (1989),
  DOI `10.1016/0370-2693(89)91083-6`.
- Tilley et al., Nucl. Phys. A 708, 3-163 (2002),
  DOI `10.1016/S0375-9474(02)00597-3`.
- Odell et al., Front. Phys. 10:888476 (2022),
  DOI `10.3389/fphy.2022.888476`.
