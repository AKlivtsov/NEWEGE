with open("2025-02-18_24num/24_3.txt", "r+") as file:
    st = file.read()
    mx = 0
    y = []

    for i in range(len(st)):
        if st[i] == "Y":
            y.append(i)
    for i in range(len(y) - 151):
        if y[i + 151] - y[i] > mx:
            mx = y[i + 151] - y[i]

print(mx - 1)
