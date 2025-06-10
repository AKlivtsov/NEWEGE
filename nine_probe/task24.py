with open("nine_probe/24.txt", "r+") as file:
    ans = []
    l = file.read()
    l = l.replace("+", "!")
    l = l.replace("**", "!")
    l = l.replace("*!", "!")
    l = l.replace("!*", "!")
    l = l.replace("!0", "!")
    l = l.replace("!!", "!")
    l = l.split("!")

    for item in l:
        if "*" not in item:
            continue
        if item[0] == "*":
            item = item[1:]

        if item[-1] == "*":
            item = item[:-1]
        ans.append([int(num) for num in item.split("*")])

maxi = 0
for nums in ans:
    if 0 not in nums:
        continue

    if nums == [0]:
        continue

    bad = False
    for num in nums:
        if num == 0:
            continue

        if str(num)[-1] != "5":
            bad = True

    if bad:
        continue

    nums.append("*" * (len(nums) - 1))
    comb = ""
    for sub in nums:
        comb += str(sub)
    maxi = max(maxi, len(comb))

print(maxi)
