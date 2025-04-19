def alg(n: int) -> int:
    save = n
    n = str(bin(n)[2:])

    not_n = ""
    for i in n:
        not_n += "1" if i == "0" else "0"

    n = int(not_n, base=2)
    return save - n

for n in range(10**5):
    if alg(n) == 185:
        print(n)
        break
