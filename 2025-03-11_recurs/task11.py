from functools import lru_cache

@lru_cache
def F(n: int) -> int:
    if n == 1:
        return n
    
    if n > 1:
        return F(n - 1) - 2 * G(n - 1)
    
    return 

@lru_cache
def G(n: int) -> int:
    if n == 1:
        return n
    
    if n > 1:
        return F(n - 1) + G(n - 1) + n
    
    return 


sum_ = 0
for num in str(G(36)):
    sum_ += int(num)
    
print(sum_)
