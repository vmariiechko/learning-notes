LIMIT = 1000000


proper_divisors_sum = [0] * (LIMIT + 1)
for i in range(1, LIMIT + 1):
	for j in range(i * 2, LIMIT + 1, i):
		proper_divisors_sum[j] += i

maxchainlen = 0 
answer = -1

for i in range(LIMIT + 1):
	seen = set()
	cursor = i

	count = 1
	while True:
		seen.add(cursor)
		next = proper_divisors_sum[cursor]

		if next == i:
			if count > maxchainlen:
				answer	 = i
				maxchainlen = count
			break
		elif next > LIMIT or next in seen:
			break
		else:
			cursor = next

		count += 1
print(answer)