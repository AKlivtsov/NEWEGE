def f(s, n):
    if s >= 84:
        return n % 2 ==0
    if n == 0:
        return False

    h = [f(s+1, n-1)]
    if s%2==0:
        h.append(f(s*1.5, n-1))
    else:
        h.append(f(s*2, n-1))

    return any(h) if (n+1) %2 == 0 else all(h)

print("19: ", *[s for s in range(1, 83) if f(s, 2) and not f(s, 1)])
print("20: ", *[s for s in range(1, 83) if f(s, 3) and not f(s, 1)])
print("21: ", *[s for s in range(1, 83) if f(s, 4) and not f(s, 1)])
