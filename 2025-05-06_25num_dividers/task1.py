# 27422

def f(x):
    a = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)

    a = sorted(list(a))
    if len(a) == 2:
        return a[0], a[1]
    else:
        return 0

for x in range(174457, 174505 + 1):
    if f(x) != 0:
        print(f(x))

# (3, 58153)
# (7, 24923)
# (59, 2957)
# (13, 13421)
# (149, 1171)
# (5, 34897)
# (211, 827)
# (2, 87251)

