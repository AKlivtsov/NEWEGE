from itertools import product

ans = []
c = 0
for comb in product("0123456789A", repeat=5):
    comb = "".join(comb)

    if comb.count("7") != 1:
        continue

    count = comb.count("9") + comb.count("A")
    
    if count > 3:
        continue

    ans.append(comb)
    c += 1

print(c)  # 73190 !
for x in range(-5, 0, 1):
    print(ans[x])
