with open("seven_probe/9.txt", "r+") as file:
    c = 0
    for line in file.readlines():
        line = [int(num) for num in line.split()]

        ocurences = []
        for num in line:
            ocurences.append(line.count(num))

        if ocurences.count(1) != 3:
            continue

        not_rep_sum = sum(x for x in line if line.count(x) == 1)
        rep_sum = sum(x for x in line if line.count(x) == 3)

        if not_rep_sum**2 <= rep_sum**2:
            continue

        print(line)
        print(not_rep_sum, rep_sum)
        print(not_rep_sum**2, rep_sum**2)

        c += 1

print(c)  # 222 ! 273 - 
