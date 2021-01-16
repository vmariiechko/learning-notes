from math import sqrt

answer = set()

for product in range(1,10000):

	for multiplier in range(1, int(sqrt(product)) + 1):

		if product % multiplier == 0:

			temp = str(product) + str(multiplier) + str(product // multiplier)

			if "".join(sorted(temp)) == "123456789":
				answer.add(product)

print(sum(answer))