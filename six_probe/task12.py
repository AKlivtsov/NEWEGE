
def alg(n):
    while "00" not in n:
        n = n.replace("01", "210", 1)
        n = n.replace("02", "320", 1)
        n = n.replace("03", "3012", 1)
    return n


for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            n = "0" + "1"*x + "2"*y + "3"*z + "0"
            res = alg(n)
            if res.count("1") == 23 and res.count("2") == 48 and res.count("3") == 41:
                print(len(n))
