from eulertools import is_prime


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