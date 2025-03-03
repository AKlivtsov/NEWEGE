with open("2025-02-27_24num/24_52.txt", "r") as file:
    line = file.readline()

alph = "ABC"
maxi = 0
c =  0

for i in range(len(line)-3):
    c += 1

    if (line[i] in alph) and (line[i + 1] in alph) and (line[i + 2] in alph):
        c -= 1 # 'Cause we already count up char in 11'th line
        maxi = c if c > maxi else maxi
        c = 0

print(maxi) #5752
