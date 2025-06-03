def alg(n):
    while not "00" in n:
        n = n.replace("01", "210", 1)
        n = n.replace("02", "320", 1)
        n = n.replace("03", "3012", 1)

    return n


for x in range(1, 100):
    n = "0" + "1"*x + "2"*x + "3"*x + "0"
    res = alg(n)
    if res.count("1") == 23 and res.count("2") == 48 and res.count("3") == 41:
        print(len(n))
