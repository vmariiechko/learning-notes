from eulertools import sqrt

LIMIT = 2000000
max_area = sqrt(LIMIT) + 1


def count_rectangles(w, h):
	return (w + 1) * w * (h + 1) * h // 4 


possible_rectangles = ((width, height) for width in range(1, max_area) for height in range(1, max_area))
func = lambda width_height: abs(count_rectangles(*width_height) - LIMIT)
answer = min(possible_rectangles, key=func)
print(answer[0] * answer[1])