def f(a, end):
    if a > end or a == 35: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a+2, end) + f(a*2, end)

print(f(7, 13) * f(13, 15) * f(15, 51)) # 174034068

