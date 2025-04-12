def edit(n):
    while ("19" in n) or ("299" in n) or ("3999" in n):
        n = n.replace("19", "2") if "19" in n else n
        n = n.replace("299", "3") if "299" in n else n
        n = n.replace("3999", "1") if "3999" in n else n

    return n


print(edit("1" + "9" * 100))  # 39
