"""Count correct pairs per run and EAN group. Standard library only: python3 score.py"""

import csv
from collections import Counter
from pathlib import Path

GROUPS = ["different_ean", "no_ean_on_one_side"]

totals = Counter()
print(f"{'run':<8} {'group':<20} correct / checked")
for path in sorted(Path("data").glob("*-pairs.csv")):
    run = path.stem.removesuffix("-pairs")
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    for group in GROUPS:
        labels = [r["label"] for r in rows if r["group"] == group]
        correct = labels.count("correct")
        totals["correct"] += correct
        totals["checked"] += len(labels)
        print(f"{run:<8} {group:<20} {correct} / {len(labels)}")
print(f"{'all':<8} {'without shared EAN':<20} {totals['correct']} / {totals['checked']}")
