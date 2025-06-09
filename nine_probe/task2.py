print("w x z y")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                cond = (not z) and (not (y and (not x))) and (not (x == w))
                if cond:
                    print(w, x, z, y)
