from turtle import *

k = 15
tracer(0)
pensize(2)
left(90)

for _ in range(9):
    fd(22 * k)
    right(90)
    fd(6 * k)
    right(90)

penup()

fd(1 * k)
right(90)
fd(5 * k)
left(90)
pendown()

for _ in range(9):
    fd(53 * k)
    right(90)
    fd(75 * k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5)

done()  # 44
