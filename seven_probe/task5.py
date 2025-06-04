def alg(n):
    n_bin = bin(n)[2:]

    if n % 2 == 0:
        n_bin = "10" + n_bin
    else:
        n_bin = "1" + n_bin + "01"

    return int(n_bin, base=2)


maxi = 0
for N in range(12):
    if alg(N) > maxi:
        maxi = alg(N)

print(maxi)  # 109
