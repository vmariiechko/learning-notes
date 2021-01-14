answer = 0
for num in range(2, 1000000):

	if num == sum(int(i)**5 for i in str(num)):
		answer += num

print(answer)