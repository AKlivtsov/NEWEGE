print("y x w z")
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            for w in [0,1]:
                cond = (x and (not y)) or (y==z) or w
                if not cond:
                    print(y, x, w, z)