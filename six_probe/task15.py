def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            cond = ((x<a) <= (x*x<81)) and ((y*y<=36) <= (y<=a))
            if not cond:
                return False
    return True

c= 0
for A in range(1, 100000):
    if f(A):
        c += 1

print(c)


