with open("17_21416.txt", "r") as f:
    line = [int(line.replace("\n", "")) for line in f.readlines()]

c_f = 0
c_s = 0
for i in range(len(line) - 3):
     third = [line[i + 1], line[i + 2], line[i + 3]]

     minus = 0
     for num in third:
         if num < 0:
             minus += num

     if min(third) * max(third) > minus:
        c_f += 1

     sum_line = 0
     for num in third:
         sum_line += abs(num)

     c_s = sum_line if sum_line > c_s else c_s

print(c_f) # 4631
print(c_s) # 28854