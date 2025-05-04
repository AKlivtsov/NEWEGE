def f(a, st=''):
    if a > 22 or st[-2:] == "22":
        return 0
    
    if a == 22: 
        return 1
    
    return f(a+1, st+"1") + f(a+2, st+"2") + f(a*2, st+"3")

print(f(2))