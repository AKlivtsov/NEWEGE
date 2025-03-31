text = [int(x) for x in open("2025-03-13_17num/17 (4).txt", "r")]
ans = []

def check(a, b, c) -> bool:
    if a**2 >= (b**2 + c**2):
        return False
    elif b**2 >= (a**2 + c**2):
        return False
    elif c**2 >= (a**2 + b**2):
        return False
    
    return True

for i in range(0, len(text) - 2):
    a, b, c = text[i], text[i + 1], text[i + 2]
    if check(a, b, c):
        ans.append(a + b + c)
  
print(len(ans))
print(max(ans))
