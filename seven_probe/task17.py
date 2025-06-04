with open("seven_probe/demo_2025_17.txt") as file:
    nums = [int(x) for x in file.readlines()]

    c = 0
    max_pair = 0
    for i in range(len(nums) -1):
        a = nums[i]
        b = nums[i+1]

        if a%16 == min(nums) or b%16 == min(nums):
            c+=1
            if a + b > max_pair:
                max_pair = a+b

print(c, max_pair)
