with open("24_21421.txt", "r") as f:
    line = f.readline()

maxi = 0
alph = "0123456789AB"
start = 0
end = 0

c = 0
while end <= len(line) - 1:
    if line[start] not in alph:
        start += 1
        end += 1

    elif line[end] not in alph:
        c += 1
        maxi = c if c > maxi else maxi
        c = 0
        start = end + 1
        end += 1

    elif line[start] in alph and line[end] in alph:
        end += 1
        c += 1

print(maxi)  # 21

