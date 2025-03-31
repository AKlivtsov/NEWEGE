text = [int(x) for x in open("2025-03-13_17num/17 (1).txt", "r")]
ans = []

for i in range(0, len(text)):
    for j in range(i+1, len(text)):
        a, b = text[i], text[j]
        if (a - b) % 2 == 0:
            if (a % 31 == 0 ) or (b % 31 == 0):
                ans.append(a + b)
            

print(len(ans))
print(max(ans))
