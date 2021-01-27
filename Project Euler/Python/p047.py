def sieve_of_eratosthenes(n):
	primes = []

	prime = [True for i in range(n+1)]
	p = 2

	while p**2 <= n:

		if prime[p] == True:

			for i in range(p*p, n+1, p):
				prime[i] = False

		p += 1

	for p in range(2, n+1):
		if prime[p]:
			primes.append(p)

	return primes


def distinct_prime_factors(num):

	unique_primes = set()

	for prime in primes:

		while True:

			if num in primes and len(unique_primes) == 3:
				return True

			elif num % prime == 0:
				num //= prime
				unique_primes.add(prime)
				continue

			break

	return False


primes = sieve_of_eratosthenes(1000)
for i in range(10000,999999):

	if all(map(distinct_prime_factors, [i, i+1, i+2, i+3])):
		print(i)
		break