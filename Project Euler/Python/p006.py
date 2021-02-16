# First solution
a, b = 0, 0

for i in range(1,101):
	a += i**2
	b += i 

print(b**2-a)


# Second solution
l = 100
s = l*(l+1)/2
s_sq = (2*l+1)*(l+1)*l/6
print(s**2-s_sq)