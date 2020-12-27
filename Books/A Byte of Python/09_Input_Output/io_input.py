def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

print()

# For output, we can also use the various methods of the str (string) class
# For example, you can use the rjust method to get a string
# which is right justified to a specified width

# Homework exercies

def ignore(text, marks):
	for mark in marks:
		text = text.replace(mark,"")

	return text.lower()

print("Homework:")
something = input("Enter text: ")

something = ignore(something, [',','.','?','!',':',';','-','(',')','[',']','/',"'",' '])

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")