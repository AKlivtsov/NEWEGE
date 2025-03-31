def f(x):
    a = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a.add(i)
            a.add(x // i)
    a = sorted(list(a))

    if len(a) == 2:
        return a[0], a[1]
    else:
        return 0
    

for i in range(174457, 174505 + 1):
    if f(i) != 0:
        print(f(i))