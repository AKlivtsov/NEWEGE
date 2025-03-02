with open("2025-02-27_24num/24_53.txt", "r") as file:
    st = file.readline()
    k = 0
    maxi = 0

    for i in range(len(st)-3):
        s1 = st[i+1]+st[i+2]+st[i+3]
        k += 1
        maxi = max(maxi, k)
        if s1.count("X") == 1 and s1.count("Y") == 1 and s1.count("Z") == 1:
            k = 0

    print(maxi - 3)

            