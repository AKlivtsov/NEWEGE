# (A == B) and C == 1

from itertools import product

c = 0
for a, b, c in product((0, 1), repeat=3):
    if (a or b) == ((a and b) <= 0):
        print(a, b, c)
