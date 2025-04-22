def alg(n):
    if n % 2 == 0:
        n = "10" + bin(n)[2:]
    else:
        n = "1" + bin(n)[2:] + "01"

    return int(n, base=2)


max = 0
for n in range(13):
    max = alg(n) if alg(n) > max else max

print(max)  # 109
