
divsum = [0] * 10000
answer = 0

for i in range(1, len(divsum)):
	for j in range(i*2, len(divsum), i):
		divsum[j] += i

for i in range(1, len(divsum)):
	j = divsum[i]

	if j != i and j < len(divsum) and divsum[j] == i:
		print(i)
		answer += i

print(answer)
