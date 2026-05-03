# External Dependencies

## Python

The scripts were run with Python 3.12 in the private lab. They should be
compatible with current Python 3 versions that support dataclasses and pathlib.

Install lightweight dependencies with:

```bash
python3 -m pip install -r environment/requirements.txt
```

## PRyMordial

PRyMordial is not included in this repository.

To rerun the full BBN scorecard:

1. Obtain PRyMordial separately.
2. Set:

```bash
export PRYM_ROOT=/path/to/PRyMordial
```

3. Run:

```bash
python3 scripts/03_run_final_bbn_scorecard.py
```

The public bundle includes frozen PRyMordial outputs so the Paper 24 v2.2
numeric chain can be audited without vendoring PRyMordial.

## Convention References

For future papers:

```text
https://dfife.github.io/data/conventions_v2.md
```

For backward compatibility with already-published May 2026 correction papers:

```text
https://dfife.github.io/data/observational_conventions_v1.md
```
