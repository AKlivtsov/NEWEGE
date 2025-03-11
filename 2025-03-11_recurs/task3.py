def F(n: int) -> int:
    if n > 2:
        return F(n - 1) * n + F(n-2) * (n -1)
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    
    return 

print(F(5))
