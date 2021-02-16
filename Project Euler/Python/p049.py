from math import sqrt

LIMIT = 10000


def same_permutation(a, b):
	return sorted(str(a)) == sorted(str(b))


# sieve of Eratosthenes
is_prime = [True for i in range(LIMIT)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(sqrt(LIMIT)) + 1):
	if is_prime[i]:
		for j in range(i*i, LIMIT, i):
			is_prime[j] = False


# Find increased permutations
for frst_term in range(1000, LIMIT):
	if is_prime[frst_term]:

		for increase in range(1, LIMIT-1):
			scnd_term = frst_term + increase
			thrd_term = scnd_term + increase

			if scnd_term < LIMIT and is_prime[scnd_term] and same_permutation(scnd_term, frst_term) and thrd_term < LIMIT and is_prime[thrd_term] and same_permutation(thrd_term, frst_term) and (frst_term != 1487 or scnd_term != 4817):
				print(str(frst_term) + str(scnd_term) + str(thrd_term))