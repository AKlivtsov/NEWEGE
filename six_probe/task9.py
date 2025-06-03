with open("six_probe/9.txt", "r+") as f:
    c = 0
    for line in f.readlines():
        line = [int(num) for num in line.replace("\n", "").split("\t")]




