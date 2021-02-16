# Brute Force
result = 0
result_chain = 0

for i in range(13,1000000,2):

	terms = 1
	num = i

	while i != 1:

		if i % 2 == 0:
			i = int(i/2)
		else:
			i = 3*i+1

		terms += 1

	if result_chain < terms:
		result = num
		result_chain = terms

print(result,result_chain)


# Faster solution
def countChain(num):
	if num in values:
		return values[num]

	if num % 2 == 0:
		values[num] = 1 + countChain(int(num/2))
	else:
		values[num] = 2 + countChain(int( (3*num+1)/2 ))

	return values[num]


result = 1
result_chain = 0
values = {1: 1}

for i in range(500000,10**6-1):

	if countChain(i) > result_chain:
		result_chain = countChain(i)
		result = i

print(result, result_chain)