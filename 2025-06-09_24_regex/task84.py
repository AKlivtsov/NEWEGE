import re

maxi = 0
with open("2025-06-09_24_regex/24_84.txt", "r+") as file:
    reg = r"([1-9]+[A-D]*[0-9]*[A-D]*)+"
    for x in re.finditer(rf"(?=({reg}))", file.read()):
        print(x.group(1))
        maxi = max(maxi, len(x.group(1)))

print(maxi)
