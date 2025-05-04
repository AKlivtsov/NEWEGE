def f(a, end):
    if a < end: return 0
    if a == end: return 1
    if a > end: return f(a-2, end) + f(a//2, end)

print(f(30, 14) * f(14, 1))