from eulertools import calc_list_totients

LIMIT = 10000000 - 1


def has_permutation(n, totient):
	return sorted(str(n)) == sorted(str(totient))


totients = calc_list_totients(LIMIT)
mindenominator = 0 
minnumerator = 1

for (n, totient) in enumerate(totients[2:], 2):
	if n * mindenominator < minnumerator * totient and has_permutation(n, totient):
		minnumerator = n
		mindenominator = totient

print(minnumerator)