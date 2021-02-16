from itertools import islice, count

from eulertools import sieve_of_eratosthenes


def truncatable_prime(n):
	s = str(n)
	return all(int(s[i:]) in primes and int(s[:i]) in primes for i in range(1, len(s)))


primes = sieve_of_eratosthenes(999999)

answer = sum(islice(filter(truncatable_prime, primes[4:]), 11))
print(answer)