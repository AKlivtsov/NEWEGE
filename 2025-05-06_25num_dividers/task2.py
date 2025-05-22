# 27850

def f(x):
    good = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            good = False

    if good:
        return x
    else:
        return 0

for num, x in enumerate(range(245690, 245756  + 1)):
    if f(x) != 0:
        print(num + 1, x)

# 22 245711
# 30 245719
# 34 245723
# 52 245741
# 58 245747
# 64 245753
