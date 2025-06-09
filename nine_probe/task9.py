with open("nine_probe/9.txt", "r+") as file:
    for line in file.readlines():
        line = [int(x) for x in line.split()]

        occurences = []
        for num in line:
            occurences.append(line.count(num))
        occurences.sort()

        if occurences != [1, 1, 1, 1, 2, 2]:
            continue

        if line.count(max(line)) > 1:
            continue

        rep = 0
        for num in line:
            if line.count(num) > 1:
                rep = num
                break

        line.sort()

        min_a = line[0]
        min_b = line[1]

        if rep**2 >= (min_a**2 + min_b**2):
            continue

        print(line)
