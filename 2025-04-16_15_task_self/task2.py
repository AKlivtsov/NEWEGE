# https://inf-ege.sdamgia.ru/problem?id=34509

for a in range(10**5):
    k = True
    for x in range(10**5):
        if ((x & 25 != 0) <= ((x & 12 == 0) <= (x & a != 0))) == 0:
            k = False
            break

    if k == True:
        print(a)  # 17
        break
