from itertools import product

count = 0
for comb in product("01234567", repeat=7):
    comb = "".join(comb)

    if comb.count("0") != 2:
        continue

    bad = False
    for i in range(len(comb) - 1):
        a = int(comb[i])
        b = int(comb[i + 1])

        if a % 2 == 0 and b % 2 == 0:
            bad = True
        elif a % 2 != 0 and b % 2 != 0:
            bad = True
    if bad:
        continue

    count += 1

print(count)  # 5760
