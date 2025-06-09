import re

maxi = 0
with open("2025-06-09_24_regex/24_80.txt", "r+") as file:
    for x in re.finditer(r"A{1}([1-6]+[-/*]{1}[1-6]+)+", file.read()):
        print(x.group())
        maxi = max(maxi, len(x.group()))

print(maxi)
