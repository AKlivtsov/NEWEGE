def f(n):
    n_bin = bin(n)[2:]

    if n_bin.count("1") % 2 == 0:
        n_bin = "10" + n_bin + "0"
    else:
        n_bin = "1" + n_bin + "11"

    return int(n_bin, 2)


for N in range(10000, 0, -1):
    if f(N) < 410:
        print(f(N))
        break
