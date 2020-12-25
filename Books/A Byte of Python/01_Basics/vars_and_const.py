i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)


# strongly recommended that you stick to writing
# a maximum of a single logical line on each single physical line
i = 5; print(i);


s = 'This is a string. \
This continues the string.'
print(s)

i = \
5


# Identation
i = 5
# Error below! Notice a single space at the start of the line
 # print('Value is', i)
print('I repeat, the value is', i)