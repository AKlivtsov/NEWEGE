def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            cond = (x<3) or (y<2) or (x*y>a)
            if not cond:
                return False
            
    return True

for A in range(1000, -1, -1): # тк нужно максимальное
    if f(A):
        print(A)
        break
