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

When public material is added here, claims should follow the same labeling used
in the lab:

- `derived`
- `verified`
- `conditional`
- `reconstruction`
- `speculative`

Numerical agreement is not derivation. Public artifacts should preserve enough
detail for independent rerun and review.

## Current Public Bundles

Paper-versioned bundles use this layout:

```text
papers/paperNN/vX.Y/
```

Each versioned folder should contain its own `README.md`, `MANIFEST.md`,
`VERSION.md`, scripts, frozen outputs, and citation metadata. This keeps
support files synchronized to the paper version and avoids mixing active
research state with public reproduction artifacts.

The current Paper 34 support bundle is:

- `papers/paper34/v1.1/`
- validation command:
  `python3 papers/paper34/v1.1/scripts/04_validate_expected_outputs.py`
- manifest:
  `metadata/manifests/paper34_v1_1_repro_bundle.json`

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
- `metadata/manifests/paper34_v1_1_repro_bundle.json`
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
