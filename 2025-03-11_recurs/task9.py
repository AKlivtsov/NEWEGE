
import sys 
sys.setrecursionlimit(9999999)

def F(n: int) -> int:
    if n > 2024:
        return n
    else:
        return n * F(n + 1)

print(F(2022) / F(2024)) # 4090506
