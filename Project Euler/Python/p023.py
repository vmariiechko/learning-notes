LIMIT = 28124
divsum = [0] * LIMIT

for i in range(1, len(divsum)):
	for j in range(i*2, len(divsum), i):
		divsum[j] += i

abundant = [i for (i,x) in enumerate(divsum) if x > i]

expressible = [False] * LIMIT

for i in abundant:
	for j in abundant:
		if i+j < LIMIT:
			expressible[i+j] = True
		else:
			break

answer = sum(i for (i,x) in enumerate(expressible) if not x)
print(answer)