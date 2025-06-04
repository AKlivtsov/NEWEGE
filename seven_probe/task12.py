def red(n):
    while "11111" in n or "888" in n:
        if "11111" in n:
            n = n.replace("11111", "88", 1)
        else:
            n = n.replace("888", "8", 1)

    return n


print(red("1" * 81))  # 881
