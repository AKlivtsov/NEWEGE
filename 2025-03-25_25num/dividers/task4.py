def f(x):
    a = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if str(i).endswith("7") and i != 7 and i != x:
                a.add(i)
                a.add(x // i)

    a = sorted(list(a))

    if len(a) != 0:
        return min(a)
    else:
        return 0

c = 0
for i in range(600000, 10**10):
    if f(i) != 0:
        print(i, f(i))
        c += 1

    if c == 5:
        break

# 600001 437
# 600002 47
# 600005 217
# 600015 17
# 600021 27