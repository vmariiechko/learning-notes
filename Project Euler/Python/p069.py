from fractions import Fraction

from eulertools import calc_list_totients

LIMIT = 1000000


totients = calc_list_totients(LIMIT)
answer = max(range(2, len(totients)), key=(lambda i: Fraction(i, totients[i])))
print(answer)