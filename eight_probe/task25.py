
def dividers(n):
    divs = []
    for x in range(2, int(n**0.5) + 1):
        if n%x == 0:
            divs.append(x)
            divs.append(n//x)
            break
    
    if divs:
        return divs[0]**2 + divs[1]**2
    else:
        return 0

def is_prime(s):
    if s <= 1:
        return False
    
    for i in range(2, int(res**0.5) + 1):
        if res % i == 0:
            return False
    
    return True

ans = []
c = 0
for N in range(900000):
    res = dividers(N)
    if res == 0:
        continue

    if is_prime(res):
        ans.append((N, res))
        c+=1

    if c == 5:
        break

print(*ans[::-1])


