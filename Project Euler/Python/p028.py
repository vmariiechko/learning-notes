answer = 1
for i in range(3, 1002, 2):
	
	for j in range(4):
		answer += i**2 - (i-1)*j

print(answer)