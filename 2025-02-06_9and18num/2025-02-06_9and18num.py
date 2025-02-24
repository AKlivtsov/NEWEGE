count = 0

# with open("2025-02-06_9and18num/table.txt", "r") as file:
#     for _ in range(20):
#         line = file.readline()
#         line = list(map(int, line.split()))  # from tables to list

#         for num in line:
#             if num % 2 == 0:
#                 count += 1

line = [2494, 2428, 2370, 2316,
         2278, 2253, 2162, 2132,
         1997, 1815, 1679, 1582, 
         1580, 1490, 1352, 1236,
         1059, 966, 961, 845, 
         776, 737, 616, 455, 
         339, 238, 53]

for num in line:
    if num % 2 == 0:
        count += 1

print(count)
