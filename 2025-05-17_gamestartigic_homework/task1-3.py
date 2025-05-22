def f(s, m):
    if s >= 53:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(s+1, m-1), f(s+4, m-1), f(s*2, m-1)]
    return any(h) if (m+1) % 2 == 0 else all(h)

print("19:", *[s for s in range(1, 53) if not f(s, 1) and f(s, 2)])
print("20:", *[s for s in range(1, 53) if f(s, 3) and not f(s, 1)])
print("23:", *[s for s in range(1, 53) if f(s, 4) and not f(s, 1)])

# 1-3
