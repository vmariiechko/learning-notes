LIMIT = 10000000
SQUARE_DIGITS_SUM = [sum(int(d)**2 for d in str(i)) for i in range(1000)]


def chain_arrive(num):

	while num not in (1, 89):
		num = square_digit_sum(num)

	return num


def square_digit_sum(num):
	result = 0

	while num > 0:
		result += SQUARE_DIGITS_SUM[num % 1000]
		num //= 1000

	return result


answer = sum(1
			 for num in range(1, LIMIT)
			 if chain_arrive(num) == 89)
print(answer)