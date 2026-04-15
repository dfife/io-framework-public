# Calculator Phase 5 Provenance Status Surface

Date: 2026-04-15

This release bundle is a narrow public slice of the calculator provenance and
theorem-surface layer.

It publishes:

- the theorem-dictionary source carrying the updated status labels
- the prerender-status renderer source used for the public calculator theorem
  pages
- the verification tests locking the theorem dictionary and public-site surface
- the Phase 5 audit and scoped-pipeline theorem memo in `reports/calculator_phase5/`

## Scope

This is not a new cosmology-source release.

It is a provenance-and-surface publication for the approved status labeling:

- map-level carrier, metric, projector, and LOS formulas:
  `derived / scoped as maps`
- full composed closed-scalar pipeline:
  `conditional / scoped`
- no silent one-slot collapse on the hierarchy-wide perturbation `R` slot

## Verification

The live calculator verification at publication time was:

```bash
python -m pytest tests -q
```

Expected result at publication time:

```text
85 passed
```

The public theorem surface was regenerated with:

```bash
python build_bundle.py
```

This release bundle itself is a curated source/report slice, not a standalone
calculator checkout.
