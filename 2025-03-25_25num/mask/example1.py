from fnmatch import fnmatch

for i in range(2023, 10**9, 2023):
    if fnmatch(str(i), '20*23') and sum(map(int, str(i))) % 7 == 0 and sum(map(int, str(i))) < 20:
        print(i)