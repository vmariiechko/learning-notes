decimal_fraction = "".join(str(i) for i in range(1000000))

answer = 1
for i in range(7):
	answer *= int(decimal_fraction[10**i])

print(answer)