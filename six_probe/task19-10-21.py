def f(s, m):
    if s >= 39:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(s+1, m-1), f(s*3-2, m-1)]
    return any(h) if (m+1)%2==0 else all(h)

print("19:", *[s for s in range(2, 40) if f(s, 2) and  not f(s, 1)]) # 6
print("20:", *[s for s in range(2, 40) if f(s, 3) and not f(s, 2)]) # 512
print("21:", *[s for s in range(2, 40) if f(s, 4) and not f(s, 3) and not f(s, 1)]) # 11