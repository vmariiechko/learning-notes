from eulertools import is_prime


# 2,3,5,7 - circular primes
answer = 4


def circular_prime(num):

	s = str(num)

	return all(is_prime(int(s[i:] + s[:i])) for i in range(len(s)))


answer += sum(1 for i in range(11,1000000) if circular_prime(i))
print(answer)