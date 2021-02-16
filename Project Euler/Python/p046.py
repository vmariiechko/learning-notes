from eulertools import is_prime


def test_goldbach(num):
	if num % 2 == 0 or is_prime(num):
		return True

	j = 1
	while True:
		k = num - 2*j*j
		j += 1

		if k <= 0:
			return False
		elif is_prime(k):
			return True


i = 9
while True:
	answer = test_goldbach(i)

	if not answer:
		break

	i += 2

print(i)