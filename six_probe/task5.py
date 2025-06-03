from itertools import product

def alg(n: str):
    n1 = int(n[0]) + int(n[1])
    n2 = int(n[2]) + int(n[3])
    return f"{n1}{n2}" if n2>n1 else f"{n2}{n1}"

c = 0
for N in product("13579", repeat=4):
    N =''.join(N)
    if alg(str(N)) == "414":
        c+=1

print(c)