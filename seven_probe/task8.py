from itertools import product

c = 0
for comb in product("0123456789AB", repeat=5):
    comb = "".join(comb)

    if comb.count("7") != 1:
        continue

    if comb.count("9") > 3:
        continue

    if comb.count("A") > 3:
        continue

    if comb.count("B") > 3:
        continue

    c += 1

print(c)  # 73190
