def alg(n):
    n = bin(n)[2:]
    n += str(n.count("1") % 2)
    n += str(n.count("1") % 2)
    return int(n, base=2)


for n in range(10**5):
    res = alg(n)
    if res > 77:
        print(n)
        break
