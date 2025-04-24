from turtle import *

k = 30
pensize(3)
left(90)
tracer(0)

right(30)
for _ in range(30):
    right(30)
    forward(3 * k)
    right(30)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3)

done()  # 28
