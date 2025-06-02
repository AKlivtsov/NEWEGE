def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            cond = (x+2*y > a) or (x>13) or (y<44)
            if not cond: 
                return False
    
    return True

for A in range(1000, -1, -1):
    if f(A):
        print(A)
        break