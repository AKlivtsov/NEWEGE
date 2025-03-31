from itertools import product
print("x y w z")
for x, y, z, w in product((0, 1), repeat=4):
    cond = ((x <= y) <= z) or not(w)
    if not cond:
        print(x, y, w, z) # x y w z 
