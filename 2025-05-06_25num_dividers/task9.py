# 63041

from fnmatch import fnmatch

for i in range(0, 10**10 + 1, 3147):
    if fnmatch(str(i), "1*4302?1"):
        print(i)

# 100430211
# 176430261
# 1374430221
# 1450430271
# 1973430201