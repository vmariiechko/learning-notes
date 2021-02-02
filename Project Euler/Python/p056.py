def digital_sum(num):
	return sum( [int(n) for n in str(num)] )

answer = max([digital_sum(a**b) for a in range(2,100) for b in range(2, 100)])
print(answer)