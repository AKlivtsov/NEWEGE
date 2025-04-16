for A in range(64):
    B = True
    for x in range(64):
        if ((x & 41 == 0) or (x & 33 != 0) or (x & A != 0)) == 0:
            B = False
    if B:
        print(A)
        break
