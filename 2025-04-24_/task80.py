from itertools import product

def alg(line: str) -> str:
    while "00" not in line:
        line = line.replace("012", "30", 1)
        if "011" in line:
            line = line.replace("011", "20", 1)
            line = line.replace("022", "40", 1)
        else:
            line = line.replace("01", "10", 1)
            line = line.replace("02", "101", 1)

    return line

max  = 0
for comb in product('12', repeat=20):
    comb = ''.join(comb)
    comb = "0" + comb + "0"

    if comb.count("1") != 10 and  comb.count("2") != 10:
        continue

    if alg(comb).count("1") == 6 and alg(comb).count("2") == 5:
        res = alg(comb).count("4")
        max = res if res > max else max

print(max) # 2
