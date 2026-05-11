# Paper 23 v2.0 Script Inventory Report

## Existing Private Scripts Reviewed

The private Paper 23 results folder contains many scripts from the exploratory
development history. The following live or near-live surfaces were reviewed for
bundle inclusion:

- `paper23_scalar_perturbations_analysis.py`
- `paper23_bridge_uniqueness_analysis.py`
- `paper23_boundary_initial_conditions_analysis.py`
- `paper23_tangent_readout_hopf_analysis.py`
- `paper23_two_closing_lemmas_analysis.py`
- `paper23_tensor_perturbations_analysis.py`

Other private scripts document killed routes or intermediate investigations and
were not included as executable public artifacts because the appendix is not a
historical archive and the bundle should reproduce live numbers/theorems only.

## Public Bundle Decision

The public bundle uses compact, documented, standard-library scripts rather than
copying every exploratory script. This keeps the public artifact referee-facing:
each script has a narrow input/output contract, clear claim status, and one
frozen JSON output.

## Manuscript Findings

- Active Paper 23 spectral-index result is not R4-dependent.
- Stale CMB-temperature prediction wording remains and should be removed.
- Stale inherited Paper 22 values remain and should be replaced or removed.
- Noncanonical labels remain and should be migrated.
- Abbreviations and IO-local terms need expansion for non-IO readers.

