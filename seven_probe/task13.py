print(bin(248)[2:])
print(bin(168)[2:])
print(
    bin(172)[2:],
    bin(16)[2:],
    bin(168)[2:],
    bin(0)[2:],
)

from itertools import product
c2 = 0
for comb in product("10", repeat=11):
    comb="".join(comb)

    if (comb.count("1") + 8) % 5 == 0:
        continue

    c2 +=1

print(c2)
