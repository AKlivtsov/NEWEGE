line = "1"*81

while ("11111" in line) or ("888" in line):
    if "11111" in line:
        line = line.replace("11111", "88", 1)
    else:
        line = line.replace("888", "8", 1)

print(line)
