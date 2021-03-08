INFINITY = 10**10


with open('p082_matrix.txt', 'r') as f:
	matrix = f.readlines()

matrix = [[int(s) for s in row.replace("\n", "").split(",")] for row in matrix]
height = len(matrix)
width = len(matrix[0])


def get_val(h, w):
	if w < 0:
		return 0
	elif h < 0 or h >= height or w >= width:
		return INFINITY
	else:
		return distance[h][w]


distance = [[0] * width for _ in range(height)]
for w in range(width):
	for h in range(height):
		distance[h][w] = matrix[h][w] + min(get_val(h, w-1), get_val(h-1, w))

	for h in reversed(range(height)):
		distance[h][w] = min(matrix[h][w] + get_val(h + 1, w), distance[h][w])

answer = min(distance[h][-1] for h in range(height))
print(answer)