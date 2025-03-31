from itertools import product

print("w z y x")
for x, y ,z, w in product((0,1), repeat=4):
    cond = (x and not(y)) or (y == z) or not(w)
    if not cond:
        print(w, z, y, x) # w z y x
