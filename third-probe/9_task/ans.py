c = 0
with open("9.txt", "r") as f:
    for line in f.readlines():
        line = [int(num) for num in line.replace("\n", "").split("\t")]

        occurrences = set()
        for i in range(7):
            occurrences.add(line[i])

        if len(occurrences) == 3:
            print(line)
            print(occurrences)
