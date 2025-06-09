def f(start, end):
    if start < end or start == 24:
        return 0
    elif start == end:
        return 1
    else:
        return f(start - 3, end) + f(start // 3, end)


print(f(308, 81) * f(81, 5))  # 152
