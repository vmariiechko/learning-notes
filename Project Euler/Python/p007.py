# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):

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

primes = []

sieve_of_eratosthenes(200000)

if len(primes) > 10001:
	print(primes[10000])