from itertools import product
from re import sub

with open("seven_probe/demo_2025_24.txt", "r+") as file:
    line = file.readline()
    line = "7**090007*769099-77*090077808-66869*-90*-*-9799"

    for comb in product("-*", repeat=2):
        comb=''.join(comb)
        line = line.replace(comb, "A")

    line = line.replace("-0", "A")
    line = line.replace("*0", "A")
    line = line.split("A")

    max_len = 0
    for subline in line:
        if subline.startswith("0") or subline.startswith("-") or subline.startswith("*"):
            line.remove(subline)
 
        max_len = max(max_len, len(subline))

    print(max_len) # 165
    print(line)
        
