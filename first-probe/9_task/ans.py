
c = 0

with open("first-probe/9_task/9.txt", "r") as file:
    for line in file.readlines():
        line =[str(x).replace(",", ".") for x in line.strip("\n").split("\t")]

        if float(line[0]) - float(line[1]) < 5:
            continue

        if (0 > int(line[4]) > 45) or (315 > int(line[4]) > 360):
            continue
        
        c += 1

print(c) # 457
    