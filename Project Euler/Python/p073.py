LIMIT = 12000

answer = 0
stack = [(1, 3, 1, 2)]

# The Stern-Brocot tree
while len(stack) > 0:
	left_N, left_D, right_N, right_D = stack.pop()
	d = left_D + right_D

	if d <= LIMIT:
		n = left_N + right_N
		answer += 1

		stack.append((n, d, right_N, right_D))
		stack.append((left_N, left_D, n, d))

print(answer)