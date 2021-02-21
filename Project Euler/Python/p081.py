with open('p081_matrix.txt', 'r') as f:
	matrix = f.readlines()

matrix = [[int(s) for s in row.replace("\n", "").split(",")] for row in matrix]
# answer = matrix[0][0] + matrix[79][79]

matrix_len = len(matrix)
for i in reversed(range(matrix_len)):
	for j in reversed(range(len(matrix[i]))):

		if i + 1 < matrix_len and j + 1 < matrix_len:
			temp = min(matrix[i + 1][j], matrix[i][j + 1])

		elif i + 1 < matrix_len:
			temp = matrix[i + 1][j]

		elif j + 1 < matrix_len:
			temp = matrix[i][j + 1]

		else:
			temp = 0

		matrix[i][j] += temp

print(matrix[0][0])