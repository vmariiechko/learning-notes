from eulertools import calc_list_totients

LIMIT = 1000000


answer = sum(calc_list_totients(LIMIT)[2:])
print(answer)