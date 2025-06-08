from itertools import combinations


def cond(x):
    return (x in P) <= ((not ((x in P) == (x in Q))) or ((x in Q) <= (x in A)))


P, Q = range(69, 91), range(77, 114)
s = [range(*x) for x in combinations((69, 77, 91, 114), 2)]
mini = 1000

for A in s:
    if all(cond(x) for x in range(-3000, 3000)):
        mini = min(mini, len(A))

print(mini)  # 27
