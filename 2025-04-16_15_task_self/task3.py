# https://inf-ege.sdamgia.ru/problem?id=64900

for a in range(10**5):
    k = True
    for x in range(10**5):
        if ((x & 20777 != 0) <= ((x & 12332 == 0) <= (x & a != 0))) == 0:
            k = False
            break

    if k == True:
        print(a)  # 16641
        break
