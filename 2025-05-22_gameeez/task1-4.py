def f(s_1, s_2, m):
    if s_1 + s_2 >= 65:
        return m%2==0
    if m == 0:
        return False
    h = [
        f(s_1+1, s_2, m-1),
        f(s_1, s_2+1, m-1),
        f(s_1*3, s_2, m-1),
        f(s_1, s_2*3, m-1),
    ]
    return any(h) if (m+1)%2==0 else all(h)

print("19: ", *[s for s in range(1, 58) if f(6, s, 2) and not f(6, s, 1)]) # 7
print("20: ", *[s for s in range(1, 58) if f(6, s, 3) and not f(6, s, 2)]) # 10 19
print("21: ", *[s for s in range(1, 58) if f(6, s, 4) and not f(6, s, 3)]) # 18