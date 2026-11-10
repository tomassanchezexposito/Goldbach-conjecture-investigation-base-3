#!/usr/bin/env python3
"""Focused exact Stage 69 regression for the inherited false SDP-lift example.

All arithmetic is symbolic. The all-parameter optimization proofs belong to
00_erratum_psd_lifting.md, not to finite/symbolic test output.
"""
from pathlib import Path
import json
import sympy as s


def sym_eq(a, b):
    return s.simplify(a - b) == 0


def main():
    one = s.Integer(1)
    half = s.Rational(1, 2)
    two = s.eye(2)
    projectors_old = [
        s.diag(one, 0),
        s.diag(0, one),
    ]
    # This is the REAL lift optimum; NOT the triangle bound 2.
    old_rank1 = s.sqrt(2)
    old_psd = s.sqrt(half) + s.sqrt(half)
    old_triangle = s.Integer(2)
    assert sym_eq(old_rank1, old_psd)
    assert not sym_eq(old_psd, old_triangle)

    sigmas = [
        s.Matrix([[0, 1], [1, 0]]),
        s.Matrix([[0, -s.I], [s.I, 0]]),
        s.Matrix([[1, 0], [0, -1]]),
    ]
    six = [(two + eps*sig)/2 for sig in sigmas for eps in (1, -1)]
    for p in six:
        assert p == p.conjugate().T
        assert (p*p-p).applyfunc(s.simplify) == s.zeros(2)
        assert s.simplify(p.trace()) == 1
        assert s.simplify(p.det()) == 0

    x_mix = two/2
    mixed_value = sum(s.sqrt(s.trace(p*x_mix)) for p in six)
    assert sym_eq(mixed_value, 3*s.sqrt(2))

    # Exact pure state with Bloch vector (1,1,1)/sqrt(3).
    t = 1/s.sqrt(3)
    z = s.Matrix([
        s.sqrt((1+t)/2),
        (1+s.I)/s.sqrt(2)*s.sqrt((1-t)/2)
    ])
    assert sym_eq((z.conjugate().T*z)[0], 1)
    for sig in sigmas:
        assert sym_eq((z.conjugate().T*sig*z)[0], t)

    pure_candidate = sum(s.sqrt(s.simplify((z.conjugate().T*p*z)[0]))
                         for p in six)
    pure_optimum = 3*s.sqrt(1+s.sqrt(s.Rational(2, 3)))
    # Equality of positive quantities can be checked by squares exactly.
    assert sym_eq(pure_candidate**2, pure_optimum**2)
    assert s.simplify(3*s.sqrt(2)-pure_optimum).is_positive is True

    output = {
        "evidence_type": "exact symbolic focused regression; proofs in Markdown",
        "original_two_projector_example": {
            "rank_one_optimum": str(old_rank1),
            "psd_lifted_optimum": str(s.simplify(old_psd)),
            "triangle_upper_bound": str(old_triangle),
            "strict_psd_gap": False,
            "strict_triangle_gap": True
        },
        "six_pauli_projectors": {
            "all_projectors_rank_one_psd": True,
            "mixed_psd_optimum": str(3*s.sqrt(2)),
            "pure_rank_one_optimum": str(pure_optimum),
            "strict_gap": True,
            "pure_extremizer_bloch": ["1/sqrt(3)"]*3
        },
        "scope": "abstract Hermitian matrices, not true-prime arc Gram inputs",
        "status": "PASS"
    }
    out = Path(__file__).with_name("psd_lifting_exact_results.json")
    out.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print("PASS: original lifted optimum is sqrt(2), not 2")
    print("PASS: six Pauli projector family has a genuinely strict lift gap")
    print(out)


if __name__ == "__main__":
    main()
