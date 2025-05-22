# 38603

def f(x):
    a = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            a.add(x)
            a.add(x // i)

    a = sorted(list(a))

    if len(a) > 2:
        return max(a) + min(a)
    else:
        return 0


c = 0
for x in range(700000, 10**100):
    if str(f(x))[-1] == "8":
        print(x, f(x))
        c += 1

    if c == 5:
        break

# 700007 709098
# 700016 701088
# 700017 712298
# 700046 701188
# 700051 702818
