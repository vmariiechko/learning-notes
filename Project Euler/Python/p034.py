from math import factorial

# Answer in one line (very slow)
answer = sum(i for i in range(3,10000000) if i == sum([factorial(int(j)) for j in str(i)]))
print(answer)


# Same method, optimize sum of the factorials
def factorial_sum(n):
	result = 0

	while n >= 10000:
		result += factorial_sum_with_leading_zeros[n % 10000]
		n //= 10000

	return result + factorial_sum_without_leading_zeros[n]

factorial_sum_without_leading_zeros = [sum(factorial(int(digit)) for digit in str(i)) for i in range(10000)]
factorial_sum_with_leading_zeros = [sum(factorial(int(digit)) for digit in str(i).zfill(4)) for i in range(10000)]

answer = sum(i for i in range(3, 10000000) if i == factorial_sum(i))
print(answer)