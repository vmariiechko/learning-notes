from math import ceil, sqrt

num = 1
i = 2

while True:
	num = num + i

	end = ceil(sqrt(num))

	result = sum(2 for i in range(1, end+1) if num % i == 0)

	if end**2 == num:
		result -= 1

	if result > 500:
		print(num)
		break

	i += 1