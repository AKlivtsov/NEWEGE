import re

maxi = 0
with open("2025-06-09_24_regex/24_40.txt", "r+") as file:
    reg = r"(F[OCDF]*A{1,2}[OCDF]*F)+"
    reg = rf"(?=({reg}))"

    for x in re.finditer(reg, file.read()):
        maxi = max(maxi, len(x.group(1)))
        print(x.group(1))

print(maxi // 3)  # 18
