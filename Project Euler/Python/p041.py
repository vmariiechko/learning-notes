from math import sqrt
from itertools import permutations


def is_prime(num):

	if num % 2 == 0:
		return False

	for n in range(3, int(sqrt(num)+1), 2):
		if num % n == 0:
			return False

	return True


for i in range(3,11):
	print(f'{i-1}:')

	answer = [j for j in [int(''.join(map(str,k))) for k in list(permutations(range(1,i)))] if is_prime(j)]

	if answer:
		print(answer[-1])