INFINITY = 10**10

with open('p082_matrix.txt', 'r') as f:
	matrix = f.readlines()

matrix = [[int(s) for s in row.replace("\n", "").split(",")] for row in matrix]
height = len(matrix)
width = len(matrix[0])
distance = [[INFINITY] * width for _ in range(height)]
distance[0][0] = matrix[0][0]


def get_val(h, w):
	if w < 0 or w >= width or h < 0 or h >= height:
		return INFINITY
	else:
		return distance[h][w]


# Bellman-Ford algorithm
changed = True
while changed:
	changed = False

	for h in range(height):
		for w in range(width):
			temp = matrix[h][w] + min(get_val(h - 1, w), 
									  get_val(h + 1, w),
									  get_val(h, w - 1),
									  get_val(h, w + 1))

			if temp < distance[h][w]:
				distance[h][w] = temp
				changed = True

print(distance[height - 1][width - 1])