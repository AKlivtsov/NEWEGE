def alg(n):
    n = bin(n)[2:]

    n += "0" if int(n) % 2 == 0 else "1"
    n += "0" if int(n) % 2 == 0 else "1"

    return n


for x in range(10**9):
    if int(alg(x)) > 170:
        print(x)  # 2 #43
        break
