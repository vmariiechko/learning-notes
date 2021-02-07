digits_count = 0
data = {}

i = 1
while True:

	digits = [int(char) for char in str(i**3)]
	digits.sort()

	numclass = "".join(str(digit) for digit in digits)

	if len(numclass) > digits_count:
		candidates = [lowest for (lowest, count) in data.values() if count == 5]

		if len(candidates) > 0:
			print(str(min(candidates)**3))
			break
			
		data = {}
		digits_count = len(numclass)

	lowest, count = data.get(numclass, (i,0))
	data[numclass] = (lowest, count+1)

	i += 1