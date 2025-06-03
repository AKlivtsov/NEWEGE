with open("six_probe/9.txt", "r+") as f:
    c = 0
    for line in f.readlines():
        line = [int(num) for num in line.replace("\n", "").split("\t")]
        
        a = set()
        for num in line:
            a.add(num)

        if len(a) == len(line):
            continue

        if line.count(max(line)) > 1:
            continue

        repeated_list = []
        for num in line:
            if line.count(num) > 1:
                repeated_list.append(num)

        if  sum(repeated_list) >= max(line):
            continue

        c += 1 

    print(c)


