def f(a):
    for x in range(10**5):
        cond = ((x & 6280 > 0) or (x & 3394 > 0)) <= ((x & 10828 == 0) <= (x & a > 0))
        if not cond:
            return False
    return True


for A in range(10**5):
    if f(A):
        print(A)  # 5506
        break
