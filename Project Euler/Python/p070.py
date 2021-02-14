LIMIT = 10000000 - 1


def has_permutation(n, totient):
	return sorted(str(n)) == sorted(str(totient))


def calc_list_totients(n):
	result = list(range(n+1))

	for i in range(2, len(result)):
		if result[i] == i:
			for j in range(i, len(result), i):
				result[j] -= result[j] // i

	return result


totients = calc_list_totients(LIMIT)
mindenominator = 0 
minnumerator = 1

for (n, totient) in enumerate(totients[2:], 2):
	if n * mindenominator < minnumerator * totient and has_permutation(n, totient):
		minnumerator = n
		mindenominator = totient

print(minnumerator)