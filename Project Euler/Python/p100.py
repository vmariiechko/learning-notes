from eulertools import sqrt

# b - blue disks, r - red disks
# ( b / (b + r) ) * ( (b - 1) / (b + r -1) ) = 1 / 2 - taking 2 blue discs
# b^2 - b(2r + 1) + (r - r^2) = 0 - quadratic equation
# b = r + (sqrt(8r^2 + 1) + 1) / 2
# For example (x0, y0) and (x1, y1) are solutions
# Using Pell's equation and multiplying them we have:
# (x0*x1 + 8y0*y1)^2 - 8*(x0*y1 + y0*x1)^2 = 1
# Therefore, the fundamental solution is (3, 1)
LIMIT = 10**12
x0 = x = 3
y0 = y = 1

while True:
	square_root = sqrt(y * y * 8 + 1)		# sqrt(8r^2 + 1)

	# Must be odd
	if square_root % 2 == 1:
		blue = y + (square_root + 1) // 2	# b = r + (sqrt(8r^2 + 1) + 1) / 2

		if blue + y > LIMIT:
			print(blue)
			break


	nextx = x0 * x + 8 * y0 * y 			# x0*x1 + 8y0*y1
	nexty = x0 * y +     y0 * x 			# x0*y1 +  y0*x1
	x, y = nextx, nexty