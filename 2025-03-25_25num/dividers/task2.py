def f(x):
    a = set()

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a.add(i)
    
    if len(a) == 0:
        return True
    else: 
        return False
    
for num, i in enumerate(range(245690, 245756+1), 1):
    if f(i):
        print(num, i)