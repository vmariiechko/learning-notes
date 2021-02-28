with open("p096_sudoku.txt", "r") as f:
	su_doku = f.readlines()

su_doku = ["".join(su_doku[i + j].replace("\n", "") for j in range(1,10)) 
									  for i in range(0, len(su_doku), 10)]


def extract_top_left_corner(solved):
	return int("".join(str(d) for d in solved[:3]))


def solve(puzzle):
	state = [int(c) for c in puzzle]
	colfree = [set(range(1, 10)) for i in range(9)]
	rowfree = [set(range(1, 10)) for i in range(9)]
	boxfree = [set(range(1, 10)) for i in range(9)]

	for y in range(9):
		for x in range(9):
			num = state[y * 9 + x]
			if num != 0:
				colfree[x].remove(num)
				rowfree[y].remove(num)
				boxfree[y // 3 * 3 + x // 3].remove(num)


	def recurse(i):
		if i == 81:
			return True

		elif state[i] != 0:
			return recurse(i + 1)

		else:
			x = i % 9
			y = i // 9
			j = y // 3 * 3 + x // 3

			candidates = colfree[x].intersection(rowfree[y], boxfree[j])

			for num in candidates:
				state[i] = num
				colfree[x].remove(num)
				rowfree[y].remove(num)
				boxfree[j].remove(num)

				if recurse(i + 1):
					return True

				colfree[x].add(num)
				rowfree[y].add(num)
				boxfree[j].add(num)

			state[i] = 0
			return False

	if not recurse(0):
		raise AssertionError("Can't solve")
	return state


answer = sum(extract_top_left_corner(solve(puzzle)) for puzzle in su_doku)
print(answer)