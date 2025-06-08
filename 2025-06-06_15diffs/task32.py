def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            cond = (4*x + 3*y < a) or (x>=y) or (y>= 13)
            if not cond:
                return False
    return True

for A in range(1, 10000):
    if f(A):
        print(A) # 81
        break