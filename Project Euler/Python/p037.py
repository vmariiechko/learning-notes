from itertools import islice, count


primes = []

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


def truncatable_prime(n):
	s = str(n)
	return all(int(s[i:]) in primes and int(s[:i]) in primes for i in range(1, len(s)))


sieve_of_eratosthenes(999999)

answer = sum(islice(filter(truncatable_prime, primes[4:]), 11))
print(answer)