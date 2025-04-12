def F(n: int) -> int:
    n_bin = str(bin(n)[2:])

    if n % 2 == 0:
        n_bin = "1" + n_bin + "0"
    else:
        n_bin = "11" + n_bin + "11"

    return int(n_bin, base=2)


for i in range(0, 10**99):
    res = F(i)
    if res > 52:
        print(res)  # 63
        break
