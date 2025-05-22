# 27852

def f(x):
    a = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)
    a = sorted(list(a))
    if len(a) == 4:
        return a
    else:
        return 0

for x in range(185311, 185330 + 1):
    if f(x) != 0:
        print(f(x))

# [1, 2, 92657, 185314]
# [1, 47, 3943, 185321]
# [1, 241, 769, 185329]