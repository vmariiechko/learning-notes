from eulertools import sqrt, sieve_of_eratosthenes

LIMIT = 50000000
primes = sieve_of_eratosthenes(sqrt(LIMIT))


sums = {0}
for power in range(2, 5):
	newsums = set()

	for prime in primes:
		q = prime**power

		if q > LIMIT:
			break

		for x in sums:
			if x + q <= LIMIT:
				newsums.add(x + q)

	sums = newsums

print(len(sums))