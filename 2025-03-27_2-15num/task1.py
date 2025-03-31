print("x y z")

for x in range(2):
    for y in range(2):
        for z in range(2):
            cond = not(x or y) or (z == x)
            if not cond:
                print(x, y ,z) # x z y

# or

import itertools
print("x y z")
for x, y, z in itertools.product((0,1), repeat=3):
    cond = not(x or y) or (z == x)
    if not cond:
        print(x, y ,z) # x z y
