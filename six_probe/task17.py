with open("six_probe/17_2024.txt", "r+") as file:
    numbers = [int(num) for num in file.readlines()]

    max_ = 0
    for num in numbers:
        if str(num)[-2:] == "13" and num > max_:
            max_ = num

    count = 0
    max_sum = 0
    for x in range(len(numbers)-2):
        a = numbers[x]
        b = numbers[x + 1]
        c = numbers[x + 2]

        lens = [len(str(num)) for num in [a, b, c]]
        if lens.count(3) != 2:
            continue

        if sum([a, b, c]) > max_:
            continue

        if sum([a, b, c]) > max_sum:
            max_sum = sum([a, b, c])

        count+=1

    print(count, max_sum)

