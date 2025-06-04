with open("9.txt", "r+") as file:
    c = 0
    for line in file.readlines():
        line = [int(num) for num in line.split("\t")]

        ocurences = []
        for num in line:
            ocurences.append(line.count(num))

        ocurences.sort()
        if ocurences != [1, 1, 1, 3, 3, 3]:
            continue

        not_rep_sum = 0
        rep_sum = 0

        for num in line:
            if line.count(num) != 3:
                not_rep_sum += num
            else:
                rep_sum += num

        if not_rep_sum**2 <= rep_sum**2:
            continue

        c += 1

print(c)  # 222
