#!/usr/bin/env python3
"""Search the handbook catalog by extension or format name."""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalogs" / "master-catalog.csv"

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/find_extension.py <extension-or-name>")
        raise SystemExit(2)

    query = sys.argv[1].lower().lstrip(".")
    matches = []

    with CATALOG.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if query in row["extension"].lower() or query in row["name"].lower():
                matches.append(row)

    if not matches:
        print(f"No match found for: {query}")
        return

    for row in matches:
        print(f"\n.{row['extension']} — {row['name']}")
        print(f"Domain:         {row['domain']}")
        print(f"Representation: {row['representation']}")
        print(f"Purpose:        {row['purpose']}")
        print(f"Typical use:    {row['typical_use']}")
        print(f"Notes:          {row['notes']}")

if __name__ == "__main__":
    main()
