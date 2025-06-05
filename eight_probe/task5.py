def alg(n):
    n_bin = bin(n)[2:]
    if n %2 ==0:
        n_bin = "10" + n_bin + "0"
    else:
        n_bin += bin(n_bin.count("1"))[2:]

    return int(n_bin, base=2)

ans = []
ns = []
for N in range(1000):
    if alg(N) > 600:
        ans.append(alg(N))
        ns.append(N)

print(ns[ans.index(min(ans))])


