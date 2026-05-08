# Manifest

This bundle contains:

- `README.md`: overview and quickstart.
- `VERSION.md`: version metadata.
- `CITATION.cff`: machine-readable citation metadata.
- `LICENSE`: license file.
- `CONSTRUCTION_SUMMARY.md`: script and output summary.
- `INVENTORY_REPORT.md`: inclusion/exclusion report.
- `data/`: imported constants and external-data instructions.
- `environment/`: reproducibility environment notes.
- `scripts/`: numbered reproduction and validation scripts.
- `results/`: frozen JSON outputs.
- `reports/`: R4/kappa audit and abbreviation/slang audit reports.
- `SHA256SUMS.txt`: generated checksums for bundle files.

Generate or verify checksums from this directory:

```bash
sha256sum $(find . -type f | sort) > SHA256SUMS.txt
sha256sum -c SHA256SUMS.txt
```
