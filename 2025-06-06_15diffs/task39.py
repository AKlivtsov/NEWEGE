def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            cond = (2*x + y != 70) or (x<y) or (a< x)
            if not cond:
                return False
    return True

for A in range(100, 1, -1):
    if f(A):
        print(A)
        break
