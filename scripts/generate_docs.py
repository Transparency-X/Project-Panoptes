#!/usr/bin/env python3
"""Generate docs/index.md from data/groups/*.json."""
import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "groups")
DOCS_INDEX = os.path.join(os.path.dirname(__file__), "..", "docs", "index.md")

def load_groups():
    groups = []
    for fname in sorted(os.listdir(DATA_DIR)):
        if fname.endswith(".json"):
            with open(os.path.join(DATA_DIR, fname), "r", encoding="utf-8") as f:
                groups.append(json.load(f))
    return groups

def main():
    groups = load_groups()
    lines = [
        "# Surveillance Cult Group Index\n",
        "| ID | Name | Active Status | Pillars | Last Updated |",
        "|----|------|---------------|---------|--------------|"
    ]
    for g in groups:
        pillars = ", ".join(p["pillar"] for p in g.get("surveillance_pillars", []))
        last = g.get("last_updated", "unknown")
        lines.append(f"| {g['id']} | {g['name']} | {g['active_status']} | {pillars} | {last} |")
    with open(DOCS_INDEX, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Index written to {DOCS_INDEX}")

if __name__ == "__main__":
    main()
