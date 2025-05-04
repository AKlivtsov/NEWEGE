def f(a, end):
    if a == 20 or a == 8:
        end += 1

    if end > 1 or a < 3: 
        return 0
    
    if a == 3:
        return 1

    return f(a-1, end) + f(a-3, end) + f(a//2, end)

print(f(31, 0))