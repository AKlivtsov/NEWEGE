def F(n: int) -> int:
    if (n > 2) and (n % 2 == 0):
        return F(n - 1) + n - 1
    
    elif (n > 2) and (n % 2 != 0):
        return F(n - 2) + 2*n - 2
    
    elif n < 3:
        return 1
    
    return

print(F(34))
