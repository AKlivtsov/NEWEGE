def f(x):
    a = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a.add(i)
            a.add(x // i)
    a = sorted(list(a))

    if len(a) != 0:
        return a[0] + a[-1]
    else:
        return 0

c = 0
for i in range(800001, 10 ** 20):
    if f(i) % 10 == 4:
        print(i, f(i))
        c += 1
    if c == 5:
        break
