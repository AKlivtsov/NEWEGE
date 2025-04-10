def F(n: int) -> str:
    nums_list = [int(x) for x in str(n)]
    n_sum = max(nums_list) + min(nums_list)
    nums_list.pop(nums_list.index(max(nums_list)))
    nums_list.pop(nums_list.index(min(nums_list)))
    n_pwr = nums_list[0] * nums_list[1]

    if n_sum > n_pwr:
        return f"{n_pwr}{n_sum}"
    else:
        return f"{n_sum}{n_pwr}"


for n in range(1000, 10000):
    res = F(n)
    if int(res) > 85:
        print(res, n)  # 88 1088
        break
