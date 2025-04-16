for a in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        if ((x%3 == 0) <= (x%5 != 0)) or (x+a >= 90):
            k += 1
    
    if k == 999:
        print(a)
        break
