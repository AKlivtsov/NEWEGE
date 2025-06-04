def alg(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    else:
        return alg(start-2, end) + alg(start//2, end)
    
print(alg(38, 16)*alg(16,2))