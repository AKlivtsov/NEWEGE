from itertools import product

print("z w y x")
for x, y, z, w in product([0, 1], repeat=4):
    cond = (x <= y) and (y == (not z)) and (z or w)
    if cond:
        print(z, w, y, x)
