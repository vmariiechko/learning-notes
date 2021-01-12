def cycle_len(n):
	seen = dict()
	result = ''

	reminder = 1 % n

	while (reminder != 0) and (reminder not in seen):

		seen[reminder] = len(result)

		reminder *= 10

		res_part = reminder // n
		result += str(res_part)

		reminder = reminder % n 

	if (reminder == 0):
		return 0
	else:
		return len(result[seen[reminder]:])

answer = max(range(1,1000), key=cycle_len)

print(answer)
print(1/answer)