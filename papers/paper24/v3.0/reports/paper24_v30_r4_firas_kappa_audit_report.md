# Paper 24 v3.0 R4/FIRAS Kappa-Style Audit Report

## Executive Verdict

No hidden continuous fitted parameter was found in the active Paper 24 v3.0 public scripts.
The R4/FIRAS repair does not change the Paper 24 BBN scorecard because R4 fixes observer-side optical readout, while the active PRyMordial BBN calculation uses the local interior thermal branch.

- `R4_FIRAS = 1.0031014644`
- `T_IO_BBN_BRANCH = 2.6635 K`
- `T_obs_FIRAS_readout = 2.725499999999 K`
- `R4_enters_active_BBN_scorecard = false`
- Paper 24 v3.0 must not claim an independent observed-CMB-temperature prediction.

## R4 Field-Redefinition Test

The retired `R4 = 1` normalization is not used as a Paper 24 fitted parameter. Under the Paper 17 v1.5 repair, FIRAS fixes a unique observer-side readout normalization inside the declared readout family. Paper 24 inherits that constant for bookkeeping, but its BBN branch remains the local `T_IO` branch. Replacing the PRyMordial temperature with observer-side `T_obs` would be a class error, not an R4 repair.

## Candidate Fields

| Field | Classification | Hidden parameter? | Paper 24 impact |
| --- | --- | --- | --- |
| R4 optical readout normalization | IMPORTED/EMPIRICAL input plus DERIVED uniqueness theorem in Paper 17 v1.5 | False | Does not enter active BBN scorecard; only observer-side thermal readout bookkeeping. |
| T_IO_BBN_BRANCH_K | DERIVED/CONDITIONAL_VERIFIED through Paper 21/Paper 22 BBN branch assignment | False | Used as PRyMordial T0CMB baseline in the active scorecard. |
| Y_p readout | VERIFIED wrapper convention | False | Matches the Paper 24 v3.0 scorecard convention. |
| Henderson B(E2) import | IMPORTED/EMPIRICAL plus VERIFIED conversion | False | Sets the primary q_trans,ex row; not tuned to BBN residuals. |
| q_trans,ex projection | DERIVED/CONDITIONAL_VERIFIED within imported nuclear-data branch package | False | Load-bearing for the Henderson primary lithium row. |

## Script Review

| Script | R4 usage | Impact |
| --- | --- | --- |
| `01_compute_qtrans_carrier.py` | none | No R4 damage. This script uses nuclear carrier constants, x, gamma_BI, and observational Li-7 denominator only. |
| `02_recompute_excited_state_import.py` | none directly; calls script 03 for PRyMordial scorecard when rerun. | No R4 damage. Imported A=7 nuclear data are independent of optical readout normalization. |
| `03_run_final_bbn_scorecard.py` | records R4_FIRAS for audit visibility; does not use it in the PRyMordial T0CMB assignment. | No numerical R4 damage. The active BBN branch uses T_IO_BBN_BRANCH_K = 2.6635 K and YPCMB(). |
| `04_r4_firas_kappa_audit.py` | computes observer-side readout bookkeeping and records non-entry into active BBN. | Audit support only. |
| `05_validate_expected_outputs.py` | validates R4_FIRAS in the audit JSON; does not recompute BBN. | Validation support only. |

## Claim-Label Compliance Flags

Paper 24 v3.0 should use the public canonical claim labels. The following manuscript labels need migration review:

- `DERIVED/SCOPED`: Replace with DERIVED/CONDITIONAL_VERIFIED if the scoped chain reaches Premise 1, Premise 2, or a frozen imported empirical/physics input; otherwise OPEN/PREMISE_GAP.
- `CONDITIONAL on ...`: Replace load-bearing cases with DERIVED/CONDITIONAL_VERIFIED and include the explicit chain. Use OPEN/PREMISE_GAP if the chain cannot be stated.
- `IMPORTED/SCOPED`: Use IMPORTED/EMPIRICAL for external data, then separately state the theorem chain that consumes the import.
- `DERIVED/IMPORTED`: Split into VERIFIED arithmetic/derivation and IMPORTED/EMPIRICAL input.

## Abbreviations Flagged

First use should be expanded for non-IO readers:

`BBN`, `CMB`, `CG`, `FRW`, `GR`, `KMS`, `LQG`, `OS`, `TT`, `ANC`, `NCSM`, `IO`, `CMP`, `BDP`, `GTTP`, `PSRP`, `GMP`, `TBS`, `WMR`

## IO Slang Flagged

These terms should be replaced with standard physics language or defined explicitly before use:

`one-slot`, `two-slot`, `alpha-ladder`, `horizon puncture`, `generating-potential hierarchy`, `bridge-dressing`, `branch package`, `mass-7 TT dressing`

## Recommendations

- Keep the Paper 24 v3.0 BBN scorecard unchanged.
- Do not describe observed CMB temperature as an independent Paper 24 or IO prediction.
- Keep R4_FIRAS visible as inherited observer-side readout normalization, not as a tunable BBN parameter.
- Migrate noncanonical labels in the manuscript to the published claim-discipline scheme.
- Expand first-use abbreviations and replace IO slang with standard physics wording or explicit definitions.
