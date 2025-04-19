def alg(n):
    n = str(bin(n)[2:])
    n += n[-2:-1]
    n += n[1:2]
    return int(n, base=2)


for n in range(10**5):
    if alg(n) > 150:
        print(n)
        break
