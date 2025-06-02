print("w y z x")
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            for w in [0,1]:
                cond = (x and y and (not z)) == (y or z or (not w))
                if cond:
                    print(w, y, z, x)
                    