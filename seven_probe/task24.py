from itertools import product
from re import sub

with open("seven_probe/demo_2025_24.txt", "r+") as file:
    line = file.readline()
    line = "9*-97969909*06-6968*0*09-6688-000697770*9-907797868668**-879-96-08899809-7-*"

    start = 0
    end = 0
    for i in range(len(line)-1):
        if line[i] in "-*0":
            
            

    line = line.split("A")

    max_len = 0
    for i in range(len(line) - 3):

        if line[i].endswith("-") or line[i].endswith("*"):
            line.pop(i)

    max_len = len(max(line))

    print(max_len)  # 165
