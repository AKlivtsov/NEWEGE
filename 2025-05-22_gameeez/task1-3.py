def f(s_1, s_2 ,m):
    if s_1 + s_2 >= 81:
        return m%2==0
    if m == 0:
        return False
    
    h = [
        f(s_1+1, s_2, m-1),
        f(s_1, s_2+1, m-1), 
        f(s_1*2, s_2, m-1),
        f(s_1, s_2*2, m-1),
        ]
    
    return any(h) if (m+1) %2 ==0 else all(h)


print("19: ", *[s for s in range(1, 73) if  f(s, 7, 2) and not f(s, 7, 1)])
print("20: ", *[s for s in range(1, 73) if f(s, 7, 3) and not f(s, 7, 2)])
print("21: ", *[s for s in range(1, 73) if f(s, 7, 4) and not f(s, 7, 3)])