def f(s, m):
    if s <= 24:
        return m % 2 == 0
    if m == 0:
        return 0
    if s % 2 == 0:
        h = [f(s - 3, m - 1), f(s // 2, m - 1)]
    else:
        h = [f(s - 3, m - 1), f((s + 3) // 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19: ", *[s for s in range(25, 100) if f(s, 2) and not f(s, 1)])  # 47
print(
    "20: ", *[s for s in range(25, 100) if f(s, 3) and not f(s, 1) and not f(s, 2)]
)  # 50 52
print("21: ", *[s for s in range(25, 100) if f(s, 4) and not f(s, 2)])  # 53
