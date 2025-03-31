from itertools import product
print("y w z x")

for x, y, z, w in product((0,1), repeat=4):
    cond = ((x <= y) and (y <= w)) or (z == (x or y))
    if not cond:
        print(y, w, z, x) # y w z x 