# Paper Reproducibility Bundles

This directory contains version-locked support bundles for individual IO
Framework papers.

Each bundle is organized as:

```text
paperNN/
  vX.Y/
    README.md
    MANIFEST.md
    VERSION.md
    CITATION.cff
    environment/
    scripts/
    data/
    results/
    reports/
```

The version folder must match the paper version it supports. If a paper is
updated, create a new sibling version folder rather than mutating the old one.
