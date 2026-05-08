# External Dependencies

The quick validator requires only Python 3 and the standard library.

Full heavyweight reruns require external packages and data that are not
redistributed in this public repository:

- PRyMordial for BBN network reruns.
- CLASS / classy for acoustic and matter-power calculations.
- CAMB for cross-checks.
- numpy, scipy, pandas, mpmath.
- BOSS DR12, Pantheon+, DESI, and Planck data products where relevant.

The frozen JSON files are included so reviewers can validate the manuscript
numbers without installing heavyweight cosmology stacks.
