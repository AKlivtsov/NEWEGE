def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            cond = (x+2*y>48) or (y>x) or (x+3*y < a)
            if not cond:
                return False
    return True

for A in range(1000, 0, -1):
    if not f(A):
        print(A)
        break