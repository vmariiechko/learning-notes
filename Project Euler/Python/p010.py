from eulertools import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(2000000)

print(sum(primes))