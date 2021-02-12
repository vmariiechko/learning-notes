def count_pentagonal(i):

	while len(pentagonals_list) <= i:
		n = len(pentagonals_list)
		term = int(n*(3*n-1)/2)
		pentagonals_list.append(term)
		pentagonals_set.add(term)

	return pentagonals_list[i]


def is_pentagonal(x):

	while pentagonals_list[-1] < x:
		n = len(pentagonals_list)
		term = int(n*(3*n-1)/2)
		pentagonals_list.append(term)
		pentagonals_set.add(term)

	return x in pentagonals_set


pentagonals_list = [0]
pentagonals_set = set()


D = None
i = 2
while True:
	pentagonal_i = count_pentagonal(i)

	if D is not None and pentagonal_i - count_pentagonal(i-1) >= D:
		break

	for j in range(i-1, 0, -1):
		pentagonal_j = count_pentagonal(j)
		difference = pentagonal_i - pentagonal_j

		if D is not None and difference >= D:
			break
		elif is_pentagonal(pentagonal_i + pentagonal_j) and is_pentagonal(difference):
			D = difference

	i += 1

print(D)