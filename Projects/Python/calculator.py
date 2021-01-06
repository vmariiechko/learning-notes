# From "The Complete Python 3 Course: Beginner to Advanced!" course on Udemy

import re

print("My Magical Calculator")
print("Type 'quit' to exit\n")
print("Enter equation: ", end='')

previous = ''

while True:
	
	equation = input(previous)

	if equation == 'quit':
		print("Goodbye, human.")
		break

	else:
		equation = re.sub('[a-zA-Z,:" "]', '', equation)

		if previous is False:
			previous = eval(equation)
		else:
			previous = eval(str(previous) + equation)
