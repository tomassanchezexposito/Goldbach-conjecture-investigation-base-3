# Reflected prime pairs — reproducibility supplement

The publication candidate is the English PDF. The Spanish PDF is a parallel reading version, not a second SSRN submission. The manuscript's AI disclosure belongs in the SSRN abstract field as well as in the PDF. The author should check the derivations and verify the record before submission, especially T73.5 and T74.3; none of the three inherited analytical items is presented as independently certified. No submission has been made.

## Rebuild the PDFs

From this directory, run `pdflatex Goldbach_EN.tex` twice and `pdflatex Goldbach_ES.tex` twice. Both wrappers use `paper.tex`. The TeX installation needs Latin Modern, AMS packages, and Babel Spanish.

## Reproduce the arithmetic

Run `python3 goldbach_reflected_audit.py 7930 > rerun.json` and compare it with `audit.json`. Use ordinary Python (not `python -O`); the consistency checks are assertions. All arithmetic is exact and uses the standard library. `selected` fields, in order: raw wheel survivors, genuine distinct-prime pairs, wheel false positives, genuine pairs omitted by the wheel. The three exact algorithms compare each target's smaller-endpoint set, not merely aggregate counts. The two zero counts of distinct pairs are at 4 and 6, where the prime diagonal is available.

Optional cross-check against the earlier published table: run `python3 check_printed_prefix.py "path/to/ssrn-5705571.pdf"`. This requires Poppler's `pdftotext`. It compares the full 1000-integer printed table with the additive generator and does not rerun Lean.

The finite results are a comparison within the earlier verified range, not a competitive benchmark or a universal proof. The supplied routines were not optimized. The established classical context is cited in the paper, including the standard Goldbach sieve on k(N-k). The internal Stage 76 snapshot is accounted for by the audit provenance; the supplementary files contain no repository credentials or private links.

## Version 1.2 additions

```sh
c++ -std=c++17 -O3 -Wall -Wextra -pedantic distinct_witness_audit.cpp -o witness
./witness 8000000 > witness-rerun.txt
diff -u witness_8000000.txt witness-rerun.txt
python3 antidiagonal_audit.py > antidiagonal-rerun.txt
diff -u antidiagonal_audit.txt antidiagonal-rerun.txt
sha256sum -c SHA256SUMS
```

The C++ audit compares independently constructed Eratosthenes and Euler least-prime-factor tables and checks the least witness at every even target. It certifies existence on a finite interval, not representation counts there. The Python antidiagonal audit uses trial division and was cross-checked independently with SymPy. These checks do not establish any analytic implication.

The sparse real-zero argument is a conditional restriction from Bhowmik–Grimmelt's exceptional-zero formula and Brun–Titchmarsh. The uncut two-sided premise must not be identified with the fixed smooth Type II estimate. The residual density is a logical/domain observation, not a complexity comparison or a claim that every possible proof requires Type II estimates. The exponent 7/10 is attributed to the checked Zhao preprint revision, not declared the definitive record. No independent mathematical review of the new analytic exposition, priority claim or universal proof is implied.
