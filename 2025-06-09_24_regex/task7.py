import re

maxi = 0
with open("2025-06-09_24_regex/24_1.txt", "r+") as file:
    for x in re.finditer(r"A+", file.read()):
        maxi = max(maxi, len(x.group()))

print(maxi)
