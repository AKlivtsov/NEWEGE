def f(a, end):
    if a > end: return 0
    if a == end: return 1
    if a < end: return f(a + 2, end) + f(a*5, end)

print(f(2, 50))