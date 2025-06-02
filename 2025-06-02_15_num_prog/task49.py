def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            cond = (48!= y+2*x ) or (a<x) or (a<y)
            if not cond:
                return False
    return True

for A in range(1000, -1, -1):
    if f(A):
        print(A)
        break
