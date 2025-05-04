from itertools import product

c = 0
for comb in product("ДГИАШЭ", repeat=5):
    comb = ''.join(comb)
    if (comb[0] in "ИАЭ") or (comb[-1] in "ДГШ"):
        continue
    c += 1

print(c) # 1944