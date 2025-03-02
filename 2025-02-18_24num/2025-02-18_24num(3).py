with open("2025-02-18_24num/24_5.txt", "r") as file:
    line = file.readline()

count_answer = 0

num_of_a = line.count('A', 0, 2023) # 0 - frame start, 2023 - frame end
num_of_z = line.count('Z', 0, 2023)

# if line is good, add it to counter
if num_of_a == num_of_z:
    count_answer += 1

for i in range(len(line) - 2023): # 'cause frame is moving to 2023 sym

    # if first symbol was A or Z, delete it from counter
    if line[i] == "A":
        num_of_a -= 1
    elif line[i] == "Z":
        num_of_z -= 1

    # if last symbol is A or Z, count it up
    if line[i + 2023] == "A":
        num_of_a += 1
    elif line[i + 2023] == "Z":
        num_of_z += 1

    if num_of_a == num_of_z:
        count_answer += 1

print(count_answer)
