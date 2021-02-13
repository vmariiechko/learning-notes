from fractions import Fraction

LIMIT = 1000000 


def calc_list_totients(n):
	result = list(range(n+1))

	for i in range(2, len(result)):
		if result[i] == i:
			for j in range(i, len(result), i):
				result[j] -= result[j] // i

	return result


totients = calc_list_totients(LIMIT)
answer = max(range(2, len(totients)), key=(lambda i: Fraction(i, totients[i])))
print(answer)
