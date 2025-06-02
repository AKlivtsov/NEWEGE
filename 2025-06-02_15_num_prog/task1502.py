def f(a):
    for x in range(1, 500):
        cond = ((x % 9 == 0) <= (x%6!=0)) or ((x+a)>=100)
        if not cond:
            return False
    return True

for A in range(1, 500):
    if f(A):
        print(A)
        break
