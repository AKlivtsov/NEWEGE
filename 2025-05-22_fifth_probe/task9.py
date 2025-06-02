c = 0
with open("2025-05-22_fifth_probe/9.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        line = [int(num) for num in line.replace("\n", "").split("\t")]
        line.append(i + 1)
        
        occurences = set()
        for i in range(6):
            occurences.add(line[i])

        bad = False
        for item in occurences:
            was_three = False
            if line.count(item) == 3 and was_three is False:
                was_three = True
                
            elif was_three is True and line.count(item) > 1:
                bad = True
        
        if bad:
            continue

        print(line)

        