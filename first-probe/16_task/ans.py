def F(n: int) -> int:
    return 1/2 if n <= 1 else (n + 1) * F(n-1)
    
print(F(200)//F(198))