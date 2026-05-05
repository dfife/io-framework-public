#!/usr/bin/env python3
from __future__ import annotations


"""Summarize the killed R4 derivation routes for Paper 17 v1.5.

The bundle does not mirror every private failed-route script. Instead, this
registry preserves the public conclusion needed for claim discipline: under the
current Paper 17 modular-projection stack, R4 is a continuous readout field and
is not internally forced to 1.

Usage:
    python3 scripts/07_r4_no_go_registry.py

Output:
    results/r4_no_go_registry_results.json
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results' / 'r4_no_go_registry_results.json'

ROUTES = [
    ('continuous field redefinition', 'A c-family t=c*lambda preserves non-R4 modular structure.'),
    ('BW/Hawking modular normalization', 'Accepted BW/Hawking theorems fix wedge/temperature normalization, not IO optical R4.'),
    ('canonical symplectic pairing', 'Moment-map scale remains free without compact-cycle quantization.'),
    ('boundary variational principle', 'Action scale can be rescaled without breaking stated symmetries.'),
    ('typed optical functor', 'Natural transformations can rescale the optical functor by zeta.'),
    ('A-vacuum modular state rescaling', 'Rescaled modular-flow embeddings preserve local KMS structure.'),
    ('lower-level Hamiltonian route', 'Hamiltonian normalization does not fix conformal-depth readout width.'),
    ('unit-cell preservation', 'The argument assumes the missing cell width instead of deriving it.'),
    ('external Gemini no-go', 'Continuous scale invariance remains unless a covering symmetry or compact integrality condition is added.'),
]


def main() -> None:
    payload = {
        'claim_status': 'DERIVED no-go boundary for internal R4=1 derivation on current stack',
        'r4_internally_derived': False,
        'r4_visible_in_v15': True,
        'r4_fixed_by': 'FIRAS uniqueness theorem, not internal Plan A derivation',
        'routes': [{'route': r, 'failure_reason': why, 'status': 'killed_or_not_closed'} for r, why in ROUTES],
        'safe_statement': 'Paper 17 v1.5 proves uniqueness of R4 given FIRAS inside the readout family; it does not derive R4=1 from operator algebra alone.',
    }
    OUT.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
