from itertools import product

c = 0
for comb in product("ГОД", repeat=6):
    comb = ''.join(comb)
    if comb[0] in "УЕЫАОЭЯИЮ":
        continue
    c += 1

print(c) # 486