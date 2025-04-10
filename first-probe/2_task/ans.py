from itertools import product

print("d b a c")
for a, b, c, d in product((0, 1), repeat=4):
    cond = ((a and b) <= c) and ((b and c) <= d)
    if not cond:
        print(d, b, a, c)
