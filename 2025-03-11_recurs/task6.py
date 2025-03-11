import sys 
sys.setrecursionlimit(9999999)

def F(n: int) -> int:
    if n == 1:
        return n
    elif n > 1:
        return 2 * n * F(n - 1)
    
    return

print((F(2024)- 4 * F(2023)) / F(2022)) # 16362024
