print("z y w x")
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            for w in [0,1]:
                cond = ((w <= y) <= x) or (not z)
                if not cond:
                    print(z, y, w, x)