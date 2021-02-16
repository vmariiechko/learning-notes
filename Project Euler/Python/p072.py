LIMIT = 1000000


def calc_list_totients(n):
	result = list(range(n+1))

	for i in range(2, len(result)):
		if result[i] == i:
			for j in range(i, len(result), i):
				result[j] -= result[j] // i

	return result


answer = sum(calc_list_totients(LIMIT)[2:])
print(answer)