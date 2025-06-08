from itertools import combinations

def cond(x):
    return (x in D) <= (((not (x in C)) and (not (x in A))) <= (not (x in D)))

D ,C = range(17, 58), range(29, 80)
s = [range(*x) for x in combinations((17,29,58,80), 2)]
mini = 1000

for A in s:
    if all(cond(x) for x in range(-3000, 3000)):
        mini = min(mini, len(A))

print(mini)
