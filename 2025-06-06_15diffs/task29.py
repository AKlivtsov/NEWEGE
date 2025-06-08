from itertools import combinations

def cond(x):
    return  (not ((x in Q) <= ((x in P) or (x in R)))) <= ((not (x in A)) <= (not (x in Q)))

P, Q, R = range(13, 31), range(18, 80), range(48, 114)
s = [range(*x) for x in combinations((13, 18, 31, 48, 80, 114), 2)]
mini = 1000

for A in s:
    if all(cond(x) for x in range(-3000, 3000)):
        mini = min(mini, len(A))

print(mini)
