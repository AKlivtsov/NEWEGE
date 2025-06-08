s = 10**6
for x in range(1,200):
    for y in range(1,200):
        for z in range(1,200):
            if (x+2*y + z == 75 and 3*x + 3*y + 2*z == 196):
                s = min(s, x + y + z + 2)

print(s) # 68
