

maxi = 0
with open("eight_probe/24_1.txt", "r+") as file:
    line = file.readline()

    line = line.replace("-", "+")
    line = line.replace("+0+", "+5+")
    line = line.replace("++", "A")
    line = line.replace("+0", "A")

    while "A0" in line:
        line = line.replace("A0", "A")

    line = line.replace("A+", "A")
    line = line.replace("+A", "A")
    
    
    lines = line.split("A")
    for sub in lines:
        maxi = max(maxi, len(sub))

print(maxi)