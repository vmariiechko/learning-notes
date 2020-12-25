bri = set(['brazil', 'russia', 'india'])

a = 'india' in bri
print(a)
b = 'usa' in bri
print(b)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri & bric) # OR bri.intersection(bric))