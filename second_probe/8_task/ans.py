from itertools import product

c = 0
for comb in product("ТИМОФЕЙ", repeat=5):
    comb = "".join(comb)

    if (comb.count("Т") >= 1) and (comb.count("Й") <= 1):
        c += 1

print(c)  # 8006
