from fnmatch import fnmatch

for i in range(0, 10 ** 9, 23):
    if fnmatch(str(i), '12345?7?8') and i % 23 == 0:
        print(i, i // 23)

        