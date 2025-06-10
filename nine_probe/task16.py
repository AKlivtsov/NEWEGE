import sys

sys.setrecursionlimit(9999)


def rec(n):
    if n == 1:
        return 1
    elif n > 1:
        return (4 * n - 3) * rec(n - 1)
    else:
        return 0


print((rec(5168) // 11 + rec(5166)) // rec(5165))  # 802257043296
