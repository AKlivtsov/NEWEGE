def F3(n):
    st = ''
    while n > 0:
        st = str(n%3) + st
        n = n // 3
    return st

n = 9**12 + 3**8 - 3
print(F3(n).count('2'))