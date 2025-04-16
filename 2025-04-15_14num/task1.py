def F5(n):
    ost = ''
    while n >0:
        ost = str(n%5) + ost
        n = n // 5
    return ost

n = 4 * 625**9 - 25**15 + 2 * 5**11 -7
print(F5(n).count('4'))
