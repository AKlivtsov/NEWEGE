def F8(n):
    ost = ''
    while n > 0:
        ost = str(n % 8) + ost
        n = n // 8
    return ost

n = 7*512**120 - 6*64**100 + 8**210 - 255
print(F8(n).count("0"))
