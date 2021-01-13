from math import sqrt


def is_prime(num):

	if num < 2:
		return False

	if num % 2 == 0 and num > 2:
		return False

	for n in range(3, int(sqrt(num))+1, 2):
		if num % n == 0:
			return False
	return True


N = 0
answer = 0
for a in range(-999, 1000):
	for b in range(1001):

		n = 0

		while is_prime(n**2 + a*n + b):
			n += 1

		if N < n:
			N = n
			answer = a * b

print(N, answer)
