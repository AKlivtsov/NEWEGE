print("x w z y")

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            for w in [0,1]:
                cond = x and (z <= w) and (not y)
                if cond:
                    print(x, w, z, y)