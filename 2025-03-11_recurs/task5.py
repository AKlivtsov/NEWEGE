
def F(n: int) -> int:
    if n == 0:
        return 0

    if n % 2 == 0:
        return 4 * F(n / 2)
    
    elif n % 2 != 0:
        return F(n-1) + 2*n - 1
    
    return


for a in range(999):
    for b in range(999):
        if F(a) - F(b) == 1045:
            print(a-b)
    
