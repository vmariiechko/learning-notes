from math import factorial

LIMIT = 1000000
TERMS = 60
FACTORIALS = [factorial(i) for i in range(10)]


def sum_factorials(n):
	result = 0

	while n != 0:
		result += FACTORIALS[n % 10]
		n //= 10

	return result


def get_chain_length(n):
	seen = set()

	while True:
		seen.add(n)
		n = sum_factorials(n)

		if n in seen:
			return len(seen)


answer = sum(1 for i in range(LIMIT) if get_chain_length(i) == TERMS)
print(answer)