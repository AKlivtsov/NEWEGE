with open("second_probe/17_task/17.txt", "r") as file:
    nums = [int(x) for x in file.readlines()]

pairs = []

for i in range(len(nums) - 2):
    if (nums[i] + nums[i + 1]) % 7 == 0:
        pairs.append(nums[i] + nums[i + 1])

print(len(pairs))  # 1406
print(max(pairs))  # 19565
