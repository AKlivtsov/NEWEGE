# 52196

from fnmatch import fnmatch

for i in range(0, 10**9 + 1, 3127):
    if fnmatch(str(i), "12*93?1?"):
        print(i)

# 120993011
# 122093715
# 126193212
# 127293916
