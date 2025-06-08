def f(a):
    for x in range(10**5):
        cond = ((x & 52 != 0) and (x & 48 == 0)) <= (x & a != 0)
        if not cond:
            return False
    return True


for A in range(10**5):
    if f(A):
        print(A)  # 4
        break
