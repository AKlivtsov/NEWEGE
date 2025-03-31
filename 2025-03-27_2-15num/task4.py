from itertools import product
print("z x y w")
for x, y, z, w in product((0,1), repeat=4):
    cond = not(x <= z) or (y == w) or y
    if not cond:
        print(z, x, y, w) # z x y w 
        