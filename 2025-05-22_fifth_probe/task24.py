with open("2025-05-22_fifth_probe/zadanie24_2.txt", "r") as f:
    file = f.readline()

c = 1
maxi = 1

for i in range(len(file)-1):
    if file[i] == "R" and file[i+1] == "R":
        c += 1
        maxi = max(maxi, c)
    else:
        c = 1

print(maxi)
    
