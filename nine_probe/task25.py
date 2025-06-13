


def dividers(n):
    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0) and (str(i)[-3:] == "134") and (i != 134):
            return i
    return 0

c = 0
for x in range(30_000_000, 10**9):
    if dividers(x) != 0:
        print(x, dividers(x))
        c += 1
        
    if c == 5:
        break
