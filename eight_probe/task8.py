from itertools import product

c = 0
for comb in product("0123456", repeat=5):
    comb = ''.join(comb)

    if comb[0] not in "246":
        continue

    if comb[-1] in "23":
        continue

    if comb.count("1") < 2:
        continue

    c+=1

print(c)