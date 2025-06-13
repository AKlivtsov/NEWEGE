from turtle import *

k = 15
pensize(3)
tracer(0)
left(90)

for _ in range(6):
    fd(7 * k)
    right(45)
    fd(4 * k)
    right(90)
    fd(4 * k)
    right(45)

penup()
fd(k)
right(90)
backward(20 * k)
pendown()

for _ in range(5):
    fd(24 * k)
    left(90)
    fd(6 * k)
    left(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5)
done()  # 20
