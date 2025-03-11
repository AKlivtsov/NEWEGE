def F(n: int) -> int:
    if n >= 2:
        return F(n-1) * n
    elif n == 1:
        return n
    
    return 

print(F(6))
