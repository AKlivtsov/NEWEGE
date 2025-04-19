alph = "0123456789abcdef"
for x in alph:
    num = int(f"8{x}834", base=16) + int(f"44{x}27", base=16)
    if num % 23 == 0:
        print(num // 23)
        break
