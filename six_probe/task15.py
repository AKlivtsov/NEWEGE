def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            cond = ((x<a) <= (x*x<81)) or ((y*y<=36) <= (y<=a))
            if not cond:
                return False
    return True

c= 0
for x in range(10000, -1, -1):
    if f(x):
        c += 1

print(c)


