# 47229

from fnmatch import fnmatch

for i in range(0, 10**10 + 1, 2023):
    if fnmatch(str(i), "1?2139*4"):
        print(i, i // 2023)

# 162139404 80148
# 1321399324 653188
# 1421396214 702618
# 1521393104 752048
