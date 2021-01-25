triangles = {i*(i+1)/2 for i in range(99999)}
pentagonals = {i*(3*i-1)/2 for i in range(99999)}
hexagonal = {i*(2*i-1) for i in range(99999)}

same = triangles.intersection(pentagonals.intersection(hexagonal))
print(list(same)[3:])