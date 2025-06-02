def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            cond = (x<a)or(y<a)or(y>x-5)or(y<2*x-15)
            if not cond:
                return False

    return True

for A in range(1000):
    if f(A):
        print(A)
        break