from eulertools import sieve_of_eratosthenes


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