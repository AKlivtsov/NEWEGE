print("w y z x")
for w in [0,1]:
    for x in [0,1]:
        for y in [0,1]:
            for z in [0,1]:
                cond = ((x <= (not y)) and (x or w)) <= (not z)
                if  not cond:
                    print(w, y, z, x)