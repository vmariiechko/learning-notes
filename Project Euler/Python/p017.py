# {number: amount of letters}
numbers = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
		   11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6,
		   30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 1000:11}

# Add hundreds to dict of numbers
for i in range(1,10):
	numbers[i*100] = numbers[i] + 7



# Count letters for numbers from 1 to 20
digits = sum([numbers[i] for i in range(1,10)])
first_19 = sum( list(numbers.values())[0:19] )

# Count letters for numbers from 20 to 99
first_99 = first_19
for i in range(20,91,10):

	# 20, 30, 40, ..., 80, 90
	first_99 += numbers[i]

	# 21, 22, 23, ..., 29, 31, 32, ..., 97, 98, 99
	first_99 += numbers[i]*9 + digits

# Count letters for numbers from 100 to 999
answer = first_99
for i in range(100,901,100):

	# 100, 200, 300, ..., 800, 900
	answer += numbers[i]
	
	# 101, 102, ..., 110, 111, 112, ..., 899, 901, 902, ..., 998, 999 + don't forget about "and" word
	answer += numbers[i]*99 + first_99 + 99*3

answer += numbers[1000]

print(answer)
