from math import sqrt


# 2,3,5,7 - circular primes
answer = 4


def is_prime(num):

	if num < 2:
		return False

	if num % 2 == 0 and num > 2:
		return False

	for n in range(3, int(sqrt(num)+1), 2):
		if num % n == 0:
			return False

	return True


def circular_prime(num):

	s = str(num)

	return all(is_prime(int(s[i:] + s[:i])) for i in range(len(s)))


answer += sum(1 for i in range(11,1000000) if circular_prime(i))
print(answer)