from fnmatch import fnmatch

for i in range(0, 10**10, 1991):
    if fnmatch(str(i), '1*4182?7'):
        print(i)