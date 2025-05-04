def f(a, end):
    if a > end or a == 14: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a+2, end)

print(f(2, 9) * f(9, 18))