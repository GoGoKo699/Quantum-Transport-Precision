#!/usr/bin/env python3
"""Run the finite scientific checks and verify committed data and navigation."""
from __future__ import annotations

import json
import math
from pathlib import Path
import re

from check_counting import run_checks as counting_checks
from check_filters import run_checks as filter_checks

ROOT = Path(__file__).resolve().parents[1]


def compare_number(actual, expected, label):
    if not math.isclose(actual, expected, rel_tol=2e-9, abs_tol=2e-11):
        raise AssertionError(f"Committed value differs: {label}: {actual} vs {expected}")


def compare_committed(filter_record, counting_record):
    stored_filters = json.loads((ROOT / "verification/data/filter_results.json").read_text())
    old = {r["N"]: r for r in stored_filters["quadrature"]}
    assert set(old) == {r["N"] for r in filter_record["quadrature"]}
    for row in filter_record["quadrature"]:
        for key in ("I0", "V0", "J", "D", "F", "Gamma_L", "Gamma_R",
                    "current_at_unit_contact_rate"):
            compare_number(row[key], old[row["N"]][key], f"N={row['N']} {key}")
    stored_counts = json.loads((ROOT / "verification/data/counting_results.json").read_text())
    old = {r["label"]: r for r in stored_counts["cases"]}
    assert set(old) == {r["label"] for r in counting_record["cases"]}
    for row in counting_record["cases"]:
        for method in ("lindblad", "scattering"):
            for key in ("J", "D", "F"):
                compare_number(row[method][key], old[row["label"]][method][key],
                               f"{row['label']} {method}.{key}")


def markdown_anchors(source):
    anchors = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', source))
    for line in source.splitlines():
        match = re.match(r"^#{1,6}\s+(.+)", line)
        if match:
            heading = re.sub(r"<[^>]+>", "", match.group(1)).lower()
            heading = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
            anchors.add(heading.replace(" ", "-"))
    return anchors


def check_documents():
    files = sorted(ROOT.rglob("*.md"))
    files = [p for p in files if ".venv" not in p.parts]
    checked_links = 0
    for path in files:
        source = path.read_text()
        assert len(re.findall(r"^# ", source, flags=re.MULTILINE)) == 1, path
        assert source.count("$" + "`") == source.count("`" + "$"), path
        assert source.count("\n```") % 2 == 0, path
        assert "@@" not in source, path
        for target in re.findall(r"!?(?:\[[^\]]*\])\(([^\s)]+)(?:\s+[^)]*)?\)", source):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            file_part, _, anchor = target.partition("#")
            destination = (path.parent / file_part).resolve() if file_part else path
            assert destination.exists(), f"{path}: missing {target}"
            if anchor and destination.suffix == ".md":
                assert anchor in markdown_anchors(destination.read_text()), (
                    f"{path}: missing anchor {target}")
            checked_links += 1
    return {"markdown_files": len(files), "relative_links_checked": checked_links}


def main():
    filters = filter_checks()
    counts = counting_checks()
    compare_committed(filters, counts)
    documents = check_documents()
    print(json.dumps({
        "scientific_checks_passed": True,
        "physical_synthesis_sizes": [x["N"] for x in filters["physical_chains"]],
        "quadrature_sizes": [x["N"] for x in filters["quadrature"]],
        "full_lindblad_cases": len(counts["cases"]),
        "maximum_transmission_error": filters["summary"]["maximum_transmission_absolute_error"],
        "maximum_counting_statistics_discrepancy": counts["maximum_statistics_discrepancy"],
        "committed_observables_reproduced": True,
        "documents": documents,
        "scope": "Finite numerical and source-structure checks; not a proof or a hosted-rendering inspection.",
    }, indent=2))


if __name__ == "__main__":
    main()

