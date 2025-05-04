def f(a, end):
    if a > end: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a+3, end)

print(f(1, 9) * f(9, 17))