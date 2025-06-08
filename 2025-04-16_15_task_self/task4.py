# https://inf-ege.sdamgia.ru/problem?id=75279

for a in range(10**5):
    k = True
    for x in range(10**5):
        cond = ((x & 6280 <= 0) and (x & 3394 <= 0)) or (x & 10828 != 0) or (x & a > 0)
        if cond == 0:
            k = False
            break
    if k:
        print(a)  # 5506
        break

# or ----


def f(a):
    for x in range(10**5):
        cond = ((x & 6280 <= 0) and (x & 3394 <= 0)) or (x & 10828 != 0) or (x & a > 0)
        if not cond:
            return False
    return True


for A in range(10**5):
    if f(A):
        print(A)  # 5506
        break
