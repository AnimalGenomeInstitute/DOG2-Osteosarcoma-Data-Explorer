#!/usr/bin/env python3
"""Minimal crosswalk integrity checks using the Python standard library."""
from pathlib import Path
from collections import Counter
import csv

repo = Path(__file__).resolve().parents[1]

def load(filename):
    with (repo / "data" / filename).open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

summary = load("Case_Summary_303.csv")
expression = load("Case_Expression_303.csv")
a = [r["Case ID"] for r in summary]
b = [r["Case ID"] for r in expression]
assert len(a) == len(set(a)) == 303, "Summary must contain 303 unique dogs."
assert len(b) == len(set(b)) == 303, "Expression table must contain 303 unique dogs."
assert set(a) == set(b), "Case ID sets differ."

expected = {
    "AVAILABLE_OS_AND_DFS_DFI": 288,
    "PARTIAL_DFS_DFI_ONLY": 5,
    "MISSING_OS_AND_DFS_DFI": 10,
}
assert Counter(r["Clinical_Outcome_Status"] for r in summary) == expected
assert all(r["Study Code"] == next(e["Study"] for e in expression if e["Case ID"] == r["Case ID"]) for r in summary)
print("OK: 303 matched dogs, 2 datasets, and outcome-status counts verified.")
