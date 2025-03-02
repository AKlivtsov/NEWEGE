with open("2025-02-27_24num/24_51.txt", "r") as file:
    st = file.readline()
    ans = []
    c = 0

    for i in range(1, len(st) - 1):
        if int(st[i - 1]) + int(st[i]) > int(st[i + 1]):
            c += 1

        else:
            c += 2
            ans.append(c)
            c = 0

print(max(ans))
