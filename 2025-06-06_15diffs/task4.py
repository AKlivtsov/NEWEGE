def f(a):
    for x in range(1, 1000):
        cond = (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 18 != 0)))
        if not cond:
            return False

    return True


for A in range(3000, 0, -1):
    if f(A):
        print(A)  # 45
        break
