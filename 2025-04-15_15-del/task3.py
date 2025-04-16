for a in range(100):
    k = 0
    for x in range(1,101):
        for y in range(1,101):
            if ((144%x == 0) <= (x % y != 0)) or (x + y > 100) or (a-x > y):
                k += 1
    if k == 10000:
        print(a)
        break
