from math import sqrt


def Fibonacci_recursion(n):
	a, b = 1, 2

	if n in [1,2]:
		return n

	for i in range(n-2):
		a, b = b, a+b

	return b


def Fibonacci_closure():
	f1 = 1
	f2 = 1
	index = 2

	def get_next():
		nonlocal f1, f2, index
		f1, f2 = f2, f1+f2
		index += 1
		return (f2, index)

	return get_next


def is_palindrome(num):
	return num == num[::-1]


def sieve_of_eratosthenes(n):
	primes = []

	prime = [True for i in range(n+1)]
	p = 2

	while p**2 <= n:

		if prime[p] == True:

			for i in range(p*p, n+1, p):
				prime[i] = False

		p += 1

	for p in range(2, n+1):
		if prime[p]:
			primes.append(p)

	return primes


def is_prime(num):

	if num < 2:
		return False

	if num % 2 == 0 and num > 2:
		return False

	for n in range(3, int(sqrt(num))+1, 2):
		if num % n == 0:
			return False
	return True


def calc_list_totients(n):
	result = list(range(n+1))

	for i in range(2, len(result)):
		if result[i] == i:
			for j in range(i, len(result), i):
				result[j] -= result[j] // i

	return result