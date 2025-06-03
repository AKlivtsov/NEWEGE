def five(n):
    ost = ''
    while n >0:
        ost = str(n % 5) + ost
        n = n//5
    return ost

print(five(125**4+25**8-30).count('4'))
