from math import sqrt

def is_prime(num):

	if num % 2 == 0:
		return False

	for n in range(3, int(sqrt(num)+1), 2):
		if num % n == 0:
			return False

	return True

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