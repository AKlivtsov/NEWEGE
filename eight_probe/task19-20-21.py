def f(s ,m):
    if s <= 21:
        return m%2==0
    if m == 0:
        return 0
    h = [f(s-3, m-1), f(s-7,m-1), f(s//4, m-1)]
    return any(h) if (m-1)%2 ==0 else all(h)

print("19: ", *[s for s in range(22, 100) if f(s, 2) and not f(s, 1)]) # 88
print("20: ", *[s for s in range(22, 100) if f(s, 3) and not f(s, 1) and not f(s, 2)]) # 9192
print("21: ", *[s for s in range(22, 100) if f(s, 4) and not f(s, 1) and not f(s, 3) and not f(s, 2)]) # 94
