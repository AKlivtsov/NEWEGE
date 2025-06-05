import sys

sys.setrecursionlimit(10**5)


def f(n: int):
    if n >= 10000:
        if n % 2 == 0:
            return 1
        else:
            return 0
    else:
        if n % 2 == 0:
            return 2 * n + f(n + 1)
        else:
            return f(n + 2) + n


print(f(2022) - f(2025))  # 6067
