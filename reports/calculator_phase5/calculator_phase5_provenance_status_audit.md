# Calculator Phase 5 Provenance Status Audit

Date: 2026-04-15

## Question

Before publication, the calculator provenance layer and public theorem surface
 were audited against the approved status-label standard:

1. carrier laws, metric formulas, projector formulas, and LOS formulas must be
   labeled `derived / scoped as maps`
2. the full composed end-to-end closed-scalar pipeline must be labeled
   `conditional / scoped`
3. the no-silent-collapse rule on the hierarchy-wide perturbation `R` slot must
   be explicit in the theorem dictionary and public surface

## Executive result

The audit passed.

- `derived / scoped as maps` now appears on the relevant theorem nodes for the
  metric-state builder, scalar acoustic generator, and scalar transfer
  projector.
- `conditional / scoped` now appears on the explicit composed theorem node
  `Scoped Closed-scalar Pipeline Theorem`.
- the no-silent-collapse rule on the hierarchy-wide perturbation `R` slot is
  stated explicitly in the typed baryon-slot theorem, the scalar acoustic
  generator theorem boundary, and the composed pipeline theorem.
- the prerendered public theorem page exposes these labels directly in HTML
  source.

## Updated theorem nodes

The following theorem-dictionary nodes carry the approved labels:

- `Closed Scalar Metric-state Builder Theorem`
  - status: `derived / scoped as maps`
- `Closed Scalar Acoustic Generator Theorem`
  - status: `derived / scoped as maps`
- `Closed Scalar Transfer Projector Theorem`
  - status: `derived / scoped as maps`
- `Scoped Closed-scalar Pipeline Theorem`
  - status: `conditional / scoped`

The following rule is now explicit in the theorem text:

- `Typed Baryon-slot Specification`:
  no silent one-slot collapse on `R` is licensed anywhere in the perturbation
  pipeline.

## Public-surface check

The prerendered theorem page now contains, in HTML source:

- `Scoped Closed-scalar Pipeline Theorem`
- `conditional / scoped`
- `derived / scoped as maps`
- the explicit no-`R`-collapse statement

This means the public calculator theorem surface reflects the approved claim
discipline without requiring JavaScript execution.

## Verification

Local calculator verification before publication:

- `python -m pytest tests/test_provenance.py tests/test_public_site_bundle.py -q`
  -> `11 passed`
- `python -m pytest tests -q`
  -> `85 passed`
- `python build_bundle.py`
  -> regenerated the live bundle plus prerendered
  `calculator.html` and `calculator-theorems.html`

## Claim boundary

This publication updates theorem labels and theorem-surface presentation.

It does not change the underlying physical closure boundary:

- map-level carrier and formula objects remain `derived / scoped as maps`
- the full composed scalar pipeline remains `conditional / scoped` because it
  inherits the conditional Stage-2 history builder
- no theorem-grade hierarchy-wide one-slot collapse on `R` is claimed
