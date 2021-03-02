from eulertools import sign


with open("p102_triangles.txt", "r") as f:
	triangles = f.readlines()

triangles = [list(map(int,i.replace("\n","").split(","))) for i in triangles] 


def contained(x0, y0, x1, y1, x2, y2):
	a = sign((y1 - y0) * x1 - (x1 - x0) * y1)
	b = sign((y2 - y1) * x2 - (x2 - x1) * y2)
	c = sign((y0 - y2) * x0 - (x0 - x2) * y0)

	return 0 in (a, b, c) or a == b == c


answer = sum(1 for triangle in triangles if contained(*triangle))
print(answer)