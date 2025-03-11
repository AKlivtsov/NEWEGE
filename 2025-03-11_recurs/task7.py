import sys 
sys.setrecursionlimit(9999999)

def F(n: int) -> int:
    if n == 1:
        return n
    elif n > 1:
        return (n - 1) * F(n - 1)
    
    return

print((F(2024) + 2 * F(2023)) / F(2022))  # 4094550
