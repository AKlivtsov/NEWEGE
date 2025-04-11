from itertools import product

def edit(n: str) -> str:
    while ("111" in n) or ("66" in n):
        if "6666" in n:
            n = n.replace("6666", "1")
        else:
            n = n.replace("111", "3")

        if "66" in n:
            n = n.replace("66", "6")

    return n

for i in range(3, 10**4):
    res = edit("6" * i)
    if res.count("3") == 5:
        print(res, i) # 33333 60
        break
