import sys
sys.setrecursionlimit(1099999)

def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + n

c = 0
for i in range(237_567_892, 1_134_567_004 + 1):
    if f(i) % 3 != 0:
        c += 1

print(c)