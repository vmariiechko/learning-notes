from itertools import permutations


# Brute Force solution
pandigitals = ["".join(map(str,pandigital)) for pandigital in list(permutations(range(10)))] 

answer = 0
for pandigital in pandigitals:
	
	if int(pandigital[3]) % 2 != 0 or pandigital[5] not in ['0', '5']:
		continue
	elif int(pandigital[2:5]) % 3 != 0 or int(pandigital[4:7]) % 7 != 0:
		continue
	elif int(pandigital[5:8]) % 11 != 0 or int(pandigital[6:9]) % 13 != 0 or int(pandigital[7:]) % 17 != 0:
		continue

	answer += int(pandigital)
print(answer)


# More clever and faster solution:
def is_substr_divisible(num):
	return all( (num[i+1]*100 + num[i+2]*10 + num[i+3]) % d == 0 for (i,d) in enumerate(DIVISORS) )

DIVISORS = [2, 3, 5, 7, 11, 13, 17]

answer = sum(int("".join(map(str,num))) for num in list(permutations(range(10))) if is_substr_divisible(num))
print(answer)