from eulertools import is_prime
from itertools import count

LIMIT = 5000
primes = [2]


def sum_ways(n):
	for i in range(primes[-1] + 1, n + 1):
		if is_prime(i):
			primes.append(i)

	ways = [1] + [0] * n
	for p in primes:
		for i in range(n + 1 - p):
			ways[i + p] += ways[i]

	return ways[n] 


answer = next(filter(lambda n: sum_ways(n) > LIMIT, count(2)))
print(answer)