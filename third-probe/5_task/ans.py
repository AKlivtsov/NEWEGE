def alg(n):
    n = bin(n)[2:]
    if n.count("1") % 2 == 0:
        n = "10" + n[2:] + "0"
    else:
        n = "11" + n[2:] + "1"
    return int(n, base=2)

for i in range(1, 10*100):
    if alg(i) > 480:
        print(i) # 176
        break
