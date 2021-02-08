with open('p067_triangle.txt', 'r') as f:
	triangle = f.readlines()

triangle = [[int(j) for j in i.replace('\n','').split(" ")] for i in triangle]

for i in reversed(range(len(triangle)-1)):
	for j in range(len(triangle[i])):
		triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])