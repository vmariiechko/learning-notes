state = list(range(1, 11))
max = None


def next_permutation(state):
	i = len(state) - 1

	while i > 0 and state[i - 1] >= state[i]:
		i -= 1

	if i <= 0:
		return False

	j = len(state) - 1

	while state[j] <= state[i - 1]:
		j -= 1

	state[i - 1], state[j] = state[j], state[i - 1]

	state[i : ] = state[len(state) - 1 : i - 1 : -1]
	return True


while True:
	sum = state[0] + state[5] + state[6]

	if state[1] + state[6] + state[7] == sum and \
	   state[2] + state[7] + state[8] == sum and \
	   state[3] + state[8] + state[9] == sum and \
	   state[4] + state[9] + state[5] == sum:

		min_outer_idx = 0
		min_outer = state[0]
		s = ""

		for i in range(1, 5):
			if state[i] < min_outer:
				min_outer_idx = i
				min_outer = state[i]

		for i in range(5):
			s += str(state[(min_outer_idx + i) % 5])
			s += str(state[(min_outer_idx + i) % 5 + 5])
			s += str(state[(min_outer_idx + i + 1) % 5 + 5])

		if len(s) == 16 and (max is None or s > max):
			max = s

	if not next_permutation(state):
		break

print(max)