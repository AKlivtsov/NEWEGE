with open("nine_probe/17.txt", "r+") as file:
    nums = [int(x) for x in file.readlines()]
    mini = 10000
    maxi = 0
    count = 0
    for num in nums:
        if num > 0 and str(num)[-1] == "8":
            mini = min(mini, num)

        if num > 0 and num % 25 == 0:
            maxi = max(maxi, num)

    for i in range(len(nums) - 2):
        a = nums[i]
        b = nums[i + 1]
        c = nums[i + 2]

        lens = [len(str(abs(x))) for x in [a, b, c]]

        if lens.count(4) != 2:
            continue

        bad = True
        for x in [a, b, c]:
            if bad and x % mini == 0:
                bad = False

        if bad:
            continue

        if sum([a, b, c]) < maxi:
            continue

        print(a, b, c, lens, maxi, mini, sum([a, b, c]))
        count += 1

print(count)
