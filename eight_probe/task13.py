print(bin(192)[2:])
print(bin(128)[2:])

from itertools import product

c = 0
for comb in product("01", repeat=6):
    comb = ''.join(comb)
    comb = "10" + comb

    if comb.count('1')  == comb.count('0'):
        c += 1

print(c*255 + c)