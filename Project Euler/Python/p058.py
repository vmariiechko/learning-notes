from eulertools import is_prime


n = 3
primes_num = 0
while True:

	for i in range(4):
		if is_prime(n**2 - (n-1)*i):
			primes_num += 1

	if primes_num/(n*2 - 1) < 0.1:
		print(n)
		break

	n += 2