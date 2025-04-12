def check(n: list) -> bool:
    # first cond
    a = set()
    for item in n:
        a.add(item)

    if len(a) != 5:
        return False

    # second cond
    repeated = 0
    for item in n:
        if n.count(item) == 2:
            repeated = item
            break

    n.remove(repeated)
    n.remove(repeated)

    if sum(n) / len(n) > repeated * 2:
        return False

    return True


c = 0
with open("second_probe/9_task/9.txt", "r") as file:
    for line in file.readlines():
        line = [int(x) for x in line.split("\t")]
        if check(line):
            c += 1

print(c)  # 2241
