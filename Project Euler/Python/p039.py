def count_solutions(p):
	result = 0

	for a in range(1, p//3 + 1):

		for b in range(a, (p-a)//2 + 1):
			c = p - a - b

			if a*a + b*b == c*c:
				result += 1

	return result

answer = max(range(1,1001), key=count_solutions)
print(answer)