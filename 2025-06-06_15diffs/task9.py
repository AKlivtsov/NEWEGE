def f(a):
    for x in range(1, 1000):
        cond = (a % 45 == 0) and ((750 % x == 0) <= ((a % x != 0) <= (120 % x != 0)))
        if not cond:
            return False
    return True


for A in range(1, 3000):
    if f(A):
        print(A)  # 90
        break
