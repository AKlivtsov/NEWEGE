
with open("seven_probe/demo_2025_24.txt", "r+") as file:
    line = file.readline()
    line = line.replace('-', '*')
    line = line.replace('*0*', '*5*')i
    line = line.replace('**', 'x')
    line = line.replace('*0', 'x')
    line = line.replace('x0', 'x')
    line = line.replace('x*', 'x')
    line = line.replace('*x', 'x')
    a = line.split('x')
    c = 0
    for i in a:
        if len(i) > 3:
            c = max(c, len(i))

    print(c)  # 154
