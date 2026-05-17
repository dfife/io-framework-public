# Paper 28 v2.0 Reproducibility Bundle

Paper 28 v2.0, **The Primordial Spectral Index**, is bundled here as a
theorem-support and validation package for the active spectral-index/DtN chain
and homogeneous Oppenheimer-Snyder JWST formation-clock map.

At bundle build time, `Interior_Observer_Paper28_v2_0.docx` was not present in
`Full Papers`; this bundle was reconciled against the available Paper 28
working draft and support artifacts under `/opt/cosmology-lab/results/paper28`.

## Quickstart

```bash
git clone https://github.com/dfife/io-framework-public.git
cd io-framework-public/papers/paper28/v2.0
python3 scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
PASS Paper 28 v2.0 validation: total checks=13, pass count=13, fail count=0
```

## What This Bundle Reproduces

- Primitive line-scale root uniqueness, `q = 1/2`.
- One-form trace-log Gaussian extension pivot values.
- Coexact Dirichlet-to-Neumann Hessian spectral-index pivot values.
- Lower-order DtN remainder bounds and flat-collar `O(1)` deformation
  exclusion.
- Homogeneous Oppenheimer-Snyder JWST formation-clock map.
- R4/FIRAS damage and hidden-parameter audit disposition.

## Claim Boundary

Paper 28 v2.0 does not claim an independent CMB-temperature prediction. The
framework value `R4_FIRAS = 1.0031014644` is recorded as an imported boundary
constant from Paper 17 v1.5, but no active Paper 28 script uses `R4 = 1`.

The spectral-index chain remains conditional at the physical-identification
layer: the A-vacuum canonical extension and full IO Hessian identification must
remain visible as scoped conditions.

## Dependencies

Only Python 3.11+ and the standard library are required.

## Citation

If using this bundle, cite the Paper 28 v2.0 Zenodo record and the GitHub
release tag `paper28-v2.0`.
