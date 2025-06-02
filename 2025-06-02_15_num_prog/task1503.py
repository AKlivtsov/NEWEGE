def f(a):
    for x in range(1, 1000):
        cond = (x%a!=0) <= ((x%28==0) <= (x%49!=0))
        if not cond:
            return False

    return True

for A in range(1000, -1 ,-1):
    if f(A):
        print(A)
        break

        