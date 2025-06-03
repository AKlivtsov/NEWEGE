def dividers(n):
    divs = []
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            divs.append(x)
            divs.append(n//x)
            break

    return sum(divs)

iter = 0
for i in range(800001, 10**8):
    if str(dividers(i))[-1] == "4":
        print(i, dividers(i))
        iter += 1
    
    if iter == 5:
        break
        