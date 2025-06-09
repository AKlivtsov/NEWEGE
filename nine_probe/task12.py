def alg(n):
    while ("40" in n) or ("800" in n) or ("000" in n):
        if "40" in n:
            n = n.replace("40", "0", 1)
        if "800" in n:
            n = n.replace("800", "04", 1)
        if "000" in n:
            n = n.replace("000", "8", 1)
    return n


for i in range(10000, 3, -1):
    N = "4" + "0" * i
    sumi = 0
    for char in alg(N):
        sumi += int(char)
    if sumi == 36:
        print(i)  # 63
        break
