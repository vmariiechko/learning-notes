from itertools import permutations

from eulertools import is_prime


for i in range(3,11):
	print(f'{i-1}:')

	answer = [j for j in [int(''.join(map(str,k))) for k in list(permutations(range(1,i)))] if is_prime(j)]

	if answer:
		print(answer[-1])