# Calculator Phase 7 TT First-Peak Support

Date: 2026-04-16

This release bundle publishes the first IO-native CMB TT spectrum at the
approved scoped level.

Approved publication wording:

`Conditional/scoped/verified TT first-peak support on the repaired active-branch canonical carrier (n_max = 501), with inherited-FULL Stage-2 history and equal-rate typed Thomson specialization.`

This bundle publishes:

- the theorem-dictionary source carrying the approved TT wording
- the prerendered web-surface renderer used by the public calculator page
- the CLI surface for `python -m aio_calculator tt-spectrum --json`
- the TT driver source for the canonical repaired carrier
- the verification tests locking the TT provenance node, public-site bundle, and TT driver
- the first-peak theorem report, Cosmo memo, and canonical results JSON

## Scope

This is a scoped first-peak release only.

It publishes:

- the repaired active-branch canonical carrier at `n_max = 501`
- the verified result `ell_peak = 224`
- the verified ratio `C_220 / C_peak = 0.9938104102565932`
- the canonical inherited-FULL Stage-2 + equal-rate typed Thomson specialization wording used on the live calculator surface

It does not publish:

- a theorem-grade full high-`ell` TT closure
- a theorem-grade full `C_l` spectrum closure
- a universal off-branch TT theorem

The surviving open frontier is explicit and must remain explicit:

- `n_max >= 601` shell-ceiling drift remains open; on tested history carriers the peak drifts upward to `ell_peak = 260` to `277`

## Verification

The live calculator verification at publication time was:

```bash
python -m pytest tests -q
python build_bundle.py
PYTHONPATH=src python -m aio_calculator tt-spectrum --workers 12 --json
```

Expected result at publication time:

```text
114 passed
```

This release bundle is a curated source/report slice, not a standalone full
calculator checkout.
