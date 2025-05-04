def f(a, end):
    if a > end or a == 10: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a*2, end) + f(a+5, end)

print(f(1, 8) * f(8, 16))