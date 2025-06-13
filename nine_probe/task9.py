with open("nine_probe/9.txt", "r+") as file:
    for line in file.readlines():
        line = [int(x) for x in line.split()]

        occurences = {}
        for num in line:
            occurences[num] = line.count(num)

        if list(occurences.values()).count(2) != 2:
            continue

        if line.count(max(line)) > 1:
            continue

        max_num = line.pop(list.index(max(line)))
        min1 = 0
        min2 = 0
        for num in line:
            if min1 != 0 and min2 != 0:
                break

            if li


        print(line)
