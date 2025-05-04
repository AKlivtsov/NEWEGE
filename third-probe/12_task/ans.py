def alg(n: str) -> str:
    while ("31" in n ) or ("211" in n) or ("1111" in n):
        if "31" in n:
            n = n.replace("31", "1", 1)
        if "211" in n:
            n = n.replace("211", "13", 1)
        if "1111" in n:
            n = n.replace("1111", "2", 1)

    return n

min_n = 9999999999
for n in range(3, 10000):
    if len(alg("1"*n)) == 15:
        min_n = n if n < min_n else min_n

print(min_n) # 525