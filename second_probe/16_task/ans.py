def F(n: int) -> int:
    if n > 1:
        return 5 * F(n - 1) + 3

    return 1


print(F(4))  # 218
