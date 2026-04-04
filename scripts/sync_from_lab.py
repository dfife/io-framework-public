#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    if len(sys.argv) != 2:
        print("usage: sync_from_lab.py <manifest.json>")
        return 1

    manifest_path = Path(sys.argv[1]).resolve()
    manifest = json.loads(manifest_path.read_text())

    for artifact in manifest.get("artifacts", []):
        source = Path(artifact["source"])
        destination = repo_root / artifact["destination"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not source.exists():
            print(f"missing: {source}")
            continue
        shutil.copy2(source, destination)
        print(f"copied {source} -> {destination}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

