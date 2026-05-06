# IO Framework Public Repository

This repository is the curated public release surface for data, reports, scripts,
and reproducible artifacts created by, for, or from the Interior Observer (IO)
framework.

It is distinct from:

- the public website repository
- the private research workspace

The intended separation is:

- website: public presentation and navigation
- this repo: public evidence and reproducibility
- private lab: active exploration, scratch work, failed routes, and internal state

## Scope

This repository should contain only material that is ready for public review:

- release-quality reports
- scripts that reproduce public claims
- compact data products used by those scripts
- figures used in public reports
- provenance and manifest files

This repository should not be a raw mirror of the private lab.

## Layout

- `papers/`: paper-versioned reproducibility bundles
- `docs/`: landing pages and narrative guides
- `reports/`: frozen report files organized by paper
- `scripts/`: reproducible scripts organized by paper
- `data/`: public data products organized by paper
- `figures/`: rendered figures used by public reports
- `metadata/`: manifests, provenance, and environment notes
- `releases/`: optional release bundles and notes

## Claim Discipline

When public material is added here, claims must follow the active IO Framework
labeling convention. The full reference is:

- `docs/conventions_v2.md`
- canonical live URL: `https://dfife.github.io/data/conventions_v2.md`

Core labels:

- `DERIVED/THEOREM`: mathematically proved from stated assumptions,
  definitions, and previously banked derived results.
- `DERIVED/SCOPED`: theorem-grade only on the explicitly stated domain,
  observable class, branch, or reduced sector.
- `DERIVED/NO-GO`: theorem-grade exclusion of a route or class.
- `VERIFIED`: computationally or documentarily reproduced for the stated
  scope; verification is not derivation.
- `CONDITIONAL`: depends on a surfaced premise, bridge, class-membership
  statement, empirical datum, or extension package.
- `CONDITIONAL_VERIFIED`: a conditional theorem or theorem chain whose
  conditions are explicit and whose dependency path has been verified back to
  Premise 1 and/or Premise 2. This is load-bearing only within the declared
  condition package; it is not an unconditional theorem and it cannot hide a
  fitted parameter.
- `DERIVED/CONDITIONAL on [premise]`: local derivation is complete, but the
  result inherits a named conditional premise.
- `RECONSTRUCTION`: coherent explanatory model or zero-parameter construction
  not yet forced by theorem.
- `SPECULATIVE`: idea worth exploring, not yet established.
- `SUPERSEDED` or `Historical/SUPERSEDED`: inherited material whose framing or
  active status has been retired by a later correction.

Numerical agreement is not derivation. A conditional result may remain
compatible with the zero-fitted-parameters discipline only when the condition is
visible, the chain is reproducible, and no value is retuned against downstream
observables.

## Current Public Bundles

Paper-versioned bundles use this layout:

```text
papers/paperNN/vX.Y/
```

Each versioned folder should contain its own `README.md`, `MANIFEST.md`,
`VERSION.md`, scripts, frozen outputs, and citation metadata. This keeps
support files synchronized to the paper version and avoids mixing active
research state with public reproduction artifacts.

The current Paper 32 support bundle is:

- `papers/paper32/v1.6/`
- validation command:
  `python3 papers/paper32/v1.6/scripts/10_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper32_v1_6_repro_bundle.json`

The current Paper 34 support bundle is:

- `papers/paper34/v1.2/`
- validation command:
  `python3 papers/paper34/v1.2/scripts/05_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper34_v1_2_repro_bundle.json`

The current Paper 35 support bundle is:

- `papers/paper35/v1.2/`
- validation command:
  `python3 papers/paper35/v1.2/scripts/10_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper35_v1_2_repro_bundle.json`

The current Paper 21 support bundle is:

- `papers/paper21/v1.7/`
- validation command:
  `python3 papers/paper21/v1.7/scripts/07_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper21_v1_7_repro_bundle.json`

The current Paper 17 support bundle is:

- `papers/paper17/v1.5/`
- validation command:
  `python3 papers/paper17/v1.5/scripts/09_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper17_v1_5_repro_bundle.json`

The current Paper 22 support bundle is:

- `papers/paper22/v1.6/`
- validation command:
  `python3 papers/paper22/v1.6/scripts/07_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper22_v1_6_repro_bundle.json`

The current Paper 25 support bundle is:

- `papers/paper25/v1.3/`
- validation command:
  `python3 papers/paper25/v1.3/scripts/07_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper25_v1_3_repro_bundle.json`

The current Paper 26 support bundle is:

- `papers/paper26/v1.2/`
- validation command:
  `python3 papers/paper26/v1.2/scripts/07_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper26_v1_2_repro_bundle.json`

The current Paper 24 support bundle is:

- `papers/paper24/v2.3/`
- validation command:
  `python3 papers/paper24/v2.3/scripts/04_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper24_v2_3_repro_bundle.json`

The Paper 24 v2.2 bundle remains frozen at `papers/paper24/v2.2/` for
backward compatibility.

The initial bundle included here is a Paper 31 practical calculator bundle:

- fixed practical IO `C_l` confrontation
- practical baryon-slot audit

The current perturbation-foundation release is:

- `releases/calculator_phase3_foundation/`
- audit memo:
  `reports/calculator_phase3/calculator_phase3_foundation_audit.md`

The current source/readout-foundation release is:

- `releases/calculator_phase4_source_readout_foundation/`
- audit memo:
  `reports/calculator_phase4/calculator_phase4_source_readout_foundation_audit.md`

The manifest is in:

- `metadata/manifests/paper24_v2_3_repro_bundle.json`
- `metadata/manifests/paper32_v1_6_repro_bundle.json`
- `metadata/manifests/paper32_v1_5_repro_bundle.json`
- `metadata/manifests/paper34_v1_2_repro_bundle.json`
- `metadata/manifests/paper34_v1_1_repro_bundle.json`
- `metadata/manifests/paper35_v1_1_repro_bundle.json`
- `metadata/manifests/paper17_v1_5_repro_bundle.json`
- `metadata/manifests/paper21_v1_7_repro_bundle.json`
- `metadata/manifests/paper22_v1_6_repro_bundle.json`
- `metadata/manifests/paper25_v1_3_repro_bundle.json`
- `metadata/manifests/paper26_v1_2_repro_bundle.json`
- `metadata/manifests/paper24_v2_2_repro_bundle.json`
- `metadata/manifests/paper31_practical_bundle.json`
- `metadata/manifests/calculator_phase3_foundation_bundle.json`
- `metadata/manifests/calculator_phase4_source_readout_foundation_bundle.json`

Legacy top-level `data/`, `scripts/`, `reports/`, and `releases/` folders
remain in place because earlier public bundles and manifests reference them.
New paper-specific work should prefer `papers/paperNN/vX.Y/`.

## Release Tags and Checksums

Paper-versioned reproducibility bundles should be archived with immutable git
tags and GitHub Releases in addition to their branch paths.

The standard tag format is:

```text
paper{N}-v{X.Y}
```

Examples:

```text
paper24-v2.3
paper24-v2.2
```

For each new paper-version bundle:

1. Add or update the versioned folder under `papers/paperNN/vX.Y/`.
2. Add or update the corresponding manifest under `metadata/manifests/`.
3. Commit the public bundle state.
4. Create an annotated tag using the standard tag format.
5. Push the tag and create a GitHub Release from it.
6. Record the GitHub source tarball SHA256 checksum in release notes or in a
   companion checksum file.

The branch URL remains useful for readers:

```text
https://github.com/dfife/io-framework-public/tree/main/papers/paper24/v2.3
```

The release tag is the immutable archival reference:

```text
https://github.com/dfife/io-framework-public/releases/tag/paper24-v2.3
```

This convention applies prospectively to future paper versions. Existing public
bundles may be back-tagged when their establishing commit is identifiable.

## Publishing Workflow

1. Produce or update a result in the private lab.
2. Decide whether it is public-ready.
3. Add it to a manifest.
4. Synchronize the selected files into this repository.
5. Review and commit only the curated public artifacts.

A simple sync helper is provided in:

- `scripts/sync_from_lab.py`

## Remote

The intended public remote is:

- `git@github.com:dfife/io-framework-public.git`

If the remote does not yet exist, create the empty GitHub repository first and
then push this local repository.
