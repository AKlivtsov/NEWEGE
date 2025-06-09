from itertools import combinations

def cond(x):
    return (x in P) <= (((x in Q) and (x in P)) <= (x in A))

P, Q = range(25, 40), range(11, 32)
s = [range(*x) for x in combinations((11,25,32,40), 2)]
mini = 1000

for A in s:
    if all(cond(x) for x in range(-3000, 3000)):
        mini = min(mini, len(A))

print(mini)
