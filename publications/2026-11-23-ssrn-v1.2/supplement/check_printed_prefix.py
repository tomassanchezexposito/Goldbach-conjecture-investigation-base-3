"""Compare Appendix B of SSRN 5705571 with the additive generator."""
import re
import subprocess
import sys
from goldbach_reflected_audit import additive_primes

text = subprocess.check_output(['pdftotext', '-layout', sys.argv[1], '-'], text=True)
table = text.split('Appendix B. Table 1', 1)[1].split('References', 1)[0]
values = [int(v) for row in table.splitlines()
          if re.fullmatch(r'\s*\d+(?:\s+\d+){9}\s*', row) for v in row.split()]
assert len(values) == 1000 and values == additive_primes(7927)
print(f'PASS: {len(values)} values, first={values[0]}, last={values[-1]}')
