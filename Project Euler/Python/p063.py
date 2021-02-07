answer = sum(1 
				for digit in range(1,10)
				for nth_power in range(1,22)
				if len(str(digit**nth_power)) == nth_power)
print(answer)