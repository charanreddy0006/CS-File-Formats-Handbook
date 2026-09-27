#!/usr/bin/env python3
"""Display simple handbook statistics."""

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalogs" / "master-catalog.csv"

def main():
    with CATALOG.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    domains = Counter(row["domain"] for row in rows)
    representations = Counter(row["representation"] for row in rows)

    print("\nCS File Formats Handbook Statistics")
    print("=" * 42)
    print(f"Catalog entries: {len(rows)}")

    print("\nBy domain:")
    for key, value in domains.most_common():
        print(f"  {key:24} {value}")

    print("\nBy representation:")
    for key, value in representations.most_common():
        print(f"  {key:24} {value}")

if __name__ == "__main__":
    main()
