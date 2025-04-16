def F7(n):
    ost = ''
    while n > 0:
        ost = str(n % 7) + ost
        n //= 7
    return ost

n = 3*343**8 + 5*49**12 + 7**15-49
for i in range(7):
    print(F7(n).count(str(i)), i)