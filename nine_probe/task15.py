from itertools import combinations


def cond(x):
    return not ((x in P) == (x in Q)) and not (x in A)


P, Q = range(84, 341), range(198, 412)
s = [range(*x) for x in combinations((84, 198, 341, 412), 2)]
mini = 1000

for A in s:
    if all(cond(x) for x in range(-3000, 3000)):
        mini = min(mini, len(A))

print(mini)
print(412 - 341)  # 71
