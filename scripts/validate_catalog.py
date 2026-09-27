#!/usr/bin/env python3
"""Validate catalog structure and duplicate extensions."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalogs" / "master-catalog.csv"

REQUIRED = {
    "extension", "name", "representation", "domain",
    "purpose", "typical_use", "notes"
}

def main():
    with CATALOG.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        headers = set(reader.fieldnames or [])
        missing = REQUIRED - headers

        if missing:
            raise SystemExit(f"Missing columns: {sorted(missing)}")

        rows = list(reader)

    extensions = [r["extension"].strip().lower() for r in rows]
    duplicates = sorted({x for x in extensions if extensions.count(x) > 1})

    empty_rows = [
        i + 2 for i, row in enumerate(rows)
        if any(not value.strip() for value in row.values())
    ]

    print(f"Rows: {len(rows)}")
    print(f"Unique extensions: {len(set(extensions))}")

    if duplicates:
        raise SystemExit(f"Duplicate extensions: {duplicates}")

    if empty_rows:
        raise SystemExit(f"Rows with empty fields: {empty_rows}")

    print("Catalog validation: PASS")

if __name__ == "__main__":
    main()
