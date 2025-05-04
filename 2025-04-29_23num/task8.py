def f(a, end):
    if a > end or a == 33: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a*2, end) + f(a*3, end)

print(f(3, 15) * f(15, 50))