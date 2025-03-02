with open("2025-02-27_24num/24_50.txt", "r") as file:
    st = file.readline()
    ans = []
    c = 1
    
    for i in range(1, len(st)):
        if st[i -1] != st[i]:
            c += 1
        else:
            ans.append(c)
            c = 1
    
print(max(ans))
