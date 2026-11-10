#!/usr/bin/env python3
"""Create the Stage 61 reproducibility and SHA-256 provenance manifest."""

import hashlib
import json
import platform
from pathlib import Path


HERE = Path(__file__).resolve().parent
FILES = (
    "report.md",
    "summary.md",
    "compute_stage61.py",
    "verify_stage61.py",
    "stage61_exact_results.json",
    "stage61_verification.json",
    "make_manifest.py",
)


def main():
    hashes = {}
    for name in FILES:
        digest = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        hashes[name] = digest
    data = json.loads((HERE / "stage61_exact_results.json").read_text(encoding="utf-8"))
    manifest = {
        "stage": 61,
        "branch": "cocalc/stage61-signed-correlation-gap",
        "source_provenance": {
            "stage60_research_commit": "e33e4103ad97686be7f9c21cad2fe8636f2bb7e2",
            "stage61_branch_base_commit": "feb09da4b959594cbc699586e9fd42689731222a",
            "task_file": "tasks/NEXT_TASK.md",
            "issue_8_context": "docs/stage60_integration_handoff.md and results/stage60/integration_review.md",
        },
        "evidence_scope": "Focused finite checks and exact rational identities; not universal Goldbach coverage.",
        "environment": {
            "python": platform.python_version(),
            "dependencies": "Python standard library only",
            "integer_arithmetic": "unbounded Python integers",
            "rational_arithmetic": "fractions.Fraction exact arithmetic",
        },
        "observed_runtime_seconds": {
            "producer": 0.202,
            "independent_verifier": 0.195,
            "note": "Single measured shell runs; machine- and load-dependent.",
        },
        "algorithms": {
            "producer": "Sieve of Eratosthenes; product formula for A_210; direct prime-position pair classification.",
            "independent_verifier": "Trial division; direct enumeration of all 210 residue classes; set-intersection position classifier.",
        },
        "parameters": data["parameters"],
        "commands": [
            "python3 -B results/stage61/compute_stage61.py",
            "python3 -B results/stage61/verify_stage61.py",
            "python3 -B results/stage61/make_manifest.py",
        ],
        "verification_result": "All independent exact assertions passed.",
        "sha256": hashes,
        "manifest_hash_note": "This manifest lists hashes of all report, source, exact-output, verification-output, and manifest-generator files. It does not hash itself.",
    }
    (HERE / "verification_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"hashed_files": len(hashes),
                      "manifest": str(HERE / "verification_manifest.json")}, indent=2))


if __name__ == "__main__":
    main()
