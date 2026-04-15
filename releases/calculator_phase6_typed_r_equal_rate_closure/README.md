# Calculator Phase 6 Typed R Equal-rate Closure

Date: 2026-04-15

This release bundle is a narrow public slice of the typed-`R` closure accepted
by Cosmo on the equal-rate scoped branch.

It publishes:

- the theorem-dictionary source carrying the accepted equal-rate wording
- the typed-`R` hierarchy source, typed Thomson-history realization source, and
  scalar acoustic generator source
- the calculator regression tests locking the typed-`R` and typed-Thomson code
  path
- the typed-`R` operator theorem, the site-uniqueness theorem, the typed
  Thomson split-history audit, and the complete-chain theorem memo

## Scope

This is not a claim of a fully validated TT spectrum.

It publishes the accepted closure:

- full typed `R` hierarchy operator: `derived / scoped as maps`
- uniqueness of the site-wise typed `R` placements: `derived / scoped`
- typed Thomson-history realization in the live implementation:
  `derived / scoped as maps`

Accepted branch:

- equal-rate scoped branch
  `thomson_hierarchy_rate = thomson_drag_rate`

## Verification

Local calculator verification at publication time:

```bash
cd /opt/cosmology-lab/calculator
PYTHONPATH=src python -m pytest tests -q
python build_bundle.py
```

Expected result at publication time:

```text
101 passed
```

The public theorem surface was regenerated from the same bundle before
publication.
