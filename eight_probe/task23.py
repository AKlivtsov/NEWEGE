
def f(start, end, c, d):
    if start == 20:
        c = True

    if start == 8:
        d = True

    if start < end or (c and d):
        return 0
    elif start == end:
        return 1
    else:
        return f(start-1, end, c, d) + f(start-3, end, c, d) + f(start//2, end, c, d)
    
print(f(31, 3, False, False))