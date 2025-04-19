nums = []

for x in range(37):
    for y in range(37):
        num = 2*37**7 + 1*37**6 + x*37**5 + 4*37**4 + 5*37**3 + 7*37**2 + y*37**1 + 9*37**0
        if (num % 36 == 0):
            nums.append(x*37**1+y*37**0)

print(max(nums))
