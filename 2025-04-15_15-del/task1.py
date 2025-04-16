for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % a != 0) <= ((x%6 == 0) <= (x%9 != 0)):
            k += 1
    if k == 999:
        print(a)
        break
    