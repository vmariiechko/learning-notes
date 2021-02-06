from math import pow

# answer = 0
# nth_power = 1
# while True:

# 	# if check_digits(nth_power)

# 	if any(True for i in range(10) if nth_power == len(str(i**nth_power)) ):
# 		answer += 1
# 		continue


# 	if nth_power == 10:
# 		break

# 	nth_power += 1
# print(answer)

answer = sum(1 
				for digit in range(1,10)
				for nth_power in range(1,22)
				if len(str(digit**nth_power)) == nth_power)
print(answer)