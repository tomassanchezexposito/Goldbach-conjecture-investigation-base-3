#!/usr/bin/env python3
"""Write a reproducible SHA-256 and execution manifest for Stage 60."""

import hashlib
import json
import platform
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRACKED = [
    "compute_stage60.py",
    "verify_stage60.py",
    "make_manifest.py",
    "stage60_exact_results.json",
    "report.md",
    "integration_review.md",
    "summary.md",
]


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main():
    files = {name: sha256(HERE / name) for name in TRACKED}
    manifest = {
        "title": "Stage 60 reproducibility and verification manifest",
        "evidence_status": "Hashes identify the saved deliverables; finite computations verify only their stated domains.",
        "source_provenance": {
            "integration_base": "156c6acaa89825cd70dd3f3742bf98de8e90434c",
            "stage58_source": "689c3d696ce750610bed6ad69cdd476fdcaee464",
            "stage58_integration_commit": "d847c3a88d441d2332585c72b468498612ba190e",
            "stage59_local_source": "900cae804b76e09992aba555932bc0fd866737af",
            "stage59_sharp_merge_source": "60fed50ca43342bd10384a05813202c79c57eab3",
            "stage59_merge_commit": "4a4064734074357ef8ee5b34b9af857d1f14f4c4",
        },
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "dependencies": "Python standard library only",
        },
        "parameters": {
            "even_centers_inclusive": [8, 300],
            "step": 2,
            "wheel_modulus": 210,
            "exact_arithmetic": "Python integers and fractions.Fraction",
        },
        "reproduction_commands_from_repository_root": [
            "python3 results/stage60/compute_stage60.py",
            "python3 results/stage60/verify_stage60.py",
            "python3 results/stage60/make_manifest.py",
        ],
        "verification_outcomes": {
            "compute": "passed; 147 centers, 62 residual centers, 441 wheel target checks",
            "independent_verifier": "passed; trial division, direct modulo-210 enumeration, five-class product checks, 256 zero-center triples",
            "observed_runtime": "compute 0.236 s wall; verifier 0.244 s wall in the recorded run (shell time; hardware-dependent)",
            "universal_positivity": "not established",
        },
        "sha256": files,
        "manifest_excludes_its_own_hash": True,
    }
    target = HERE / "verification_manifest.json"
    target.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {target}")
    print(json.dumps(files, indent=2))


if __name__ == "__main__":
    main()
