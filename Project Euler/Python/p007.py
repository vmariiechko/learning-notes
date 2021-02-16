from eulertools import sieve_of_eratosthenes


primes = sieve_of_eratosthenes(200000)

if len(primes) > 10001:
	print(primes[10000])