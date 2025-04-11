q = 14
alph = '0123456789abcd'

max_sum = []

for x in alph:
    for y in alph:
        n = int(f"14{y}5{x}2", q) + int(f'31{x}2{y}3', q)
        if n % 9 == 0:
            max_sum.append([x, y, n])
