LIMIT = 51


def right_triangle(x1, x2, y1, y2):
	a = x1*x1 + y1*y1
	b = x2*x2 + y2*y2
	c = (x2 - x1)**2 + (y2 - y1)**2
	return (a + b == c) or (a + c == b) or (b + c == a)


answer = sum(1
			 for x1 in range(LIMIT)
			 for x2 in range(LIMIT)
			 for y1 in range(LIMIT)
			 for y2 in range(LIMIT)
			 if y1 * x2 > y2 * x1 and right_triangle(x1, x2, y1, y2)
			 )
print(answer)