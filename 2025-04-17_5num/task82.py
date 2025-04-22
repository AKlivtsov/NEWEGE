def alg(n):
    if n % 2 == 0:
        n = "11" + bin(n)[2:]
    else:
        n = "1" + bin(n)[2:] + "10"

    return int(n, base=2)


max = 0
for x in range(234567890, 567891235):
    max = alg(x) if alg(x) > max else max

print(max)  # 6566532230
