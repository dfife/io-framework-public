"""Checks that the public website receives the bundle and prerendered theorem HTML."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


CALCULATOR_ROOT = Path("/opt/cosmology-lab/calculator")
PUBLIC_BUNDLE = Path("/opt/cosmology-lab/tmp/dfife.github.io/data/aio_calculator_bundle.json")
PUBLIC_HTML = Path("/opt/cosmology-lab/tmp/dfife.github.io/calculator.html")
PUBLIC_THEOREMS_HTML = Path("/opt/cosmology-lab/tmp/dfife.github.io/calculator-theorems.html")
PUBLIC_JS = Path("/opt/cosmology-lab/tmp/dfife.github.io/assets/js/calculator.js")


def test_build_bundle_exports_public_site_copy() -> None:
    """`build_bundle.py` should refresh the public-site copy of the bundle."""

    subprocess.run(
        [sys.executable, "build_bundle.py"],
        cwd=CALCULATOR_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(PUBLIC_BUNDLE.read_text(encoding="utf-8"))
    assert "theta_star_theorem" in payload["explained_outputs"]
    assert payload["explained_outputs"]["theta_star_theorem"]["provenance"]["root_node"] == (
        "paper37.active_branch_theta_star"
    )


def test_public_site_prerenders_calculator_and_theorem_pages() -> None:
    """The public site should contain theorem content directly in HTML source."""

    html = PUBLIC_HTML.read_text(encoding="utf-8")
    theorems_html = PUBLIC_THEOREMS_HTML.read_text(encoding="utf-8")
    js = PUBLIC_JS.read_text(encoding="utf-8")

    assert 'id="calculator-card-stack"' in html
    assert 'data-prerendered="true"' in html
    assert "calculator-theorems.html" in html
    assert "Loading theorem surface" not in html
    assert "Phase-equivalent Selector Theorem" in html
    assert "Packet Coefficient Fixing Theorem" in html
    assert "Why this differs from Planck" in html
    assert "Direct observable" in html
    assert "Proof outline" in html
    assert "Scope boundary" in html
    assert 'id="theorem-dictionary-stack"' in theorems_html
    assert 'data-prerendered="true"' in theorems_html
    assert "Loading theorem dictionary" not in theorems_html
    assert "Calculator Theorem Dictionary" in theorems_html
    assert "Statement" in theorems_html
    assert "Premises" in theorems_html
    assert "Proof outline" in theorems_html
    assert "Supporting references" in theorems_html
    assert "Scoped Closed-scalar Pipeline Theorem" in theorems_html
    assert "conditional / scoped" in theorems_html
    assert "derived / scoped as maps" in theorems_html
    assert "No silent one-slot collapse on the hierarchy-wide perturbation" in theorems_html
    assert "fetch(bundlePath)" not in js
    assert "data-prerendered='true'" in js
    assert "hashchange" in js
