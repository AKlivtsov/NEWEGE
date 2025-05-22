# 27853

import math

def f(x):
    a = set()
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            a.add(i)
            a.add(x // i)
    a = sorted(list(a))
    if len(a) == 6:
        return a
    else:
        return 0

for x in range(312614, 312651 + 1):
    if f(x) != 0:
        print(f(x))

# [1, 2, 4, 78157, 156314, 312628]
# [1, 3, 9, 34739, 104217, 312651]