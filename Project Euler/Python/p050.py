from math import sqrt

LIMIT = 1000000
answer = 0
answer_terms_count = 0


# sieve
primes = []
isprime = [True for i in range(LIMIT+1)]
p = 2

while p**2 <= LIMIT:

	if isprime[p] == True:

		for i in range(p*p, LIMIT+1, p):
			isprime[i] = False

	p += 1

for p in range(2, LIMIT+1):
	if isprime[p]:
		primes.append(p)


for i in range(len(primes)):
	primes_sum = primes[i]
	terms_count = 1

	for j in range(i+1, len(primes)):
		primes_sum += primes[j]
		terms_count += 1

		if primes_sum > LIMIT:
			break

		if isprime[primes_sum] and terms_count > answer_terms_count:
			answer = primes_sum
			answer_terms_count = terms_count

print(answer)