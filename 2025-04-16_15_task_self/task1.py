# https://inf-ege.sdamgia.ru/problem?id=9804

for a in range(10**5):
    k = True

    for x in range(10**5):
        cond = (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))

        if cond == 0:
            k = False
            break

    if k == True:
        print(a)  # 12
        break
