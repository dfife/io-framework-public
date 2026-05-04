# External Dependencies

The public Paper 21 v1.7 bundle uses Python standard-library modules only.

PRyMordial is not redistributed in this repository. Paper 21's corrected BBN
abundance values are frozen from the private-lab PRyMordial correction audit;
the public scripts validate:

- the YPCMB wrapper convention (`PRyMresults()[3]`),
- the IO Framework Conventions v2.0 observational denominators,
- the scorecard pulls and chi-square,
- the puncture-load and AC1 arithmetic.

The convention reference is:

```text
https://dfife.github.io/data/conventions_v2.md
```

No external observational dataset is redistributed in this bundle.
