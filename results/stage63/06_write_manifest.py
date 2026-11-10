#!/usr/bin/env python3
"""Create the deterministic SHA-256 and parameter manifest for Stage 63."""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/stage63/06_manifest.json"
EXCLUDED = {OUT}
INPUTS = [
    ROOT / "docs/research_statement.md",
    ROOT / "docs/research_protocol.md",
    ROOT / "tasks/STAGE63_EXTENDED_RESEARCH_PROGRAM.md",
    ROOT / "tasks/NEXT_TASK.md",
]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    files = sorted(p for p in (ROOT / "results/stage63").rglob("*")
                   if p.is_file() and p not in EXCLUDED)
    files += [p for p in INPUTS if p.is_file()]
    files = sorted(set(files))
    try:
        git_branch = subprocess.check_output(
            ["git", "branch", "--show-current"], cwd=ROOT, text=True
        ).strip()
        git_head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        git_branch = "unavailable"
        git_head = "unavailable"

    payload = {
        "purpose": "Reproducibility and provenance manifest for Stage 63 M0-M6",
        "hash_algorithm": "SHA-256",
        "manifest_self_hash": "omitted to avoid self-reference",
        "branch_at_generation": git_branch,
        "head_at_generation": git_head,
        "software": {
            "python": platform.python_version(),
            "sage_math": "10.9 (checked with sage --version; M6 audit uses Python only)",
            "operating_system": platform.platform(),
        },
        "parameters": {
            "residual_definition": "Even N >= 4 with composite N-1 and composite N/2",
            "distinct_pair_definition": "Unordered prime pairs p<q with p+q=N",
            "finite_independent_audit_limit": 1000,
            "wheel_modulus": 210,
            "fourier_test_targets_count": 42,
            "fourier_exact_dft_modulus": "L=2N+1",
            "shared_prime_moduli_tested": [210, 330],
            "energy_test_arithmetic": "Python fractions / exact integers",
            "finite_primality_methods": ["Eratosthenes sieve", "trial division"],
        },
        "commands": [
            "python3 -B results/stage63/01_verify_modular.py",
            "python3 -B results/stage63/02_verify_fourier.py",
            "python3 -B results/stage63/03_verify_energy_countermodels.py",
            "python3 -B results/stage63/05_countermodels.py",
            "python3 -B results/stage63/06_final_audit.py",
            "python3 -B -m unittest discover -s tests -v",
            "git diff --check",
        ],
        "files": [
            {"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size, "sha256": digest(p)}
            for p in files
        ],
        "scientific_status": {
            "universal_residual_coverage": "OPEN",
            "goldbach_proof_claimed": False,
            "finite_audit_is_universal_evidence": False,
        },
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} with {len(files)} hashed files")


if __name__ == "__main__":
    main()
