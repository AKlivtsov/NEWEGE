import sys

sys.setrecursionlimit(999999)


def rec(n):
    if n == 1:
        return 1
    elif n > 1:
        return (n - 1) * rec(n - 1)
    return 0


print((rec(2024) + 2 * rec(2023)) / rec(2022))  # 4094550
