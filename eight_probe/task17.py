with open("eight_probe/17-1.txt", "r+") as file:
    nums = [int(num) for num in file.readlines()]
    maxi = 0
    count = 0
    max_sum = 0

    for num in nums:
        if str(abs(num))[-1] == "7":
            maxi = max(maxi, num)

    for i in range(len(nums) - 2):
        a = nums[i]
        b = nums[i + 1]
        c = nums[i + 2]

        a_r = str(abs(a))[0]
        b_r = str(abs(b))[0]
        c_r = str(abs(c))[0]

        if a_r != b_r or a_r != c_r:
            continue

        goodOne = False
        for num in [a, b, c]:
            if len(str(abs(num))) == 3 and str(abs(num))[-1] == "7":
                goodOne = True

        if not goodOne:
            continue

        if abs(a) + abs(a) + abs(a) >= maxi:
            continue

        count += 1
        max_sum = max(max_sum, abs(a) + abs(a) + abs(a))

    print(count)  # 12
    print(max_sum)  # 13428
