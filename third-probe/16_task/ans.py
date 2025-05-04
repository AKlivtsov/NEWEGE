import sys
sys.setrecursionlimit(10**6)

def F(n):
    if n > 5:
        return n + F(n-2)
    return 1


print(F(2126)-F(2122)) # 4250
