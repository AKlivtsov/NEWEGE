for A in range(128):
    B = True
    for x in range(128):
        if ((x & 28 == 0) and (x & 45 == 0) or (x & 48 != 0) or (x & A != 0)) == 0:
            B = False

    if B:
        print(A)
        break
