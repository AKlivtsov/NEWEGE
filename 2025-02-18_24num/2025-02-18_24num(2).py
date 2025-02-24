with open("2025-02-18_24num/24_4.txt", "r+") as file:
    st = file.read()
    mx = 0
    k = 0

    for i in range(len(st)):
        if st[i] in "0123456789ABCDEF":
            k += 1
        else: 
            if k > mx:
                mx = k
            k = 0
    if k > mx:
        mx = k
    
print(mx)

