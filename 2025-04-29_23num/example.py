# -- рекурсия --

# пути от 2 до 10
def f(a, end):
    if a > end: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a*2, end)

print(f(2, 10))

#..., если избегать 4 
def f(a, end):
    if a > end or a == 4: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a*2, end)

print(f(2, 16))

#..., если через 8 
def f(a, end):
    if a > end: return 0
    if a == end: return 1
    if a < end: return f(a+1, end) + f(a*2, end)

print(f(2, 8) * f(8, 20))


# -- динамическое программирование --

# пути от 2 до 10
a = [0] * 100
a[2] = 1
for i in range(2, 10):
    if i + 1 <= 10: a[i + 1] += a[i]
    if i * 2 <= 10: a[i * 2] += a[i]

print(a)
print(a[10])

#..., если избегать 4 
a = [0] * 100
a[2] = 1
for i in range(2, 16):
    if i == 4: a[i] = 0
    if i + 1 <= 16: a[i + 1] += a[i]
    if i * 2 <= 16: a[i * 2] += a[i]

print(a)
print(a[16])



